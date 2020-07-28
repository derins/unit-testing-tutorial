from datetime import datetime

def get_time_of_day():
    '''Returns time of day (morning, afternoon, night, evening)'''
    now = datetime.now().time()

    if now.hour >= 0 and now.hour < 6:
        return 'Night'

    if now.hour >= 6 and now.hour < 12:
        return 'Morning'

    if now.hour >= 12 and now.hour < 18:
        return 'Afternoon'

    return 'Evening'


# def get_time_of_day(time = datetime.now()):
#     '''Returns time of day (morning, afternoon, night, evening)'''
#
#     if time.hour >= 0 and time.hour < 6:
#         return 'Night'
#
#     if time.hour >= 6 and time.hour < 12:
#         return 'Morning'
#
#     if time.hour >= 12 and time.hour < 18:
#         return 'Afternoon'
#
#     return 'Evening'
