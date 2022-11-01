def up_to_vowel(s):
    '''
    (str) -> str

    Return a substring of a s from index 0 up to but not including the 1st vowel in s.

    '''
    before_vowel=''
    i=0

    while i<len(s) and not(s[i] in 'aeiouAEIOU'):
        before_vowel = before_vowel+s[i]
        i=i+1


    return before_vowel
    
def get_answer(prompt):
    answer=input(prompt)

    while not (answer == 'yes' or answer == 'no'):
        answer = input(prompt)

    return answer

def double_even_indices(lst):
    i = 0
    while i<len(lst):
        lst[i] = lst[i]*2
        i = i+2
def count_adjacent_repeats(s):
    repeats = 0
    for i in range(len(s)-1):
        if s[i]== s[i+1]:
            repeats = repeats + 1

    return repeats

def shift_left(L):
    first_item = L[0]
    for i in range(1,len(L)):
        L[i-1]=L[i]

    L[-1]=first_item

def sum_items(list1,list2):
    '''(list of number, list of number) -> list of number
    Return a new list in whihc each item is the sum of the items at the corresponding positions of list 1 and list 2.
    Precondition: len(list1)==len(list2)
    '''
    sum_list=[]
    for i in range(len(list1)):
        sum_list.append(list1[i]+list2[i])

    return sum_list

def count_matches(s1,s2):
    '''(str,str)-> int
    Returns the number of positions in s1 that contain the same character at the corresponding position in s2.
    Precondition: len(s1)== len(s2)
    '''
    num_matches=0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            num_matches = num_matches+1

    return num_matches

def calculate_average(asn_grades):
    '''(list of list of [str, number]) -> float
    Returns the aveage of the grades in asn_grades.
    '''
    total = 0

    for item in asn_grades:
        total=total+item[1]

    return total/len(asn_grades)

def averages(grades):
    '''
    (list of list of number) -> list of float

    >>> average([70,75,80],[70,80,90,100],[80,100]
    [75.0,85.0,90.0]

    '''
    averages=[]

    for grades_list in grades:
        #calc ave of grades and append it
        total = 0
        for mark in grades_list:
            total = total + mark

        averages.append(total/len(grades_list))
    return averages
