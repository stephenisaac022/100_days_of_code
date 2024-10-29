print('WELCOME TO THE BODY MASS INDEX CALCULATOR')
Height = input('What is your Height in m \n')
Weight = input('What is your Weight in Kg \n')


New_Height = float(Height)
New_Weight = float(Weight)


# print(type(New_Height))

Real_Height = New_Height**2


result = New_Weight/Real_Height
#print f is used to concanate a sring with integer

print(f'Your Body Mass Index is {result}')
print(int(result))
