import copy
# item 1
my_dict = {"name": "Karen", "city": "Seattle", "cake": "chocolate",
           "fruit": "mango", "salad": "waldorf", "pasta": "seafood"}
print ("{name} is from {city}, and she likes {cake} "
       "cake , {fruit}, {salad} salad, and {pasta} pasta").format(**my_dict)


# item 2
num = [number for number in range(16)]
hexadecimal = [hex(number) for number in range(16)]
print(dict(zip(num, hexadecimal)))


# item 3
print ({number: hex(number) for number in range(16)})


# item 4
my_dict_copy = copy.deepcopy(my_dict)
print {key: value.count("a") for key, value in my_dict.items()}

# item 5

S2 = {number for number in range(21) if number % 2 == 0}
S3 = {number for number in range(21) if number % 3 == 0}
S4 = {number for number in range(21) if number % 4 == 0}

print S2
print S3
print S4

S2, S3, S4 = [{numbers for numbers in range(21) if numbers % i == 0} for i in
              range(2, 5)]

print (S2, S3, S4)
