from day_3 import (  
    process_data
)

sample_data = '''
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''

def get_test_data(data: str) -> list:
    return process_data(data)

def test_process_data():
    assert get_test_data(sample_data) == [
        ['vJrwpWtwJgWr', 'hcsFMMfFFhFp'],
        ['jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL'],
        ['PmmdzqPrV', 'vPwwTWBwg'],
        ['wMqvLMZHhHMvwLH', 'jbvcjnnSBnvTQFn'],
        ['ttgJtRGJ', 'QctTZtZT'],
        ['CrZsJsPPZsGz', 'wwsLwLmpwMDw'],
    ]

