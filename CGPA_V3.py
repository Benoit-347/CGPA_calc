#write special identification value for unknown
#write predict
#code tester
#change code to store individual values to be able to change
#code changer
#mistake try again

import csv

def read_marks():
    global dict1
    dict1 = {}
    with open("MarksV3.csv", 'r') as file1:
        a = csv.reader(file1) #reading through the reader fn gives us the data formated according to all the corner cases
        for i in a:
            dict1[i[0]] = {"Lab": float(i[1]), "IA": float(i[2]), "credits": float(i[3])}



def get_all_sub_marks():
    sub = ['math', 'chemistry', 'plc', 'caed', 'civil', 'english', 'sfh', 'kannada']
    all = {}
    for i in sub:
        print(f"For subject {i}:")
        a, b = get_assignment_mark()
        assignment_mark = [a,b]
        a, b = get_lab_mark()
        lab_mark = [a,b]
        a, b =  get_IA_mark()
        IA_mark = [a,b]
        credit = [int(input("enter course credit weight: "))]
        all[i] = {'assignment': assignment_mark, 'lab': lab_mark, 'IA': IA_mark, 'credit': credit}
    return all

def get_IA_mark():
    num_IA = int(input("enter no. of IAs: "))
    total = 0
    mark = 0
    for i in range(num_IA):
        print(f"For IA {i}:")
        total += 50
        mark += int(input("enter mark (scaled  to 50): "))
    return total, mark

def get_lab_mark():
    num_lab = int(input("enter no. of labs: "))
    total = 0
    mark = 0
    for i in range(num_lab):
        print(f"For Lab {i}:")
        total += 30
        mark += int(input("enter mark (scaled each lab to 30): "))
    return total, mark

def get_assignment_mark():
    num_assignment = int(input("enter no. of assignments: "))
    total = 0
    mark = 0
    for i in range(num_assignment):
        print(f"For assignment {i}:")
        total += 10
        mark += int(input("enter mark of assignment: "))
    return total, mark

def write_get_sub_to_csv():
    raw_data = get_all_sub_marks()
    formatted_data = []
    for i in raw_data:
        row = []
        row.append(i)
        for j in raw_data[i]:
            type = raw_data[i]
            row.append(j)
            row.extend(type[j])
        formatted_data.append(row)
    file_name = "Marks_V3_bet.csv"
    with open(file_name, 'w') as file1:
        writer = csv.writer(file1)
        writer.writerows(formatted_data)
    import os
    os.startfile(file_name)

def read_from_csv():
    with open("Marks_V3_bet.csv", 'r') as file1:
        reader = csv.reader(file1)
        formated_data = []
        for i in reader:
            if i[0] != "":
                formated_data.append(i)
    return formated_data

def convert_csv_to_dict():
    all = {}
    for row in read_from_csv():
        if row:
            all[row[0]] = {row[1]: [int(row[2]), int(row[3])], row[4]: [int(row[5]), int(row[6])], row[7]: [int(row[8]), int(row[9])], row[10]: int(row[11])}
    return all

#can be added to next fn to reduce quantity and confusion
def calc_total_value_done_sub(sub_dict):
    a = sub_dict['assignment'][0]       #This is also used later, combine to reduce computation
    if a:
        assignment = a
    else:
        assignment = 0
    a = sub_dict['lab'][0]/25
    if a:
        lab = a
    else:
        lab = 0
    a = sub_dict['IA'][0]/7.5
    if a:
        ia = a
    else:
        ia = 0
    total = assignment + lab + ia
    return assignment, lab, ia, total
    

def calc_total_value_done():
    dict_total_value = {}
    for sub in all_dict:
        sub_dict = all_dict[sub]
        total_value = sub_dict['assignment'][0] + sub_dict['lab'][0] + sub_dict['IA'][0]
        dict_total_value[sub] = total_value
    return dict_total_value

def calc_CGPA_all():
    cgpa_dict = {}
    for sub in all_dict:
        sub_dict = all_dict[sub]

        if sub_dict['assignment'][0]:
            assignment = sub_dict['assignment'][1]/sub_dict['assignment'][0]
        else:
            assignment = 0

        if sub_dict['lab'][0]:
            lab = sub_dict['lab'][1]/sub_dict['lab'][0]
        else:
            lab = 0

        if sub_dict['IA'][0]:
            ia = sub_dict['IA'][1]/sub_dict['IA'][0]
        else:
            ia = 0

        a, b, c, d = calc_total_value_done_sub(sub_dict)
        if assignment or lab or ia:
            total_cgpa = (assignment*a + lab*b + ia*c)/d
        else:
            total_cgpa = 0
        cgpa_dict[sub] = [round(total_cgpa*10, 2), sub_dict['credit']]
    return cgpa_dict

def calc_CGPA_sem():
    dict = calc_CGPA_all()
    total_mark = 0
    total_credit = 0
    for i in dict:
        sub = dict[i]
        total_credit += sub[1]
        if sub[0] == 0:
            total_mark += 9*sub[1]
        else:
            total_mark += sub[0]*sub[1] 
    return (total_mark)/total_credit

def get_req_value(sub_name, sub_dict, num_IA, req_cgpa, external_expected):
    total = calc_total_value_done_sub(sub_dict)[3]
    ia_value = 50/7.5
    extra_total = (num_IA*ia_value + 50)
    current_value = (cgpa_dict[sub_name][0]/10)*total
    req_value = req_cgpa*(total + extra_total)/10 - current_value
    return round((req_value-50*external_expected)/num_IA, 1)

def predict(req_cgpa, IA_left, external_expected):
    req_mark_list = []
    for dict in all_dict:
        sub_name = dict
        req_mark_list.append([dict, get_req_value(sub_name, all_dict[dict], IA_left, req_cgpa, external_expected)*7.5])
    return req_mark_list

    #how much mark to earn in IA to get a CGPA?
    pass

def predict_avg_mark(list1):
    sub = ['math', 'chemistry', 'plc', 'caed', 'civil', 'english', 'sfh', 'kannada']
    credits = [4, 4, 3, 3, 3, 1, 1, 1]
    total = 0
    j = 0
    for i in list1:
        total += i*credits[j]
        j += 1
    avg_mark_req = total/20
    return avg_mark_req
    #calc on avg how much mark each sub on IA 
    pass

def main():
    global all_dict, cgpa_dict
    all_dict = convert_csv_to_dict()
    cgpa_dict = calc_CGPA_all()
    print(f"\nDict of each sub cgpa and credit:\n\n{cgpa_dict}")
    print(f"\nThis sem's CGPA: {round(calc_CGPA_sem(), 2)}\n")
    marks_req_list = predict(9, 2, 0.9)
    print(marks_req_list)
    print(predict_avg_mark(marks_req_list))

main()
#dsa
#dar
#ddca
#os
#dae
