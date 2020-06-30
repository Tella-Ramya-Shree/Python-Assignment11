#1.Write a python program to sum all the items in a list
total = 0
list1 = [11, 5, 9, 18, 23]  
for ele in range(0, len(list1)): 
    total = total + list1[ele] 
print("Sum of all elements in given list: ", total) 
#Output:-
#Sum of all elements in given list:  66

#2.Write a python program to multiplies all the items in the list
total = 1
list2 = [1,6,9,4,2,5,3]  
for ele in range(0, len(list2)): 
    total = total * list2[ele] 
print("Product of all elements in given list: ", total)
#Output:-
#Product of all elements in given list:  6480

#3.Write a python program to get the largest and smallest number from a list
list3 = [10, 20, 1, 2,45, 99] 
print("Largest element is:", min(list3)) 
print("Smallest element is:",max(list3))
#Output:-
#Largest element is: 1
#Smallest element is: 99

#4.Write a python program to remove duplicates from a list
test_list = [1, 3, 5, 6, 3, 5, 6, 1] 
print ("The original list is : " ,str(test_list)) 
res = [] 
for i in test_list: 
    if i not in res: 
        res.append(i) 
print ("The list after removing duplicates : " ,str(res)) 
#Output:-
#The original list is :  [1, 3, 5, 6, 3, 5, 6, 1]
#The list after removing duplicates :  [1, 3, 5, 6]

#5.Write a python program to check a list is empty or not
l=[]
if not l:
    print ("List is empty")
else:
    print ("List is not empty")
#Output:-
#List is empty

#6.Write a python program to clone or copy a list
original_list = [10, 22, 64, 43, 4]
new_list = list(original_list)
print( "Original List:",original_list)
print( "After cloning :",new_list)
#Output:-
#Original List: [10, 22, 64, 43, 4]
#After cloning : [10, 22, 64, 43, 4]

#7.Write a python program to print a specified list after removing the 0th,4th and 5th elements
fruit = ['Apple', 'Banana', 'Orange', 'Grapes', 'Kiwi', 'Mango']  
fruit= [x for (i,x) in enumerate(fruit) if i not in (0,4,5)]  
print(fruit) 
#Output:-
#['Banana', 'Orange', 'Grapes']

#8.Write a python program to print the numbers of the specified list after removing even numbers
list = [4,5,6,7,8,1,2,3]
print("Original list:",list)
for i  in list:
	if(i%2 == 0):
	    list.remove(i)
print ("List after removing even numbers:",list)
#Output:-
#Original list: [4, 5, 6, 7, 8, 1, 2, 3]
#List after removing even numbers: [5, 7, 1, 3]

#9.Write a python program to shuffle and print a specified list
import random 
list= [1, 4, 5, 6, 3]
print ("The original list is : ",list) 
random.shuffle(list) 
print ("The shuffled list is : " ,list)
#Output:-
#The original list is :  [1, 4, 5, 6, 3]
#The shuffled list is :  [4, 3, 6, 5, 1]

#10.Write a python program to get the difference between the two lists
list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]
diff_list1_list2 = list(set(list1) - set(list2))
diff_list2_list1 = list(set(list2) - set(list1))
total_diff = diff_list1_list2 + diff_list2_list1
print(total_diff)
#Output:-
#[9, 3, 5, 8, 2, 4, 6]












