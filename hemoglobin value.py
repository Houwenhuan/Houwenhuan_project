# A normal hemoglobin value for adult females is between 117-155 g/l.
# A normal hemoglobin value for adult males is between 134-167 g/l.

male = float(input('enter your hemoglobin value(g/l) for male:'))
if male < 117:
    print('Your hemoglobin value for male is low')
elif male > 155:
    print('Your hemoglobin value is for male high')
else:
    print('Your hemoglobin value for male is normal')

female = float(input('enter your hemoglobin value(g/l) for female:'))
if female < 134:
    print('Your hemoglobin value for female is low')
elif male > 167:
    print('Your hemoglobin value is for female high')
else:
    print('Your hemoglobin value for female is normal')



