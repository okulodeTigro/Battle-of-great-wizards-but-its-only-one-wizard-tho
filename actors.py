import random
import time


class Entities:
    def __init__(self, name, level, shield):
        self.name = name
        self.level = level
        self.shield = shield

    def attack(self, enemie):
        print(f"{self.name} [ATTACK] {enemie.name}")
        my_attack_roll = random.randint(1,20) * self.level
        enemie_defence_roll = random.randint(1,20) * enemie.shield
        time.sleep(1)
        print(f"Your spell have power of {my_attack_roll}\r")
        time.sleep(1)
        print(f"{enemie.name} have protection {enemie_defence_roll}\r")

        if my_attack_roll >= enemie_defence_roll:
            time.sleep(1)
            print(f"Blizzard cast very much spell. {enemie.name} died. {enemie.text}")
            return True
        else:
            time.sleep(1)
            print(f"Wiz cant cast enough much spell to kill {enemie.name}")
            return False

    def protecc(self, enemie):
        time.sleep(1)
        print("[ENIEME TURN]\r")
        time.sleep(1)
        print(f"{self.name} [PROTECT] from {enemie.name}\r")
        my_defence_roll = random.randint(1,20) * self.shield
        enemie_atack_roll = random.randint(1,20) * enemie.level
        time.sleep(1)
        print(f"{enemie.name} {enemie.atk_descr} with power {enemie_atack_roll}\r")
        time.sleep(1)
        print(f"{self.name} have protection {my_defence_roll}\r")

        if my_defence_roll >= enemie_atack_roll:
            print(f"{enemie.name} cant atac though wizzards protection spells")
            return True
        else:
            print(f"{enemie.loss}")
            print("YOU DEAD\rGAME OVER\rRIP\r")
            answ = (input("YOU wANNA TRY AGAINGN? (Y/N?)\r\n")).lower()
            if answ == "y":
                print("We resurrecting your ass niBBa")
                time.sleep(1)
            else:
                print("TOO BAD. COME BACK WHEN YOU GET SOME BALLS")
                quit()
            return False

    def cry(self, enemie):
        print(f"you cry very loud and {enemie.name} run. now its gone. no {enemie.name}, {enemie.text}")


    def run(self, enemie):
        print(f"You coward pussy. Run from {enemie.name}, RUN!")

class Player(Entities):
    inv  = [
            "majik stuff",
            "stinky robe",
            "strange pervert journals",
            "bread"
        ]

    def __init__(self, name, level, shield, char):
        super().__init__(name, level, shield)
        self.char = char

    def show_inventory(self):
        print("you have with you")
        for index, entity in enumerate(self.inv):
            print('* {0} - {1}\r'.format(index, entity))
        print (f"Your majik levl is {self.level}, your armror is {self.shield} and you are still {self.char}")


class Enemies(Entities):
    def __init__(self, name, level, shield, victory_text, loss_text, atk_descr):
        super().__init__(name, level, shield)
        self.text = victory_text
        self.loss = loss_text
        self.atk_descr = atk_descr

    def __repr__(self):
        return f"Eniemie {name} of lvl {level}"


class Humans(Enemies):
    # you can add here shit for humans enemies just like in "Boss" class
    # also, here you can specified loot for each TYPE of enemy, or can just
    # add loot as argument in Enemies class and specified loot for
    # each enemy
    pass

class Monsters(Enemies):
    # you can add here shit for monster enemies just like in "Boss" class
    pass

class Robots(Enemies):
    # you can add here shit for robots enemies just like in "Boss" class
    pass

class Boss(Enemies):
    def __init__(self, name, level, shield, victory_text, loss_text, atk_descr, special_move):
        super().__init__(name, level, shield, victory_text, loss_text, atk_descr)
        self.special_move = special_move
