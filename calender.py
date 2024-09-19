import calendar

def display_calendar(year, month):
    cal = calendar.month(year, month)
    print(cal)

def main():
    print("Welcome to the Calendar!")

    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))

    if 1 <= month <= 12:
        display_calendar(year, month)
    else:
        print("Invalid month. Please enter a number from 1 to 12.")

if __name__ == "__main__":
    main()

