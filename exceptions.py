# Crown Crafted Content

# exception
#        events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("\nEnter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    result = numerator / denominator
    #  print(result)
except ZeroDivisionError:
    print("No dividing by 0!")
except ValueError:
    print("Enter only numbers please")
except Exception as e:
    print("Something went wrong:", e)
else:  # <-- if no errors (exceptions) occurred
    print(result)  # result is available OUTSIDE of try block (and else/finally blocks)
    # NOTE: if an exception occurs before assignment, variable will not be created
finally:  # good opportunity to close files, etc.
    print("This will always execute")  # whether an exception is thrown or not
