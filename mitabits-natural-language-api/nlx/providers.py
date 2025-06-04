import os

from nlx.kb import KnowledgeBase
from nlx.pipelines.default import DefaultPipeline
from nlx.process import EntityType


class ServiceProvider(object):
    def __init__(self, resources_path):
        self._resources_path = resources_path
        self.kb = self.init_knowledge_base()
        self.nlp = self.init_pipeline()

    def init_pipeline(self):
        raise NotImplementedError("not implemented")

    def init_knowledge_base(self):
        raise NotImplementedError("not implemented")


class DefaultServiceProvider(ServiceProvider):
    def init_knowledge_base(self):
        return KnowledgeBase(**{
            EntityType.PERSON.name: os.path.join(self._resources_path, "people.yml"),
            EntityType.ORGANISATION.name: os.path.join(self._resources_path, "organisations.yml"),
        })

    def init_pipeline(self):
        return DefaultPipeline()
