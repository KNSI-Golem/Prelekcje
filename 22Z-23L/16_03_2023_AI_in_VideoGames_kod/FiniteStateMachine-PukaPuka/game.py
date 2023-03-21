# -*- coding: windows-1250 -*- #

import tkinter as xx
import random as rng

def main():

    window = xx.Tk()
    window.title("Puka Puka the Game")

    box = xx.Canvas(window, width = 600, height = 600)


    box.configure(background='black')
    box.pack()

    class PukaPuka:

        def __init__(self):

            #rozmiar
            self.width = 600
            self.height = 600
            self.size = 10


            #startowe pozycje
            self.xs = 5
            self.ys = 30
            self.xb = 57
            self.yb = 30
            self.xp1 = 1000
            self.yp1 = 1000
            self.xp2 = 1000
            self.yp2 = 1000
            self.xp3 = 1000
            self.yp3 = 1000
            self.xp4 = 1000
            self.yp4 = 1000
            self.xp5 = 1000
            self.yp5 = 1000
            self.xp6 = 1000
            self.yp6 = 1000

            self.statek=[]
            self.boss=[]
            self.pocisk1=[]
            self.pocisk2=[]
            self.pocisk3=[]
            self.pocisk4=[]
            self.pocisk5=[]
            self.pocisk6=[]
            self.laser = []

            #bazowe wartosci
            self.wynik = 0
            self.highscore = 0
            self.collision = False
            self.Pause = False
            self.TimerDelay = 30
            #self.AIMove = 0
            self.MissileNumber = 1
            self.Special = 0
            self.SpecialDelayCount = 0
            self.Paaam = 0
            self.WhereAmIGoing = rng.randint(1,2)
            self.SpecialDelay = 20

            self.kolorSt = 'black'
            self.kolorStO = 'red'
            self.kolorAtt = 'red'
            self.kolorAttO = 'red'

            #especially special config
            self.specialcharge = 0
            self.specialclock = 0
            self.specialclock2 = 0
            self.specialclock3 = 0
            self.specialclock4 = 0
            self.specialclock5 = 0
            self.specialrest = 0
            self.twinkle = 0
            self.specialwalk = 0
            self.specialwalkback = 0
            self.hellcount = 0
            self.loc1 = 0
            self.loc2 = 0
            self.loc3 = 0
            self.loc4 = 0
            self.locnumber = 1
            self.flash =  0

            #bossconfig

            self.MissileSpeed = 1
            self.SpecialDelay *= 5
            self.BaseShootDelay = 20
            self.kolorBoss = 'blue'
            self.kolorBossO = "black"



