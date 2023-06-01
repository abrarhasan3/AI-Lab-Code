#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 08:50:35 2023

@author: kanizfatema
"""

def getMembershipService(service):
    print("HI")
    
def speed(food):
    
    degree = {}
    
    if food < 0 or food > 30:
        degree["h"] = 0
        degree["l"] = 0
    
    elif food <=10:
        degree["l"] = 1
        degree["h"] = 0
    
    elif food>10 and food<20:
        degree["l"] = float((20-food)*(1/(20-10)))
        degree["h"] = float((food-10)*1.0/(20-10))
      
    elif food >= 20 and food <= 30:
        
        degree["l"] = 0
        degree["h"] = 1
        
    return degree

def rd(food):
    degree = {}    
    if food < 0 or food > 100:
        degree["l"] = 0
        degree["a"] = 0
        degree["h"] = 0
    elif food <=30:
        degree["l"] = 1
        degree["a"] = 0
        degree["h"] = 0
    
    elif food>30 and food<40:
        degree["l"] = float((40-food)*(1/(40-30)))
        degree["a"] = float((food-30)*1.0/(40-30))
        degree["h"] = 0
    elif food >=40 and food <=60:
        degree["l"] = 0
        degree["a"] = 1
        degree["h"] = 0
    elif food>60 and food<70:
        degree["a"] = float((70-food)*(1/(70-60)))
        degree["h"] = float((food-60)*1.0/(70-60))
        degree["l"] = 0
    elif food >= 70 and food <= 100:
        degree["l"] = 0
        degree["a"] = 1
        degree["h"] = 0
        
    return degree


   


def ruleEvalationAssessment(service,food):
    cheap=[],average=[],generous=[]
    
    
    return cheap,average,generous


def defuzzificationAssessment(cheap,average,generous ):
    cog = 0
    #cog formula  
    return cog

#input

relative,sp = 1, 30




r1=rd(relative)
s1=speed(sp)

print(r1,s1)

#rules 
rule1 = max(r1['l'],s1['h'])
rule2 = r1['h']
rule3 = min(r1['a'],s1['h'])
rule4 = min(r1['a'],s1['l'])
rule5 = max(rule2,rule4)

i=10
down=0
COG = 0
while(i<=100):
    if(i<=30):
        COG=COG + i*rule5
        down=down+rule5
    elif(i<=60):
        COG+=i*rule3
        down=down+rule3
    elif(i<=100):
        COG+=i*rule1
        down=down+rule1
    i=i+10
#COG = ((0+10+20)*rule5+(30+40+50+60)*rule3+(70+80+90+100)*rule1)/(rule5*3+rule3*4+rule1*4)
print(COG/down)


#cheap,average,generous = ruleEvalationAssessment(s,f)



#conAssessment = defuzzificationAssessment(cheap,average,generous )
#print("Fuzzified Continuous Assessment: ",conAssessment)