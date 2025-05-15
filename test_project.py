
from project import get_amount, get_category, get_difficulty

def test_get_amount(monkeypatch):
    values=iter(["10","11","20","22"])
    monkeypatch.setattr("builtins.input",lambda _:next(values))
    assert get_amount()==10
    assert get_amount()==20


def test_get_category(monkeypatch):
    values=iter(["5","7","10","15","12"])
    monkeypatch.setattr("builtins.input",lambda _:next(values))
    assert get_category()=="geography"
    assert get_category()=="music"
    assert get_category()=="sport_and_leisure"


def test_get_difficulty(monkeypatch):
    values=iter(["1","2","3","-1","11"])
    monkeypatch.setattr("builtins.input",lambda _:next(values))
    assert get_difficulty()=="easy"
    assert get_difficulty()=="medium"
    assert get_difficulty()=="hard"
