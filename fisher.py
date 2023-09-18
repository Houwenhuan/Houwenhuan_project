# 42及以上才可以放生，42以下要release
length = float(input('enter the length of a zander in centimeters:'))
size_limit = 42
if length >= size_limit:
    print('Congratulations！You can take away the zander')
else:
    below_size_limit = size_limit - length
    print(f'The centimeter is below the size limit:{below_size_limit:.2f}')
    print('Release the fish back into the lake!')