## generuj

        def BoxSt(self, x, y):
            box.create_rectangle([x , y, x + self.size, y + self.size], fill = self.kolorSt, outline = self.kolorStO)
        def BoxAtt(self, x, y):
            box.create_rectangle([x , y, x + self.size, y + self.size], fill = self.kolorAtt, outline = self.kolorAttO)
        def BoxBoss(self, x, y):
            box.create_rectangle([x , y, x + self.size, y + self.size], fill = self.kolorBoss, outline = self.kolorBossO)
        def BoxLaser(self, x, y, x1, y1):
            box.create_rectangle([x , y, x1, y1], fill = 'yellow', outline = 'yellow')
        def BoxEye(self, x, y):
            box.create_rectangle([x , y, x + self.size, y + self.size], fill = 'yellow', outline = 'black')

        def checkCol(self):
            colValuesS = [[self.xs+3,self.ys],[self.xs+2,self.ys-2],[self.xs+2,self.ys+2],[self.xs+1,self.ys-1],[self.xs+1,self.ys+1]]
            colValuesP = [[self.xp1,self.yp1],[self.xp2,self.yp2],[self.xp3,self.yp3],[self.xp4,self.yp4],[self.xp5,self.yp5],[self.xp6,self.yp6]]

            colValuesSLaser = [[self.ys], [self.ys+1],[self.ys-1],[self.ys+2],[self.ys-2]]
            colValuesBLaser =[[self.yb-4],[self.yb-3]]
            for x in colValuesP:
                if x in colValuesS:
                    self.collision = True

            if self.Special == 2 and self.specialcharge == 40:
                for x in colValuesBLaser:
                    if x in colValuesSLaser:
                        self.collision = True

        def Update(self):
            self.statek = [[self.xs-2,self.ys-2],[self.xs-1,self.ys-2],[self.xs,self.ys-2],[self.xs+1,self.ys-2],[self.xs,self.ys-1],[self.xs-1,self.ys],[self.xs,self.ys],[self.xs+1,self.ys],[self.xs+2,self.ys],[self.xs,self.ys+1],[self.xs-2,self.ys+2],[self.xs-1,self.ys+2],[self.xs,self.ys+2],[self.xs+1,self.ys+2]]
            self.boss = [[self.xb-2,self.yb-5],[self.xb-1,self.yb-5],[self.xb,self.yb-5],[self.xb+1,self.yb-5],[self.xb-2,self.yb-4],[self.xb+1,self.yb-4],[self.xb-3,self.yb-3],[self.xb-2,self.yb-3],[self.xb+1,self.yb-3],[self.xb-4,self.yb-2],[self.xb-3,self.yb-2],[self.xb-2,self.yb-2],[self.xb-1,self.yb-2],[self.xb,self.yb-2],[self.xb+1,self.yb-2],[self.xb-5,self.yb-1],[self.xb-3,self.yb-1],[self.xb-1,self.yb-1],[self.xb,self.yb-1],[self.xb+1,self.yb-1],[self.xb,self.yb],[self.xb+1,self.yb],[self.xb-5,self.yb+1],[self.xb-3,self.yb+1],[self.xb--1,self.yb+1],[self.xb,self.yb+1],[self.xb-1,self.yb+1],[self.xb-4,self.yb+2],[self.xb-3,self.yb+2],[self.xb-2,self.yb+2],[self.xb-1,self.yb+2],[self.xb,self.yb+2],[self.xb-3,self.yb+3],[self.xb-2,self.yb+3],[self.xb-1,self.yb+3]]
            self.pocisk1 = [[self.xp1,self.yp1],[self.xp1+1,self.yp1],[self.xp1+2,self.yp1]]
            self.pocisk2 = [[self.xp2,self.yp2],[self.xp2+1,self.yp2],[self.xp2+2,self.yp2]]
            self.pocisk3 = [[self.xp3,self.yp3],[self.xp3+1,self.yp3],[self.xp3+2,self.yp3]]
            self.pocisk4 = [[self.xp4,self.yp4],[self.xp4+1,self.yp4],[self.xp4+2,self.yp4]]
            self.pocisk5 = [[self.xp5,self.yp5],[self.xp5+1,self.yp5],[self.xp5+2,self.yp5]]
            self.pocisk6 = [[self.xp6,self.yp6],[self.xp6+1,self.yp6],[self.xp6+2,self.yp6]]
            self.laser = [[self.xb+1,self.yb-4, self.xs-20,self.yb-2]]
            self.eye = [[self.xb-1,self.yb-4],[self.xb,self.yb-4],[self.xb-1,self.yb-3],[self.xb,self.yb-3]]

        def create(self):
            for x in self.statek:
                self.BoxSt(x[0] * self.size, x[1] * self.size)
            for x in self.boss:
                self.BoxBoss(x[0] * self.size, x[1] * self.size)
            for x in self.pocisk1:
                self.BoxAtt(x[0]*self.size, x[1]*self.size)
            for x in self.pocisk2:
                self.BoxAtt(x[0]*self.size, x[1]*self.size)
            for x in self.pocisk3:
                self.BoxAtt(x[0]*self.size, x[1]*self.size)
            for x in self.pocisk4:
                self.BoxAtt(x[0]*self.size, x[1]*self.size)
            for x in self.pocisk5:
                self.BoxAtt(x[0]*self.size, x[1]*self.size)
            for x in self.pocisk6:
                self.BoxAtt(x[0]*self.size, x[1]*self.size)

            #do speciala 2
            if self.Special == 2:
                if self.specialcharge == 40:
                    for x in self.laser:
                        self.BoxLaser(x[0]*self.size, x[1]*self.size, x[2]*self.size, x[3]*self.size)
                else:
                    if self.twinkle == 0:
                        self.twinkle+=1
                    else:
                        for x in self.eye:
                            self.BoxEye(x[0]*self.size, x[1]*self.size)
                        self.twinkle = 0

        def MoveMissiles(self):
            self.xp1-=1
            self.xp2-=1
            self.xp3-=1
            self.xp4-=1
            self.xp5-=1
            self.xp6-=1

        def MeStupidTellMeWhatToShoot(self):
                    if self.MissileNumber == 1:
                        self.yp1=self.yb
                        self.xp1=self.xb-5
                        self.MissileNumber+=1
                    elif self.MissileNumber == 2:
                        self.yp2=self.yb
                        self.xp2=self.xb-5
                        self.MissileNumber+=1
                    elif self.MissileNumber == 3:
                        self.yp3=self.yb
                        self.xp3=self.xb-5
                        self.MissileNumber+=1
                    elif self.MissileNumber == 4:
                        self.yp4=self.yb
                        self.xp4=self.xb-5
                        self.MissileNumber+=1
                    elif self.MissileNumber == 5:
                        self.yp5=self.yb
                        self.xp5=self.xb-5
                        self.MissileNumber+=1
                    else:
                        self.yp6=self.yb
                        self.xp6=self.xb-5
                        self.MissileNumber=1

        def draw(self):
            box.delete("all")
            self.wynik+=1

            if self.Pause == True:
                self.create()
                box.create_text([self.width/2, self.height/2], text = "Pauza", font=("Arial",40,"italic"), fill = 'white' )
                box.create_text([self.width/2, self.height/2+self.size*4], text = "Wcisnij Esc, aby kontynuowac", font=("Arial",20,"italic"), fill = 'orange' )

            elif self.collision == True:
                self.create()
                if self.wynik > self.highscore:
                    self.highscore = self.wynik
                    box.create_text([self.width/2, self.height/2-self.size*8], text = "Nowy najwyzszy wynik!", font=("Arial",20,"italic"), fill = 'yellow' )
                box.create_text([self.width/2, self.height/2-self.size*5], text = "Przegrales! Wynik:", font=("Arial",30,"italic"), fill = 'white' )
                box.create_text([self.width/2, self.height/2], text = self.wynik, font=("Arial",50,"italic"), fill = 'red' )

            else:
                self.create()
