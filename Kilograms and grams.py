talents = float(input('enter the number of talents'))

pounds = float(input('enter the number of pounds'))

lots = float(input('enter the number of lots'))

talents = talents * (20 * 32 * 13.3)

pounds = pounds * (32 * 13.3)

lots = lots * 13.3

kgs = int((talents + pounds + lots) / 1000)

grams = talents + pounds + lots - kgs * 1000

print(f'The weight in modern units is: \n{kgs} kgs and {grams:.2f} grams')