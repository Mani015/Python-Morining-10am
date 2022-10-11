# Enclosing variable:

def function1():
    # Global variable or Non-Local variable
    x='python'
    def function2():
        y='developer'
        print(x)
        print('concation the global variable + local variable: ',y+x)
    function2()
    print('enclosing variable (or) global variable:',x)
function1()