class empolyee:
      def __init__(self):
        self.name=""
        self.id=""
        self.salary=""

     def getempolye(self):
        self.name =input("enter empolye name: ")
        self.id =input("enter empolye id: ")    
        self.salary =input("enter empolye salary:")

    def shoeempolye(self):
        print("enpolyee deatils...")
        print(f"NAME: { self.name}")
        print(F"id: {self.id}")
        print(f"salary;{self.salary}")

    def updatesalary(self):
        self.salary =int (input("enter updated salary:"))
        print("updatedsalary",self.salary)
        
e1= empolyee()
e1.getempolye()
e1.shoeempolye()
e1.updatesalary()


              

