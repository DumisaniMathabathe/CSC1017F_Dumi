# Dumisani Mathabathe
# 01 March 2024

def is_leap_year(year):
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        return True
    else:
        return False

def main():
    try:
        year = int(input("Enter a year:\n"))
        if year < 0:
            print("Please enter a positive year.")
        else:
            if is_leap_year(year):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()

