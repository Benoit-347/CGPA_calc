#welcome to Benoit's CGPA calc
#enter values by:
# each row signifies a subject
# each coulumn has attributes: 0. subject name 1. lab marks scaled to 300 out of 12 marks 2. Internals mark lost in total (150) 3. Credit weightage of the subject in question

def read_marks():
    import csv
    global dict1
    dict1 = {}
    with open("Marks1.csv", 'r') as file1:
        a = csv.reader(file1) #reading through the reader fn gives us the data formated according to all the corner cases
        for i in a:
            dict1[i[0]] = {"Lab": float(i[1]), "IA": float(i[2]), "credits": float(i[3])}


#convert the raw data to value points scaled to 10 each subject
def calc_cgpa_dict():
    global calc_dict, n
    calc_dict = {}
    n = 0
    for Dict in dict1:
        a = round((dict1[Dict]["Lab"]/25 + dict1[Dict]["IA"]/7.5)/10, 2)
        calc_dict[Dict] =  [a, dict1[Dict]["credits"]]
        n = n + a*dict1[Dict]["credits"]
    n = n/20

#print cgpa of only 1 sub
def p_sub_cgpa(a):
    print(f"The cgpa of {a} is: {calc_dict[a]}")

#this sem only, lost
def p_sem():
    print(f"CGPA lost this sem alone: {round(n,2)}")

#all 4 years
def p_total_cgpa():
    print(f"CGPA lost in Total: {round(n/8, 2)}")

#used to automate adding marks later
def get_key(a):
    if a == 0:
        return "Subject"
    if a == 1:
        return "Lab"
    if a == 2:
        return "IA"
    if a == 3:
        return "Credits"

#automate entering marks through terminal
def create_values():
    import csv
    b = []
    for i in range(1, 9):
        c = []
        for j in range(4):
            a = str(i) + " Enter " + get_key(j) + ": "
            c.append(input(a))
        b.append(c)
    with open("Marks1.csv", 'w', newline="") as file1:
        a = csv.writer(file1)
        a.writerows(b)

#to check if above automation works as intended
def test_create_values():
    import csv
    with open("Marks2.csv", 'w', newline="") as file1:
        a = csv.writer(file1)
        a.writerows([["m",0,12,4],["c",0,5,4],["a",0,0,1],["b",0,0,4],["d",0,0,4],["e",0,0,4],["f",0,0,4],["g",0,0,4]])

#To change the values of individual sub alone (saves time and effort)
def change_this(x):
    import csv
    with open("Marks1.csv", 'r') as file1:
        a = csv.reader(file1)
        b = []
        for i in a:
            if i[0] == x:
                i = [x, input("Enter Lab: "), input("Enter IA: "), input("Enter Credits: ")]
            b.append(i)
    with open("Marks1.csv", 'w', newline= "") as file1:
        a = csv.writer(file1)
        a.writerows(b)

def predict():
    for i in calc_dict:
        a = round(((10 - calc_dict[i][0])*9))
        print("\n", i, "\n", a, "need", round(90 - a, 2), "for 9.0 CGPA")
        
def main():
    read_marks()
    calc_cgpa_dict()
    p_sem()
    p_total_cgpa()
main()

predict()

