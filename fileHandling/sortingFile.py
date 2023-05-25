



lines = open("test.log", 'r').readlines()
output = open("intermediate_alphabetical_order.txt", 'w')
print lines

for line in sorted(lines, key=lambda line: line.split()[1]):
    output.write(line)

output.close()