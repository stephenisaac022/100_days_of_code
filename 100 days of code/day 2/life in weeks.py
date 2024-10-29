# Want to know more about life...note this calender does not calculate leap years


age = int(input('What your Current Age \n'))
time = int(input('How Many years do your want to live \n '))
years = age * 365
weeks = age  * 52
months = age * 12
print(f'YOU HAVE LIVED {years} Days, {weeks} Weeks,and {months} Months')
life_in_weeks = int(time - age)

rem_days = life_in_weeks * 365
rem_weeks = life_in_weeks * 52
rem_months = life_in_weeks * 12

print(f'YOU HAVE  {rem_days} Days, {rem_weeks} Weeks, and  {rem_months} Months LEFT....')
print('All By God grace .......Thank you  ')


