# __author__ = 'ispmarin'

import jellyfish
from retriever.retrieve import Retrieve


class Matcher:

    def __init__(self, threshold):
        self.threshold = threshold
        self.retriever = Retrieve()

    def match_by_cep(self, df_client, df_correios):
        for index_client, client in df_client.iterrows():
            addresses_correios = df_correios[df_correios.cep == client['cep_norm']]
            matches = {}
            for index_correios, address_correios in addresses_correios.iterrows():
                matches.update(
                     {
                         index_correios: self.compare_address(
                             client['logradouro_norm'],
                             address_correios['log_no_norm']
                         )
                     }
                 )
            sorted_results = sorted(matches.values())
                #sorted(matches.items(), key=operator.itemgetter(1))
            if sorted_results:
                print sorted_results


    def compare_address(self, string_left, string_right):
        return jellyfish.jaro_winkler(unicode(string_left), unicode(string_right))
