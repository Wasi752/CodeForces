person, upNum = map(int, input().split())
eachNum = list(map(int, input().split()))
eachNum.sort(reverse=True)
mark = eachNum[upNum - 1]
counter = 0
for x in eachNum:
    if mark <= x and x > 0:
        counter = counter + 1
print(counter)


