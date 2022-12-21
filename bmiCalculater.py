weight = input('Enter weight : ')
height = input('Enter height : ')

bmi = float(weight)/pow(float(height), 2)

if bmi < 18.5:
    print('Underweight')
elif bmi < 25:
    print('Normal')
elif bmi < 30:
    print('Overweight')
else:
    print('Obesity')