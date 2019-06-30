# A terminal program that can record and display,
# your time spent programming

# 07.01.2019 Carsen Weinzetl

# Initializing modules and classes
import time_module
Timer = time_module.Timer()

# Title printout
print('''
 _                     _             _                 
| |__   ___  _ __ ___ | | ___   __ _(_)_   _ _ __ ___  
| '_ \ / _ \| '__/ _ \| |/ _ \ / _` | | | | | '_ ` _ \ 
| | | | (_) | | | (_) | | (_) | (_| | | |_| | | | | | |
|_| |_|\___/|_|  \___/|_|\___/ \__, |_|\__,_|_| |_| |_|
                               |___/                   
-------------------------------------------------------
	''')

# List options
options = '''
Things you can do:
start > starts to record time
log > log your time and reset the timer
quit > exit the program and log your progress
options > show this list
'''
print(options)

#
# Prompt the user with a list of commands
usr_input = input('What would you like to do? ')

# Disseminate commands
while usr_input:

    if usr_input == 'quit':
        '''Stop the timer if started, log the time, and exit'''
        break

    elif usr_input == 'start':
        '''Begin the timer'''
        Timer.timer('start')
        break

    elif usr_input == 'log':
        '''Log the elapsed time'''
        print('Logging progress...')
        # Timer.timer('log') // This is broken for the time being
        break

    elif usr_input == 'options':
        print(options)
        break
