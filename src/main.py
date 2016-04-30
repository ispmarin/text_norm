# __author__ = 'ispmarin'

from nltk.corpus import stopwords
import string
from transform.normalizer import *
from transform.parser import *

# Definitions
encoding = "utf-8"
separator_mob = "|"
separator_cor = ","
cep_digits = 8
useful_columns = [0, 12, 13, 15, 26, 27, 28, 29, 30]
column_names = ['tel', 'nome', 'cat', 'cpf', 'end', 'cidade', 'estado', 'uf', 'cep']

text_columns = {'input': 'endereco', 'filtered': 'logradouro'}
text_columns_correios = {'input': 'endereco', 'filtered': 'log_no'}

punctuation = set(string.punctuation)
language = 'portuguese'

prefix_file = '../data/prefixes.csv'

with open(prefix_file, 'r') as g:
    prefixes = g.read().splitlines()
address_prefixes = prefixes


if __name__ == "__main__":

    #test_string="Rua XV de uátiki, 23124 bloco 23"
    test_string="Viela 15 de uátiki, 23124 bloco 23"

    print(normalize_address(test_string, punctuation, stopwords.words(language), address_prefixes))

    print(parse_address(fourth_step))



