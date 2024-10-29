# #data types f string operation and types conversion
# #data types -string,boolean,interger,float
 
# print('hello'[0]) #the method of letter from a string is known as subscript
# # numbering starts from 0(binary) in programing 
# print('hello'[-1]) 
 
# #type conversion-----   

#       # Day 2 task 
#         #user to input two number 
#         #output should be the sum of the two number inserted
#         #using type conversion to solve this challenge 
# two_digit_number = input ('Type a two digit number \n')
# #print(type(two_digit_number))
# # #user is to input two numbers 
# # sum_of_two_number = int(two_digit_number) 
# # print(type(sum_of_two_number))
# #integer cannot be subscript ....lol
# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]
# # able to subscript them...next is to change their type to int
# real_first_digit = int(first_digit)
# real_second_digit = int(second_digit)
# print(real_first_digit + real_second_digit)
#     #math operation
    
# # 5+6
# # 3*4
# # ** exponetial 
# # PEMDAS python uses PEMDAS in python it use the one that is close to the left in 
# #python btw muliplication and division
print(3+3-3*3/3)  #() use parenthesis to isolate a code a make it the of your priority



#python print in float ....to round number in python you nee to use the round function
# round(8/4, 2) 2 stands for the number of places
4//4# is called floor division it converts your division from float to int ...
score = 5 
score += 1 #the result will get the former score and perform operation if the score is the printed 
#it would print the actually
print(score)   #it used to manipulate a value based on its previous value

score *=2  
score-=3


#print f is used to concanate a sring with integer

result = 12
print(f'Your Body Mass Index is {result}')