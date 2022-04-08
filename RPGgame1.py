import random
import sys
import time


class Monster:
    def __init__(self) -> None:
        super().__init__()
        list_name = ["Goblins", "Bear", "Devil", "Titan"]
        self._name = random.choice(list_name)
        self._hp = 900
        self._atk = 60
        self.sensitivity = 8
        self.level = 1
        self._state = True
        self.mdefense = 20
        self.pdefense = 20

    @property
    def hp(self):
        return self._hp

    @property
    def atk(self):
        return self._atk

    def attack(self, obj):
        if obj.hp < 0:
            print(obj.name, "is dead")
            return
        else:
            hurt = self._atk - obj.pdefense
            print("------",self._name, "damage on hero:", hurt,"------")
        obj.be_hurt(hurt)

    def lev(self, player_level):
        if player_level <= 3:
            self._hp = 900
            self._atk = 60
        elif player_level < 10:
            self.level = random.randint(player_level - 3, player_level + 3)
            self._hp = 900 + (900 * 0.06 * (self.level - 1))
            self._atk += 60 + (60 * 0.09 * (self.level - 1))
            self.sensitivity += 8 + (8 * 0.12 * (self.level - 1))
        elif player_level < 20:
            self.level = random.randint(player_level - 3, player_level + 3)
            self._hp = 900 + (900 * 0.12 * (self.level - 1))
            self._atk += 60 + (60 * 0.8 * (self.level - 1))
            self.sensitivity += 8 + (8 * 0.12 * (self.level - 1))
        elif player_level < 30:
            self.level = random.randint(player_level - 3, player_level + 3)
            self._hp = 900 + (900 * 0.3 * (self.level - 1))
            self._atk += 60 + (60 * 1.2 * (self.level - 1))
            self.sensitivity += 8 + (8 * 0.12 * (self.level - 1))
        else:
            self.level = random.randint(player_level - 3, player_level + 3)
            self._hp = 900 + (900 * 0.5 * (self.level - 1))
            self._atk += 60 + (60 * 1.8 * (self.level - 1))
            self.sensitivity += 8 + (8 * 0.12 * (self.level - 1))

    def be_hurt(self, hurt):
        if self._state:
            self._hp = 0 if self._hp - hurt < 0 else self._hp - hurt
            self._state = self._hp > 0
        else:
            print("Show some respect to the death!")


# Fight between Hero and monsters
def fight(m, w):  # m: master/warrior, w: mmonster
    while m.hp > 0 and w.hp > 0:
        time.sleep(0.1)
        if m.sensitivity > w.sensitivity:
            chose = random.randint(0, 2)
            m.attack(chose, w)
            print( w._name, "was attacked,remaining HP:", w.hp)
            if w.hp > 0:
                w.attack(m)
                print(m._name, "was attacked,remaining HP:", m.hp)
        else:
            w.attack(m)
            print( m._name, "was attacked,remaining HP:", m.hp)
            if m.hp > 0:
                chose = random.randint(0, 2)
                m.attack(chose, w)
                print( w._name, "was attacked, remaining HP:", w.hp)
        if m.hp == 0:
            print( w._name, " wins")
        elif w.hp == 0:
            empirical = random.randint(50, 150)
            m.empirical += empirical
            m.money += 50
            print( m._name, " wins, Get coins:50; EXP:", empirical)



class Account:
    def __init__(self) -> None:
        super().__init__()
        self.__id = "123"
        self.__password = "123456"
        self.__balance = 1000
        self.__role_balance = 0

    @property
    def id(self):
        return self.__id

    @property
    def password(self):
        return self.__password

    @property
    def balance(self):
        return self.__balance

    @property
    def role_balance(self):
        return self.__role_balance

    def login(self):
        id = input("ID:")
        pwd = input("Passward:")

        if id == self.__id and pwd == self.password:
            print("Login Succeed, please")
        else:
            print("Wrong account ID/ passward, please input again")
            self.login()


    def oprator(self, obj):
        print("""
--------------------------------------
     How much do you want to recharge?
        (1Rmb=1000 coins)
--------------------------------------
""")
        print("""
        1.5 $
        2.10 $
        3.15 $
        4.20 $
        others(exit)
        """)
        choice = input("Input your choice:")
        if "1" <= choice <= "4":
            if self.__balance - int(choice) * 5 > 0:
                self.__balance -= int(choice) * 5
                self.__role_balance += int(choice) * 5 * 1000
            else:
                print("Not enough balance")
            print("Balance:", self.__balance)
            obj._money += self.__role_balance
            print("Succeed in recharging with coin left:", obj.money)

        else:
            return "EXIT"


