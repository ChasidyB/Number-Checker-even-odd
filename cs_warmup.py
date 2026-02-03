def get_number():
    try:
        return int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid whole number.")
        return None
    
def check_even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
    
def main():
    while True:
        num = get_number()
        if num is None:
            continue

        result = check_even_or_odd(num)
        print(f"That number is {result}")

        again = input("Try another number? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            break

main()