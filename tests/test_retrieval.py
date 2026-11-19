from kisansaathi.retrieval import retrieve_notes

def test_retrieval_returns_relevant_notes():
    notes = [
        "Yellowing and leaf spots can have many causes.",
        "Check soil moisture and standing water.",
        "Consult an agriculture officer for rapidly spreading symptoms."
    ]
    result = retrieve_notes("yellow spots on leaves", notes)
    assert result
    assert "Yellowing" in result[0]["text"]

def test_empty_query_returns_no_notes():
    assert retrieve_notes("", ["some note"]) == []
