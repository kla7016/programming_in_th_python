def n_length_combo(lst, n):
     
    if n == 0:
        return [[]]
     
    l =[]
    for i in range(0, len(lst)):
         
        m = lst[i]
        remLst = lst[i + 1:]
         
        for p in n_length_combo(remLst, n-1):
            l.append([m]+p)
             
    return l

# from itertools import combinations
myInput = input('')
n = int(myInput.split()[0])
ran = int(myInput.split()[1])
minus = int(myInput.split()[2])
list_input = []
for i in range(n):
    input_detail = input('')
    list_input.append([int(x) for x in input_detail.split()])
lastInput = [int(x) for x in input('').split()]

sum = 0
if minus == 0:
    for i in range(len(lastInput)):
        if i == len(lastInput) - 1:
            break
        num = lastInput[i]
        num_n = lastInput[i + 1]
        sum = sum + list_input[num - 1][num_n - 1]
elif minus == 1:
    myData = dict()
    for i in range(len(lastInput)):
        if i == len(lastInput) - 1:
            break
        num = lastInput[i]
        num_n = lastInput[i + 1]
        myData[i] = list_input[num - 1][num_n - 1]
        # sum = sum + list_input[num - 1][num_n - 1]
    sorted_values = sorted(myData.values())
    sorted_values.reverse()
    sorted_dict = {}
    for i in sorted_values:
        for k in myData.keys():
            if myData[k] == i:
                sorted_dict[k] = myData[k]
                break
    lastInput.pop(list(sorted_dict.keys())[0])
    for i in range(len(lastInput)):
        if i == len(lastInput) - 1:
            break
        num = lastInput[i]
        num_n = lastInput[i + 1]
        sum = sum + list_input[num - 1][num_n - 1]
else:
    list_ran = range(ran)
    # perm = combinations(list_ran,2)
    perm = n_length_combo(list_ran,2)

    for p in list(perm):
        temp_last_input = lastInput[:]
        new_p = list(p)
        new_p.reverse()
        for j in new_p:
            temp_last_input.pop(j)
        temp_sum = 0
        for i in range(len(temp_last_input)):
            if i == len(temp_last_input) - 1:
                break
            num = temp_last_input[i]
            num_n = temp_last_input[i + 1]
            temp_sum = temp_sum + list_input[num - 1][num_n - 1]
        if sum == 0:
            sum = temp_sum
        else:
            if temp_sum < sum:
                sum = temp_sum

print(sum)
