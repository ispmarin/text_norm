from retrieve.search import *

doc1 = {
    'street': 'XV de novembro',
    'number': 123,
    'complement': 'bloco 22',
    'cep': '02837-223',
    'city': 'São Paulo'
}
doc2 = {
    'street': 'XV de piracicaba',
    'number': 123,
    'cep': '02833-023',
    'city': 'São Paulo'
}

doc3 = {
    'street': 'Grande marcha de novembro',
    'number': 123,
    'complement': 'bloco 22',
    'cep': '02833-023',
    'city': 'São Paulo'
}

schema = create_schema()
idx = create_index(schema, 'indexdir')
add_documents([doc1, doc2, doc3], idx)
results = search('pindamonhaga', 'street', idx)
print(results)

