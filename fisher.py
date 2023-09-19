# 42及以上才可以放生，42以下要release

length = float(input('enter the length of a zander in centimeters:'))
length_limit = 42
if length >= length_limit:
    print('Congratulations! You can take away the zander!')
else:
    centimeters_below_the_size_limit = float(length_limit - length)
    print(f'The centimeters below the size limit is {centimeters_below_the_size_limit:.2f} cm')
    print('Please release the fish back into the lake!')
