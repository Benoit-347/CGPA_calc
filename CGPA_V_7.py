"""Features:


Adding:


#custom calc for some subjects with different layout (create a fn that will serve as all subject fn(para changes formula by itself))
#feature to do practical calc (rns method)

#need to add:

#code tester
#add feature to do practical calc (rns method)
#show colored graph of marks needed
#highlight marks with huge variance (and analysis like lab vs ia)

#if possible convert program into an android app with website


#added:

#creates and reads from a config file to create marks dictionary (feature to seperate adding standard value of max assignment, value, scale for each entry, standardizing it)
#easily change individual values of exel file with one command
#easily print organised data of individual subjects with one command
#give data with expected externals input or if want to include externals as well in prediction
#change code to store individual values to be able to change later
#predict mark needed per sub to get req cgpa
#predict avg mark req in all sub to get req cgpa (useful if you sucked in a few subs and recover through others)
#has error handling with wrong input to not re-enter whole program
#shows when its not possible to obtain specified cgpa"""

import csv

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



def get_configure_dict(num_of_subjects):
    sub_dict = {}
    for i in range(num_of_subjects):
        while True:
            sub_name = input("enter subject name: ")
            temp = { "max_assignment_num": get_int("maximum number of assignments: "),"assignment_num":get_int("Enter number of assignments completed: "), "assignment_scale": get_int("Enter scale of assignment: "),"assignment_value": get_int("value of assignments (out of whole course): "),
                     "max_lab_num": get_int("maximum number of labs: "),"lab_num":get_int("Enter number of labs completed: "), "lab_scale": get_int("Enter scale of lab: "),"lab_value": get_int("value of lab (out of whole course): "),
                     "max_ia_num": get_int("maximum number of IAs: "),"ia_num":get_int("Enter number of IAs completed: "), "ia_scale": get_int("Enter scale of IA: "),"ia_value": get_int("value of IA (out of whole course): "),
                      "credit": get_int("enter credit weight of course: ")}
            if temp["assignment_value"] + temp["lab_value"] + temp["ia_value"] == 50:
                if temp["assignment_num"] <= temp["max_assignment_num"] and temp["lab_num"] <= temp["max_lab_num"] and temp["ia_num"] <= temp["max_ia_num"]:
                    break
                else:
                    print("\nNumber of assignments/labs/IA greater than maximum\nTry again:")
            else:
                print("\nTotal value != 100\nTry again:")
        sub_dict[sub_name] = temp
    return sub_dict

#the dict: {'math': {'ia': [["value:", value], [9, 10],[8,10]], 'lab':.., 'credit': [[]]}}

def convert_config_to_csv(dict_config):
    result = []
    for sub in dict_config:
        row = []
        row.append(sub)
        sub_dict = dict_config[sub]
        for type in sub_dict:
            row.append(type)
            row.append(sub_dict[type])
        result.append(row)
    return result

def write_config(csv_format, file_name):
    with open(file_name, 'w') as file1:
        writer = csv.writer(file1)
        writer.writerows(csv_format)
        import os
        os.startfile(file_name)

def create_config(num_subjects, file_name):
    write_config(convert_config_to_csv(get_configure_dict(num_subjects)), file_name)


def convert_config_to_dict(csv_format):
    result = {}
    for row in csv_format:
        sub_name = row[0]
        dict1 = {}
        for i in range(1, 1+ 3*4*2 + 2, 2):
            dict1[row[i]] = row[i+1]
        result[sub_name] = dict1
    return result


def get_assignment_mark(num, scale):
    list1 = []
    for i in range(1, num+1):
        print(f"For assignment {i}:")
        list1.append([get_int("enter mark: "), scale])
    return list1

def get_lab_mark(num, scale):
    list1 = []
    for i in range(1, num+1):
        print(f"For lab {i}:")
        list1.append([get_int("enter mark: "), scale])
    return list1

def get_ia_mark(num, scale):
    list1 = []
    for i in range(1, num+1):
        print(f"For ia {i}:")
        list1.append([get_int("enter mark: "), scale])
    return list1


def get_all_sub_marks(config_data):
    print(config_data)
    all = {}
    for sub_name in config_data:
        sub_dict = config_data[sub_name]
        num_assignment, num_lab, num_ia, scale_assignment, scale_lab, scale_ia = sub_dict['assignment_num'], sub_dict['lab_num'], sub_dict['ia_num'], sub_dict['assignment_scale'], sub_dict['lab_scale'], sub_dict['ia_scale']
        print(f"For subject {sub_name}:")
        assignment_list = get_assignment_mark(num_assignment, scale_assignment)
        lab_list = get_lab_mark(num_lab, scale_lab)
        ia_list =  get_ia_mark(num_ia, scale_ia)
        assignment_value, lab_value, ia_value = sub_dict['assignment_value'], sub_dict['lab_value'], sub_dict['ia_value']
        max_assignment_num, max_lab_num, max_ia_num = sub_dict['max_assignment_num'], sub_dict['max_lab_num'], sub_dict['max_ia_num']
        credit = sub_dict['credit']
        all[sub_name] = {'assignment_value': [[assignment_value]],
                  'assignment_num': [[num_assignment]],
                  'assignment': assignment_list,
                  'lab_value': [[lab_value]], 
                  'lab_num': [[num_lab]], 
                  'lab': lab_list, 
                  'ia_value': [[ia_value]],
                  'ia_num': [[num_ia]],
                  'ia': ia_list,
                  'credit': [[credit]],
                  'max_assignment_num': [[max_assignment_num]],
                  'max_lab_num': [[max_lab_num]],
                  'max_ia_num': [[max_ia_num]]
                  }
    return all


