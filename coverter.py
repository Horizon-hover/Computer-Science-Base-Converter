def binary_to_decimal(binary_str):
    """Converts binary string to decimal number."""
    try:
        return int(binary_str, 2)
    except ValueError:
        raise ValueError("Invalid binary number")

def decimal_to_binary(decimal_num):
    """Converts decimal number to binary string."""
    try:
        return bin(int(decimal_num))[2:]
    except ValueError:
        raise ValueError("Invalid decimal number")

def decimal_to_hexadecimal(decimal_num):
    """Converts decimal number to hexadecimal string."""
    try:
        return hex(int(decimal_num))[2:].upper()
    except ValueError:
        raise ValueError("Invalid decimal number")

def hexadecimal_to_decimal(hex_str):
    """Converts hexadecimal string to decimal number."""
    try:
        return int(hex_str, 16)
    except ValueError:
        raise ValueError("Invalid hexadecimal number")

def binary_to_hexadecimal(binary_str):
    """Converts binary string to hexadecimal string."""
    try:
        decimal_num = binary_to_decimal(binary_str)
        return decimal_to_hexadecimal(decimal_num)
    except ValueError:
        raise ValueError("Invalid binary number")

def hexadecimal_to_binary(hex_str):
    """Converts hexadecimal string to binary string."""
    try:
        decimal_num = hexadecimal_to_decimal(hex_str)
        return decimal_to_binary(decimal_num)
    except ValueError:
        raise ValueError("Invalid hexadecimal number")

def decimal_to_octal(decimal_num):
    """Converts decimal number to octal string."""
    try:
        return oct(int(decimal_num))[2:]
    except ValueError:
        raise ValueError("Invalid decimal number")

def octal_to_decimal(octal_str):
    """Converts octal string to decimal number."""
    try:
        return int(octal_str, 8)
    except ValueError:
        raise ValueError("Invalid octal number")

def binary_to_octal(binary_str):
    """Converts binary string to octal string."""
    try:
        decimal_num = binary_to_decimal(binary_str)
        return decimal_to_octal(decimal_num)
    except ValueError:
        raise ValueError("Invalid binary number")

def octal_to_binary(octal_str):
    """Converts octal string to binary string."""
    try:
        decimal_num = octal_to_decimal(octal_str)
        return decimal_to_binary(decimal_num)
    except ValueError:
        raise ValueError("Invalid octal number")

def hexadecimal_to_octal(hex_str):
    """Converts hexadecimal string to octal string."""
    try:
        decimal_num = hexadecimal_to_decimal(hex_str)
        return decimal_to_octal(decimal_num)
    except ValueError:
        raise ValueError("Invalid hexadecimal number")

def octal_to_hexadecimal(octal_str):
    """Converts octal string to hexadecimal string."""
    try:
        decimal_num = octal_to_decimal(octal_str)
        return decimal_to_hexadecimal(decimal_num)
    except ValueError:
        raise ValueError("Invalid octal number")

def display_main_menu():
    """Displays the main menu."""
    print("\nComputer Science Converter")
    print("1. Binary Conversions")
    print("2. Decimal Conversions")
    print("3. Hexadecimal Conversions")
    print("4. Octal Conversions")
    print("5. Program Usage")
    print("6. Exit")

def display_binary_menu():
    """Displays the binary conversion menu."""
    print("\nBinary Conversions")
    print("1. Binary to Decimal")
    print("2. Binary to Hexadecimal")
    print("3. Binary to Octal")
    print("4. Back to Main Menu")

def display_decimal_menu():
    """Displays the decimal conversion menu."""
    print("\nDecimal Conversions")
    print("1. Decimal to Binary")
    print("2. Decimal to Hexadecimal")
    print("3. Decimal to Octal")
    print("4. Back to Main Menu")

def display_hexadecimal_menu():
    """Displays the hexadecimal conversion menu."""
    print("\nHexadecimal Conversions")
    print("1. Hexadecimal to Decimal")
    print("2. Hexadecimal to Binary")
    print("3. Hexadecimal to Octal")
    print("4. Back to Main Menu")

def display_octal_menu():
    """Displays the octal conversion menu."""
    print("\nOctal Conversions")
    print("1. Octal to Decimal")
    print("2. Octal to Binary")
    print("3. Octal to Hexadecimal")
    print("4. Back to Main Menu")

def display_program_usage():
    """Displays the program usage information."""
    print("\nProgram Usage:")
    print("This program allows you to convert numbers between different bases commonly used in computer science:")
    print("1. Binary: Base 2")
    print("2. Decimal: Base 10")
    print("3. Hexadecimal: Base 16")
    print("4. Octal: Base 8")
    print("\nYou can choose from the main menu to convert numbers between these bases.")
    print("Each sub-menu provides options for specific conversions within that number system.")
    print("Simply follow the prompts to input your number and get the converted result.")
    print("Error handling is included to guide you if you enter an invalid number.")
    print("\nSelect 'Back to Main Menu' from any sub-menu to return to the main menu.")
    print("Select 'Exit' from the main menu to close the program.")

