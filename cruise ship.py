cabin_class = (input('enter the cabin class of a cruise ship(LUX,A,B,C): '))
if cabin_class == 'LUX':
    print('LUX: upper-deck cabin with a balcony.')
elif cabin_class == 'A':
    print('A: above the car deck, equipped with a window.')
elif cabin_class == 'B':
    print('B: windowless cabin above the car deck.')
elif cabin_class == 'C':
    print('C: windowless cabin below the car deck')
else:
    print('error message:Invalid cabin class')
