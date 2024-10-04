
def displaySerpentin(bigTable,table):
    
    i = 0
    
    print("\n\n")
    print("\t+   **************       + +--------------------------------+ +    ******************     +")
    print("\t+   ***        ***       + |                                | +    ******************     +")
    print("\t+   ***        ***       + |      BUREAU DU PROFESSEUR      | +                 *****     +")
    print("\t+   **************       + |                                | +           ***********     +")
    print("\t+   ***                  + +--------------------------------+ +           ***********     +")
    print("\t+   ***                                                                         *****     +")
    print("\t+   ***                                                             *****************     +")
    print("\t+   ***                                                             *****************     +")
    print("\t+--------------------+ +--------------------+ +--------------------+ +--------------------+")
    while i < len(table)-7 : 
        bench1 = "\t| " + str(bigTable[table[i]-1].prenom).center(18," ") +" | | " +  str(bigTable[table[i+2]-1].prenom).center(18," ") +" | | " +str(bigTable[table[i+4]-1].prenom).center(18," ")+" | | " +str(bigTable[table[i+6]-1].prenom).center(18," ")+" |"
        bench2 = "\t| " + str(bigTable[table[i+1]-1].prenom).center(18," ") +" | | " +  str(bigTable[table[i+3]-1].prenom).center(18," ") +" | | " +str(bigTable[table[i+5]-1].prenom).center(18," ")+" | | " +str(bigTable[table[i+7]-1].prenom).center(18," ")+" |"

        print(bench1)
        print(bench2)
        i += 8
        print("\t+--------------------+ +--------------------+ +--------------------+ +--------------------+")

    print(f"\t|                    | |                    | |"+str(bigTable[table[40]-1].prenom).center(20," ")+"| |                    |")
    print(f"\t|                    | |                    | |"+str(bigTable[table[41]-1].prenom).center(20," ")+"| |                    |")

    print("\t+--------------------+ +--------------------+ +--------------------+ +--------------------+")