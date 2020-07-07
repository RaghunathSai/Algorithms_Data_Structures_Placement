class Stack:
    def __init__(self,stack):
        self.stack = stack

    def push(self,data):
        stack.append(data)

    def pop(self):
        value = stack[len(stack)-1]
        print(value)
        stack.remove(value)
        print("Pop value = ",value)

    def peep(self):
        value = stack[len(stack)-1]
        print("Peep value is",value)

    def view_stack(self):
        for i in range(len(stack)):
            print(stack[len(stack)-i-1])

if __name__ == '__main__':
    stack = list()
    s = Stack(stack)
    choice = 1
    while(choice != 0):
        choice = int(input("1.To push data 2.Pop data 3.Peep data 0.To Exit : "))
        if (choice == 1):
            data = input("Enter stack value")
            s.push(data)
        elif (choice == 2):
            s.pop()
        elif (choice == 3):
            s.peep()

    s.view_stack()    
    print("Exited")

