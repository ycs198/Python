#!/usr/bin/python
def search_for_vowels(phrase):
    """adding the new value example program """
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))
search_for_vowels('bala')