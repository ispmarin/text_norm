# -*- coding: utf-8 -*-
# __author__ = 'ispmarin'

from unidecode import unidecode
from functools import partial, reduce


def transform_encoding(input_string):
    return unidecode(input_string)

def transform_case(input_string):
    return input_string.lower().strip()

def remove_punctuation(input_string, punctuation):
    return u''.join([ch for ch in input_string if ch not in punctuation])

def remove_stopwords(input_string, stopwords):
    return u' '.join(
        [word for word in input_string.split() if word not in stopwords]
    )

def remove_address_prefixes(input_string, address_prefixes):
    return ' '.join(
        ['' if input_string.split()[0] in address_prefixes else input_string.split()[0]] + input_string.split()[1:]
    ).strip()

def normalize_name(input_string, punctuation, stopwords, prefixes):
    pipeline = [
        transform_encoding,
        transform_case,
        partial(remove_punctuation, punctuation=punctuation),
    ]
    return reduce((lambda value, func: func(value)), pipeline, input_string)

def normalize_address(input_string, punctuation, stopwords, prefixes):
    pipeline = [
        transform_encoding,
        transform_case,
        partial(remove_punctuation, punctuation=punctuation),
        partial(remove_stopwords, stopwords=stopwords),
        partial(remove_address_prefixes, address_prefixes=prefixes)
    ]
    return reduce((lambda value, func: func(value)), pipeline, input_string)
