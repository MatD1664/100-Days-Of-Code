#FileNotFound
# with open("a_file.txt") as file:
#     file.read()

#KeyError
# a_dict = {"key":"value"}
# value = a_dict["non_existent_key"]

#IndexError
# fruit_list = ["Apple","Pear","Lemon"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)

"""Exceptions are dealt with in the following order,
Try: 'Something that might cause an exception'
Except: 'Do this if there was an exception'
Else: 'Do this if there were no exceptions'
Finally: 'Do this no matter what happens'"""

try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["abcd"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")
    #raise TypeError("This is an error I made up")


if height > 3:
    raise ValueError("Human height should not be over 3 metres")

height = float(input("Height: "))
weight = int(input("Weight: "))

bmi = weight / height ** 2
print(bmi)
