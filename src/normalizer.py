# -*- coding: utf-8 -*-
# __author__ = 'ispmarin'
# 2015-10-29
# Telefonica Data Labs

from unidecode import unidecode
import string


class Normalizer:

    def __init__(self, encoding, stopwords, prefixes):
        self.encoding = encoding
        self.stopwords = stopwords
        self.prefixes = prefixes
        self.punctuation = set(unicode(string.punctuation.decode()))

    @staticmethod
    def convert_to_unicode(input_string):
        if type(input_string) == unicode:
            return input_string
        return unicode(input_string)

    def remove_punctuation(self, string_input):
        return u''.join([ch for ch in string_input if ch not in self.punctuation])

    def remove_stopwords(self, string_input):
        return u' '.join(
            [word for word in string_input.split() if word not in self.stopwords]
        )

    def remove_address_prefixes(self, string_input):
        print string_input
        return u' '.join(
            [u'' if string_input.split()[0] in self.prefixes else string_input.split()[0]] + string_input.split()[1:]
        ).strip()

    def normalize_name(self, input_string):
        return self.convert_to_unicode(
            self.remove_punctuation(
                input_string.lower().strip()
            )
        )

    def normalize_address(self, input_string):
        return self.remove_address_prefixes(
            self.remove_stopwords(
                self.remove_punctuation(
                    self.convert_to_unicode(
                        input_string.lower().strip()
                    )
                )
            )
        )


