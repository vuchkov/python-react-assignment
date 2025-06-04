import os

from nlx.kb import KnowledgeBase


def get_resources_path():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'nlx', 'resources')


def test_search():
    kb = KnowledgeBase(**{
        'PERSON': os.path.join(get_resources_path(), 'people.yml')
    })
    results = kb.search('PERSON', 'Alan Turing')
    assert results[0].score == 1.0
    assert results[0].obj.name == 'Alan Turing'
