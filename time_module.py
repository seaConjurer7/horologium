# Module for all functions to be used by 'horologium' to record
# and return time spent programming

import time


class Timer:
    '''Class that holds the logic behind the time recordings'''

    def __init__(self):
        '''Initialize time on timer by reading it from file'''
        file = 'record.py'
        with open(file, 'r') as f_obj:
            self.total_time = f_obj.read()

        # Translating str to int
        self.total_time = int(self.total_time)

    def timer(self, command):
        '''According to input, start or stop the timer'''

        if command == 'start':
            # Prints the different between the start/stop as
            # the elapsed time
            start = time.time()
            end = input('Type "stop" to stop the timer ')

            if end == 'stop':
                stop = time.time()
                elapsed = round(stop - start)

                # Print the elapsed time
                print('You have worked for, '
                      + str(elapsed)
                      + ' seconds.')
                self.total_time += elapsed

                # Translating int back to str
                self.total_time = str(self.total_time)

                # Automatically writing the time elapsed to file
                file = 'record.py'
                with open(file, 'w') as f_obj:
                    f_obj.write(self.total_time)

            else:
                print('Thats not how you spell stop dumbass')

        elif command == 'log':
            '''Show total accrued time that is in the record'''

            # Opening record
            file = 'record.py'
            with open(file, 'r') as f_obj:
                accrued = f_obj.readlines()

            statement = print('\nYou have spent a total of, '
                              + str(accrued)
                              + ' secconds doing whatever you were doing!')
            print(statement)

        else:
            # For if I break something
            print('Whoops...')
