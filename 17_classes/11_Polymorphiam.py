"""
Poly:many
morphism : forms
"""

#1. Duck Typing
#~~~~~~~~~~~~~~~~~~~

class VSCode: # Type 1
    
    def execute(self):
        print("VS Code is running")

class jupter:

    def execute(self):
        print("jupter is running")

class Laptop: # interface class

    def run_tool(self,tool):
        tool.execute()

# Create some instance of the tools
tool_1 = VSCode()
toool_2 = jupter()

# Create the Interface
dell_1 = Laptop()

# Send instance to the interface class instance
dell_1.run_tool(tool_1)
dell_1.run_tool(toool_2)

print()
##############################
#2. Method overriding : Method with the same Name between super class and child class
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class car:
    def parking(self):
        print("Car is parking")

class VW(car):
    def parking(self): # method overrides the super class implementation
        print("VW is parking")

class Audi(car):
    pass

VW_1 = VW()
VW_1.parking() # VW is parking

audi_1 = Audi()
audi_1.parking() # Car is parking
#############################################
#3. Method overloading ---> does not exists in python


print()
################################################
