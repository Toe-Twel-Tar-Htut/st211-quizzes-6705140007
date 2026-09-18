def test_addition():
    assert 1 + 1 == 2

def test_string():
    assert "hello".upper() == "HELLO"

def test_list_length():
    fruits = ["apple", "banana", "cherry"]
    assert len(fruits) == 3


def count_vowels(s: str) -> int:
    return sum(1 for char in s.lower() if char in 'aeiou')