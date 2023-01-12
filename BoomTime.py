# Timer

# Import modules
import time

#time.sleep(3)
#print('Sleep cycle complete')

# Define countdown function
def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Execute')

# Input time in seconds
t = input('Enter time to execute in seconds: ')
print('Program will execute in:')

# Function call
countdown(int(t))