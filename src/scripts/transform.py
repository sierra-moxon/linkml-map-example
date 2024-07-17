from linkml_map.session import Session
import graphviz
from linkml_runtime.utils.schemaview import SchemaView
from pprint import pprint
from linkml_runtime.dumpers import yaml_dumper

# Load the schema
schema_path = "src/linkml_map_example/schema/linkml_map_example.yaml"
sv = SchemaView(schema_path)

# Initialize Session and SchemaBuilder
session = Session()

# Set the source schema in the session
session.set_source_schema(sv)


# Transformer specification (in YAML)
session.set_object_transformer("""
class_derivations:
    Person:
        populated_from: Person
        slot_derivations:
            given_name:
                populated_from: first_name
            family_name:
                populated_from: last_name
            name:
                expr: "{first_name} + ' ' + {last_name}"    
            age_in_months:
                expr: age_in_years * 12
                range: integer
""")

obj = {
        "first_name": "Jane",
        "last_name": "Doe",
        "age_in_years": 25
}

pprint(session.transform(obj))

print(yaml_dumper.dumps(session.target_schema))

dot = session.graphviz()
if isinstance(dot, graphviz.Digraph):
    dot.render('session_graph', format='png', cleanup=True)
    dot.view()
else:
    print("graphviz() did not return a Digraph object.")