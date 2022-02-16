# https://www.geeksforgeeks.org/stepping-numbers/

start_num = 0
end_num = 50
step_num = []
for num in range(start_num, end_num + 1):
    num = str(num)
    if len(num) == 1:
        step_num.append(int(num))
    else:
        for pos in range(1, len(num)):
            if abs(int(num[pos - 1]) - int(num[pos])) != 1:
                continue
            step_num.append(int(num))

print(step_num)
