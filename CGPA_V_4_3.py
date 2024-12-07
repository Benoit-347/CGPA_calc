"""Features:


Adding:

#change code to store individual values to be able to change later
#code changer


#need to add:

#code tester
#add feature to do practical calc (rns method)
#show colored graph of marks needed
#highlight marks with huge variance (and analysis like lab vs ia)

#if possible convert program into an android app with website


#added:

#predict mark needed per sub to get req cgpa
#predict avg mark req in all sub to get req cgpa (useful if you sucked in a few subs and recover through others)
#has error handling with wrong input to not re-enter whole program
#shows when its not possible to obtain specified cgpa"""

import csv

#the dict: {'math': {'ia': [["value:", value], [9, 10],[8,10]], 'lab':.., 'credit': [[]]}}

def get_int(a, max = None):
    if max == None:
        while True:
            try:
                num = int(input(a))
                return num
            except:
                print("error: input was not int\nTry again:")
    else:
        while True:
            try:
                num = int(input(a))
                if num <= max:
                    return num
                else:
                    print("\nToo high, try again:\n")
            except:
                print("error: input was not int\nTry again:")


def get_assignment_mark():
    num = get_int("enter no. of assignments: ", 3)
    value = get_int("enter value: ")
    scale = get_int("enter scale: ")
    list1 = []
    for i in range(1, num+1):
        print(f"For assignment {i}:")
        list1.append([get_int("enter mark: "), scale])
    return value, num, list1

def get_lab_mark():
    num = get_int("enter no. of labs: ", 12)
    value = get_int("enter value: ")
    scale = get_int("enter scale: ")
    list1 = []
    for i in range(1, num+1):
        print(f"For lab {i}:")
        list1.append([get_int("enter mark: "), scale])
    return value, num, list1

def get_ia_mark():
    num = get_int("enter no. of ias: ", 3)
    value = get_int("enter value: ")
    scale = get_int("enter scale: ")
    list1 = []
    for i in range(1, num+1):
        print(f"For ia {i}:")
        list1.append([get_int("enter mark: "), scale])
    return value, num, list1


def get_all_sub_marks():
    sub = ['math', 'chemistry', 'plc', 'caed', 'civil', 'english', 'sfh', 'kannada']
    all = {}
    for i in sub:
        print(f"For subject {i}:")
        assignment_value, assignment_num, assignment_list = get_assignment_mark()
        lab_value, lab_num, lab_list = get_lab_mark()
        ia_value, ia_num, ia_list =  get_ia_mark()
        credit = get_int("enter course credit weight: ")
        all[i] = {'assignment_value': [[assignment_value]],
                  'assignment_num': [[assignment_num]],
                  'assignment': assignment_list,
                  'lab_value': [[lab_value]], 
                  'lab_num': [[lab_num]], 
                  'lab': lab_list, 
                  'ia_value': [[ia_value]],
                  'ia_num': [[ia_num]],
                  'ia': ia_list,
                  'credit': [[credit]]
                  }
        
    return all


def write_get_sub_to_csv():
    dict_data = get_all_sub_marks()
    formatted_data = []
    for sub_name in dict_data:  #column sub name
        row = []
        row.append(sub_name)
        types_dict = dict_data[sub_name]
        for type_name in types_dict:    #ia, lab..
            row.append(type_name)
            type_list = types_dict[type_name]
            for i in type_list: #the value list, marks list
                row.extend(i)
        formatted_data.append(row)
    file_name = "Marks_V4_trial.csv"
    with open(file_name, 'w') as file1:
        writer = csv.writer(file1)
        writer.writerows(formatted_data)
    import os
    os.startfile(file_name)


def read_from_csv():
    with open("Marks_V4_trial.csv", 'r') as file1:
        reader = csv.reader(file1)
        formated_data = []
        for i in reader:
            if len(i) != 0:
                if i[0] != "":
                    new_list = []
                    for j in i:
                        if j != "":
                            try:
                                new_list.append(int(j))
                            except:
                                new_list.append(j)
                    formated_data.append(new_list)
    return formated_data


