





def count_vowel(s):
    '''
    (str) -> int
    Return the number of vowels in s. Y is not a vowel.

    >>> count_vowel('Happy Anniversary')
    5
    >>> count_vowel('xyz')
    0
    '''
    vowel_count=0

    for char in s:
        if char in 'aeiouAEIOU':
            vowel_count=vowel_count+1

    return vowel_count



def collect_vowel(s):
    '''
    (str)->str
    Return vowels from s.

    >>> collect_vowel("Happy Anniversary")
    'aAiea'
    >>> collect_vowel('yxz')
    ' '
    '''
    vowel_collector=''

    for char in s:
        if char in 'aeiouAEIOU':
            vowel_collector= vowel_collector + char

    return vowel_collector
