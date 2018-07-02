

# 1. Basic
for i in range(0,156):
    print(i)
    
# 2. Mutliples of Five
for i in range(5,1000001,5):
    print(i)

# 3. Counting, the Dojo Way
for i in range(1,101):
    if i % 5 == 0:
        print("Coding")
    if i % 10 == 0:
        print("Dojo")
    else:
        print(i)

# 4. Whoa. That Sucker's Huge
total = 0
for i in range(1,101):
    if i % 2 != 0:
       total += i

print (total)

# 5. Countdown by Fours
for i in range(2018,0,-4):
    print(i)

# 6. Flexible Countdown
for i in range(lowNum,highNum+1):
    if i % mult == 0:
        print(i)

# A common mistake?
# 3,5,1,2
# error
# 0,1,2,3


def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a)

