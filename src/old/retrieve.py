
class Retrieve:

    def __init__(self):
        pass

    def retrieve_addresses_from_cep(self, nr_cep, cep_col, df):
        return df[df[cep_col] == nr_cep]
