# __author__ = 'ispmarin'

import numpy as np
import re


def parse_digits(digits, valid_digits):
    clean_digits = digits.replace("-", "").replace(".", "").zfill(valid_digits)
    if len(clean_digits) > valid_digits:
        return np.nan
    return clean_digits


def parse_address(address):
    matched = re.findall(r'^(\S+\D*?)\s*(\d+)|(\S.*)', address)
    clean = filter(None, [e for l in matched for e in l])
    if len(clean) < 3:
        clean.append(np.nan)
    return {'logradouro': clean[0], 'numero':clean[1], 'complemento':clean[2]}
    #return pd.Series(clean, index=['logradouro', 'numero', 'complemento'])
