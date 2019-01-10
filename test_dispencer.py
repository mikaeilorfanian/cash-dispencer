import pytest

from dispencer_engine import dispence, InvalidArgumentException, NoteUnavailableException


def test_simple_cases():
    assert dispence('0') == []
    assert dispence('') == []
    assert dispence('10') == [10]


@pytest.mark.parametrize(
    'invalid_number',
    [
        '-1',
        '-10',
        '-2.5',
        '12ab100',
        '1b',
        'cd',
    ],
)
def test_invalid_numbers(invalid_number):
    with pytest.raises(InvalidArgumentException):
        dispence(invalid_number)


@pytest.mark.parametrize(
    'unavailable_number',
    [
        '5',
        '2',
        '1',
        '15',
        '21',
        '123452',
        '0.1',
        '123.5',
        '01234.1'
    ],
)
def test_invalid_numbers(unavailable_number):
    with pytest.raises(NoteUnavailableException):
        dispence(unavailable_number)
