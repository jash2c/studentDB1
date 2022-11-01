def read_grade(location):
    '''
    (str) -> list
    Reads the and prints it at the screen.

    '''
    file = open(location, 'r')
    store = []
    line = file.readline()
    
    while line.find('Assignemnt 1 grades')>-1 and line.find('Columns:')>-1 and line.find('ID')>-1 and line.find('Grade')>-1:
        store.append(int(line))

    return store