## boss
        def SpecialReset(self):
            self.Special = 0
            self.specialcharge = 0
            self.specialclock = 0
            self.specialclock2 = 0
            self.specialclock3 = 0
            self.specialclock4 = 0
            self.specialclock5 = 0
            self.SpecialDelayCount = 0
            self.specialrest = 0
            self.specialwalk = 0
            self.specialwalkback = 0
            self.loc1 = 0
            self.loc2 = 0
            self.loc3 = 0
            self.loc4 = 0
            self.locnumber = 1
            self.flash = 0

        def AI(self):

            #czy special
            if self.SpecialDelayCount == self.SpecialDelay:
                    if self.hellcount != 5:
                        self.Special = rng.randint(1,2)
                        self.SpecialDelayCount=0
                    else:
                        self.Special = 3

            #zwykly ruch
            if self.Special == 0:
                self.kolorBoss = 'blue'
                self.kolorBossO = 'black'
                self.SpecialDelayCount += 1

                if self.WhereAmIGoing == 1:
                    self.yb-=1
                    self.Update()
                    if self.yb <8:
                        self.WhereAmIGoing = 0
                else:
                    self.yb+=1
                    self.Update()
                    if self.yb>53:
                        self.WhereAmIGoing = 1

                if self.Paaam == self.BaseShootDelay:
                    self.kolorBoss = 'orange'
                    self.kolorBossO = 'orange'
                    self.MeStupidTellMeWhatToShoot()
                    self.Paaam = rng.randint(0,self.BaseShootDelay-5)
                else:
                    self.Paaam+=1


            ## pierwszy special
            if self.Special == 1:

                #laduj
                if self.specialcharge != 20:
                    self.kolorBossO = 'white'
                    self.kolorBoss = 'white'
                    self.specialcharge+=1

                #strzelaj
                else:
                    if self.specialclock != 4:
                        if self.specialclock2 == 0:
                            if self.loc1 == 0:
                                self.loc1 = rng.randint(self.ys-5,self.ys+5)
                                self.loc2 = 60 - self.loc1
                                if self.loc1>45 or self.loc1<15:
                                    self.loc3 = rng.randint(15,45)
                                    self.loc4 = 60 - self.loc3
                                else:
                                    self.loc3 = rng.randint(45,56)
                                    self.loc4 = 60 - self.loc3
                            if self.locnumber == 1:
                                self.yb = self.loc1
                                self.locnumber+=1
                            elif self.locnumber == 2:
                                self.yb = self.loc2
                                self.locnumber+=1
                            elif self.locnumber == 3:
                                self.yb = self.loc3
                                self.locnumber+=1
                            else:
                                self.yb = self.loc4
                                self.locnumber = 1
                            self.Update()
                            self.MeStupidTellMeWhatToShoot()
                            self.specialclock2 = 3
                            self.specialclock += 1
                        else:
                            self.specialclock2-=1
                #odpocznij
                    if self.specialclock == 4:
                        if self.specialrest != 20:
                            self.specialrest+=1
                        else:
                            self.SpecialReset()
                            self.hellcount +=1

            ##drugi special
            if self.Special == 2:
                self.kolorBoss = 'blue'
                self.kolorBossO = 'black'

                #mrugaj
                if self.specialcharge != 40:
                    self.specialcharge+=1
                else:
                    #gdzie isc
                    if self.specialclock != 1:
                        if self.specialwalk == 0:
                            if self.yb<30:
                                self.specialwalk = 2
                            else:
                                self.specialwalk = 1
                        #zap do konca planszy
                        else:
                            if self.specialwalk == 1:
                                if self.yb<17:
                                    self.specialclock = 1
                                else:
                                    self.yb-=1
                                    self.Update()
                            if self.specialwalk == 2:
                                if self.yb>49:
                                    self.specialclock = 1
                                else:
                                    self.yb+=1
                                    self.Update()
                    else:
                        self.SpecialReset()
                        self.hellcount +=1

            if self.Special == 3:
                self.kolorBoss = 'red'
                self.kolorBossO = 'red'

                #gdzie idzie
                if self.specialcharge != 1:
                    if self.yb<30:
                        self.specialwalk = 0
                    else:
                        self.specialwalk = 1
                    self.specialcharge = 1

                #idz na srodek
                else:
                    if self.specialclock2 != 1:
                        if self.specialwalk == 0:
                            self.yb+=1
                        else:
                            self.yb-=1
                        self.Update()
                        if self.yb == 30:
                                self.specialclock2 = 1
                    else:
                        if self.specialclock != 48:
                            if self.specialclock == 16:
                                self.kolorStO = 'white'
                            if self.specialclock == 32:
                                self.kolorSt = 'white'
                            self.specialclock+=1

                        #podejdz
                        else:
                            if self.specialclock3 != 1:
                                if self.flash != 1:
                                    box.configure(background='white')
                                    self.flash+=1
                                else:
                                    box.configure(background='black')
                                self.xs = 20
                                self.ys = 30
                                self.xb-=1
                                self.Update()
                                if self.xb-self.xs < 25:
                                    self.specialclock3 = 1
                            #uwal
                            else:
                                if self.specialclock4 != 400:
                                    self.xs = 20
                                    if self.specialclock5 == 20:
                                        self.yb = rng.randint(self.ys-2, self.ys+2)
                                        self.xb = self.xs+24
                                        self.MeStupidTellMeWhatToShoot()
                                        self.Update()
                                        self.specialclock5 = 0
                                    else:
                                        self.specialclock5 +=1
                                    self.specialclock4+=1

                                #zmyj sie
                                else:
                                    if self.specialwalkback != 1:
                                        self.kolorSt = 'black'
                                        self.kolorStO = 'red'
                                        self.xb+=1
                                        if self.xb == 57:
                                            self.specialwalkback = 1
                                    else:
                                        self.kolorBoss = 'blue'
                                        self.kolorBossO = 'black'
                                        self.hellcount = 0
                                        self.SpecialReset()