def write_get_sub_to_csv(sub_list, file_name):
    dict_data = get_all_sub_marks(sub_list)
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
    with open(file_name, 'w') as file1:
        writer = csv.writer(file1)
        writer.writerows(formatted_data)
    import os
    os.startfile(file_name)


def read_from_csv(file_name):
    with open(file_name, 'r') as file1:
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
def convert_csv_to_dict(readlines_data):

    all = {}
    for row in readlines_data:

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
def get_req_value(sub_dict, req_cgpa, max_assignment = 3, max_lab = 10, max_ia = 3, external_expected = None, lab_expected = 0.9):
    
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
        req_ia_only_value = req_value - external_expected/2
        per_ia = req_ia_only_value/num_ia_left
        ia_mark_req = max_ia*50*(per_ia/ia_value)
        return ia_mark_req

#main prediction fn
#basically: how much marks needed to be earned in each ia remaining to get a req CGPA
def predict(all_dict, req_cgpa, max_assignment = 3, max_lab = 10, max_ia = 3, external_expected = None, lab_expected = 0.9):


    req_mark_list = []
    for sub_name in all_dict:
        sub_dict = all_dict[sub_name]
        credit = sub_dict['credit'][0][0]
        if external_expected == None: 
            num_ia_left, ia_mark, external_mark = get_req_value(sub_dict, req_cgpa, max_assignment, max_lab, max_ia, external_expected, lab_expected)   
            ia_mark, external_mark = round(ia_mark), round(external_mark)
            if not ia_mark >50: 
                req_mark_list.append([sub_name, {'num_IA_left': num_ia_left, 'IA': ia_mark, 'Finals': external_mark, 'credit': credit}])
            else:
                print(f"Note: Not possible to get {req_cgpa} in {sub_name}\n")
                req_mark_list.append([sub_name, {'num_IA_left': num_ia_left, 'IA': ia_mark, 'Finals': external_mark, 'credit': credit}])
        else:
            num_ia_left = max_ia - sub_dict['ia_num'][0][0]
            ia_mark= get_req_value(sub_dict, req_cgpa, max_assignment, max_lab, max_ia, external_expected, lab_expected)   
            ia_mark, external_mark = round(ia_mark), external_expected
            if not ia_mark >50: 
                req_mark_list.append([sub_name, {'num_IA_left': num_ia_left, 'IA': ia_mark, 'Finals': external_mark, 'credit': credit}])
            else:
                print(f"Note: Not possible to get {req_cgpa} in {sub_name}\n")
                req_mark_list.append([sub_name, {'num_IA_left': num_ia_left, 'IA': ia_mark, 'Finals': external_mark, 'credit': credit}])
        

    return req_mark_list


#calc on avg how much mark you require for each sub on ia to get req sem cgpa
def predict_avg_mark(req_mark_list):
    total_ia = 0
    total_external = 0
    j = 0
    for sub_list in req_mark_list:
        credit = sub_list[1]['credit']
        total_ia += sub_list[1]['IA']*credit
        total_external += sub_list[1]['Finals']*credit
        j += 1
    avg_ia_mark_req = total_ia/20
    avg_external_mark_req = total_external/20
    if avg_ia_mark_req<=50 and avg_external_mark_req <= 100:
        return avg_ia_mark_req, avg_external_mark_req
    else:
        return None, "\n***************\n\nMarks too low, it is not possible to get specified CGPA\n\n***************\n\nDon't be delusional.\n\n(tip: try changing req cgpa)\n"


def get_subject_from_csv(sub, sub_list, csv_data):
    sub_index = sub_list.index(sub)
    row = csv_data[sub_index]
    assignment_num_index = 4
    assignment_num = row[assignment_num_index]
    print("\n\nSubject: Math")
    for i in range(assignment_num):
        index = assignment_num_index+2+i*2
        print(f"\nAssignment{i+1}: scored {row[index]} out of {row[index + 1]}")
    print("\n", end = "")
    lab_num_index = assignment_num_index+assignment_num*2+5
    lab_num = row[lab_num_index]
    for i in range(lab_num):
        index = lab_num_index+2+i*2
        print(f"\nLab{i+1}: scored {row[index]} out of {row[index + 1]}")
    print("\n", end = "")

    ia_num_index = lab_num_index+lab_num*2+5
    ia_num = row[ia_num_index]
    for i in range(ia_num):
        index = ia_num_index+2+i*2
        print(f"\nIA{i+1}: scored {row[index]} out of {row[index + 1]}")
    print("\n", end = "")


