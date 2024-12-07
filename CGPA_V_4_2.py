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

def get_IA_mark():
    num = get_int("enter no. of IAs: ", 3)
    value = get_int("enter value: ")
    scale = get_int("enter scale: ")
    list1 = []
    for i in range(1, num+1):
        print(f"For IA {i}:")
        list1.append([get_int("enter mark: "), scale])
    return value, num, list1


def get_all_sub_marks():
    sub = ['math', 'chemistry', 'plc', 'caed', 'civil', 'english', 'sfh', 'kannada']
    all = {}
    for i in sub:
        print(f"For subject {i}:")
        assignment_value, assignment_num, assignment_list = get_assignment_mark()
        lab_value, lab_num, lab_list = get_lab_mark()
        IA_value, IA_num, IA_list =  get_IA_mark()
        credit = get_int("enter course credit weight: ")
        all[i] = {'assignment_value': [[assignment_value]],
                  'assignment_num': [[assignment_num]],
                  'assignment': assignment_list,
                  'lab_value': [[lab_value]], 
                  'lab_num': [[lab_num]], 
                  'lab': lab_list, 
                  'IA_value': [[IA_value]],
                  'IA_num': [[IA_num]],
                  'IA': IA_list,
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
        for type_name in types_dict:    #IA, lab..
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
                  'IA_value': [[IA_value]],
                  'IA_num': [[IA_num]],
                  'IA': IA_list,
                  'credit': [[credit]]
                  }}

#the list: [['math', 'assignment_value', 12, 'assignment_num', 2, 'assignment', 12, 12, 12, 12, 'lab_value', 12, 'lab_num', 2, 'lab', 1, 1, 1, 1, 'IA_value', 30, 'IA_num', 1, 'IA', 40, 50, 'credit', 4]

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

        IA_num_index = lab_num_index+lab_num*2+5
        IA_num = row[IA_num_index]
        IA_value = row[IA_num_index-2]
        IA_list = []
        for i in range(IA_num):
            IA_list.append(row[IA_num_index+2+i*2 : IA_num_index+4+i*2])
        length = len(row)
        all[row[0]] = {row[1]: [[assignment_value]], row[3]: [[assignment_num]], row[5]: assignment_list, row[lab_num_index-3]: [[lab_value]], row[lab_num_index-1]: [[lab_num]], row[lab_num_index+1]: lab_list,row[IA_num_index-3]: [[IA_value]], row[IA_num_index-1]: [[IA_num]], row[IA_num_index+1]: IA_list, row[length-2]: [[row[length-1]]]}
    return all






#used to in the calculating cgpa (the denominator)
def calc_total_value_done_sub(sub_dict):
    assignment = sub_dict['assignment_value'][0][0]       #This is also used later, combine to reduce computation

    lab = sub_dict['lab_value'][0][0] 

    ia = sub_dict['IA_value'][0][0] 

    total = assignment + lab + ia
    
    return total
"""
        'math':   {'assignment_value': [[assignment_value]],
                  'assignment_num': [[assignment_num]],
                  'assignment': assignment_list,
                  'lab_value': [[lab_value]], 
                  'lab_num': [[lab_num]], 
                  'lab': lab_list, 
                  'IA_value': [[IA_value]],
                  'IA_num': [[IA_num]],
                  'IA': IA_list,
                  'credit': [[credit]]
                  }
"""

#main CGPA calculator
def calc_CGPA_all(all_dict):
    cgpa_dict = {}
    for sub in all_dict:
        sub_dict = all_dict[sub]

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

        IA_mark = 0
        for i in range(sub_dict['IA_num'][0][0]):
            IA_mark += sub_dict['IA'][i][0]
        if IA_mark:
            IA = IA_mark*sub_dict['IA_value'][0][0]/(sub_dict['IA'][0][1]*sub_dict['IA_num'][0][0])
        else:
            IA = 0

        total = calc_total_value_done_sub(sub_dict)
        if total:
            total_cgpa = (assignment + lab + IA)/total
        else:
            total_cgpa = 0
        cgpa_dict[sub] = [round(total_cgpa*10, 2), sub_dict['credit'][0][0]]
    return cgpa_dict

print(calc_CGPA_all(convert_csv_to_dict()))