
student_dump=[]

def data_entry():
    container = []
    temp_list= []
    while True:
        idnum=input('Enter ID #: ')
        while not idnum.isdigit():
            idnum=input('Enter ID#: ')
        temp_list.append(idnum)
        
        fname=input('First Name: ')
        while not fname.isalpha():
            fname=input('Enter a first name: ')
        temp_list.append(fname)

        lname=input('Last Name: ')
        while not lname.isalpha():
            lname=input('Enter a last name: ')
        temp_list.append(lname)

        container.append(temp_list)
        temp_list=[]

        print('Student file is complete. \n')
        choice = input('Do you want to register another student? Y/N : ')
        if choice.upper() == 'N':
            break
        while not choice in 'YyNn':
            choice=input('Enter Y or N! ')
        
    for element in container:
        print(element)
        
    return container

def search():
    print('''
    Welcome to the Search Function of the Student DB by Joaquin''')
    
    searchitem=input('Enter ID#: ')
    while not searchitem.isdigit():
        searchitem=input('Enter ID#: ')

    for element in student_dump:
        for i in element:
            if not not i==searchitem:
                print('Found!')
                print(element)
    main()




def main():
    print('''
    Welcome to Student DB by Joaquin

    Please choose from the following options:

        A. Enter New Student

        B. Search Student

        ''')
    choice=input('What would like to do? ')

    if choice.upper() =='A':
        temp=[]
        temp=data_entry()
        student_dump.append(temp)
        for element in student_dump:
            print(element)
        main()

    if choice.upper()== 'B':
        search()
        main()
    if choice.upper!='A' or choice.upper!='B':
        print('''Student DB is unable to process the request due to the option selected being out of what is accepted by the program so far. Please choice either A or B.''')
        main()

    
main()

print('to the developer: things to do, make sure student dump receives container by running a for loop. Adjust after the fact.')
      
