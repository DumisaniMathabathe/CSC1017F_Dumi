# Dumisani Mathabathe
# 21 March 2024

def count_odd_numbers(numbers):
    count = 0
    for num in numbers:
        if num % 2 != 0:
            count += 1
    return count

def main():
    integer_values = []
    for i in range(10):
        value = int(input("Enter an integer value:\n"))
        integer_values.append(value)
    
    odd_count = count_odd_numbers(integer_values)
    if odd_count == 1:
        print(f"There is 1 odd number.")
    else:
        print(f"There are {odd_count} odd numbers.")

if __name__ == "__main__":
    main()

