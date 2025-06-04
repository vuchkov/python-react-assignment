from enum import Enum


class EntityType(Enum):
    DATE = 1
    PERSON = 2
    ORGANISATION = 3
    ROLE = 4


class Mention(object):
    def __init__(self, entity_type, content, begin_offset, end_offset, metadata=None):
        self.entity_type = entity_type
        self.content = content
        self.begin_offset = begin_offset
        self.end_offset = end_offset
        self.metadata = metadata

    def as_dict(self):
        kwargs = {}
        if self.metadata:
            if hasattr(self.metadata, 'as_dict'):
                kwargs['metadata'] = self.metadata.as_dict()
            elif isinstance(self.metadata, dict):
                kwargs['metadata'] = self.metadata
            else:
                raise ValueError("Invalid metadata format! Supposed to be dict or object with as_dict() method")

        return dict(type=self.entity_type.name, content=self.content,
                    begin_offset=self.begin_offset, end_offset=self.end_offset, **kwargs)


class Document(object):
    def __init__(self, text):
        super().__init__()
        self._text = text
        self._mentions = []

    def as_dict(self):
        return dict(text=self.text, mentions=[m.as_dict() for m in self.mentions])

    @property
    def text(self):
        return self._text

    @property
    def mentions(self):
        return self._mentions

    def add_mention(self, entity_type, begin_offset, end_offset, metadata):
        self._mentions.append(Mention(entity_type=entity_type, content=self.text[begin_offset:end_offset],
                                      begin_offset=begin_offset, end_offset=end_offset, metadata=metadata))


class Pipeline(object):
    document_class = Document

    def __init__(self, components):
        super().__init__()
        self.components = components

    def add_component(self, component):
        self.components.append(component)

    def process_text(self, text):
        doc = self.document_class(text)
        self.process_document(doc)
        return doc

    def process_document(self, doc):
        for c in self.components:
            c.process_document(doc)
        return doc


class PipelineComponent(object):
    def __init__(self):
        super().__init__()

    def process_document(self, doc):
        raise NotImplementedError("not implemented")
