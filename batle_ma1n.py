import random
from actors import Player, Enemies, Humans, Monsters, Robots, Boss, Entities


def main():
    hader()
    while True:
        main_loop()
        # activate_banana()


def hader():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("WELCOMS HOUMIE TO GRAET WEEZAHRD BATLE THE GAEM")
    print("PLEAS SORY FOR MY MISPELIN. I BAD ENDLISH")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")


def get_char():
    cmd = (input("CHOOSE YOUR CLASS [G]OOD WEZRD, [D]AD WIZAD or [W]IZARD GIRL?\r\n")).lower()
    while True:
        if cmd in {'g', 'good'}:
            char = 'good'
            wiz_level = 1
            wiz_protect = 5
            return char, wiz_level, wiz_protect
        elif cmd == {'d', 'dad'}:
            char = 'Dad'
            wiz_level = 3
            wiz_protect = 2
            return char, wiz_level, wiz_protect
        elif cmd == 'w':
            char = 'majik girl'
            wiz_level = 4
            wiz_protect = 1
            return char, wiz_level, wiz_protect
        else:
            print('WHAT?')
            char = 'Dad'
            wiz_level = 3
            wiz_protect = 2
            return char, wiz_level, wiz_protect


def get_name():
    name = input('ENTer YOUV MAJIK NAME\r\n')
    return name


def wiz_atr():
    name = get_name()
    char_atr = get_char()
    char = char_atr[0]
    level = char_atr[1]
    shield = char_atr[2]
    return name, char, level, shield


def main_loop():
    loop_counter = 0
    loop_counter += 1
    if loop_counter == 1:
        atr = wiz_atr()
        name = atr[0]
        char = atr[1]
        level = atr[2]
        shield = atr[3]
        hero = Player(name, level, shield, char)
    # if you want new enemei just add it belov
    # name, atc, def, win text, lose text, atk_descr
    special_moves_list = [
        "stomp", "gromp", "bomb", "swomp", "chew"
    ]
    special_move = random.choice(special_moves_list)

    enemies = [
        Humans('funny face', 2, 1, "whos laughin now, you stinky bastard?", "wizard cant beat face? at least you can"
                                                                            " beat his meat",
               "laughing at wizard very hardr"),
        Humans('happy lovers', 4, 2, "why they should be happy?", "they was so happy and cute so wizard kill himself"
                                                                  " to death", "kissing each other"),
        Humans('math teacher', 6, 1, "this is sweat revenge", "math teacher just beat wizrad till ded",
               "teach you about algoritms"),
        Monsters('fat mom', 5, 9, "she was so fat so she nearly kill you, when falling dead",
                 "fat mom lay at wizard when he was casting majik spells", "trying talk shit about wizzards"),
        Monsters('satan, the third', 7, 7, "at least it wasn't his brother",
                 "wizrds soul forever will be in hell and die",
                 "casting big fireball"),
        Monsters('giant spider bus', 8, 6, "no one seen such a glorious death", "wizord've been drove to death",
                 "riding in the storm"),
        Robots('two big shrobots with shoots', 6, 9, "GET OUT OF HERE TIN CAN",
               "wizard was shooted with shoots", "peu-peu big shoots-whoots"),
        Robots('robo dragon', 8, 10, "its time to get over with that japanies bullshit",
             "robo dragon was too cute so weezart melted because fire", "eating wizrados brain"),
        Robots('robo slime of exquisite depravity', 12, 8, "yeah! get your stubid metal slime things off",
             "robo slime take out wizard to a date, he was cute and then die and you die too because cry and sad",
             "trying to gift metal roses to you"),
        Boss('your social anxiety', 15, 15, "you win the battle, but not the war",
             f"Brave {hero.name} can resist fire and ice, but never can go out home and play with bois", "happens",
             special_move),
        Boss('wizard laziness', 16, 16, 'wizard cant resist and lay down for relax', 'meh, too lazy to write',
             'wizzrd just lay down and sleep', 'just relax bro')
    ]

    encouters = [
        'appears from the sky',
        'materialise right in front of you',
        'got out from earth',
        'commin from local subway',
        'croos the road'
    ]
    atack_starter = [
        "its your chance for atac",
        "do smthng you dumbo",
        "FIGHT",
        "STRIFE!"
    ]
    # print(enemies)
    while True:
        active_creature = random.choice(enemies)
        current_encounter = random.choice(encouters)
        atack_start = random.choice(atack_starter)
        print(f"Beware! {hero.char} {hero.name} countinue his wey\r\n")
        while True:
            cmd1 = (input("[G]O FIND SMTHN, [I]NVENTORY AND STATS\r\n")).lower()

            if cmd1.find('g') != -1 or cmd1.find('go') != -1:
                print(
                    f"You moving forwrd and {active_creature.name} {current_encounter}. "
                    f"It has lvl {active_creature.level}"
                )
                print(f"{atack_start}")
                break

            elif cmd1.find('i') != -1 or cmd1.find('inventory') != -1:
                hero.show_inventory()

        cmd2 = (input("[A]TACC, [C]RY, [R]UN, [Q]EXIT\r\n")).lower()
        if cmd2.find('a') != -1 or cmd2.find('atacc') != -1:
            while True:
                if hero.attack(active_creature):
                    enemies.remove(active_creature)
                    print("encrease your lvl and protection\r\n")
                    hero.level += 1
                    hero.shield += 1
                    break
                else:
                    a = hero.protecc(active_creature)
                    if a == False:
                        break

        elif cmd2.find('s') != -1 or cmd2.find('cry') != -1:
            hero.cry(active_creature)
            enemies.remove(active_creature)

        elif cmd2.find('r') != -1 or cmd2.find('run') != -1:
            hero.run(active_creature)
            enemies.remove(active_creature)

        elif cmd2.find('q') != -1 or cmd2.find('quit') != -1:
            quit()
        else:
            print('WHAT')

        if not enemies:
            print(f"You defleat all enemies. Congrats {hero.name} {hero.char}, you complete teh gaem "
                  f"your end gaaem majik lvl is {hero.level} with protection {hero.shield}\r\n")
            input("SORRY NOTHING")
            quit()


if __name__ == '__main__':
    main()
