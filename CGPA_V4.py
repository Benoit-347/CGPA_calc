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


def get_assignment_mark():
    num = get_int("enter no. of assignments: ", 3)
    value = get_int("enter value: ")
    scale = get_int("enter scale: ")
    list1 = ["value:", value]
    for i in range(1, num+1):
        print(f"For assignment {i}:")
        list1.append([get_int("enter mark: "), scale])
    return list1

def get_lab_mark():
    num = get_int("enter no. of labs: ", 12)
    value = get_int("enter value: ")
    scale = get_int("enter scale: ")
    list1 = ["value:", value]
    for i in range(1, num+1):
        print(f"For lab {i}:")
        list1.append([get_int("enter mark: "), scale])
    return list1

def get_IA_mark():
    num = get_int("enter no. of labs: ", 3)
    value = get_int("enter value: ")
    scale = get_int("enter scale: ")
    list1 = ["value:", value]
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
        credit = [get_int("enter course credit weight: ")]
        all[i] = {'assignment': assignment_list, 
                  'lab': lab_list, 
                  'IA': IA_list, 
                  'credit': credit
                  }
    return all


def write_get_sub_to_csv():
    dict_data = get_all_sub_marks()
    formatted_data = []
    for sub_name in dict_data:
        row = []
        row.append(sub_name)
        types = dict_data[sub_name]
        for type_name in types:
            row.append(type_name)
            type_list = types[type_name]
            for i in type_list:
                row.extend(i)
        formatted_data.append(row)
    file_name = "Marks_V4_trial.csv"
    with open(file_name, 'w') as file1:
        writer = csv.writer(file1)
        writer.writerows(formatted_data)
    import os
    os.startfile(file_name)

write_get_sub_to_csv()