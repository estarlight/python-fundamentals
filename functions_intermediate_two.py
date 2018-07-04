x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]



for idx,val in enumerate(x):
    for idx,val in enumerate(x[1]):
      x[1][0] = 15
print(x)

for key,val in students:
  students[0]['last_name'] = 'Bryant'
print (students)

for key,val in sports_directory.items():
  sports_directory['soccer'][0] = 'Andres'
print (sports_directory)

for d in z:
    d.update((y, 30) for y, v in d.items() if v == 20)
print(z)


#2

for i in range(len(students)):
  for key,val in students[i].items():  
    print(key,":",val)

def iterateDictionary (list):
    for i in range(len(list)):
        for key,val in list[i].items():
            print(key,":",val)

for i in range(len(students)):  # for i in students:
  str = ""
  for key,val in students[i].items():  # for key,val in i.items():
    str += "{} - {},".format(key,val)
  print(str)

#3 

for i in students:
  print(i['first_name'])

#4

def printDojoInfo(dojo):
    for key,val in dojo.items():
        print (len(dojo[key]),key)
        for i in range(len(dojo[key])):
            print(val[i])
        print(" ")

        
