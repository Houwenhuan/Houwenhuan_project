# A normal hemoglobin value for adult females is between 117-155 g/l.
# A normal hemoglobin value for adult males is between 134-167 g/l.
gender = input('enter your gender(male or female):')
value = float(input('enter your value'))
if gender == 'male':
    if value < float('117'):
        print('Your hemoglobin value for male is low')
    elif float('117') <= value <= float('155'):
        print('Your hemoglobin value is for male is normal')
    else:
        print('Your hemoglobin value for male is high')
if gender == 'female':
    if value < float('134'):
        print('Your hemoglobin value for female is low')
    elif float('134') <= value <= float('167'):
        print('Your hemoglobin value is for female normal')
    else:
        print('Your hemoglobin value for female is high')