# Roles
class Role:
    def __init__(self, name) -> None:
        super().__init__()
        self._name = name
        self._empirical = 0
        self._level = 1
        self._money = 0
        self._bag = []

    @property
    def name(self):
        return self._name

    # package
    def save_bag(self, value):
        self._bag.append(value)
        return self._bag

    # coins
    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = value

    # experience
    @property
    def empirical(self):
        return self._empirical

    @empirical.setter
    def empirical(self, value):
        self._empirical = value

    # level
    @property
    def level(self):
        return self._level

    def attack(self, value, obj):
        pass

    def be_hurt(self, hurt):
        pass


# master
class Master(Role):

    def __init__(self, name) -> None:
        super().__init__(name)
        self.__hp = 800
        self.__atk = 120
        self.__magic = 800
        self.__mdefense = 50
        self.__pdefense = 20
        self.__sensitivity = 12
        self.__attribute = "wizard"

    @property
    def attribute(self):
        return self.__attribute

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self,value):
        self.__hp = value

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def magic(self):
        return self.__magic

    @magic.setter
    def magic(self, value):
        self.__magic = value

    @property
    def mdefense(self):
        return self.__mdefense

    @mdefense.setter
    def mdefense(self, value):
        self.__mdefense = value

    @property
    def pdefense(self):
        return self.__pdefense

    @pdefense.setter
    def pdefense(self, value):
        self.__pdefense = value

    @property
    def sensitivity(self):
        return self.__sensitivity

    # upgrade
    def upgrade(self, value):
        if value >= 100 and self._level < 40:
            self._level += value // 100
            self._empirical = value % 100
            self.__hp = 800 + (800 * 0.08 * (self._level - 1))
            self.__atk += self.__atk * 0.13
            self.__magic = 800 + (800 * 0.12 * (self._level - 1))
            self.__mdefense += self.__mdefense * 0.12
            self.__pdefense += self.__pdefense * 0.11
            self.__sensitivity += self.__sensitivity * 0.119
        else:
            if value < 100:
                self.empirical = value
            elif value > 4000 - self.level * 100:
                self._level = 40  # maximum level
                self.empirical = 100  # EXP needed

    def attack(self, value, obj):  # attack attribute 
        if obj.hp <= 0:
            print("Already dead")
            return
##################################### still need to think of the cool name of skills ##########################################
        else:
            if value == 0:
                hurt = self.__atk - obj.mdefense
                print(self._name, "attack", obj._name, ", damage;", hurt)
            elif value == 1:
                if self.magic > 100:
                    hurt = self.__atk * 1.5 - obj.mdefense
                    print(self._name, "skill 1", obj._name, "damage:", hurt)
                    self.__magic -= 100
                else:
                    hurt = self.__atk - obj.mdefense
                    print("Not enough MP,attack!", obj._name, ",damage:", hurt)
            else:
                if self.magic > 100:
                    hurt = self.__atk * 0.9 - obj.mdefense
                    print(self._name, "skill 2", obj._name, ",damage:", hurt)
                    self.__magic -= 100
                else:
                    hurt = self.__atk - obj.mdefense
                    print("Not enough MP,attack!", obj._name, "damage:", hurt)
        obj.be_hurt(hurt)

    def be_hurt(self, hurt):
        if self.hp > 0:
            self.__hp = 0 if self.__hp - hurt < 0 else self.__hp - hurt
        else:
            print("Already dead")

    # equipment
    def get_bag(self):
        choose = input("Choose your equipment:")
        if self.level < 10:
            print("Your level is too low and there is no suitable equpiments")
            return False
        elif self.level < 20:
            if choose == "Series_1":
                self.__atk += 15 * self.level
                self.__mdefense += 10 * self.level
                self.__pdefense += 25 * self.level
                print("Succeed in equipping")
                self._bag.remove("Series 1")
                return True
            else:
                print("Your level doesn't match")
                return False
        elif self.level < 30:
            if choose == "Series_2":
                self.__atk += 20 * self.level
                self.__mdefense += 20 * self.level
                self.__pdefense += 20 * self.level
                print("Succeed in equipping")
                self._bag.remove("Series_2")
                return True
            else:
                print("Your level doesn't match")
                return False
        elif self.level < 40:
            if choose == "Series_3":
                self.__atk += 30 * self.level
                self.__mdefense += 30 * self.level
                self.__pdefense += 30 * self.level
                print("Succeed in equipping")
                self._bag.remove("Series_3")
                return True
            else:
                print("Your level doesn't match")
                return False
        else:
            if choose == "Series_4":
                self.__atk += 40 * self.level
                self.__mdefense += 40 * self.level
                self.__pdefense += 40 * self.level
                print("Succeed in equipping")
                self._bag.remove("Series_4")
                return True
            else:
                print("Your level doesn't match")
                return False


