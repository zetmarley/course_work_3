from src.main import last_five, last_five_result

def test_last_five():
    for i in last_five():
        assert i["state"] == "EXECUTED"
        assert len(i["from"].split()) >= 2

def test_last_five_result():
    assert last_five_result().count("Перевод") == 5
    assert last_five_result().count("****") == 5
    assert last_five_result().count("->") == 5