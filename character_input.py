name = input("Enter your name:     ")
year = int(input("Enter the year you were born:     "))
hundred_year = year + 100
message = "{}, you will turn 100 in the year {}"
print(message.format(name, hundred_year))
