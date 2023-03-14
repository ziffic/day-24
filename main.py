# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# No need to close file with 'with'
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# to override a file
# with open("my_file.txt", mode="w") as file:
#     file.write("99828940 New URL")

# to append a file
# with open("my_file.txt", mode="a") as file:
#     file.write("\n45796654 sample")

with open("new_file.txt", mode="w") as file:
    file.write("\ncreate")
