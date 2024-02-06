import sys

# read arguments
program_filepath = sys.argv[1]

""" Tokenization, Lexical phase 
    (scanning the source code and breaking it down into tokens such as keywords, identifiers, constants, and ops while discarding whitespaces) 
"""

# Reading the file's lines
program_lines = []
with open(program_filepath, "r") as program_file:
    program_lines = [
        line.strip()
        for line in program_file.readlines()]


program = []
token_counter = 0
label_tracker = {}
for line in program_lines:
    parts = line.split(" ")
    opcode = parts[0]

    # check for empty line
    if opcode == "":
        continue

    # check if its a label
    if opcode.endswith(":"):
        label_tracker[opcode[:-1]] = token_counter
        continue

    # store opcode token
    program.append(opcode)
    token_counter += 1

    # handle each opcode
    if opcode == "ግፋ":
        # expecting a number
        number = int(parts[1])
        program.append(number)
        token_counter += 1
    elif opcode == "ማተም":
        # parse string literal
        string_literal = ' '.join(parts[1:])[1:-1]
        program.append(string_literal)
        token_counter += 1
    elif opcode == "ዝለል.እኩ.0":
        # read label
        label = parts[1]
        program.append(label)
        token_counter += 1
    elif opcode == "ዝለል.ይበ.0":
        # read label
        label = parts[1]
        program.append(label)
        token_counter += 1

#     Interpret Program


class Stack:

    def __init__(self, size):
        self.buf = [0 for _ in range(size)]
        self.sp = -1

    def push(self, number):
        self.sp += 1
        self.buf[self.sp] = number

    def pop(self):
        number = self.buf[self.sp]
        self.sp -= 1
        return number

    def top(self):
        return self.buf[self.sp]


pc = 0
stack = Stack(256)
print(program)

while program[pc] != "ተው":
    opcode = program[pc]
    pc += 1

    print("Executing opcode:", opcode)
    print("Stack:", stack.buf[:stack.sp + 1])

    if opcode == "ግፋ":
        number = program[pc]
        pc += 1
        stack.push(number)
    elif opcode == "ንቀል":
        stack.pop()
    elif opcode == "ጨምር":
        a = stack.pop()
        b = stack.pop()
        stack.push(a+b)
    elif opcode == "ቀንስ":
        a = stack.pop()
        b = stack.pop()
        stack.push(b-a)
    elif opcode == "ማተም":
        string_literal = program[pc]
        pc += 1
        print(string_literal)
    elif opcode == "አንብ":
        number = int(input())
        stack.push(number)
    elif opcode == "ዝለል.እኩ.0":
        number = stack.top()
        if number == 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    elif opcode == "ዝለል.ይበ.0":
        number = stack.top()
        if number > 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
