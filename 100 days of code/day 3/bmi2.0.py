print('WELCOME TO THE BODY MASS INDEX CALCULATOR')
Height = float(input('What is your Height in m \n'))
Weight = float(input('What is your Weight in Kg \n'))


# print(type(New_Height))

Real_Height = Height**2


result =Weight/Real_Height
#print f is used to concanate a string with integer
new_result = int(result)
if new_result < 18.5 :
  print(f'Your Body Mass Index is {new_result},You are under weight')
elif new_result < 25 :
  print(f'Your Body Mass Index is {new_result},You have a normal weight.')
elif new_result < 30 :
    print(f'Your Body Mass Index is {new_result}, oops you are  overweight ')
elif new_result < 35 :
    print(f'Your Body Mass Index is {new_result},sorry you are obese ')
else :
    print(f'Your Body Mass Index is {new_result},Trufully speaking you are clinically obese')