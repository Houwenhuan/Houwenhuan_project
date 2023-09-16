talents = float(input('enter the number of talents'))

pounds = float(input('enter the number of pounds'))

lots = float(input('enter the numeber of lots'))

talent = talents * (20 * 32 * 13.3)

pound = pounds * (32 * 13.3)

lot = lots * 13.3

kg = (talents + pounds + lots) / 1000

kgs = int(kg)

grams = talents + pounds + lots - kg * 1000

print(f'The weight in modern units is: {kgs} kgs and {grams:.2f} grams')
