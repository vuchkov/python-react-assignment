# Add to imports
from src.annotators.role_annotator import RoleAnnotator

# Add to the annotators list
annotators = [
    DateAnnotator(),
    PersonAnnotator(),
    OrganizationAnnotator(),
    RoleAnnotator()  # New annotator
]
