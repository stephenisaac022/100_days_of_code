 # learning objective for day 3 
 # conditonal statement,logical operators, code block and scope 
 # global and local scaping
 #   conditional statement
 #  --if /else - it would do either A or B
#indentation and how to use if/else statement..ifand else must be on 
# the same indentation level
#DRAW.IO USED FOR DRAWING FLOWCHART
#    camparison operators
        # the use of <  for less than starts from the number lower  than the exact number
        # the use of >  for greater than starts from the number higher than the exact number
        # the use of >= for greater/equal-starts from that number exactly to any number above it...
        # the use of <= for less than /equal-starts from that number exactly to any number below
        # the use of == for equal 
        # the use of = is for assignment of  a quantity to a variable 
        # the use of != for not equal 
# = (one equal to sign)is used for assigning a number to a variable
# == (two equal to sign)is used to check for equality
    # NESTED IF\ELSE STATEMENT
       # ANOTHER IF ELSE STATEMENT IN AND IF ELSE STATEMENT  

        



print('WELCOME TO HEIGHT CHECKER')

height = float(input("What is your Height in CM \n "))

if height > 100:
    age = int(input('What is your Age '))
    if age == 18: 
      print ('nice one...')
    elif age >= 18 :
      print('welcome to the gang ')
       
    print('KUDOS, You are TALL')
else:
    print( 'OOPS, You are SHORT...!!!' )
