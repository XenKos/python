from datetime import datetime, timedelta

def get_days_from_today(date):
    
    try:
        date=input("Input the date: ") 
        date=datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print ("Incorrect date format. Input the date in format YYYY-MM-DD.")
        return None

    else:
        current_date=datetime.today()
        days_difference =date  - current_date
        return days_difference.days
    
date = None
days_difference=get_days_from_today(date)

if days_difference is not None:

    print("Get days from today: ", days_difference)
