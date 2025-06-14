# This program takes a list of numbers from the user and stores them in a list.
user_wants=int(input("How many number do you want to enter:"))
list1=[]#empty list to store numbers
for i in range(user_wants):
    number= int(input("Enter number ro entire in the list:"))
    list1.append(number)
# Reversing the list   
list1.reverse()
# Displaying the reversed list
print("The reverse number ara:", list1)