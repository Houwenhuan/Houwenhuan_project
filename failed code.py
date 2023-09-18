# this code is undone,even if there are some mistakes, I need to try it out
gender = input('enter your gender:')
if gender == 'male':
    print('enter your hemoglobin value(g/l) for male:')
else:
    print('enter your hemoglobin value(g/l) for female:')
value = 'male'
if value < str(117):
    print('Your hemoglobin value for male is low')
elif value > str(155):
    print('Your hemoglobin value is for male is high')
else:
    print('Your hemoglobin value for male is normal')