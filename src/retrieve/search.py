import os
from whoosh.fields import Schema, TEXT, NUMERIC, ID
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser
from whoosh.query import FuzzyTerm


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


def create_index(schema, index_path):
    if os.path.exists(index_path):
        return open_dir(index_path)
    else:
        os.mkdir(index_path)
        return create_in(index_path, schema)


def add_documents(documents, s_index):
    writer = s_index.writer()
    for doc in documents:
        writer.update_document(
            street=doc.get('street'),
            complement=doc.get('complement'),
            number=doc.get('number'),
            cep=doc.get('cep'),
            city=doc.get('city'),
            state=doc.get('state')
        )
    writer.commit()


class GeralFuzzyTerm(FuzzyTerm):
    def __init__(
            self,
            fieldname,
            text,
            boost=1.0,
            maxdist=2,
            prefixlength=1,
            constantscore=True
    ): super(GeralFuzzyTerm, self).__init__(
        fieldname, text, boost, maxdist, prefixlength, constantscore
    )


def search(query_string, search_field, s_index):
    qp = QueryParser(search_field, schema=s_index.schema, termclass=GeralFuzzyTerm)
    q = qp.parse(query_string)
    result_list = []
    with s_index.searcher() as s:
        results = s.search(q)
        print(list(q.docs(s)))
        for result in results:
            result_list.append(dict(result))
    return result_list


def all_documents(s_index):
    return s_index.searcher().documents()