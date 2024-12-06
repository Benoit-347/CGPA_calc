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
    list1 = [["value:", value], ["num", num]]
    for i in range(1, num+1):
        print(f"For assignment {i}:")
        list1.append([get_int("enter mark: "), scale])
    return list1

def get_lab_mark():
    num = get_int("enter no. of labs: ", 12)
    value = get_int("enter value: ")
    scale = get_int("enter scale: ")
    list1 = [["value:", value], ["num:", num]]
    for i in range(1, num+1):
        print(f"For lab {i}:")
        list1.append([get_int("enter mark: "), scale])
    return list1

def get_IA_mark():
    num = get_int("enter no. of IAs: ", 3)
    value = get_int("enter value: ")
    scale = get_int("enter scale: ")
    list1 = [["value:", value], ["num", num]]
    for i in range(1, num+1):
        print(f"For IA {i}:")
        list1.append([get_int("enter mark: "), scale])
    return list1


def get_all_sub_marks():
    sub = ['math', 'chemistry', 'plc', 'caed', 'civil', 'english', 'sfh', 'kannada']
    all = {}
    for i in sub:
        print(f"For subject {i}:")
        assignment_list = get_assignment_mark()
        lab_list = get_lab_mark()
        IA_list =  get_IA_mark()
        credit = get_int("enter course credit weight: ")
        all[i] = {'assignment': assignment_list, 
                  'lab': lab_list, 
                  'IA': IA_list, 
                  'credit': [[credit]]
                  }
    print(all)
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
                print("extended:", i)
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
    print(formated_data)
    return formated_data


#the dict: {'math': {'ia': [["value:", value], ['num:', num] [9, 10],[8,10]], 'lab':.., 'credit': [[]]}}
#the list: [['math', 'assignment', 'value:', '10','num':, 2, '10', '10', '10', '10', 'lab', 'value:', '12', '12', '12', '12', '12', 'IA', 'value:', '30', '40', '50', 'credit', 'credit', '[4]'], [...]]
def convert_csv_to_dict():
    all = {}
    for row in read_from_csv():


        #gets ia_list, assignment_list, lab_list
        num_assignment_index = 5
        num_assignment = row[num_assignment_index]
        assignment_list = [row[2:4], row[4:6]]
        for i in range(num_assignment):
            assignment_list.append(row[num_assignment_index+1+i*2 : num_assignment_index+3+i*2])
        print(assignment_list) 
        num_lab_index = num_assignment_index+num_assignment*2+5
        num_lab = row[num_lab_index]
        print(num_lab)
        lab_list = [row[num_lab_index-3:num_lab_index-1], row[num_lab_index-1:num_lab_index+1]]
        for i in range(num_lab):
            lab_list.append(row[num_lab_index+1+i*2 : num_lab_index+3+i*2])

        num_IA_index = num_lab_index+num_lab*2+5
        num_IA = row[num_IA_index]
        IA_list = [row[num_IA_index-3:num_IA_index-1], row[num_IA_index-1:num_IA_index+1]]
        for i in range(num_IA):
            IA_list.append(row[num_IA_index+1+i*2 : num_IA_index+3+i*2])
        length = len(row)
        all[row[0]] = {row[1]: assignment_list, row[num_lab_index-4]: lab_list, row[num_IA_index-4]: IA_list, row[length-2]: [[row[length-1]]]}
    print(all)    
    return all

def write_get_sub_to_csv():
    dict_data = convert_csv_to_dict()
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
                print("extended:", i)
        formatted_data.append(row)
    file_name = "Marks_V4_trial_beta.csv"
    with open(file_name, 'w') as file1:
        writer = csv.writer(file1)
        writer.writerows(formatted_data)
    import os
    os.startfile(file_name)
write_get_sub_to_csv()