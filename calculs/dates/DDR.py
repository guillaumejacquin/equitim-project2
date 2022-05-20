from datetime import date
from dateutil.relativedelta import relativedelta
import datetime

def today_date(Class):
    today = date.today()
    #date d'aujourd'hui
    d4 = today.strftime("%d/%m/%Y")
    Class.DDR = d4
    
    #Date d'aujourd'hui - 1
    Class.DDR1 = datetime.datetime.strptime(d4, '%d/%m/%Y') - relativedelta(days=1)