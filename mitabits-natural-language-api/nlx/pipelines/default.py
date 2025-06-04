from nlx.process import Pipeline
from nlx.process.components import DateAnnotator, PersonAnnotator, OrganisationAnnotator


class DefaultPipeline(Pipeline):
    def __init__(self, components=None):
        if components is None or len(components) == 0:
            components = self.get_default_components()
        super().__init__(components)

    def get_default_components(self):
        return [DateAnnotator(), PersonAnnotator(), OrganisationAnnotator()]