class Warrior(Role):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.__hp = 1066
        self.__atk = 100
        self.__magic = 300
        self.__mdefense = 20
        self.__pdefense = 20
        self.__sensitivity = 12
        self.__attribute = "physics"

    @property
    def attribute(self):
        return self.__attribute

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def magic(self):
        return self.__magic

    @magic.setter
    def magic(self, value):
        self.__magic = value

    @property
    def mdefens(self):
        return self.__mdefense

    @mdefens.setter
    def mdefens(self, value):
        self.__mdefens = value

    @property
    def pdefense(self):
        return self.__pdefense

    @pdefense.setter
    def pdefense(self, value):
        self.__pdefense = value

    @property
    def sensitivity(self):
        return self.__sensitivity

    # upgrade
    def upgrade(self, value):
        if value >= 100 and self._level < 40:
            self._level += value // 100
            self._empirical = value % 100
            self.__hp = 1066 + (1066 * 0.11 * (self._level - 1))
            self.__atk += self.__atk * 0.13
            self.__magic = 300 + (300 * 0.11 * (self._level - 1))
            self.__mdefense += self.__mdefense * 0.11
            self.__pdefense += self.__pdefense * 0.12
            self.__sensitivity += self.__sensitivity * 0.12
        else:
            if value < 100:
                self.empirical = value
            elif value > 4000 - self.level * 100:
                self._level = 40  # maximum level
                self.empirical = 100  # EXP needed

    def attack(self, value, obj):
        if obj.hp <= 0:
            print("Already dead")
            return
        else:
            if value == 0:
                hurt = self.__atk - obj.pdefense
                print(self._name, "attack", obj._name, ",damage:", hurt)
            elif value == 1:
                if self.magic > 100:
                    hurt = self.__atk * 1.5 - obj.pdefense
                    self.__magic -= 100
                    print(self._name, "Skill 5,", obj._name, "damage:", hurt)
                else:
                    hurt = self.__atk - obj.pdefense
                    print("Not enough MP,attack", obj._name, "damage:", hurt)
            else:
                if self.magic >= 100:
                    hurt = self.__atk * 0.9 - obj.pdefense
                    print(self._name, "Skill 6", obj._name, "damage:", hurt)
                    self.__magic -= 100
                else:
                    hurt = self.__atk - obj.pdefense
                    print(self._name, "Not enough MP,attack", obj._name, "damage:", hurt)
        obj.be_hurt(hurt)

    def be_hurt(self, hurt):
        if self.hp > 0:
            self.__hp = 0 if self.__hp - hurt < 0 else self.__hp - hurt
        else:
            print("Already dead")

    # equipment
    def get_bag(self):
        choose = input("Choose your equipment:")
        if self.level < 10:
            print("Your level is too low and there is no suitable equipment")
            return False
        elif self.level < 20:
            if choose == "Seires_5":
                self.__atk += 10 * self.level
                self.__mdefense += 10 * self.level
                self.__pdefense += 10 * self.level
                print("Succeed in equipping")
                self._bag.remove("Series_5")
                return True
            else:
                print("Your level doesn't match")
                return False
        elif self.level < 30:
            if choose == "Series_6":
                self.__atk += 20 * self.level
                self.__mdefense += 20 * self.level
                self.__pdefense += 20 * self.level
                print("Succeed in equipping")
                self._bag.remove("Series_6")
                return True
            else:
                print("Your level doesn't match")
                return False
        elif self.level < 40:
            if choose == "Series_7":
                self.__atk += 30 * self.level
                self.__mdefense += 30 * self.level
                self.__pdefense += 30 * self.level
                print("Succeed in equipping")
                self._bag.remove("Series_7")
                return True
            else:
                print("Your level doesn't match")
                return False
        else:
            if choose == "Series_8":
                self.__atk += 40 * self.level
                self.__mdefense += 40 * self.level
                self.__pdefense += 40 * self.level
                print("Succeed in equipping")
                self._bag.remove("Series_8")
                return True
            else:
                print("Your level doesn't match")
                return False


