#!/usr/bin/env python3

import nltk
import re
import spacy
import string

stopword_list = nltk.corpus.stopwords.words('english')


def tokenize_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = (token.strip() for token in tokens)
    return tokens


def remove_special_characters(text):
    tokens = tokenize_text(text)
    pattern = re.compile('[{}]'.format(re.escape(string.punctuation)))
    filtered_tokens = filter(None, (pattern.sub(' ', token) for token in tokens))
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text


def remove_stopwords(text):
    tokens = tokenize_text(text)
    filtered_tokens = (token for token in tokens if token not in stopword_list)
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text


def normalize_corpus(text):
    text = text.lower()
    text = remove_special_characters(text)
    text = remove_stopwords(text)
    print('normalized: ', text)
    return text

# results with simple models and without modifying the corpus:
# clang warning and matching rule title: 0.37180452569
# clang warning and matching rule body: 0.615830443285
# clang warning and non matching rule title: 0.584492755947
# clang warning and non matching rule body: 0.73593638798

# results with elaborate models, but without modifying the corpus:
# clang warning and matching rule title: 0.533136001684
# clang warning and matching rule body: 0.624059769666
# clang warning and non matching rule title: 0.644608555382
# clang warning and non matching rule body: 0.676429375915

# results with elaborate models and with normalized corpus:
# clang warning and matching rule title: 0.400947974634
# clang warning and matching rule body: 0.6729963775
# clang warning and non matching rule title: 0.644608555382
# clang warning and non matching rule body: 0.733196149819

nlp = spacy.load('en_core_web_lg')  # spacy.load('en')
clang_warning = nlp(normalize_corpus(u'implicit conversion changes signedness'))
matching_rule_title = nlp(normalize_corpus(u'Don\'t use unsigned for subscripts'))
matching_rule_body = nlp(
    normalize_corpus(
        u'To avoid signed/unsigned confusion. To enable better optimization. To enable better error detection.\nThe built-in array uses signed subscripts. The standard-library containers use unsigned subscripts. Thus, no perfect and fully compatible solution is possible. Given the known problems with unsigned and signed/unsigned mixtures, better stick to (signed) integers.\nAlternatives for users:\n- use algorithms\n- use range-for\n- use iterators/pointers'))
non_matching_rule_title = nlp(normalize_corpus(u'Avoid global variables'))
non_matching_rule_body = nlp(
    normalize_corpus(
        u'Non-const global variables hide dependencies and make the dependencies subject to unpredictable changes.\nWho else might modify data?\nGlobal constants are useful.\nThe rule against global variables applies to namespace scope variables as well.\nAlternative: If you use global (more generally namespace scope) data to avoid copying, consider passing the data as an object by reference to const. Another solution is to define the data as the state of some object and the operations as member functions.\nWarning: Beware of data races: If one thread can access nonlocal data (or data passed by reference) while another thread executes the callee, we can have a data race. Every pointer or reference to mutable data is a potential data race.\nYou cannot have a race condition on immutable data.\nReferences: See the rules for calling functions.'))

# print(clang_warning.similarity(matching_rule_title))
# print(clang_warning.similarity(matching_rule_body))
# print(clang_warning.similarity(non_matching_rule_title))
# print(clang_warning.similarity(non_matching_rule_body))
