Design
======
- the error message corpus for a checker shall contain:
  - name of the checker (e.g. clang)
  - version of the checker (e.g. 5.0)
  - per check:
    - command line option to activate check
    - check error message without stop words in a format TBD to enable
      identification of the top N most similar rules (e.g. with word2vec's
      `most_similar` function)


Notes
=====
- check what I need from http://textminingonline.com/getting-started-with-spacy
- use compiler as linter
- figure out how much it takes to compile most of the examples, i.e. are there some standard boiler plate variants covering most of the examples and how to identify them?
- possible algorithm to match compiler warnings/linter findings to C++ Core Guidelines rules:
  - [vectorize](http://scikit-learn.org/stable/modules/feature_extraction.html#common-vectorizer-usage) C++ Core Guidelines rules
  - consider to sort the set of vectors to speed up vector comparison
  - consider to sort the vector elements/words to have the most common words at the front
  - for each code example:
    - vectorize all compiler warnings/linter findings (ignoring all words not found in C++ Core Guidelines rules)
    - for each compiler warning/linter finding vector list the top N most similar vectors from the set of C++ Core Guidelines vectors and print the original compiler warning/linter finding as well as the top N C++ Core Guideline rule titles/bodies
