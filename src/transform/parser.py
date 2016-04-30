import re
import math

def parse_address(input_string):
    matched = re.findall(r'^(\S+\D*?)\s*(\d+)|(\S.*)', input_string)
    clean = list(filter(None, [e for l in matched for e in l]))
    return {
        'street': clean[0],
        'number':clean[1],
        'complement':clean[2]
    }

def parse_digits(digits, valid_digits):
    clean_digits = digits.replace("-", "").replace(".", "").zfill(valid_digits)
    if len(clean_digits) > valid_digits:
        return math.nan
    return clean_digits