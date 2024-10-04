class student : 
    def __init__(self,s_number = 0,s_prenom = "Toto",s_gender = "M",s_statutMO = False) :
        self.number = s_number
        self.prenom = s_prenom
        self.gender = s_gender
        self.statutMO = s_statutMO



Students = [
student(1,"Amine","M"),
student(2,"Noé","M"),
student(3,"Lucas","M",True),
student(4,"Adrian","M"),
student(5,"Etienne","M",True),
student(6,"Camille","F"),
student(7,"Arthur","M",True),
student(8,"Emilie","F",True),
student(9,"Antoine C.","M"),
student(10,"Valentine","F"),
student(11,"Thomas","M"),
student(12,"Léane","F"),
student(13,"Côme","M"),
student(14,"Maho","M"),
student(15,"Benoît F.","M",True),
student(16,"Aurélie","F",True),
student(17,"Emma","F"),
student(18,"Arnaud","M",True),
student(19,"Benoit G.","M",True),
student(20,"Albane","F"),
student(21,"Paul","M"),
student(22,"Goulwen","M"),
student(23,"Antoine J.","M",True),
student(24,"Timothée","M",True),
student(25,"Barthélemy","M",True),
student(26,"Maximilien","M",True),
student(27,"Nicolas","M"),
student(28,"Matthias","M",True),
student(29,"Solène","F"),
student(30,"Pia","F"),
student(31,"Baptiste","M",True),
student(32,"François","M"),
student(33,"Moise","M"),
student(34,"Jade","F"),
student(35,"Daniel","M",True),
student(36,"Margaux","F"),
student(37,"Clémence","F",True),
student(38,"Maxence","M"),
student(39,"Maxime","M"),
student(40,"Ghaly","M"),
student(41,"Aubin","M"),
student(42,"Jérémie","M")
]


classMO_Number = 0
classNumberList = []

for e in Students :
    classNumberList.append(e.number)
    if e.statutMO == True :
        classMO_Number += 1

