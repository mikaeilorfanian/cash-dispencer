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

@pytest.mark.parametrize(
    'two_digit_number,correct_result',
    [
        ('20', [20]),
        ('50', [50]),
        ('60', [50, 10]),
        ('90', [50, 20, 20]),
        ('30', [20, 10]),
    ],
)
def test_two_digit_numbers(two_digit_number, correct_result):
    assert dispence(two_digit_number) == correct_result

def make_expected_results(num_of_100s, *other_nums):
    res = [100 for i in range(num_of_100s)]
    res.extend(other_nums)

    return res


@pytest.mark.parametrize(
    'large_num,correct_result',
    [
        ('100', [100]),
        ('110', [100, 10]),
        ('180', [100, 50, 20, 10]),
        ('10000', make_expected_results(100)),
        ('100010', make_expected_results(1000, 10)),
        ('001010', make_expected_results(10, 10)),
        ('0110', [100, 10]),
    ],
)
def test_large_numbers(large_num, correct_result):
    assert dispence(large_num) == correct_result
