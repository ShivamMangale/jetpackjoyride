# Python program to print 
# red text with green background 

from colorama import Fore, Back, Style 
print(Fore.RED + 'some red text') 
print(Back.GREEN + 'and with a green background') 
print(Style.DIM + 'and in dim text')
print('Is this normal')
print(Style.RESET_ALL) 
print('back to normal now') 