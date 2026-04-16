# initiate a class
class employee:
    #special method, dunder method- constructor
    def __init__(self):
        print('constructor started')
        self.id = 123
        self.salary = 50000
        self.designamtion ='SDE'
        print('constructor started')
    
    def travel(self, destination):
        print('travel method called manually')
        print("Employee is now travelling to", destination)

#creating an object/instance for class
sam = employee()

print(sam.salary)
sam.travel('odisha')