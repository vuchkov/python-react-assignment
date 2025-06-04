import json


def test_search(client):
    response = client.get("/api/kb/person/search?q=Alan+Turing")
    results = json.loads(response.data)
    assert len(results) == 1
    assert results[0]['object']['name'] == "Alan Turing"


def test_search_empty(client):
    response = client.get("/api/kb/person/search?q=")
    results = json.loads(response.data)
    assert len(results) == 0
