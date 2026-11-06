from datetime import date, timedelta
from catalog import WORDS, todays_word


def test_same_day_same_word():
    day = date(2026, 11, 5)
    assert todays_word(day) == todays_word(day)


def test_next_day_rotates():
    day = date(2026, 11, 5)
    assert todays_word(day) != todays_word(day + timedelta(days=1))


def test_every_concept_has_a_resource():
    for word in WORDS:
        assert word['resources']
        assert all(r['url'].startswith('https://') for r in word['resources'])
