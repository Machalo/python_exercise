#!/usr/bin/python

import sys
import random

while True:
    try:
        number = int(input("How many dwarf do you want (between 1 and 10)"))
        break
    except:
        print("That's not a valid option")


if number < 1 or number > 10 :
    sys.exit("Give a number between 1 and 10 please.")
else :

    class character:
        def __init__(self,gender,surname,name,job,age,lvl,intel,stren,agi,pv,pm):
            self.gender = gender
            self.surname = surname
            self.name = name
            self.job = job
            self.lvl = lvl
            self.intel = intel
            self.stren = stren
            self.agi = agi
            self.pv = pv
            self.pm = pm
        def __str__(self):
            return f"\n{self.surname} {self.name}, {self.gender} {self.job}\nLevel\t{self.lvl}\nIntel\t{self.intel}\nStren\t{self.stren}\nAgi\t{self.agi}\nPV\t{self.pv}\nPM\t{self.pm}"

    surnameList = ["Frostfall","Hammercloak","Goldenstone","Oakenshield","Bloodrock",
                   "Ambershaper","Magmabrew","Blessedfoot","Granitebasher","Copperhood"]
    fNameList = ["Lofrurika","Vondroula","Hukhisli","Hubolda","Honwiserd","Thurbirgit",
                 "Azeda","Lonotryd","Mastigit","Lokhuna"]
    mNameList = ["Valen","Yumol","Brandrur","Dedrak","Botdrok","Hakunli","Sirdur","Kissem",
                 "Dhormeth","Nonur"]
    genderList = ["Male","Female"]
    jobList = [["Warrior",6,1,3],["Priest",2,6,2],["Paladin",5,3,2],["Rogue",2,2,6],["Hunter",3,2,5]]


    for i in range(number) :

        p1 =  character(0,0,0,0,0,0,0,0,0,0,0)

        p1.gender = random.choice(genderList)
        p1.surname = random.choice(surnameList)

        if p1.gender == "Male":
            p1.name = random.choice(mNameList)
        else :
            p1.name = random.choice(fNameList)

        p1.lvl = random.randrange(1,10)
        
        job = random.choice(jobList)
        p1.job = job[0]

        p1.stren = p1.lvl * job[1]
        p1.intel = p1.lvl * job[2]
        p1.agi = p1.lvl * job[3]

        p1.pv = p1.lvl * 10 + p1.stren * 2
        p1.pm = p1.lvl *5 + p1.intel * 2


        print(p1)