def main():
    """Main function to run the menu-driven converter program."""
    while True:
        display_main_menu()
        main_choice = input("Enter your choice (1-6): ")

        if main_choice == '1':
            while True:
                display_binary_menu()
                binary_choice = input("Enter your choice (1-4): ")
                
                if binary_choice == '1':
                    binary_str = input("Enter a binary number: ")
                    try:
                        decimal_num = binary_to_decimal(binary_str)
                        print(f"Binary {binary_str} in Decimal is {decimal_num}")
                    except ValueError as e:
                        print(e)
                
                elif binary_choice == '2':
                    binary_str = input("Enter a binary number: ")
                    try:
                        hex_str = binary_to_hexadecimal(binary_str)
                        print(f"Binary {binary_str} in Hexadecimal is {hex_str}")
                    except ValueError as e:
                        print(e)
                
                elif binary_choice == '3':
                    binary_str = input("Enter a binary number: ")
                    try:
                        octal_str = binary_to_octal(binary_str)
                        print(f"Binary {binary_str} in Octal is {octal_str}")
                    except ValueError as e:
                        print(e)
                
                elif binary_choice == '4':
                    break
                
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
        
        elif main_choice == '2':
            while True:
                display_decimal_menu()
                decimal_choice = input("Enter your choice (1-4): ")
                
                if decimal_choice == '1':
                    decimal_str = input("Enter a decimal number: ")
                    try:
                        binary_str = decimal_to_binary(decimal_str)
                        print(f"Decimal {decimal_str} in Binary is {binary_str}")
                    except ValueError as e:
                        print(e)
                
                elif decimal_choice == '2':
                    decimal_str = input("Enter a decimal number: ")
                    try:
                        hex_str = decimal_to_hexadecimal(decimal_str)
                        print(f"Decimal {decimal_str} in Hexadecimal is {hex_str}")
                    except ValueError as e:
                        print(e)
                
                elif decimal_choice == '3':
                    decimal_str = input("Enter a decimal number: ")
                    try:
                        octal_str = decimal_to_octal(decimal_str)
                        print(f"Decimal {decimal_str} in Octal is {octal_str}")
                    except ValueError as e:
                        print(e)
                
                elif decimal_choice == '4':
                    break
                
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
        
        elif main_choice == '3':
            while True:
                display_hexadecimal_menu()
                hex_choice = input("Enter your choice (1-4): ")
                
                if hex_choice == '1':
                    hex_str = input("Enter a hexadecimal number: ")
                    try:
                        decimal_num = hexadecimal_to_decimal(hex_str)
                        print(f"Hexadecimal {hex_str} in Decimal is {decimal_num}")
                    except ValueError as e:
                        print(e)
                
                elif hex_choice == '2':
                    hex_str = input("Enter a hexadecimal number: ")
                    try:
                        binary_str = hexadecimal_to_binary(hex_str)
                        print(f"Hexadecimal {hex_str} in Binary is {binary_str}")
                    except ValueError as e:
                        print(e)
                
                elif hex_choice == '3':
                    hex_str = input("Enter a hexadecimal number: ")
                    try:
                        octal_str = hexadecimal_to_octal(hex_str)
                        print(f"Hexadecimal {hex_str} in Octal is {octal_str}")
                    except ValueError as e:
                        print(e)
                
                elif hex_choice == '4':
                    break
                
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
        
        elif main_choice == '4':
            while True:
                display_octal_menu()
                octal_choice = input("Enter your choice (1-4): ")
                
                if octal_choice == '1':
                    octal_str = input("Enter an octal number: ")
                    try:
                        decimal_num = octal_to_decimal(octal_str)
                        print(f"Octal {octal_str} in Decimal is {decimal_num}")
                    except ValueError as e:
                        print(e)
                
                elif octal_choice == '2':
                    octal_str = input("Enter an octal number: ")
                    try:
                        binary_str = octal_to_binary(octal_str)
                        print(f"Octal {octal_str} in Binary is {binary_str}")
                    except ValueError as e:
                        print(e)
                
                elif octal_choice == '3':
                    octal_str = input("Enter an octal number: ")
                    try:
                        hex_str = octal_to_hexadecimal(octal_str)
                        print(f"Octal {octal_str} in Hexadecimal is {hex_str}")
                    except ValueError as e:
                        print(e)
                
                elif octal_choice == '4':
                    break
                
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
        
        elif main_choice == '5':
            display_program_usage()
        
        elif main_choice == '6':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()


