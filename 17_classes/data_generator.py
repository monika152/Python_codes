from random import randint
class Dice:

    count_instance = 0

    def __init__(self,count_of_sides=12):
        self.count_of_sides= count_of_sides
        Dice.count_instance+=1
        self.cube_id = Dice.count_instance

    def Rolldice(self):
        print(" Roll the dice ....")
        return f" cube_{self.cube_id} value: {randint(1,self.count_of_sides)}"
       
cube_list = []
cube1=Dice()
cube2=Dice()
cube3=Dice()

cube_list.append(cube1)
cube_list.append(cube2)
cube_list.append(cube3)

for cube in cube_list:
    print(cube.Rolldice())

    print(Dice.count_instance)