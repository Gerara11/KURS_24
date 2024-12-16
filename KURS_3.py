import time
import random
class Fighter:
    def __init__(self,name: str, health: float,damage:list[float,float],attack_speed:list[float,float]):
        self.__name = name
        self.__hp = health
        self.__dmg = damage
        self.__as = attack_speed
    def get_as(self):
        return random.uniform(self.__as[0],self.__as[1])
    def get_dmg(self):
        return random.uniform(self.__dmg[0], self.__dmg[1])
    def get_hp(self):
        return self.__hp
    def get_name(self):
        return self.__name
    def __sub__(self,other):
        d=other.get_dmg()
        h=self.get_hp()
        if h>=d:
            return h-d
        else:
            return 0
    def set_hp(self,hp_new):
        self.__hp = hp_new

def Write(n:str, d:float, h1:float, h2: float, t:float):
    with open("logger.txt", 'a') as f:
        f.write(n)
        f.write(' ')

        d_s = str(d)
        f.write(d_s)
        f.write(' ')

        h1_s = str(h1)
        f.write(h1_s)
        f.write(' ')

        h2_s = str(h2)
        f.write(h2_s)
        f.write(' ')

        t_s = str(t)
        f.write(t_s)
        f.write('\n')

def BOJ(B1: Fighter,B2: Fighter):
    t=time.time()
    c=0
    n=1
    while c==0 :
        hp1 = B1.get_hp()
        hp2 = B2.get_hp()
        t1=time.time()
        dt = t1 - t
        if B1.get_as() >= B2.get_as() :
            B2.set_hp(B2 - B1)
            Write(B1.get_name(), hp2-B2.get_hp(), B1.get_hp(), B2.get_hp(), dt)
            if (B2.get_hp() == 0):
                c = 1
                with open("logger.txt", 'a') as f:
                    f.write(B1.get_name())
                    f.write(" - POBEDITEL")
                break
        else:
            B1.set_hp(B1 - B2)
            Write(B2.get_name(), hp1 - B1.get_hp(),B1.get_hp(), B2.get_hp(), dt)
            if (B1.get_hp() == 0):
                c = 1
                with open("logger.txt", 'a') as f:
                    f.write(B2.get_name())
                    f.write(" - POBEDITEL")
                break

H = Fighter("Fighter", 100,[0,25],[1,10])
S = Fighter("Bojets", 100,[0,15],[5,10])
BOJ(H,S)
