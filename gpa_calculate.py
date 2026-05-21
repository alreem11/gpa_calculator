grades = {
    "A": 4.0 , "A-": 3.67,
    "B+": 3.33 , "B": 3.00 , "B-": 2.67,
    "C+": 2.33 , "C": 2.00 , "C-": 1.67,
    "D+": 1.33 , "D": 1.00 ,
    "F": 0.00
    }

def calculate_gpa(courses):
    total_grades = 0.0
    total_credits = 0.0

    for grade, credit in courses:
        total_grades += grades[grade] * credit
        total_credits += credit
        
    gpa = total_grades / total_credits


    if gpa >= 3.5:
        msg = "Excellent work!"
    elif gpa >= 3.0:
        msg = "Very good! "
    elif gpa >= 2.0:
        msg = "good, keep going! "
    else:
        msg = "work harder (: "
    return gpa, msg
