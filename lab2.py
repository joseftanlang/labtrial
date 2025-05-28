"""print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def funcName(parameter1, parameter2): 
    print("this is a dummy function")
    return 10 """
   
"""def calculate_bmi(height, weight): 
    print("Height = " + str(height)) 
    print("Weight = " + str(weight)) 
    calculate_bmi(weight=57, height=1.73)
    bmi = weight / (height ** 2)
    print("BMI = " + str(bmi))"""
    
def calculate_bmi(height, weight): 
    print("Height = " + str(height)) 
    print("Weight = " + str(weight)) 
    #Add code here to calculate BMI 
    bmi = weight / (height ** 2)
    #Add code here to display calculate BMI 
    print("you BMI = " + str(bmi))
    if bmi < 18.5:
        print("underweight")
    elif bmi >= 18.5 and bmi < 24.9:
        print("normal weight")
    else:
        print("overweight")
calculate_bmi(weight=57, height=1.73)   


    