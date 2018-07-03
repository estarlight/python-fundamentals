#1 Biggie Size

def makeItBig (lst):
    for idx,val in enumerate(lst):
        if val > 0:
          lst[idx] = "big"

    print(lst)

arr = [-1,3,5,-5]
makeItBig(arr)

def makeItBig (lst):
    for i in range(len(lst)):
        if lst[i] > 0:
          lst[i] = "big"

    print(lst)

arr = [-1,3,5,-5]
makeItBig(arr)

#2 Count Positives

def countPositives (lst):
    count = 0
    for i in lst:
        if i > 0:
            count += 1
    lst.pop()
    lst.append(count)
    print(lst)

arr = [-1,1,1,1]
countPositives(arr)

#3 SumTotal

def sumTotal (lst):
    sum = 0
    for i in lst:
        sum += i
    print(sum)

test = [1,2,3,4]
sumTotal(test)

#4 Average

def average (lst):
    sum = 0
    avg = 0
    for i in lst:
        sum += i
    avg = sum / len(lst)
    print(avg)

test = [1,2,3,4]
average(test)

#5 Length

def length(lst):
    print(len(lst))

test = [1,2,3,4]
length(test)

#6 Minimum

def minimum (lst):
    if len(lst) < 1:
        return False
    else:
        min = lst[0]
        for i in range(len(lst)):
            if lst[i] < min:
                min = lst[i]
    print(min)

test = [1,2,3,4]
minimum(test)

#7 Maximum

def maximum (lst):
    if len(lst) < 1:
        return False
    else:
        max = lst[0]
        for i in range(len(lst)):
            if lst[i] > max
                max = lst[i]
    print(max)

test = [1,2,3,4]
minimum(test)

#8 UltimateAnalyze

def ultimateAnalyze (lst):
    sum=0
    avg=0
    min=lst[0]
    max=lst[0]
    my_dict = {}
    for i in range(len(lst)):
        sum += lst[i]
        if lst[i] < min:
          min = lst[i]
        if lst[i] > max:
          max = lst[i]
    avg = sum / len(lst)
    my_dict["Sum"] = sum
    my_dict["Average"] = avg
    my_dict["Minimum"] = min
    my_dict["Maximum"] = max
    my_dict["Length"] = len(lst)
    return(my_dict)

test = [1,2,3,4]
print(ultimateAnalyze(test))

#9 Reverse List

def reverse (lst):
    for i in range(len(lst),lst[0]-1,-1):
        print(i)

test = [1,2,3,4]
reverse(test)