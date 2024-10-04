from random import *


def studentsLayoutInClassroom(table,numberList) :
    cpt = 0
    while cpt < len(table)-2 : 
        x = randint(0,41)

        if x == 41 :
            while((( table[cpt+1].gender == table[x].gender ) or (table[cpt].gender == table[x-1].gender)) and (table[cpt].gender == "F")) :
                if (x==cpt) :
                    x = randint(0,41)
                else :
                    x = randint(0,41)
        else :
            while((( table[cpt+1].gender == table[x].gender ) or (table[cpt].gender == table[x+1].gender)) and (table[cpt].gender == "F")) :
                if (x==cpt) :
                    x = randint(0,41)
                else :
                    x = randint(0,41)
   
        temp = numberList[cpt]
        numberList[cpt] = numberList[x]
        numberList[x] = temp
        cpt+=1
        

def placeofMoses(index,indexM, table) : 
    if(index%2 == 0) :
        temp = table[index+1]
        table[index+1] = table[indexM]
        table[indexM] = temp
    else:
        temp = table[index-1]
        table[index-1] = table[indexM]
        table[indexM] = temp
    
def placeofB(ind1,ind2,indAdmin,table) : 
    a = 0
    if(not(ind1 >= 0 and ind1 < 14)) :
        a = randint(2,13)
        while (a == indAdmin) :
            a = randint(2,13)
        temp = table[ind1]
        table[ind1] = table[a]
        table[a] = temp

    if(not(ind2 >= 0 and ind2 < 14)) :
        y = randint(2,13)
        while (y == indAdmin or y == a):
            y = randint(2,13)
        temp = table[ind2]
        table[ind2] = table[y]
        table[y] = temp