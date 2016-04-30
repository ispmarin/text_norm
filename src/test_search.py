from retrieve.search import *

doc1 = {'street': 'pindamonhagaba', 'number':123, 'complement':'bloco 22', 'cep':'02837-223', 'city':'São Paulo'}
doc2 = {'street': 'pindamonhagaba madura', 'number':123, 'complement':'bloco 22', 'cep':'02833-023', 'city':'São Paulo'}
doc3 = {'street': 'pindamonhangaba', 'number':123, 'complement':'bloco 22', 'cep':'02833-023', 'city':'São Paulo'}

schema = create_schema()
idx = create_index(schema)
add_documents([doc1, doc2, doc3], idx)
results = search('pindamonhagaba', 'street', idx)
print(results)

