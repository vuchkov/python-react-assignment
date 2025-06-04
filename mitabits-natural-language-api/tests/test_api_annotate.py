import json


def request_annotate(client, text):
    return client.post("/api/annotate", json={"text": text}, follow_redirects=True)


def test_annotate(client):
    text = (
        "Alan Turing was born on 23/06/1912. "
        "During the Second World War, he worked as a scientist for the Government Code and Cypher School "
        "(currently GCHQ) at Bletchley Park, Britain's codebreaking centre that produced Ultra intelligence."
    )
    response = request_annotate(client, text)
    result = json.loads(response.data)
    assert result['text'] == text
    assert len(result['mentions']) == 3
    assert any(m['type'] == 'PERSON' and m['content'] == 'Alan Turing' for m in result['mentions'])
    assert any(m['type'] == 'DATE' and m['content'] == '23/06/1912' for m in result['mentions'])
    assert any(m['type'] == 'ORGANISATION' and m['content'] == 'GCHQ' for m in result['mentions'])


def test_annotate_empty(client):
    text = ""
    response = request_annotate(client, text)
    result = json.loads(response.data)
    assert result['text'] == text
    assert len(result['mentions']) == 0
