import random
class Sheep():
    def __init__(self):
        self.wool = 0
        self.flock = 5
        self.clock = 0
        self.hunger = 0
        self.nervs = 0
        self.day = True
        self.days = 0
        self.directions = ['north','east','south','west']
        self.baa = False
    def time(self):
        self.clock += 1
        self.hunger += 1
        print('time passed')
        if self.day == True:
            print('it is {0}am'.format(self.clock))
        else:
            print('it is {0}pm'.format(self.clock))
        if self.clock == 12 and self.day == True:
            self.clock = 0
            print('its night time')
            self.day = False
        else:
            if self.clock == 12:
                self.clock = 0
                print('its day time')
                self.day = True
                self.days += 1
                self.wool += 1
    def move(self):
        movement = input("which direction do you want to move?-north,east,south,west ")
        movement.lower()
        if movement in self.directions:
            if self.baa == True:
                follow = random.randint(3,self.flock)
                self.baa = False
            else:
                follow = random.randint(0,self.flock)
            print('you walked {0} with {1} other sheep'.format(movement,follow))
            if follow <= 2:
                print('you are lonly in your position..you get nervous')
                self.nervs += 1
    def eat(self):
        print('you ate grass. how fun')
        self.hunger -= 3
    def baaa(self):
        print('baa')
        self.baa = True
    def shear(self):
        print('you have been sheared: you lost your wool and got more nervous')
        self.wool = 0
        self.nervs += 2
    def main(self):
        if self.hunger >= 3:
            print('you are hungry')
        if self.nervs >= 3:
            print('your position is making you nervous')
        if self.wool >= 4:
            S.shear()
        buy = random.randint(1,12)
        if buy == 3:
            self.flock += random.randint(2,5)
            print('the farmer brought you more friends')
        if self.day == False:
            choise = input('do you want to move,eat,baa or go to barn')
            choise.lower()
            if choise == 'move':
                S.move()
            if choise =='eat':
                S.eat()
            if choise == 'baa':
                S.baaa()
            if choise == 'barn':
                print('you walked inside')
                N.barn()
            N.wolf()
        else:
            choise = input('do you want to move,eat or baa')
            choise.lower()
            if choise == 'move':
                S.move()
            if choise =='eat':
                S.eat()
            if choise == 'baa':
                S.baaa()
            if choise == 'barn':
                print('its locked')
        S.time()
        if self.hunger >= 8 or self.nervs >= 8:
            print('you lived {0} days'.format(S.days))
            raise Exception('ewe died')
class Night():
    def __init__(self):
        self.sheepshifter = False
        self.sheepshifter_sloved = False
    def barn(self):
        while S.day == False:
            choise = input('do you want to move,eat or baa')
            choise.lower()
            if choise == 'move':
                S.move()
            if choise == 'eat':
                S.eat()
                print('the farmer brought it inside')
            if choise == 'baa':
                N.talk()
            S.time()
    def talk(self):
        print('for some reason in here you understand sheep baas')
        if self.sheepshifter == True and self.sheepshifter_sloved == False:
            question = input('what do you want to ask: 1-how was your day? 2-do you know the sheepshifter?')
            if question == '1':
                answer = random.randint(1,3)
                if answer == 1:
                    print('the grass tasted good today')
                if answer == 2:
                    print('i saw a wolf in the woods')
                else:
                    print('this barn tastes good')
            if question == '2':
                answer = random.randint(1, 3)
                if answer == 1:
                    print('huh..whats that')
                if answer == 2:
                    print('they are somewhere. im looking')
                else:
                    print('BaAAaA(this sheep seems odd..you guess this is the sheep shifter')
                    self.sheepshifter_sloved = True
        if self.sheepshifter == True and self.sheepshifter_sloved == True:
            question = input('what do you want to ask: 1-how was your day? 2-i found the sheepshifter?')
            if question == '1':
                answer = random.randint(1,3)
                if answer == 1:
                    print('the grass tasted good today')
                if answer == 2:
                    print('i saw a wolf in the woods')
                else:
                    print('this barn tastes good')
            if question == '2':
                answer = random.randint(1, 3)
                if answer == 1:
                    print('huh..whats that')
                if answer == 2:
                    print('I knew they were here somewhere')
                else:
                    print('you cant have')
        else:
            if self.sheepshifter == False and self.sheepshifter_sloved == False:
                question = input('what do you want to ask: 1-how was your day?')
                if question == '1':
                    answer = random.randint(1, 4)
                    if answer == 1:
                        print('the grass tasted good today')
                    if answer == 2:
                        print('i saw a wolf in the woods')
                    if answer == 3:
                        print('this barn tastes good')
                    else:
                        print('I knew they were here somewhere..the sheepshifter')
                        self.sheepshifter = True
    def wolf(self):
        wolfchance = random.randint(1,4)
        if wolfchance == 2:
            print('you lived {0} days'.format(self.days))
            raise Exception('ewe died as the wolf ate you')
        else:
            print('get inside or the wolf will eat you')


S = Sheep()
N = Night()
while True:
    S.main()