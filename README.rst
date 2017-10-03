=====
rexex
=====

Rule EXample EXtractor is a proof of concept processing a 
`C++ Core Guideline <https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md>`_ 
Markdown file and extracting the code examples of each rule. rexex tries to
figure out which code examples should pass tests of the rule in question and
which ones should be reported.

Currently rexex prints the examples, the rule they belong to, and a
classification.

Later on the output can be fed to static code analyzers like ``clang-tidy``,
``cpplint.py``, or Visual Studio to understand the coverage of the rules by the
static code analyzer.


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


Usage
=====

To extract code examples:
::

    ./rexex.py ~/somewhere/CppCoreGuidelines.md


The tool prints something like:
::

    mixed example code for rule P.1:
    class Date {
        // ...
    public:
        Month month() const;  // do
        int month();          // don't
        // ...
    };
    // ************************************************************


License
=======
GNU General Public License v3.