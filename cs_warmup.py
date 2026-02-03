<<<<<<< HEAD
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

=======
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

>>>>>>> e697960d673c141b4984e0606b1ab68425211394
main()