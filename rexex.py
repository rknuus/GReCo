#!/usr/bin/env python3

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import collections
import io
import json
import pypandoc
import panflute
import re
import sys

rule_id = re.compile('(\w+[.](?:\d|\w)+):')
example = re.compile('Example(?:, (?:bad|good))?')


def action(elem, doc):
    if isinstance(elem, panflute.CodeBlock):
        doc.codeblocks.append(elem)


def match_rule_id(element):
    if not isinstance(element, panflute.Header):
        return None
    try:
        return rule_id.search(panflute.stringify(element)).group(1)
    except Exception:
        return None


def match_example_header(element):
    if not isinstance(element, panflute.Header):
        return None
    try:
        return example.search(panflute.stringify(element)).group(0)
    except Exception:
        return None


good_header = re.compile('(?:good|ok)', re.I)
bad_header = re.compile('(?:bad)', re.I)
good_comment = re.compile('//\s*(?:good|ok|do[^n]|better)', re.I)
bad_comment = re.compile('//\s*(?:bad|don\'t)', re.I)


def classify_example(codeblock_text, example_header):
    g1 = good_comment.search(codeblock_text)
    b1 = bad_comment.search(codeblock_text)
    g2 = good_header.search(example_header) if example_header else None
    b2 = bad_header.search(example_header) if example_header else None

    good = g1 or g2
    bad = b1 or b2

    if good and bad:
        return 'mixed'
    elif good:
        return 'good'
    elif bad:
        return 'bad'
    return 'undefined'


def run(args):
    if not args or len(args) < 2:
        print('Usage: rexex.py <path of CppCoreGuidelines.md> <output file>', file=sys.stderr)
        return -1

    input_file = args[0]
    output_file = args[1]
    data = pypandoc.convert_file(input_file, to='json')
    doc = panflute.load(io.StringIO(data))
    doc.headers = []
    doc.codeblocks = []
    doc = panflute.run_filter(action, doc=doc)
    rules = collections.defaultdict(lambda: collections.defaultdict(list))

    for codeblock in doc.codeblocks:
        possible_header = codeblock
        header_match = match_rule_id(possible_header)
        example_match = match_example_header(possible_header)
        while not header_match:
            if not possible_header:
                print('ERROR: cannot identify rule of codeblock\n{}'.format(codeblock.text))
                break
            if not example_match:
                example_match = match_example_header(possible_header)
            possible_header = possible_header.prev
            header_match = match_rule_id(possible_header)
        if not header_match:
            continue
        example_class = classify_example(codeblock.text, str(example_match))
        rules[header_match][example_class].append(codeblock.text)

    with open(output_file, 'w') as output:
        output.write(json.dumps(rules))


def main():
    sys.exit(run(sys.argv[1:]))


if __name__ == "__main__":
    main()
