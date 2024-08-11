with open("input1.txt") as file:
    lines = file.readlines()
    res = 0
    for line in lines:
        n = len(line)
        l = 0
        r = n - 1
        left = True
        right = True
        while l < n and r > -1:
            if left or right:
                if line[l].isdigit() and left:
                    res += (10 * int(line[l]))
                    left = False
                if line[r].isdigit() and right:
                    res += int(line[r])
                    right = False
                l += 1
                r -= 1
            else:
                break
print(res)