"""
the dict: {'math': {'assignment_value': [[assignment_value]],
                  'assignment_num': [[assignment_num]],
                  'assignment': assignment_list,
                  'lab_value': [[lab_value]], 
                  'lab_num': [[lab_num]], 
                  'lab': lab_list, 
                  'ia_value': [[ia_value]],
                  'ia_num': [[ia_num]],
                  'ia': ia_list,
                  'credit': [[credit]]
                  }}

#the list: [['math', 'assignment_value', 12, 'assignment_num', 2, 'assignment', 12, 12, 12, 12, 'lab_value', 12, 'lab_num', 2, 'lab', 1, 1, 1, 1, 'ia_value', 30, 'ia_num', 1, 'ia', 40, 50, 'credit', 4]

"""
def convert_csv_to_dict():
    all = {}
    for row in read_from_csv():


        #gets ia_list, assignment_list, lab_list
        assignment_num_index = 4
        assignment_num = row[assignment_num_index]
        assignment_value = row[2]
        assignment_list = []
        for i in range(assignment_num):
            assignment_list.append(row[assignment_num_index+2+i*2 : assignment_num_index+4+i*2])

        lab_num_index = assignment_num_index+assignment_num*2+5
        lab_num = row[lab_num_index]
        lab_value = row[lab_num_index-2]
        lab_list = []
        for i in range(lab_num):
            lab_list.append(row[lab_num_index+2+i*2 : lab_num_index+4+i*2])

        ia_num_index = lab_num_index+lab_num*2+5
        ia_num = row[ia_num_index]
        ia_value = row[ia_num_index-2]
        ia_list = []
        for i in range(ia_num):
            ia_list.append(row[ia_num_index+2+i*2 : ia_num_index+4+i*2])
        length = len(row)
        all[row[0]] = {row[1]: [[assignment_value]], row[3]: [[assignment_num]], row[5]: assignment_list, row[lab_num_index-3]: [[lab_value]], row[lab_num_index-1]: [[lab_num]], row[lab_num_index+1]: lab_list,row[ia_num_index-3]: [[ia_value]], row[ia_num_index-1]: [[ia_num]], row[ia_num_index+1]: ia_list, row[length-2]: [[row[length-1]]]}
    return all






#used to in the calculating cgpa (the denominator)
def calc_total_value_done_sub(sub_dict):
    assignment = sub_dict['assignment_value'][0][0]       #This is also used later, combine to reduce computation

    lab = sub_dict['lab_value'][0][0] 

    ia = sub_dict['ia_value'][0][0] 

    total = assignment + lab + ia
    
    return total
"""
        'math':   {'assignment_value': [[assignment_value]],
                  'assignment_num': [[assignment_num]],
                  'assignment': assignment_list,
                  'lab_value': [[lab_value]], 
                  'lab_num': [[lab_num]], 
                  'lab': lab_list, 
                  'ia_value': [[ia_value]],
                  'ia_num': [[ia_num]],
                  'ia': ia_list,
                  'credit': [[credit]]
                  }
"""

def get_assignment_lab_ia_value(sub_dict):
    assignment_mark = 0
    for i in range(sub_dict['assignment_num'][0][0]):
        assignment_mark += sub_dict['assignment'][i][0]
    if assignment_mark:
        assignment = assignment_mark*sub_dict['assignment_value'][0][0]/(sub_dict['assignment'][0][1]*sub_dict['assignment_num'][0][0])
    else:
        assignment = 0

    lab_mark = 0
    for i in range(sub_dict['lab_num'][0][0]):
        lab_mark += sub_dict['lab'][i][0]
    if lab_mark:
        lab = lab_mark*sub_dict['lab_value'][0][0]/(sub_dict['lab'][0][1]*sub_dict['lab_num'][0][0])
    else:
        lab = 0

    ia_mark = 0
    for i in range(sub_dict['ia_num'][0][0]):
        ia_mark += sub_dict['ia'][i][0]
    if ia_mark:
        ia = ia_mark*sub_dict['ia_value'][0][0]/(sub_dict['ia'][0][1]*sub_dict['ia_num'][0][0])
    else:
        ia = 0
    return assignment, lab, ia

#main CGPA calculator
def calc_CGPA_all(all_dict):
    cgpa_dict = {}
    for sub in all_dict:
        sub_dict = all_dict[sub]

        assignment, lab, ia = get_assignment_lab_ia_value(sub_dict)

        total = calc_total_value_done_sub(sub_dict)
        if total:
            total_cgpa = (assignment + lab + ia)/total
        else:
            total_cgpa = 0
        cgpa_dict[sub] = [round(total_cgpa*10, 2), sub_dict['credit'][0][0]]
    return cgpa_dict


def calc_CGPA_sem(sub_cgpa_dict):
    credit_obtained = 0
    total_credit = 0
    for i in sub_cgpa_dict:
        sub = sub_cgpa_dict[i]
        if sub[0] != 0:
            credit_obtained += sub[0]*sub[1]
            total_credit += sub[1]
            
    return (credit_obtained)/total_credit


def get_true_total_value_done(sub_dict, max_assignment, max_lab, max_ia):
    assignment_total = sub_dict['assignment_num'][0][0]/max_assignment*sub_dict['assignment_value'][0][0]
    lab_total = sub_dict['lab_num'][0][0]/max_lab*sub_dict['lab_value'][0][0]
    ia_total = sub_dict['ia_num'][0][0]/max_ia*sub_dict['ia_value'][0][0]
    return assignment_total, lab_total, ia_total

