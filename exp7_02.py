class empolyee:
    def __init__(self):
        self.name=""
        self.id=""
        self.salary=""

    def getempolye(self):
        self.name=input("enter the empolye name")
        self.id=input("enter the empolye id")
        self.salary=input("enter the empolye salary")

    def showempolye(self):
        print("empolyee details...")
        print(f"name:{self.name}")
        print(f"id : {self.id}")
        print(f"salary : {self.salary} ")

    def updatesalary(self):
        self.salary =int (input("enter updated salary:"))
        print("updatedsalary",self.salary)
        
e1= empolyee()
e1.getempolye()
e1.shoeempolye()
e1.updatesalary()


              




        
              
