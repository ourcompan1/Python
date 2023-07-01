### Work with files
# file = open('data/text.txt', 'w')  # w = reading , delete and add

# file.write('Work\n')
# file.write('Lets go!')

# file.close()

# file = open('data/text.txt', 'a')  # a (upend) = add new info

# file.write(' Work\n')
# file.write('Lets go!\n')

# file.close()

# data = input('Press text: ')
# file = open('data/text.txt', 'a')
#
# file.write(data + '\n')
#
#
# file.close()

file = open('data/text.txt', 'r') # r = read file in command window

print(file.read())
for line in file:
    print(line)

file.close()
