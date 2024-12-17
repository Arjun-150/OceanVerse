'''
Write an interactive python program which does the following:

What's your name? John
How old are you? 25
What's your favorite color? Blue
What's your favorite hobby? Reading
'''

def bio():
    user_name=input('what is your name? :')
    age=input('how old are you? :')
    colour=input('what\'s your favourite color? :')
    hobby=input('what\'s your favourite hobby? :')
    print('\n')
    print('what is your name?', user_name)
    print('how old are you?',age)
    print('what\'s your favourite color?',colour)
    print('what\'s your favourite hobby?',hobby)

    answer=input('do you want to continue (y/n) :')
    if answer=='y':
        bio()
    else:
        print('thank you')
bio()
