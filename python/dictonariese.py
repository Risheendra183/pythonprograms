student_marks={
    "jenny":99,
    "rishi":88,
    "goud":97,
    "firox":55,
    "jay":33
    }
student_grades={}
for student in student_marks:
    marks=student_marks[student]
    if marks>90:
        student_grades[student]="A+"
        
    elif  marks>80:
        student_grades[student]="A+"
    
    elif  marks>70:
        student_grades[student]="A"
    
    elif  marks>60:
        student_grades[student]="b+"
            
    elif  marks>50:
        student_grades[student]="b"
    else:
        student_grades[student]="b"
print(student_grades)
#nested dict   

student_data={
    "ram":{"rollno":10,"age":20,"course":"python"},
     "mohan":{"rollno":20,"age":80,"course":"java"},
     "ram":{"rollno":30,"age":90,"course":"c++"},
    }
print(student_data["mohan"])
print(student_data["mohan"]["rollno"])
student_data["mohan"]["phone no."]=8948878
print(student_data["mohan"])
del student_data["mohan"]["phone no."]
print(student_data["mohan"])
#nest a list in dict
travel_data={
"gujarat":["dwarakadhish",
           "somanath","statue of unity"],
"rajasthan":["jaipur","udaypur"]
    }
print(travel_data["gujarat"])
