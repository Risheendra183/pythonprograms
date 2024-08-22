student_data={
    {
        "name":"ram",
        "roll no":10,
        "age":20,
        "course":"python"
    },
    {
        "name":"rishi",
        "rollno":"20",
        "age":33,
        "course":"pyth",
    }
    }
def add_student(name,rollno,age,course):
    newstudent_data={}
    newstudent_data["name"]=name
    newstudent_data["rollno"]=rollno
    newstudent_data["age"]=20
    newstudent_data["coursre"]=course
    student_data.append(newstudent) # type: ignore
    
add_student("shyam",33,14,"c++")
print(student_data)
