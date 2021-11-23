myInput = input('')
n = int(myInput.split()[0])
start = int(myInput.split()[1])

myData = dict()
for i in range(n):
     input_detail = [int(x) for x in input('').split()]
     myData[input_detail[0]] = input_detail[1]

sorted_values = sorted(myData.values())
sorted_dict = {}
for i in sorted_values:
    for k in myData.keys():
        if myData[k] == i:
            sorted_dict[k] = myData[k]
            break

valueBefore = 0
count = 0
for key in sorted_dict.keys():
    sum = start - key + valueBefore
    if sum < 0:
        sum = sum * -1
    if sum <= sorted_dict[key]:
        count += 1
        valueBefore = sorted_dict[key]
    # print(sum)
print(count)
# print(sorted_dict)



