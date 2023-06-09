from datetime import datetime

def Date_Time_End():
    current_dateTime = datetime.now()
    print('Date: ', current_dateTime.year, '/', current_dateTime.month, '/', current_dateTime.day)
    print ('Time:', current_dateTime.hour, ':', current_dateTime.minute, ':', current_dateTime.second)
