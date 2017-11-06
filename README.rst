=====
GReCo
=====

Guideline RulE COverage will be a set of tools to identify guideline rules
covered by which checker (e.g. a compiler or a static code analysis tool).

Expected workflow:
- prepare the error message corpus of each checker
- prepare the rule corpus of each guideline document
- determine the top N guideline rules a checker error message could cover
- prepare the code examples to check against, see rexex
- for each checker apply each check on each code example of the top N guideline
  rules and report which ones could be true/false positives/negatives


rexex
=====
Rule EXample EXtractor extracts the code examples of each
`C++ Core Guideline <https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md>` rule and tries to classify the example whether it's a
good one, a bad one, a mixed one, or unclassifiable.

To extract code examples:
::

    ./rexex.py ~/somewhere/CppCoreGuidelines.md ~/somewhere/examples.json


The tool creates a JSON file containing a mapping of rules to examples grouped
by classification.


Setup
=====
::

    # install Python 3.5 or higher
    # E.g. on Mac OS X
    brew install python3
    # Or on Debian/Ubuntu
    sudo apt install python3

    # install pandoc
    # E.g. on Mac OS X
    brew install pandoc
    # Or on Debian/Ubuntu
    sudo apt install pandoc

    # install python library dependencies
    pip install -r requirements.txt

    # install basic models
    python[3] -m spacy download en
    # or more precise models: python[3] -m spacy download en_core_web_lg

    # download stopwords etc.
    python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"

    # if the locale is unknown (or non-english?!):
    export LC_ALL=en_US.UTF-8
    export LANG=en_US.UTF-8



License
=======
GNU General Public License v3.