class Store():
    def __init__(self) -> None:
        super().__init__()

    @property
    def money(self):
        return self.money

    # sell revival coin
    def resurrection(self, obj):
        if obj.money >= 1000 * obj.level:
            obj.money -= 1000 * obj.level
            if obj.attribute == "magic":
                obj.hp = 800 + (800 * 0.08 * (obj.level - 1))
                obj.magic = 800 + (800 * 0.12 * (obj.level - 1))
            else:
                obj.hp = 1066 + (1066 * 0.11 * (obj._level - 1))
                obj.magic = 300 + (300 * 0.11 * (obj._level - 1))
            print("Revival with full HP")
        else:
            print("Not enough coins, please recharge")

    # sell equipment
####################################### still need to think the cool names of the weapon series #############################################
    def buy_equipment(self, obj, grade):
        equipment_list = \
            {
                "magic": {"10": ["Series_1", 1000], "20": ["Series_2", 4000], "30": ["Series_3", 8000], "40": ["Series_4", 10000]},
                "physics": {"10": ["Series_5", 1000], "20": ["Series_6", 4000], "30": ["Series_7", 8000], "40": ["Series_8", 10000], }
            }
        if obj.attribute == "magic":
            while True:
                user_weapon = input("Please choose your weapon: \n1:Series_1\n2:Series_2\n3:Series_3\n4:Series_4")
                if user_weapon not in ["1", "2", "3", "4"]:
                    print("It's not approved, please input again")
                else:
                    if user_weapon == "1":
                        if grade >= 10 and obj.money >= equipment_list["magic"]["10"][1]:
                            print("Congratulations, you get the weapon:", equipment_list["magic"]["10"][0])
                            obj.money -= 1000
                            obj.save_bag(equipment_list["magic"]["10"][0])
                            return equipment_list["magic"]["10"][0]
                        elif grade >= 10 and obj.money < equipment_list["magic"]["10"][1]:
                            print("Not enough coins")
                            return
                        else:
                            print("Fail to meet the minimum level requirement of buying the weapons")
                            return

                    elif user_weapon == "2":
                        if grade >= 20 and obj.money >= equipment_list["magic"]["20"][1]:
                            print("Congratulations, you get the weapon:", equipment_list["magic"]["20"][0])
                            obj.money -= 4000
                            obj.save_bag(equipment_list["magic"]["20"][0])
                            return equipment_list["magic"]["20"][0]
                        elif grade >= 20 and obj.money < equipment_list["magic"]["20"][1]:
                            print("Not enough coins")
                            return
                        else:
                            print("Fail to meet the minimum level requirement of buying the weapons")
                            return

                    elif user_weapon == "3":
                        if grade >= 30 and obj.money >= equipment_list["magic"]["30"][1]:
                            print("Congratulations, you get the weapon:", equipment_list["magic"]["30"][0])
                            obj.money -= 8000
                            obj.save_bag(equipment_list["magic"]["30"][0])
                            return equipment_list["magic"]["30"][0]
                        elif grade >= 30 and obj.money >= equipment_list["magic"]["30"][1]:
                            print("Not enough coins")
                            return
                        else:
                            print("Fail to meet the minimum level requirement of buying the weapons")
                            return


                    elif user_weapon == "4":
                        if grade >= 40 and obj.money >= equipment_list["magic"]["40"][1]:
                            print("Congratulations, you get the weapon:", equipment_list["magic"]["40"][0])
                            obj.money -= 10000
                            obj.save_bag(equipment_list["magic"]["40"][0])
                            return equipment_list["magic"]["40"][0]
                        elif grade >= 40 and obj.money >= equipment_list["magic"]["40"][1]:
                            print("Not enough coins")
                            return
                        else:
                            print("Fail to meet the minimum level requirement of buying the weapons")
                            return


        if obj.attribute == "physics":
            while True:
                user_weapon = input("Please choose your weapon: \n1:Series_5\n2:Series_6\n3:Series_7\n4:Series_8")
                if user_weapon not in ["1", "2", "3", "4"]:
                    print("It's not approved, please input again")
                else:
                    if user_weapon == "1":
                        if grade >= 10 and obj.money >= equipment_list["physics"]["10"][1]:
                            print("Congratulations, you get the weapon:", equipment_list["physics"]["10"][0])
                            obj.money -= 1000
                            obj.save_bag(equipment_list["physics"]["10"][0])
                            return equipment_list["physics"]["10"][0]
                        elif grade >= 10 and obj.money < equipment_list["physics"]["10"][1]:
                            print("Not enough coins")
                            return
                        else:
                            print("Fail to meet the minimum level requirement of buying the weapons")
                            return

                    elif user_weapon == "2":
                        if grade >= 20 and obj.money >= equipment_list["physics"]["20"][1]:
                            print("Congratulations, you get the weapon:", equipment_list["physics"]["20"][0])
                            obj.money -= 4000
                            obj.save_bag(equipment_list["physics"]["20"][0])
                            return equipment_list["physics"]["20"][0]
                        elif grade >= 20 and obj.money < equipment_list["physics"]["20"][1]:
                            print("Not enough coins")
                            return
                        else:
                            print("Fail to meet the minimum level requirement of buying the weapons")
                            return

                    elif user_weapon == "3":
                        if grade >= 30 and obj.money >= equipment_list["physics"]["30"][1]:
                            print("Congratulations, you get the weapon:", equipment_list["physics"]["30"][0])
                            obj.money -= 8000
                            obj.save_bag(equipment_list["physics"]["30"][0])
                            return equipment_list["physics"]["30"][0]
                        elif grade >= 30 and obj.money < equipment_list["physics"]["30"][1]:
                            print("Not enough coins")
                            return
                        else:
                            print("Fail to meet the minimum level requirement of buying the weapons")
                            return

                    elif user_weapon == "4":
                        if grade >= 40 and obj.money >= equipment_list["physics"]["40"][1]:
                            print("Congratulations, you get the weapon:", equipment_list["physics"]["40"][0])
                            obj.money -= 10000
                            obj.save_bag(equipment_list["physics"]["40"][0])
                            return equipment_list["physics"]["40"][0]
                        elif grade >= 40 and obj.money < equipment_list["physics"]["40"][1]:
                            print("Not enough coins")
                            return
                        else:
                            print("Fail to meet the minimum level requirement of buying the weapons")
                            return



