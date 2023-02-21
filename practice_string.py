'''def mix_string(s1, s2):
    first_char = s1[0] + s2[0]
    middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]
    last_char = s1[len(s1) - 1] + s2[len(s2) - 1]
    res = first_char + middle_char + last_char
    print("Mix String is ", res)

s1 = "America"
s2 = "Japan"
mix_string(s1, s2)


def find_digits_chars_symbols(sample_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0
    for char in sample_str:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1

    print("Chars =", char_count, "Digits =", digit_count, "Symbol =", symbol_count)

sample_str = "P@yn2at&#i5ve"
print("total counts of chars, Digits, and symbols \n")
find_digits_chars_symbols(sample_str)


s1 = "Abc"
s2 = "Xyz"
s1_length = len(s1)
s2_length = len(s2)
length = s1_length if s1_length > s2_length else s2_length
result = ""

s2 = s2[::-1]


for i in range(length):
    if i < s1_length:
        result = result + s1[i]
    if i < s2_length:
        result = result + s2[i]

print(result)


str1 = "Welcome to USA. usa awesome, isn't it?"
sub_string = "USA"
temp_str = str1.lower()
count = temp_str.count(sub_string.lower())
print("The USA count is:", count)


str1 = "Apple"
char_dict = dict()

for char in str1:
    count = str1.count(char)
    char_dict[char] = count
print('Result:', char_dict)


str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
res_list = []
for s in str_list:
    if s:
        res_list.append(s)
print(res_list)


str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

new_str = str1.translate(str.maketrans('', '', string.punctuation))

print("New string is ", new_str)


str1 = 'I am 25 years and 10 months old'
print("Original string is", str1)
res = "".join([item for item in str1 if item.isdigit()])

print(res)



str1 = "Emma25 is Data scientist50 and AI Expert"
print("The original string is : " + str1)



res = []

temp = str1.split()

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)

print("Displaying words with alphabets and numbers")
for i in res:
    print(i)



import string

str1 = '/*Jon is @developer & musician!!'
print("The original string is : ", str1)
replace_char = '#'
for char in string.punctuation:
    str1 = str1.replace(char, replace_char)

print("The strings after replacement : ", str1)'''
#tuple

'''tuple1 = (10, 20, 30, 40, 50)
tuple1 = tuple1[::-1]
print(tuple1)



tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

print(tuple1[1][1])



tuple1 = (10, 20, 30, 40)

# unpack tuple into 4 variables
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)



tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple2)
print(tuple1)


tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:-1]
print(tuple2)

tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)


tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)

'''

