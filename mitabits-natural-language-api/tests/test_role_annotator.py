import pytest
from src.annotators.role_annotator import RoleAnnotator


@pytest.fixture
def role_annotator():
    return RoleAnnotator()


def test_role_detection(role_annotator):
    text = "She works as a software developer and researcher."
    results = role_annotator.annotate(text)

    assert len(results) == 2
    assert results[0]["content"] == "software developer"
    assert results[0]["type"] == "ROLE"
    assert results[1]["content"] == "researcher"


def test_case_insensitivity(role_annotator):
    text = "Jobs: Engineer, PROFESSOR, and Doctor."
    results = role_annotator.annotate(text)

    assert len(results) == 3
    assert {r["content"].lower() for r in results} == {"engineer", "professor", "doctor"}


def test_word_boundaries(role_annotator):
    text = "A bioengineer is different from an engineer."
    results = role_annotator.annotate(text)

    assert len(results) == 1
    assert results[0]["content"] == "engineer"


def test_no_false_positives(role_annotator):
    text = "The scientist visited the science museum."
    results = role_annotator.annotate(text)

    assert len(results) == 1
    assert results[0]["content"] == "scientist"
