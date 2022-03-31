def add_new_students(lastname, firstname):
    f = open("students.txt", encoding="utf8")
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    f.close()
    lines.append( lastname+ " " + firstname)
    lines.sort()
    f = open("students.txt","w", encoding="utf8")
    for line in lines:
        f.write(line + "\n")
        
def find_student(lastname, firstname=""):
    f = open("students.txt", encoding="utf8")
    if firstname:
        for line in f:
            if lastname + " " + firstname in line.strip():
                print(line.strip())
                break
    else:
        for line in f:
            if lastname in line.strip():
                print(line.strip())

def edit_student(lastname, firstname, new_lastname="", new_firstname=""):
    f = open("students.txt", encoding="utf8")
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    try:
        student_index = lines.index(lastname + " " + firstname)
        if not new_firstname:
            new_firstname = firstname
        if not new_lastname:
            new_lastname = lastname
        lines[student_index] = new_lastname + " " + new_firstname
        
        f = open("students.txt","w", encoding="utf8")
        for line in lines:
            f.write(line + "\n")
    except:
        print("студент не найден")


def remove_student_by_full_name(lastname, firstname):
    f = open("students.txt", encoding="utf8")
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    try:
        student_index = lines.index(lastname + " " + firstname)
        lines.pop(student_index)
        f = open("students.txt", "w", encoding="utf8")
        for line in lines:
            f.write(line + "\n")
    except:
        print("студент не найден")

def remove_student(lastname, firstname = ""):
    if not firstname:
        find_student(lastname)
        firstname = input("Введите имя студента ")
    remove_student_by_full_name(lastname, firstname)