#used to predict the marks req for achivieng required cgpa
def get_req_value(sub_dict, req_cgpa, external_expected = None, lab_expected = 0.9):
    max_assignment = 1
    max_lab = 6
    max_ia = 3
    num_assignment, num_lab, num_ia = sub_dict['assignment_num'][0][0], sub_dict['lab_num'][0][0], sub_dict['ia_num'][0][0]
    assignment_value_done, lab_value_done, ia_value_done = get_true_total_value_done(sub_dict, max_assignment, max_lab, max_ia)
    total_true_value_done = assignment_value_done + lab_value_done + ia_value_done
    assignment, lab, ia = get_assignment_lab_ia_value(sub_dict)
    assignment_true_got, lab_true_got, ia_true_got = assignment*num_assignment/max_assignment, lab*num_lab/max_lab, ia*num_ia/max_ia

    total_true_value_got = assignment_true_got + lab_true_got + ia_true_got

    net_req_value = (100)*req_cgpa/10 - total_true_value_got

    
    num_assignment_left, num_lab_left, num_ia_left = max_assignment - num_assignment, max_lab - num_lab, max_ia - num_ia

    assignment_value, lab_value, ia_value = sub_dict['assignment_value'][0][0], sub_dict['lab_value'][0][0], sub_dict['ia_value'][0][0]
    
    req_value = net_req_value - (num_assignment_left/max_assignment*assignment_value + num_lab_left/max_lab*lab_value)


    if external_expected == None:
        percent_req_ia_external = (req_value/(ia_value*num_ia_left/max_ia + 50))


        ia_value_req, external_value_req = ia_value*percent_req_ia_external, 50*percent_req_ia_external
        ia_mark_req = 50*(ia_value_req/ia_value)
        external_mark_req = 100*(external_value_req/50)
        return num_ia_left, ia_mark_req, external_mark_req

    else:
        req_ia_only_value = req_value - 50*req_cgpa/10
        per_ia = (req_ia_only_value)/num_ia_left
        return per_ia

#main prediction fn
#basically: how much marks needed to be earned in each ia remaining to get a req CGPA
def predict(all_dict, req_cgpa, external_expected=None):

    if external_expected== None:
        external_expected = get_int("how much do you expect to get in externals?: ")

    req_mark_list = []
    for sub_name in all_dict:
        sub_dict = all_dict[sub_name]
        credit = sub_dict['credit'][0][0]
        num_ia_left, ia_mark, external_mark = get_req_value(sub_dict, req_cgpa)
        if not ia_mark >50: 
            req_mark_list.append([sub_name, {'num_IA_left': num_ia_left, 'IA': ia_mark, 'Finals': external_mark, 'credit': credit}])
        else:
            print(f"Note: Not possible to get {req_cgpa} in {sub_name}\n")
            req_mark_list.append([sub_name, {'num_IA_left': num_ia_left, 'IA': ia_mark, 'Finals': external_mark, 'credit': credit}])
    return req_mark_list



#calc on avg how much mark you require for each sub on ia to get req sem cgpa
def predict_avg_mark(list1):
    credits = [4, 4, 3, 3, 3, 1, 1, 1]
    total = 0
    j = 0
    for i in list1:
        total += i[1]*credits[j]
        j += 1
    avg_mark_req = total/20
    if not avg_mark_req>50:
        return avg_mark_req
    else:
        return "\n***************\n\nMarks too low, it is not possible to get specified CGPA\n\n***************\n\nDon't be delusional.\n\n(tip: try changing req cgpa)\n"


#calc on avg how much mark you require for each sub on ia to get req sem cgpa
def predict_avg_mark(req_mark_list):
    total = 0
    j = 0
    for sub_list in req_mark_list:
        credit = sub_list[1]['credit']
        total += sub_list[1]*credits[j]
        j += 1
    avg_mark_req = total/20
    if not avg_mark_req>50:
        return avg_mark_req
    else:
        return "\n***************\n\nMarks too low, it is not possible to get specified CGPA\n\n***************\n\nDon't be delusional.\n\n(tip: try changing req cgpa)\n"






def main():
    all_dict = convert_csv_to_dict()
    cgpa_dict = calc_CGPA_all(all_dict)
    print(f"\nDict of each sub cgpa and credit:\n\n{cgpa_dict}")
    print(f"\nThis sem's CGPA: {round(calc_CGPA_sem(cgpa_dict), 2)}\n")
    marks_req_list = predict(all_dict, 9, 0.9)
    print(marks_req_list)
    print(f"\nNeed to score: {predict_avg_mark(marks_req_list)} marks, in all subjects to get specified CGPA\n")


main()