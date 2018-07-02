#1 Countdown
newArr = []
def countDown (num):
    for i in range(5,-1,-1):
        newArr.append(i)
    return newArr

print(countDown(5))

#2 Print and Return

def printReturn (list):
    print (list[0])
    return list[1]

list = [3,5]
printReturn(list)

#3 First Plus Length

def plusLength (arr):
    return arr[0] + len(arr)

arr = [1,2,3,4]
plusLength(arr)

#4 Values Greater than Second

def greaterThanSecond (arr):
  if len(arr) <= 2:
      return False
  else:    
    newArr = []
    count = 0
    for i in arr:
      if i > arr[1]:
        newArr.append(i)
        count += 1
  return(newArr)
  print(count)

arr = [3,5]
greaterThanSecond(arr)

#5 This Length, That Value

def lengthAndValue (size,value):
  newArr = []
  i = 0
  while i < size:
    newArr.append(value)
    i += 1
  print(newArr)

lengthAndValue(4,7)