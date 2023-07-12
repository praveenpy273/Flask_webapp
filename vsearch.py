def search4vowels(phrase: str) -> set:
    """Display any vowels found in a word"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return the letters which are common with phrase"""
    return set(letters).intersection(set(phrase))