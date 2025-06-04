import re
from datetime import datetime

from nlx.process.core import PipelineComponent, EntityType


class EntityAnnotator(PipelineComponent):
    entity_types = None

    def add_mention(self, doc, begin_offset, end_offset, entity_type=None, metadata=None):
        if entity_type is None and len(self.entity_types) != 1:
            raise ValueError("Invalid entity type!")

        if entity_type:
            et = entity_type
        else:
            et = self.entity_types[0]

        if et is None:
            raise ValueError("entity type is not provided for %s" % self.__class__.__name__)
        doc.add_mention(et, begin_offset, end_offset, metadata=metadata)

    def process_document(self, doc):
        raise NotImplementedError("not implemented")


class DateAnnotator(EntityAnnotator):
    entity_types = [EntityType.DATE]

    def process_document(self, doc):
        for m in re.finditer(r'\d{2}/\d{2}/\d{4}', doc.text, re.IGNORECASE):
            self.add_mention(doc, *m.span(0), metadata={
                "iso_date": datetime.strptime(m.group(0), "%d/%m/%Y").date().isoformat()
            })


class PersonAnnotator(EntityAnnotator):
    entity_types = [EntityType.PERSON]

    def process_document(self, doc):
        for name in ['Alan Turing', ]:
            for m in re.finditer(name, doc.text):
                self.add_mention(doc, *m.span(0))


class OrganisationAnnotator(EntityAnnotator):
    entity_types = [EntityType.ORGANISATION]

    def process_document(self, doc):
        for org in ['GCHQ', ]:
            for m in re.finditer(org, doc.text):
                self.add_mention(doc, *m.span(0))
