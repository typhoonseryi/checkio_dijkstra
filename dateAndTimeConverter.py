def date_time(time: str) -> str:
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    date, datetime = time.split()
    hours, minutes = map(int, datetime.split(':'))
    num, month, year = map(int, date.split('.'))
    texth = 'hour' if hours == 1 else 'hours'
    textm = 'minute' if minutes == 1 else 'minutes'
    return f'{num} {months[month - 1]} {year} year {hours} {texth} {minutes} {textm}'

print(date_time("01.01.2000 00:00"))

if __name__ == "__main__":
    print("Example:")
    print(date_time("01.01.2000 00:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
        date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    ), "Millenium"
    assert (
        date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
    ), "Victory"
    assert (
        date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    ), "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")