## ruchy

        def UpS(self):
            if self.ys-2 != 7:
                for x in range(len(self.statek)):
                    new = self.statek[x]
                    new[1] = new[1]-1
                self.ys-=1

        def DownS(self):
            if self.ys+2 != 52:
                for x in range(len(self.statek)):
                    new = self.statek[x]
                    new[1] = new[1]+1
                self.ys+=1

        def ForwardS(self):
            if self.xs+2 != 20:
                for x in range(len(self.statek)):
                    new = self.statek[x]
                    new[0] = new[0]+1
                self.xs+=1

        def BackwardS(self):
            if self.xs-2 != 2:
                for x in range(len(self.statek)):
                    new = self.statek[x]
                    new[0] = new[0]-1
                self.xs-=1

## core
        def move_game(self):
            self.AI()
            self.checkCol()
            self.MoveMissiles()
            self.Update()
            self.draw()

## restart

        def Restart(self):
            self.xs = 5
            self.ys = 30
            self.xp1 = 1000
            self.yp1 = 1000
            self.xp2 = 1000
            self.yp2 = 1000
            self.xp3 = 1000
            self.yp3 = 1000
            self.xp4 = 1000
            self.yp4 = 1000
            self.xp5 = 1000
            self.yp5 = 1000
            self.xp6 = 1000
            self.yp6 = 1000
            self.xb = 57
            self.yb = 30
            self.statek=[]
            self.boss=[]
            self.pocisk1=[]
            self.pocisk2=[]
            self.pocisk3=[]
            self.pocisk4=[]
            self.wynik = 0
            self.AIMove = 0
            self.collision = False
            self.MoveDelay = 30
            self.MissileSpeed = 1
            self.MissileNumber = 1
            self.kolorBoss = 'blue'
            self.kolorBossO = "black"
            self.kolorSt = 'black'
            self.kolorStO = 'red'
            self.kolorAtt = 'red'
            self.kolorAttO = 'red'
            self.move_game()
            self.SpecialReset()
            self.hellcount = 0

