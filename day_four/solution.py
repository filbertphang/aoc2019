import re

def check_valid_password(pw):
    pw = str(pw)
    valid_dups = [str(x)*2 for x in range(10)]

    for char in range(len(pw)-1):
        if int(pw[char]) > int(pw[char+1]):
            return False
    
    reps = re.findall('0{2,6}|1{2,6}|2{2,6}|3{2,6}|4{2,6}|5{2,6}|6{2,6}|7{2,6}|8{2,6}|9{2,6}', pw) # Part 2
    for duplicate in valid_dups:
        # if duplicate in pw: # Part 1
        if duplicate in reps: # Part 2
            return True 
    
    return False

no_valid = 0
# input is 254032 - 789860
for no in range(254032, 789860):
    if check_valid_password(no):
        no_valid += 1

print("Solution:", no_valid)