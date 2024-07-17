from typing import List

from linkml_map.session import Session
from linkml_model.meta import ClassDefinition
import yaml
from linkml.utils.schema_builder import SchemaBuilder
from linkml_runtime.utils.schemaview import SchemaView
import requests
import tempfile
from pprint import pprint

# URL of the schema
# Load the schema
schema_url = "https://raw.githubusercontent.com/biolink/biolink-model/master/biolink-model.yaml"

# Fetch the schema from the URL
response = requests.get(schema_url)
response.raise_for_status()  # Raise an error for bad status codes

# Load the schema content into SchemaView
schema_content = response.text

with tempfile.NamedTemporaryFile(delete=False, suffix='.yaml') as temp_file:
    temp_file.write(schema_content.encode())
    temp_file_path = temp_file.name

sv = SchemaView(temp_file_path)
# Load the schema
sv = SchemaView(schema_content)

# Initialize Session and SchemaBuilder
session = Session()

# Set the source schema in the session
session.set_source_schema(sv)

SUBSET_CLASSES = ["gene",
                  "disease",
                  "case to phenotypic feature association",
                  "gene to disease association",
                  "gene to phenotypic feature association",
                  "case",
                  "phenotypic feature",
                  ]


# Function to get Biolink class definitions
def get_biolink_classes_definitions(sv, subset_classes) -> List[ClassDefinition]:
    # Example implementation to fetch class definitions
    # This should be replaced with the actual implementation
    class_definitions = []
    for class_name in subset_classes:
        class_def = sv.induced_class(class_name)
        class_definitions.append(class_def)
    return class_definitions


# Function to build subset schema
def build_subset_schema(class_defs: List[ClassDefinition]) -> SchemaBuilder:
    sb = SchemaBuilder(name="SubsetSchema", id="https://example.org/SubsetSchema")
    for class_def in class_defs:
        for slot_def in class_def.slots:
            sb.add_slot(slot_def)
        sb.add_class(class_def)
    sb.add_defaults()
    return sb


class_definitions = get_biolink_classes_definitions(sv, SUBSET_CLASSES)
built_schema = build_subset_schema(class_definitions)
built_schema.prefixes = sv.schema.prefixes
output_file_path = "subset_schema.yaml"
with open(output_file_path, "w") as file:
    yaml.dump(built_schema.as_dict(), file, sort_keys=False)


# Transformer specification (in YAML)
session.set_object_transformer("""
class_derivations:
    GeneToDiseaseAssociation:
        populated_from: GeneToDiseaseAssociation
    GeneToPhenotypicFeatureAssociation:
        populated_from: GeneToPhenotypicFeatureAssociation
    Disease:
        populated_from: Disease
    PhenotypicFeature:
        populated_from: PhenotypicFeature
    Case:
        populated_from: Person
    Gene:
        populated_from: Gene
    CaseToPhenotypicFeatureAssociation:
        populated_from: CaseToPhenotypicFeatureAssociation
""")


#
# dot = session.graphviz()
# if isinstance(dot, graphviz.Digraph):
#     dot.render('session_graph', format='png', cleanup=True)
#     dot.view()
# else:
#     print("graphviz() did not return a Digraph object.")
