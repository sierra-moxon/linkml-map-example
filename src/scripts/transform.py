from linkml_map.session import Session
import graphviz
from linkml_runtime.utils.schemaview import SchemaView

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
        id:
            populated_from: id
        given_name:
            populated_from: first_name
        family_name:
            populated_from: last_name
  PersonCollection:
        populated_from: PersonCollection
""")

obj = {
        "given_name": "Jane",
        "family_name": "Doe",
    }

session.transform(obj)

# # Generate and save the graphviz visualization
# dot = session.graphviz().source  # Ensure that this returns the DOT source
# graph = graphviz.Source(dot)
# graph.render('session_graph', format='png', cleanup=True)
# graph.view()

dot = session.graphviz()
if isinstance(dot, graphviz.Digraph):
    dot.render('session_graph', format='png', cleanup=True)
    dot.view()
else:
    print("graphviz() did not return a Digraph object.")