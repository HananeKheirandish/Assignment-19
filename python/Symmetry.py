numbers = input('Enter ypur list:')
list = numbers.split(',')
list_revers = list.copy()
list_revers.reverse()
if list == list_revers:
    print('List is Symmerty!!')
else:
    print('List is not symmerty!!')