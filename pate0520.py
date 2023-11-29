#Assignment4
# Jahnvi Patel
def get_bmi_category(bmi):
    if bmi <= 18.4:
        return "underweight"
    elif bmi <= 24.9:
        return "healthy"
    elif bmi <= 29.9:
        return "overweight"
    elif bmi <= 34.9:
        return "severely overweight"
    elif bmi <= 39.9:
        return "obese"
    else:
        return "severely obese"

def provide_advice(bmi_category):
    if bmi_category == "underweight":
        return "Eat plenty of protein and consider building muscle through strength training."
    elif bmi_category == "healthy":
        return "Maintain a balanced diet and regular physical activity."
    elif bmi_category == "overweight":
        return "Focus on a balanced diet and regular exercise to achieve a healthy weight."
    elif bmi_category == "severely overweight":
        return "Consult with a healthcare professional for personalized advice."
    elif bmi_category == "obese":
        return "Seek guidance from a healthcare professional for a comprehensive weight management plan."
    else:
        return "Consult with a healthcare professional for personalized advice."


def main():
    print ('Welcome to the BMI Calculator')
    Height = float(input("Enter your height in CM:"))
    Weight = float(input("Enter you weight in KG:"))
    bmi = Weight / (Height/100) ** 2
    bmi_category = get_bmi_category(bmi)
    advice = provide_advice(bmi_category)
    print(f"Your BMI is: {bmi}")
    print(f"You are in the {bmi_category} category.")
    print(advice)

if __name__ == "__main__":
    main()