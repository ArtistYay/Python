wizard = 'Wizard'
elf = 'Elf'
human = 'Human'

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon = 'Dragon'
dragon_hp = 300
dragon_damage = 50

while True:
    while True:
        print('1) ' + wizard)
        print('2) ' + elf)
        print('3) ' + human)
        character = (input('Choose your character:'))
        if character == '1' or character == 'Wizard':
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            print('You have chosen the character: ' + character)
            print('Health: ', wizard_hp)
            print('Damage: ', wizard_damage)
            break
        if character == '2' or character == 'Elf':
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            print('You have chosen the character: ' + character)
            print('Health: ', elf_hp)
            print('Damage: ', elf_damage, '\n')
            break
        if character == '3' or character == 'Human':
            character = human
            my_hp = human_hp
            my_damage = human_damage
            print('You have chosen the character: ' + character)
            print('Health: ', human_hp)
            print('Damage: ', human_damage)
            break
        else:
            print('Unknown Character')
        break


    while True:
        dragon_hp = dragon_hp - my_damage

        print('The ' + character + ' damaged the Dragon! \n')
        print(dragon, 'hitpoint\'s are now: ', dragon_hp,'\n')

        if dragon_hp <= 0:
            print('Dragon is died!, Vahalla awaits! \n')
            break

        print('The Dragon strikes back at the ' + character)
        my_hp = my_hp - dragon_damage

        print(character, 'hitpoint\'s are now: ', my_hp)

        if my_hp <= 0:
            print('You are died, Freya is disappointed \n')
            break

    print('Do you wish to continue? Y/N')
    play = input('What do you choose?: ')
    while True:
        if play == 'N':
            print('Bye')
            exit() #Exits out the code
        elif play == 'Y':
            print('Welcome back!')
            dragon_hp = 300 #Revives the dragon
            break
