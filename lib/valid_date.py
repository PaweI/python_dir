months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
def valid_month(month):
    for e in months:
        if month.lower() == e.lower():
            return e
    return False

def valid_day(day): #day must be a string e.g. "21"
    if day.isdigit():
        if int(day) in range(1,32):
            return int(day)
    return False

def valid_year(year): #year must be a string as well, ex. "1985"
    if year.isdigit():
        if int(year) in range(1900, 2050):
            return int(year)
    return False

def valid_date(day, month, year):
  if valid_month(month) != False and valid_day(day) != False and valid_year(year) != False:
    return "Date is valid"
  else:
    return "Sorry your input is incorrect"

print valid_date("24", "January", "1990")

print valid_date("35", "October", "1987")

