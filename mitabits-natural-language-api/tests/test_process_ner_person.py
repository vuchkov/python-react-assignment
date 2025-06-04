from nlx.process.components.ner import PersonAnnotator
from nlx.process.core import Document


def test_ner_person():
    c = PersonAnnotator()
    doc = Document(text="My name is Alan Turing")
    c.process_document(doc)
    assert len(doc.mentions) == 1
    assert doc.mentions[0].entity_type.name == 'PERSON'
    assert doc.mentions[0].content == 'Alan Turing'
