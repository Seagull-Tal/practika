from tinydb import TinyDB
from validator import get_type

def load_templates(path='db.json'):
    db = TinyDB(path)
    return db.all()

def find_template(query_fields, templates):
    query_types = {k: get_type(v) for k, v in query_fields.items()}

    for tpl in templates:
        if "name" not in tpl:
            continue    

        name = tpl["name"]
        fields = {k: v for k, v in tpl.items() if k != "name"}

        if all(k in query_types and query_types[k] == v for k, v in fields.items()):
            return name

    return query_types