def change_and_return_data(sub_list, csv_data, sub, type, num, new_value):
    sub_index = sub_list.index(sub)
    row = csv_data[sub_index]

    assignment_num_index = 4
    assignment_num = row[assignment_num_index]

    lab_num_index = assignment_num_index+assignment_num*2+5
    lab_num = row[lab_num_index]

    ia_num_index = lab_num_index+lab_num*2+5
    ia_num = row[ia_num_index]

    if type == "assignment":
        index = assignment_num_index+2+(num-1)*2
        while new_value> row[index+1]:
            new_value = get_int("New Value too high")
        row[index] = new_value
        return csv_data

    elif type == "lab":
        index = lab_num_index+2+(num-1)*2
        while new_value> row[index+1]:
            new_value = get_int("New Value too high")
        row[index] = new_value
        return csv_data
    
    elif type == "ia":
        index = ia_num_index+2+(num-1)*2
        while new_value> row[index+1]:
            new_value = get_int("New Value too high")
        row[index] = new_value
        return csv_data

    else:
        print("Error no match for type")

"""
#fns:

calc_CGPA_all(the_original_input_dict)
#returns a dict containing each subjects cgpa

Eg: {'math': [8.87, 4], 'chemistry': [9.6, 4], 'plc': [0.0, 3], 'caed': [0.0, 3], 'civil': [0.0, 3], 'english': [0.0, 1], 'sfh': [0.0, 1], 'kannada': [0.0, 1]}


predict(all_dict, 9,max_assignment=3, max_lab=10, max_ia=3, external_expected=90)
#returns a list of lists containing dict of req marks in each exam to reach dersired cgpa

Eg: [['math', {'num_IA_left': 2, 'IA': 40, 'Finals': 90, 'credit': 4}], ['chemistry', {'num_IA_left': 2, 'IA': 34, 'Finals': 90, 'credit': 4}], ['plc', {'num_IA_left': 3, 'IA': 25, 'Finals': 90, 'credit': 3}], ['caed', {'num_IA_left': 3, 'IA': 25, 'Finals': 90, 'credit': 3}], ['civil', {'num_IA_left': 3, 'IA': 25, 'Finals': 90, 'credit': 3}], ['english', {'num_IA_left': 3, 'IA': 25, 'Finals': 90, 'credit': 1}], ['sfh', {'num_IA_left': 3, 'IA': 25, 'Finals': 90, 'credit': 1}], ['kannada', {'num_IA_left': 3, 'IA': 25, 'Finals': 90, 'credit': 1}]]


predict_avg_mark(marks_req_list)
#returns avg mark req from all subject to score desired cgpa (accurate average based of credit weight)
#Eg:    Need to score IA: 29.8 marks
        Need to score Finals: 90.0 marks in all subjects to get specified CGPA


get_subject_from_csv('math', sub_list, csv_data)
#prints text in terminal to showcase an organised data from specified file name

Eg: Subject: Math

    Assignment1: scored 10 out of 10


    Lab1: scored 18 out of 20

    Lab2: scored 20 out of 20


change_and_return_data(sub_list, csv_data, 'math', 'lab', num= 2, new_value=20)
#Used to change specific values from a csv file, returns a csv_format_list that contains the changed values
Eg: before: Lab2: scored 18 out of 20
    after:  Lab2: scored 20 out of 20
"""


def main(file_name, config_file_name):
    config_data =  convert_config_to_dict(read_from_csv(config_file_name))
    write_get_sub_to_csv(config_data, file_name)
    csv_data = read_from_csv(file_name)
    all_dict = convert_csv_to_dict(csv_data)
    cgpa_dict = calc_CGPA_all(all_dict)
    print(f"\nDict of each sub cgpa and credit:\n\n{cgpa_dict}")
    print(f"\nThis sem's CGPA: {round(calc_CGPA_sem(cgpa_dict), 2)}\n")

    marks_req_list = predict(all_dict, 9,max_assignment=3, max_lab=10, max_ia=3, external_expected=90)
    print(marks_req_list)

    avg_ia_mark_req, avg_external_mark_req = predict_avg_mark(marks_req_list)
    if avg_ia_mark_req != None:
        print(f"\nNeed to score IA: {avg_ia_mark_req} marks\nNeed to score Finals: {avg_external_mark_req} marks in all subjects to get specified CGPA\n")
    else:
        print(avg_external_mark_req)


    new_read = change_and_return_data(config_data, csv_data, 'math', 'lab', num= 2, new_value=20)


    with open(file_name, 'w') as file1:
        writer = csv.writer(file1)
        writer.writerows(new_read)

    get_subject_from_csv('math', config_data, csv_data)
main(file_name = "Marks_V7.csv", config_file_name= "config_1.csv")