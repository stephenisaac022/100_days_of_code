print('Welcome To My Rollercoaster')
height = int(input('What is Your Height in cm '))
bill = 0
if height >= 120 :
    print('nice..you can ride the rollercoaster.....')
    age = int(input('What is your age '))
    if age < 12 :
       bill = 5
       print ('child tickets cost $5.')
    elif age <= 18 :
        bill = 7
        print ('Youth ticket cost $7.')
    elif age >= 45 and age <= 55 :  
        print('Your have mid-life crises, so you got a free ticket😁😁')
        
    else :
         print ('Adult ticket cost $12. ')  
         
    photo = input('Do you want take pictures? Y or N. ')
    if photo == "y" or 'Y' :
          bill += 3
    print (f"your final bill is {bill}")
else:
   print('''Sorry,You cannot ride check back in 2030
          may be your would be tall 😁😁''')



          

          
          
    