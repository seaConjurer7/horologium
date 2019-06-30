# Module for all functions to be used by 'horologium' to record
# and return time spent programming

import time


class Records:
    '''Stores users and their logged time'''

    def __init__(self):
        '''Initialize dictionary of users'''

        self.users = {}

    def write_time(self, time):
        '''Writing the recorded time to the give users dictionary'''


class Timer:
    '''Class that holds the logic behind the time recordings'''

    def __init__(self):
        '''Initialize time on timer'''

    def timer(self, command):
        '''According to input, start or stop the timer'''
        total_time = 0

        if command == 'start':
            # Prints the different between the start/stop as
            # the elapsed time
            start = time.time()
            end = input('Type "stop" to stop the timer ')

            if end == 'stop':
                stop = time.time()
                elapsed = stop - start

                # Print the elapsed time
                print('You have worked for, '
                      + str(round(elapsed))
                      + ' seconds.')

        elif command == 'log':
            '''Writing the total time to the dictionary'''
            print('Logging time...')
