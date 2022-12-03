from day_3 import (  
    process_data,
    get_dupe_item,
    encode_char_to_int
)

sample_data = '''
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''

def get_test_data() -> list:
    return process_data(sample_data)

def test_process_data():
    assert get_test_data() == [
        ['vJrwpWtwJgWr', 'hcsFMMfFFhFp'],
        ['jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL'],
        ['PmmdzqPrV', 'vPwwTWBwg'],
        ['wMqvLMZHhHMvwLH', 'jbvcjnnSBnvTQFn'],
        ['ttgJtRGJ', 'QctTZtZT'],
        ['CrZsJsPPZsGz', 'wwsLwLmpwMDw'],
    ]

def test_get_dupe_item():
    data = get_test_data()
    assert get_dupe_item(data[0]) == 'p'

def test_encode_char_to_int():
    data = get_test_data()
    char = get_dupe_item(data[0])
    assert encode_char_to_int(char) == 16 # "p".charCode() - 96
