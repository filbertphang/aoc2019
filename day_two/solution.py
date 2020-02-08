_input = open('day_two/input.txt').read()
_input = _input.split(',')
_input = [int(x) for x in _input]

# Part 1
_input[1], _input[2] = 12, 2

def update(arr, count, opr):
    a = arr[count+1]
    b = arr[count+2]
    replace = arr[count+3]

    if opr == "+":
        arr[replace] = arr[a] + arr[b]
    if opr == "*":
        arr[replace] = arr[a] * arr[b]

    return arr, count + 4

count = 0
while count < len(_input):
    if _input[count] == 1:
        _input, count = update(_input, count, "+")

    if _input[count] == 2:
        _input, count = update(_input, count, "*")
        
    if _input[count] == 99:
        print("Solution for part 1:", _input[0])
        break


# Part 2
# Was more of a guess and check
# For my particular input, observe that:
#  - increasing noun by 1 causes output to increase by 300000 (and vice versa)
#  - increasing verb by 1 causes output to increase by 1 (and vice versa)
#
# Hence for initial (noun, verb) = (12, 2) giving an output 4090701,
# we just need to add 19690720 - 4090701 = 15600019 to it.
#
# Since 15600019 = 52(300000) + 19(1), we just increase noun by 52 and verb by 1.
# Hence, we have our solution