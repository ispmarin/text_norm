import whoosh.index as index
from whoosh.fields import Schema, TEXT, STORED, NUMERIC, ID
from whoosh.qparser import QueryParser

def create_schema():
    return Schema(
        id=ID(stored=True, unique=True),
        street=TEXT(stored=True),
        complement=TEXT(stored=True),
        number=NUMERIC(stored=True),
        cep=TEXT(stored=True),
        city=TEXT(stored=True),
        state=TEXT(stored=True)
)
def create_index(schema):
    return index.create_in("indexdir", schema=schema)

def add_documents(documents, s_index):
    writer = s_index.writer()
    for doc in documents:
        writer.add_document(
            street=doc.get('street'),
            complement=doc.get('complement'),
            number=doc.get('number'),
            cep=doc.get('cep'),
            city=doc.get('city'),
            state=doc.get('state')
        )
    writer.commit()

def search(query_string, search_field, s_index):
    qp = QueryParser(search_field, schema=s_index.schema)
    q = qp.parse(query_string)
    result_list = []
    with s_index.searcher() as s:
        results = s.search(q)
        for result in results:
            result_list.append(dict(result))
    return result_list





