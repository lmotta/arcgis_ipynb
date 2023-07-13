import json
from collections import namedtuple

Credential = namedtuple('Credential', ['host', 'user', 'pwd'] )
cred = lambda d, k:  Credential( d[k]['host'], d[k]['user'], d[k]['pwd'] )

def credential(credential_json):
    """
    Return Credentials: cred_agol, cred_prod, cred_hom
    """
    cred_agol, cred_prod, cred_hom = None, None, None
    with open(credential_json, 'r' ) as f:
        d = json.load( f )
        cred_agol = cred( d, 'agol_ibama' )
        cred_prod = cred( d, 'prod_ibama' )
        cred_hom  = cred( d, 'hom_ibama' )
    
    return cred_agol, cred_prod, cred_hom
