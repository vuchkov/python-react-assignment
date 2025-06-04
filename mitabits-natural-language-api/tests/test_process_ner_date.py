from datetime import datetime

from nlx.process.components.ner import DateAnnotator
from nlx.process.core import Document


def test_ner_date():
    c = DateAnnotator()
    today = datetime.today()
    today_dmy = today.strftime("%d/%m/%Y")
    today_iso = today.date().isoformat()
    doc = Document(text="Today is %s" % today_dmy)
    c.process_document(doc)
    assert len(doc.mentions) == 1
    assert doc.mentions[0].entity_type.name == 'DATE'
    assert doc.mentions[0].content == today_dmy
    assert doc.mentions[0].metadata['iso_date'] == today_iso
