from datetime import date
from dateutil.relativedelta import relativedelta
import datetime

def today_date(Class):
    today = date.today()
    d4 = today.strftime("%d/%m/%Y")
    Class.DDR = d4
    Class.DDR1 = datetime.datetime.strptime(d4, '%d/%m/%Y') - relativedelta(days=1)