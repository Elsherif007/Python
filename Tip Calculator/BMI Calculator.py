
height = float(input("please enter your height: \n"))

weight = int(input("please enter your weight: \n"))



BMI = weight / (height ** 2)
int_BMI = int(BMI)
#f-strings
print (f"your BMI is {int_BMI} " )