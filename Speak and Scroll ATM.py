# Typewriter code block
import sys
from time import sleep

words = "This is a test of the scroll system"
for char in words:
    sleep(0.03)
    sys.stdout.write(char)
    sys.stdout.flush()

# Install pyttsx3 module
#!pip install pyttsx3      # This is commented out because it is already installed.

# Import required module for text to speech conversion
import pyttsx3           # This is commented out because it is already imported.

# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()

# Define the voice of the ATM teller
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0" # Assign Voice ID to change the accet of the voice: Female GB English.
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # Change voice of module: changing "voices[0]" to "voices[1]": 0 = male, 1 = female
engine.setProperty("rate", 180) # Change the rate of speech
engine.runAndWait() # Continue with runAndWait

# Have words print like a typewriter
import sys
from time import sleep

# Words Class Program     SO FAR THIS HAS NOT WORKED
# Areas tried: 
# class Bank under def welcome at "input.words"
# class Bank under def print_current_balance at "words.print"
# if statements at words.bank.etc..

class Word:
    def __init__(words):
        words = ''
        for char in words:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
    
# Bank Class Program
class Bank:
    def __init__(self):
        self.total_amount = 0
        self.name = ''
        
    def welcome(self):
        engine.say('Welcome to your Bank Account. Please enter your name')
        engine.runAndWait()
        self.name = input('Welcome to your Bank Account. Please enter your name : ')
        
    def print_current_balance(self):
        engine.say('Your current balance is : {} dollars. '.format(self.total_amount))
        engine.runAndWait()
        print('Your current balance : ${} '.format(self.total_amount))   # Added print.words here to test. DID NOT WORK
        
    def deposit(self):
        engine.say('{}, Please enter amount to deposit.'.format(self.name))
        engine.runAndWait()
        self.total_amount += float(input('{}, please enter amount to deposit : '.format(self.name)))
        self.print_current_balance()
        
    def withdraw(self):
        engine.say('{}, Please enter amount to withdraw.'.format(self.name))
        engine.runAndWait()
        amount_to_withdraw = float(input('{}, please enter amount to withdraw : '.format(self.name)))
        
        if amount_to_withdraw > self.total_amount:
            engine.say('Insufficient balance!!!')
            engine.runAndWait()
            print('Insufficient balance!!!')
            
        else:
            self.total_amount -= amount_to_withdraw
            
        self.print_current_balance()
        
    def exit_account(self):
        print('Thank you {}, and have a lovely day.'.format(self.name))
        engine.say('Thank you {}, and have a lovely day.'.format(self.name))
        engine.runAndWait()
        
if __name__=="__main__":
    bank = Bank()
    bank.welcome()
    
    while True:
        engine.say('Please enter 1 to see your balance, 2 to deposit, 3 to withdraw, or 4 to exit your account')
        engine.runAndWait()
        input_value = int(input('Enter number to see:\n1- Balance\n2- Deposit\n3- Withdraw\n4- Exit your account\n'))
        
        if input_value == 1:
            bank.print_current_balance()
        elif input_value == 2:
            bank.deposit()
        elif input_value == 3:
            bank.withdraw()
        elif input_value == 4:
            bank.exit_account()
            print('Transactions Complete.')
            break
            
        else:
            engine.say('Please enter a valid input.')
            engine.runAndWait()
            print('Please enter a valid input.')