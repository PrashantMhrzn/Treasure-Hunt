import random
from time import sleep
from treasure import TREASURE

person = ['Jeff', 'Athena', 'Aries', 'Hermies', 'Aphrodieti', 'Cerberus']
riddle = ['The more of this there is, the less you see. What is it?',
          ' I follow you all the time and copy your every move, but you can’t touch me or catch me. What am I?', 'What month of the year has 28 days?', 'What can’t talk but will reply when spoken to?', 'What is black when it’s clean and white when it’s dirty?', 'Where does today come before yesterday?']
answer = ['darkness', 'shadow', 'all', 'echo', 'blackboard', 'dictonary']
treasure_room = random.randint(1, 6)


def random_person(person):
    person = random.choice(person)
    return person


def process_inside_room(room_number):
    print(f'You are in Room:{room_number}')
    print(
        f'I am {random_person(person)}, riddle me this "{riddle[room_number-1]}"')
    usr_ans = input('> ').lower()
    if usr_ans == answer[room_number-1]:
        if room_number == treasure_room:
            sleep(1)
            print('.')
            sleep(1)
            print('...')
            sleep(1)
            print(TREASURE)
            print(f'ℭ𝔬𝔫𝔤𝔯𝔞𝔱𝔲𝔩𝔞𝔱𝔦𝔬𝔫𝔰! 𝔜𝔬𝔲 𝔣𝔬𝔲𝔫𝔡 𝔦𝔱!!!\n🅶🅰🅼🅴 🅾🆅🅴🆁')
            exit()
        else:
            sleep(1)
            print('Right answer but, The wrong room fool hahahahaaa....')
            room_number = random.randint(1, 6)
            main(room_number)
    else:
        sleep(1)
        print('Wrong answer fool! You will be teleported to the next room....')
        room_number = random.randint(1, 6)
        main(room_number)


def main(room_number):
    if room_number == 1 or room_number == 2 or room_number == 3 or room_number == 4 or room_number == 5 or room_number == 6:
        process_inside_room(room_number)
    else:
        print('Room doesn\'t exists!!!Please choose between 1-6')
