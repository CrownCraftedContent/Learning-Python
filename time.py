import time

# print(time.ctime(0))    # convert a time expressed in seconds since epoch to a readable state
#                       epoch = when your computer thinks time began

# print(time.time())      # return current seconds since epoch

print(time.ctime(time.time()))  # will therefore give the current time

time_object = time.localtime()  # local time
time_object = time.gmtime()  # UTC time
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)  # string formatting
# look up the strftime documentation online

time_string = "20 April, 2020"
time_object = time.strptime(time_string, "%d %B, %Y")  # parse text into time
print(time_object)

# (year, month, day, hours, minutes, secs, #day of the week, #day of year, dst) dst = daylight savings -1 or 0
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)  # Readable string - converted from time object (tuple)

# (year, month, day, hours, minutes, secs, #day of the week, #day of year, dst) dst = daylight savings -1 or 0
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)  # Time in seconds since epoch - converted from time object (tuple)


# MESSING AROUND WITH ENUMERATE() V

periodIndex = str(time.time()).find(".")
newList = enumerate(str(time.time()))
newList = ["," + v if 10 > i != 0 and (i-10) % 3 == 0 else v for i, v in newList]
newString = ""
for i in newList:
    newString = newString + i
print(newString)
print(6 % 3)