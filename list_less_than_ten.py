cats = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
little_cats = []
for c in cats:
    if c < 5:
        little_cats.append(c)

print(little_cats)



user_num = int(input("Please enter a number:     "))
user_cats = []
for c in cats:
    if c < user_num:
        user_cats.append(c)

print(user_cats)
