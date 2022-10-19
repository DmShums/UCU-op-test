import calendar

def semester_calendar(output_type, year, first_month, last_month):
    """
    (str, int, int, int) -> str
    Output calendar in format 'txt' or 'html'
    """
    string = ""
    if output_type == "txt":
        for i in range(first_month ,last_month + 1):
            string += calendar.month(year, i)
        return string
    if output_type == "html":
        for i in range(first_month ,last_month + 1):
            string += calendar.HTMLCalendar(firstweekday = 0).formatmonth(year, i)
        return string

