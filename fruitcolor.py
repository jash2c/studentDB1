def fruit_color(fruit):
    if fruit == 'apple':
        return 'red'
    elif fruit == 'banana':
        return 'yellow'
    elif fruit == 'pear':
        return 'green'

def traffic_report(light):
    if light == 'red':
        return 'stop'
    elif light == 'yellow':
        return 'slow'
    elif light == 'green':
        return 'go'

def grade_report(grade):
    if grade >= 80:
        return 'excellent'
    elif grade >= 50:
        return 'pass'

def grade_ave(g1,g2):
    total = 0
    grade_count = 0
    if g1 >= 50:
        total = total + g1
        grade_count = grade_count + 1
    elif g2 >= 50:
        total = total + g2
        grade_count = grade_count + 1

    if grade_count > 0:
        return print(total / grade_count)
    else:
        return print(0.0)

def grade_1(grade1,grade2):
    total = 0
    grade_count = 0

    if grade1 >= 50:
        total = total + grade1
        grade_count = grade_count + 1
    if grade2 >= 50:
        total = total + grade2
        grade_count = grade_count + 1

    if grade_count > 0:
        return print(total / grade_count)
    else:
        return print(0.0)

def grade_2(grade1,grade2):
    total = 0
    grade_count = 0

    if grade1 >= 50 and grade2 >= 50:
        total = grade1 + grade2
        grade_count = 2

    if grade_count > 0:
        return print(total / grade_count)
    else:
        return print(0.0)

def greeting(name):
        return 'Hi, '+ name

def exclaim(statement):
        return statement+ ' !'

def enthusiastic_greeting(name):
        greeting_message = exclaim(greeting(name))
        return print(greeting_message)
        
