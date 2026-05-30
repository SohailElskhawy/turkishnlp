import pytest
from turkishnlp.detector import TurkishNLP


@pytest.fixture(scope="session")
def nlp():
    """Session-scoped fixture: loads word data once (data pre-downloaded via run_once_setup.py)."""
    t = TurkishNLP()
    t.create_word_set()
    return t


def test_TC01_vowel_harmonic_hard_vowels(nlp):
    """TC-01: word with only hard vowels returns True (EP)."""
    assert nlp.is_vowel_harmonic("araba") is True


def test_TC02_vowel_harmonic_mixed_vowels(nlp):
    """TC-02: word mixing hard and soft vowels returns False (EP)."""
    assert nlp.is_vowel_harmonic("kitap") is False


def test_TC03_vowel_harmonic_empty_string(nlp):
    """TC-03: empty string returns True (BVA - length 0 boundary)."""
    assert nlp.is_vowel_harmonic("") is True


def test_TC04_is_turkish_true(nlp):
    """TC-04: clear Turkish text returns True (EP)."""
    assert nlp.is_turkish("Merhaba nasılsın") is True


def test_TC05_is_turkish_false_english(nlp):
    """TC-05: English text returns False (EP)."""
    assert nlp.is_turkish("Hello how are you") is False


def test_TC06_is_turkish_origin_true(nlp):
    """TC-06: known Turkish-origin word returns True (EP)."""
    assert nlp.is_turkish_origin("yazılım") is True

def test_TC07_is_turkish_origin_invalid_type(nlp):
    """TC-07: integer input raises AttributeError (EP - invalid partition)."""
    with pytest.raises((AttributeError, TypeError)):
        nlp.is_turkish_origin(123)
        
        
def test_TC08_syllabicate_sentence_merhaba(nlp):
    """TC-08: 'merhaba' syllabicates correctly (BVA - single word)."""
    result = nlp.syllabicate_sentence("merhaba")
    assert len(result) == 1
    assert "".join(result[0]) == "merhaba"

def test_TC09_syllabicate_sentence_empty(nlp):
    """TC-09: empty string returns empty list (BVA - length 0 boundary)."""
    assert nlp.syllabicate_sentence("") == []

def test_TC10_syllabicate_sentence_single_letter(nlp):
    """TC-10: single-letter word 'O' returns a nested list (BVA - min valid word)."""
    result = nlp.syllabicate_sentence("O")
    assert len(result) == 1
    
    
def test_TC11_syllabicate_vowel_then_consonant(nlp):
    """TC-11: 'al' - vowel followed by consonant (Path P2)."""
    result = nlp.syllabicate("al")
    assert isinstance(result, list)
    assert "".join(result) == "al"

def test_TC12_syllabicate_single_vowel(nlp):
    """TC-12: 'o' - single vowel, end of string (Path P3)."""
    result = nlp.syllabicate("o")
    assert isinstance(result, list)
    assert len(result) >= 1

def test_TC13_syllabicate_empty_string(nlp):
    """TC-13: empty string - loop never entered (Path P1)."""
    result = nlp.syllabicate("")
    assert result == [""]

def test_TC14_syllabicate_single_consonant(nlp):
    """TC-14: 'k' - starts with consonant (Path P4)."""
    result = nlp.syllabicate("k")
    assert isinstance(result, list)
    assert len(result) >= 1