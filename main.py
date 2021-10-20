#My Personal Python calculator
print("My Personal Python calculator")
#inputs
num1 = int(input('Enter the first number:  '))
num2 = int(input('Enter the second number:  '))
#opration req
opr = input('Enter the type of operation you want to perform between your chosen two numbers:  ')
#calculation
if opr=='+':
    ans = num1 + num2
    # displaying the answer
    print(f'Your final answer is {ans}')
elif opr == '- ':
    ans = num1 - num2
    # displaying the answer
    print(f'Your final answer is {ans}')
elif opr=='*':
    ans = num1 * num2;
    # displaying the answer
    print(f'Your final answer is {ans}')
elif opr=='/':
    ans = num1 / num2
    # displaying the answer
    print(f'Your final answer is {ans}')
else:
    print('Invalid Entry!!!')