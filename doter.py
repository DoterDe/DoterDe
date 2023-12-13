def bmi_calculator(wheight, height):
    '''коментраии'''
    return wheight / height**2
    
weight= float(input("введите свой вес в кг: "))
height= float(input("введите свой рост в см: "))

bmi= bmi_calculator(weight, height)

if bmi < 18.5:
    print('у вас недовес . Ваш показатель bmi = {bmi}')
elif bmi > 18.5 and bmi > 24.9:
    print('у вас все ок . Ваш показатель bmi = {bmi}')
else:
    print(' у вас перевес . Ваш показатель bmi = {bmi}')
