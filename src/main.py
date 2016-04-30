# __author__ = 'ispmarin'

import argparse
import codecs
from functools import partial

import pandas as pd
from match.address_matcher import Matcher
from normalization.normalizer import Normalizer
from retriever.retrieve import Retrieve

from src.parser import parse_digits, parse_address

# Definitions
encoding = "utf-8"
separator_mob = "|"
separator_cor = ","
cep_digits = 8
cpf_digits = 11
tel_digits = 12
useful_columns = [0, 12, 13, 15, 26, 27, 28, 29, 30]
column_names = ['tel', 'nome', 'cat', 'cpf', 'end', 'cidade', 'estado', 'uf', 'cep']

text_columns = {'input': 'endereco', 'filtered': 'logradouro'}
text_columns_correios = {'input': 'endereco', 'filtered': 'log_no'}

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Household')
    parser.add_argument('-c', '--filename_clients', help='Client data')
    parser.add_argument('-s', '--stopwords', help='Stopword file')
    parser.add_argument('-p', '--prefixes', help='Prefixes file')
    args = parser.parse_args()

    with codecs.open(args.stopwords, 'r', encoding=encoding) as f:
        stopwords = f.read().splitlines()

    with codecs.open(args.prefixes, 'r', encoding=encoding) as g:
        prefixes = g.read().splitlines()

    normalizer = Normalizer(encoding, stopwords, prefixes)
    parse_cpf_digits = partial(parse_digits, valid_digits=cpf_digits)
    parse_cep_digits = partial(parse_digits, valid_digits=cep_digits)
    parse_tel_digits = partial(parse_digits, valid_digits=tel_digits)
    retriever = Retrieve()
    matcher = Matcher(0.5)

    # df_correios = pd.read_csv(
    #     args.filename_base_correios,
    #     encoding=encoding,
    #     dtype=unicode,
    #     sep=separator
    # )

    df_input = pd.read_csv(
        args.filename_clients,
        encoding=encoding,
        dtype=unicode,
        sep=separator_mob,
        header=None,
        usecols=useful_columns,
        names=column_names
    )

    df_input['name_norm'] = df_input['nome'].apply(normalizer.normalize_name)
    df_input['end_norm'] = df_input['end'].apply(normalizer.normalize_address)
    df_input['cpf_norm'] = df_input['cpf'].apply(parse_cpf_digits)
    df_input['cep_norm'] = df_input['cep'].apply(parse_cep_digits)
    df_input['tel_norm'] = df_input['tel'].apply(parse_tel_digits)
    a = df_input['end'].apply(parse_address)
    print df_input.columns
    #df_input.columns = df_input.columns.str.strip().str.lower()

    # def parse_df_stopwords(self, df_input):
    #     new_column = self.text_columns['filtered'] + '_norm'
    #     df_input[new_column] = df_input[self.text_columns['filtered']].apply(
    #         self.remove_punctuation
    #     )
    #     df_input[new_column] = df_input[new_column].apply(
    #         self.remove_stopwords,
    #         args=(self.all_stopwords,)
    #     )
    #     return df_input
    #
    # def parse_df_address(self, df_input):
    #     df_input['logradouro'], df_input['numero'], df_input['complemento'] = \
    #         zip(*df_input[self.text_columns['input']].map(self.parse_address))
    #     return df_input
    #
    # def parse_df_numbers(self, df_input):
    #     for column, valid_digit in self.digit_columns.items():
    #         new_column = column + '_norm'
    #         df_input[new_column] = df_input[column].apply(
    #             self.parse_digits,
    #             args=(valid_digit,)
    #         )
    #     return df_input


    # df_normalized = parser.parse(df_normalized)
    # df_correios = df_correios[df_correios.UFE_SG == 'RS']
    # df_correios_normalized = normalizer.normalize(df_correios)
    # df_correios_normalized = parser_correios.parse_df_stopwords(df_correios_normalized)
    # print matcher.match_by_cep(df_normalized, df_correios_normalized)





