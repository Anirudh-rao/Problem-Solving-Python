#Stack Implenetaion in Python

#Creating a Stack
def create_stack():
	stack = []
	return stack


#Creating an empty Stack
def check_empty(stack):
	return len(stack) == 0

#Adding items into the Stack
def push(stack, items):
	stack.append(items)
	print("Pushed Item: "+ item)


#Removing an element from the Stack
def pop(stack):
	if(check_empty(stack)):
		return "Stack is empty"

	return stack.pop()


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))