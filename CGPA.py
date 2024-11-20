#welcome to Benoit's CGPA calc
#enter values by:
# each row signifies a subject
# each coulumn has attributes: 1. lab marks scaled to 300 out of 12 marks 2. Internals mark lost in total (150) 3. Credit weightage of the subject in question

import csv
list1 = []
with open("Marks.csv", 'r') as file1:
    a = csv.reader(file1) #reading through the reader fn gives us the data formated according to all the corner cases
    for i in a:
        list1.append({"Lab": int(i[1]), "IA": int(i[2]), "credits": int(i[3])})
print(list1)


def create_list():
    global n, cgpa_per_sub
    n = 0
    cgpa_per_sub = []
    for i in list1:
        a = (i["Lab"]/25 + i["IA"]/7.5)/10
        cgpa_per_sub.append(a)
        b = a*i["credits"]
        n = n + b

create_list()

def p_sub():
    j = 0
    for i in cgpa_per_sub:
        j += 1
        print(f"CGPA lost from Sub {j}: {round(i,2)}")

cgpa_lost_this_sem = n/20

def p_sem():
    print(f"CGPA lost this sem alone: {round(cgpa_lost_this_sem, 2)}")

p_sub()
p_sem()
cumulative_cgpa_lost = cgpa_lost_this_sem/8
print(f"CGPA lost in Total: {round(cumulative_cgpa_lost, 2)}")