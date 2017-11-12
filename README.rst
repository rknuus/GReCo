=====
GReCo
=====

Guideline RulE COverage will be a set of tools to identify guideline rules
covered by which checker (e.g. a compiler or a static code analysis tool).


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

    # install Python 3
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


License
=======
GNU General Public License v3.