class UI:
    player = Warrior("Warrior")  # default: warriors
    account = Account()

    @classmethod
    def welcome(cls):
        print(
            """
----------------------------------------------
            Welcome to RPGGGGGGGG GAME
----------------------------------------------
            """
        )
        cls.home_page()

    @classmethod
    def home_page(cls):
        print(
            """
           * * * * * * * * * * * * * *
           *   1.Choose Player       *
           *   2.Entry Shop          *
           *   3.Entry Charge        *
           *   4.Choose weapon       *
           *   5.Player information  *
           *   6.Enter the fight     *
           *   7.Exit                *
           * * * * * * * * * * * * * *
            """
        )
        choose = input("Please input the number to select section: (1-6)")
        if choose == "1":
            cls.creat_player()
        elif choose == "2":
            cls.shopping_mall(cls.player)
        elif choose == "3":
            cls.recharge()
        elif choose == "4":
            cls.equipment(cls.player)
        elif choose == "5":
            cls.information()
        elif choose == "6":
            print(
                """
-----------------------------------
        Fight loading...
        Fight begins!
-----------------------------------
                """
            )
            cls.battle()
        elif choose == "7":
            cls.exit()
        else:
            cls.home_page()

    @classmethod
    def creat_player(cls):
        print("""\033[1;33;0m
--------------------------------------
|        Choose your role:           |
|                                    |
|          1.Warrior                 |
|          2.Magician                |
|          Other: Back               |
--------------------------------------
             """)
        choose = input("Select your roles:")
        if choose == "2":
            name = input("Input the name of your role:")
            cls.player = Master(name)
            print("Succeed in creating the role!")
            cls.home_page()
        elif choose == "1":
            name = input("Input your name:" )
            cls.player = Warrior(name)
            print("Succeed in creating the role!")
            cls.home_page()
        else:
            cls.home_page()

    @classmethod
    def shopping_mall(cls, obj):
        print("""
------------------------------------------------------------
--------------------Welcome to the shop---------------------
-1-: MAGIC
1、Series_1—— level 10(1000)        2、Series_2—— level 20(4000)
3、Series_3—— level 30(8000)        4、Series_4—— level 40(10000)
-2-: PHYSICS
1、Series_5—— level 10(1000)        2、Series_6—— level 20(4000)
3、Series_7—— level 30(8000)        4、Series_8—— level 40(10000)
-3-: REVIVAL
(Note 1: coins needed for level 1 is 1000, and it needs extra 1000 coins for each upgrade)
(eg: for level 10 it needs 10000 coins)
(Note 2: system will tell you the suitable equpiment)
            """)
        print(
            """
-------------------------
    1、Equipment
    2、Revival
    n、Back
-------------------------
           """
        )
        s = Store()
        while True:
            choose = input("Please make a choice:")
            if choose == "1":
                # shop
                s.buy_equipment(obj, obj.level)
                # back to previous level 
                while True:
                    choose = input("press n+Enter to go back to main menu")
                    if choose == "n":
                        cls.home_page()
                    else:
                        print("Wrong input, your input is:", choose)
            elif choose == "2":
                if obj.hp == 0:
                    s.resurrection(obj)
                else:
                    print("Still alive!")
                while True:
                    choose = input("Press n+Enter to go back to main menu")
                    if choose == "n":
                        cls.home_page()
                    else:
                        print("Wrong input, your input is:", choose)
            elif choose == "n":
                cls.home_page()
            else:
                print("Wrong input, your input is:", choose)

    @classmethod

    # charge 
    def recharge(cls): 
        cls.account.login()
        while True:
            cls.account.oprator(cls.player)
            choose = input("Continue charging: 1:continue, 2:back")
            if choose != "1":
                cls.home_page()
                return

    @classmethod
    def equipment(cls, obj):
        while True:
            # bag 
            bag = obj._bag  
            for i in range(len(bag)):
                print(i + 1, bag[i])
            choose = input("Continue or not: 1:Yes ,2:No")
            if choose == "1":
                if obj.get_bag():
                    choose = input("1.Enter fight(make sure you are ready) 2.back to main menu")
                    if choose == "1":
                        cls.battle()
                    else:
                        cls.home_page()
                else:
                    choose = input("1.Enter fight(make sure you are ready) 2.back to main menu")
                    if choose == "1":
                        cls.battle()
                    else:
                        cls.home_page()
            else:
                cls.home_page()
                break

    @classmethod
    def information(cls):
        print(
            """
--------------------------------------
            Player information
--------------------------------------
            """
        )
        print("Hero name:", cls.player.name, "\n", "Level:", cls.player.level, "\n", "HP:", cls.player.hp, "\n",
              "MP:", cls.player.magic, "\n", "Attack:",cls.player.atk, "\n", "Speed:", cls.player.sensitivity, "\n", "Coin:", cls.player.money)
        while True:
            choose = input("Press n+Enter to go back to main menu")
            if choose == "n":
                cls.home_page()
                return
            else:
                pass

    @classmethod
    def battle(cls):
        while True:
            y = Monster()
            y.lev(cls.player.level)
            print("-----------------", cls.player.name, "------------ VS -------------", y._name,
                  "-----------------")
            fight(cls.player, y)
            cls.player.upgrade(cls.player.empirical)
            print("Current level:", cls.player.level)
            print(
                """
----------------------------------
        Continue to fight:
           1. Yes 
           2. No
----------------------------------
                """
            )
            choose = input("Please in put your choice:")
            if choose != "1":
                cls.home_page()
                break
            else:
                pass

    @classmethod
    def exit(cls):
        print(
            """
            Welcome back, Hero!
            """
        )
        sys.exit()
        pass


if __name__ == '__main__':
    ui = UI()
    ui.welcome()