############################################
    PP = PukaPuka()

    def fail(event):
        PP.collision = True

    def refresh():
        PP.move_game()
        if PP.collision == False and PP.Pause == False:
            window.after(PP.TimerDelay, refresh)

    def reset(event):
        if PP.collision == True:
            PP.Pause = False
            PP.Restart()
            refresh()

    def pause(event):
        if PP.collision == False:
            if PP.Pause == False:
                PP.Pause = True
            else:
                PP.Pause = False
                window.after(PP.TimerDelay, refresh)

    def GoUp(event):
        PP.UpS()
    def GoDown(event):
        PP.DownS()
    def GoFwd(event):
        PP.ForwardS()
    def GoBck(event):
        PP.BackwardS()


    window.after(PP.TimerDelay, refresh)

    # STEROWANIE
    # ruch - strzalki, restart - tab, pauza- esc
    window.bind_all("<KeyPress-Tab>", reset)
    window.bind_all("<KeyPress-Escape>", pause)
    window.bind_all("<KeyPress-`>", fail)
    window.bind_all("<KeyPress-Up>", GoUp)
    window.bind_all("<KeyPress-Down>", GoDown)
    window.bind_all("<KeyPress-Right>", GoFwd)
    window.bind_all("<KeyPress-Left>", GoBck)

    window.mainloop()

main()