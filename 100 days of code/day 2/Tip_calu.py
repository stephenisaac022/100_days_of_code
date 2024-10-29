 #psedo code
 #ask the user for input of the total bill
 #get the perceentage tip
 #know how many people to slit the bill
 #print result 
 
 
 
print('Welcome to tip calculator....please note only include number and point for this calulator')
bill = float(input('What is Your Total Bill $ \n'))
tip = float(input('What is the tip would you like to Give 10, 12, 15 %  \n ' ))

pay = float(bill * tip / 100)
people = float (input ('How many people to spilt the bill \n '))

act_bill = float(pay + bill )
result = (round(act_bill / people, 2))
# using the format function to get it have two decimal places "{:.2f}".format(act_bill / people) 
result = "{:.2f}".format(act_bill / people)
print(f'Each person should pay: ${result}')
 