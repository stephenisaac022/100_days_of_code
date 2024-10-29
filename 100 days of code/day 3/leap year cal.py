year = int(input('What Year Do Want to Check \n')) 
if year % 4 == 0:
    if year % 100 == 0 :
        if year % 400 == 0 :
            print('leap year')
        else :
            print('not a leap year ')
        
    else :
        print('Leap Year')
     
else :
    print ('Not a leap year. ')
