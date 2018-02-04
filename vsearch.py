def search4vowels(phrase):
    """Return any Vowels found in a supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search4letters(phrase,letters='aeiou'):
    """Return a set of letters found in phrase"""
    return set(letters).intersection(set(phrase))
