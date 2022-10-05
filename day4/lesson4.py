


# my_name = "giorgi"

# for char in my_name:
#     print(char)

# for i in range(10):
#     print(i)

# name1 = input("enter name 1: ")
# name2 = input("enter name 2: ")

# amount_of_vowels_in_name1 = 0
# amount_of_vowels_in_name2 = 0

# for char in name1: 
#     if char in "aeiou":
#         amount_of_vowels_in_name1 += 1

# for char in name2: 
#     if char in "aeiou":
#         amount_of_vowels_in_name2 += 1


# if amount_of_vowels_in_name1 > amount_of_vowels_in_name2:
#     print("the amount of vowels in name1 is more and it contains {} vowels" . format(amount_of_vowels_in_name1))
# elif amount_of_vowels_in_name1 < amount_of_vowels_in_name2:
#     print("the amount of vowels in name2 is more and it contains {} vowels" . format(amount_of_vowels_in_name2))
# else:
#     print("they have equal ammount of vowels")



name1 = input("enter name1: ")
name2 = input("enter name2: ")

amount_of_consonant_in_name1 = 0
amount_of_consonant_in_name2 = 0

for char in name1:
    if char not in "aeiou":
        amount_of_consonant_in_name1 += 1

for char in name2:
    if char not in "aeiou":
        amount_of_consonant_in_name2 += 1


if amount_of_consonant_in_name1 > amount_of_consonant_in_name2:
    print("the amount of consonant in name1 is more and it contains {} consonant" . format(amount_of_consonant_in_name1))
elif amount_of_consonant_in_name1 < amount_of_consonant_in_name2:
    print("the amount of consonant in name2 is more and it contains {} consonant" . format(amount_of_consonant_in_name2))
else:
    print("they have equal ammount of consonant")





