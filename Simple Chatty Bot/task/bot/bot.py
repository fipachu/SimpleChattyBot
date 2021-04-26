def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")

    while True:
        print(("How many cats is the right number of cats for a programmer to own?\n"
               "0. 0\n"
               "2. 2\n"
               "999. 999\n"
               "-666. -666"))
        if input() == "2":
            break
        else:
            print("That's either too many or too few cats, I can't really tell.")

    print("That's right! Two is the exact, right number of cats!")


def end():
    print('Congratulations, have a nice day!')


greet('Adi', '2021')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
