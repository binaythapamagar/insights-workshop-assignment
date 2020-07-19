class Calculator:
    
    def add(self,a,b):
        print(f'ther result of addition is {a+b}')
    def subtract(self,a,b):
        print(f'ther result of subtraction is {a-b}')
    def multiply(self,a,b):
        print(f'ther result of multiply is {a*b}')
    def divide(self,a,b):
        if b == 0:
            print(f'Division by 0 is not possible')
            return
        print(f'ther result of division is {a/b}')
        
if __name__ == "__main__":
    calculator = Calculator()
    operand1 = int(input('Enter first number: '))
    operand2 = int(input('Enter second number: '))
    opernad = input('Enter the operation to be performed :')

    if opernad == '+':
        calculator.add(operand1,operand2)
    elif opernad == '-':
        calculator.subtract(operand1,operand2)
    elif opernad == '*':
        calculator.multiply(operand1,operand2)
    else:
        calculator.divide(operand1,operand2)
            