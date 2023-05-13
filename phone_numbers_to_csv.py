import os
import sys

Phone_numbers = ['08034484902', '08021691144', '+234 808 837 6695' ]
Phone_numbers2 = ['+234 706 719 7712', '+234 802 331 6246']

with open('Phone_numbers.csv', 'w') as numbers:
    Phone_numbers_write = numbers.writelines(Phone_numbers)
    Phone_numbers2_write = numbers.writelines(Phone_numbers2)
    print('numbers saved')
