


def report_status(sched_time,est_time):
    '''
    (number,number)-> str

    Will tell if the sched time is followed or not. 
    
    Pre_condition: 0.0 <= sched_time < 24 and 0.0 <=est_time<24

    >>> report_status(14.3,14.3)
    'on time'
    >>> report_status(12.5,11.5)
    'early'
    >>> report_status(9.0,9.5)
    'delayed'
    '''
    if sched_time == est_time:
        return 'on time'
    elif sched_time > est_time:
        return 'early'
    else:
        return 'delayed'
    
