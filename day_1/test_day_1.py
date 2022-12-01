from day_1 import process_data

########## TESTS ############
sample_data = '''
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''
def test_max_calories():
    assert max(process_data(sample_data)) == 24000
