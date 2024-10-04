import main
import json


cpt = 0
Pistons = {}
Pistons["Eleves"] = []
while cpt < 42 :
    Pistons["Eleves"].append(main.Students[main.table[cpt]-1].prenom) 
    cpt+=1


    
with open("data/pistonOrdre.json ","w") as file: 

    file.write(json.dumps(Pistons,indent=4))
