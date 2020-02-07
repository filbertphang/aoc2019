import math
_input = open("input.txt")
part = 2

# Part 1
def get_fuel_requirement(mass):
    req = math.floor(mass/3) - 2
    if req <= 0:
        req = 0
    return req

if part == 1:
    fuel_sum = 0
    for module in _input.readlines():
        fuel_sum += get_fuel_requirement(int(module))

    print("Fuel required for part 1:", fuel_sum)

if part == 2:
    fuel_sum = 0
    for module in _input.readlines():
        module_sum = 0
        current_req = get_fuel_requirement(int(module))

        while current_req != 0:
            module_sum += current_req
            current_req = get_fuel_requirement(current_req)

        fuel_sum += module_sum

    print("Fuel required for part 2:", fuel_sum)