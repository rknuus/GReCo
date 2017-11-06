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

import json
import sys
import tempfile


def run(args):
    if not args or len(args) < 1:
        print('Usage: evalyze.py <path of rule JSON file>', file=sys.stderr)
        return -1

    input_file = args[0]
    tool = 'clang-tidy'  # = args[1]
    examples = None
    with open(input_file) as json_data:
        examples = json.load(json_data)

    bad_example = examples["ES.107"]["bad"][0]
    with tempfile.NamedTemporaryFile(mode='w', suffix='.cpp', delete=False) as source_file:
        source_file.write('#include <iostream>\n#include <vector>\nusing namespace std;  // NOLINT\nvoid foo() {\n')
        source_file.write(bad_example)
        source_file.write('\n}\n')
        print('prepared file ', source_file.name)

    # clang++ -I/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1 -c --std=c++11 -Weverything /var/folders/gt/8b13k5qn5d1bjw0cpcvd81r00000gs/T/tmp61uwidl2.cpp
    # ~/Projects/FOSS/llvm/clang-build/bin/clang-tidy --checks='*,-android*' /var/folders/gt/8b13k5qn5d1bjw0cpcvd81r00000gs/T/tmp61uwidl2.cpp -- -I/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1 -std=c++11  # -stdlib=libc++


def main():
    sys.exit(run(sys.argv[1:]))


if __name__ == "__main__":
    main()
