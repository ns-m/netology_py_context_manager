from  context_manager_class import MyContextManager
from collections import Counter
from itertools import chain
from pprint import pprint

context_m = MyContextManager()

def count_words():
    with context_m, open('Shakespeare.txt') as hamlet:
        pprint(Counter(chain.from_iterable(map(str.split, hamlet))))


count_words()
