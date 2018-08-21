#question 1  Reverse the whole list using list methods.

print("<----------------solution 1 -------------------->")

list=[1,2,3,4,5]
list.reverse()
print(list)

#qustion 2   Print all the uppercase letters from a string.

print("<-----------------solution 2 ------------------->")

string= "My Name Is Prithul Babutta"
for ch in string :
    if ch.isupper():
        print(ch)


#question 3 Split the user input on comma's and store the values in a list as integers.

print("<-----------------solution 3 ------------------->")

i=input("enter the input")
list=[]
list1=i.split(',')
for n in list1:
    list.append(int(n))
print(list)



#quetion 4 Check whether a string is palindromic or not.

print("<-----------------solution 4 ------------------->")

string=input("enter the string ")
l=int(len(string)/2)
j=-1
for i in range(0,l) :
    if string[i] is string[j]:
        flag=0
    else:
        flag=1
    j-=1
if flag is 0:
    print("String is pallindrome")
else:
    print("String is not a pallindrome")



#question 5  Make a deepcopy of a list and write the difference between shallow copy and deep copy.

print("<-----------------solution 5 ------------------->")


import copy as c
list1 = [1, 2, [3,5], 4]
list2 = c.deepcopy(list1)
print ("Before deep copying")
print("list1 = ",list1)
print("list2 = ",list2)
list2[2][1] = 125
print ("After deep copying in list2")
print(list2)
print ("After deep copying in list1")
print(list1)
print('\r')
