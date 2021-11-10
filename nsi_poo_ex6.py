# -*- coding: utf-8 -*-

# -- Sheet --

from random import*
class Personnage(object):
    def __init__(self):
        self.pdv=randint(10,20)
        self.pdf=randint(10,20)
        self.pde=randint(10,20)

    def __str__(self):
        return "Point de vie : "+str(self.pdv)+" - Force du personnage : "+str(self.pdf)+" - Endurance du personnage : "+str(self.pde)

    def est_vivant(self):
        if self.pdv>0:
            return True
        else:
            return False
    
    def aborde(self,p2):
        damage=0
        if self.est_vivant() and p2.est_vivant() > 0:
            damage=self.pdf-p2.pde
            print(damage)
            if damage<0:
                damage=0
            p2.pdv-=damage

class Magicien(Personnage):
    def __init__(self):
        Personnage.__init__(self)
        self.pda=randint(15,25)
    
    def __str__(self):
        return "Point de vie : "+str(self.pdv)+" - Force du personnage : "+str(self.pdf)+" - Endurance du personnage : "+str(self.pde)+" - Point d'action : "+str(self.pda)
    def sort_attaque(self):
        if self.est_vivant() and self.pda>5:
            self.pdf+=5
            self.pda-=5

    def sort_soin(self):
        if self.est_vivant() and self.pda>5:
            self.pdv+=5
            self.pda-=5

p=Personnage()
m1=Magicien()
m2=Magicien()
print(p)
print(m1)
p.aborde(m1)
print(m1)
m1.sort_soin()
print(m1)
print("------------------------------")
print(m1)
print(m2)
m1.sort_attaque()
print(m1)
m1.aborde(m2)
print(m1)
print(m2)


