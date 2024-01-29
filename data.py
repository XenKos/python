from datetime import datetime, timedelta

def get_days_from_today():
    
    date=input("Input the date: ") 
     
    try:
        date=datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print ("Incorrect date format. Input the date in format YYYY-MM-DD.")
        return None

    else:
        current_date=datetime.today()
        delta = date  - current_date
        return delta.days
    
days_difference = get_days_from_today()

if days_difference is not None:
    print("Get days from today: ", days_difference)