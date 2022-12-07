# Magic8Ball
import random

answers = ['It is certain',
          'It is decidedly so',
          'Without a doubt',
          'Yes - definitely',
          'You may rely on it',
          'As I see it, yes',
          'Most likely',
          'Outlook good',
          'Yes',
          'Signs point to yes',
          'Signs point to hazy',
          'Try again',
          'Ask again later',
          'Better not tell you',
          'Concentrate and ask again',
          'Cannot predict now',
          'Dont count on it',
          'My reply is no',
          'My sources say no',
          'Outlook not so good',
          'Very doubtful'
          ]

print('                           __  __          ______ _____ _____    ___  ')
print('                          |  \/  |   /\   / _____|_   _/ ____|  / _ \ ')
print('                          | \  / |  /  \ | |  ___  | || |      | (_) |')
print('                          | |\/| | / /\ \| | |_  | | || |       > _ < ')
print('                          | |  | |/ ____ \ |___| |_| || |____  | (_) |')
print('                          |_|  |_/_/    \_\______|_____\_____|  \___/ ')
print('                                                                      ')
print('                                                                      ')
print('                                                                      ')
print('Hello World, I am the Magic 8 Ball, what is your name?')
print('\n')
name = input()
print('\n')
print('Hello ' + name)

def Magic8Ball():
    print('Ask me a question.')
    input()
    print('\n')
    print(answers[random.randint(0, len(answers)-1)])
    print('\n')
    print('I hope that helped!')
    Replay()
    
def Replay():
    print('Do you have another question? [Y/N] ')
    reply = input()
    if reply == 'Y':
        Magic8Ball()
    elif reply == 'N':
        exit()
    else:
        print("I'm sorry, I did not catch that. Please repeat.")
        Replay()
        
# Call the 8Ball
Magic8Ball()