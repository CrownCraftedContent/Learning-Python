# **************************************************
# if __name__ == '__main__'
# **************************************************

# This denotes whether:
#   1. Module is being run as a standalone program
#   2. Module has been imported by another

# Python interpreter sets "special variables", one of which is __name__
# The __name__ variable will be assigned __main__ if it's the INITIAL module being run

if __name__ == '__main__':
    print("running this module directly")
else:
    print("running other module indirectly")  # this current script is referred to as "other" module
# else statement fires when this script is imported to another
