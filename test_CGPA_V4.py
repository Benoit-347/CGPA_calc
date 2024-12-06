import csv
#the dict: {'matj': {'ia': [[9, 10],[8,10]], 'lab':}}


def get_int(a):
    while True:
        try:
            num = int(input(a))
            return num
        except:
            print("error: input was not int\nTry again:")

def get_IA_mark():
    num_IA = get_int("enter no. of IAs: ")
    IA_list = []
    for i in range(1, num_IA+1):
        print(f"For IA {i}:")
        IA_list.append([get_int("enter mark (scaled  to 50): "), 50])
    return IA_list


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
        credit = [get_int("enter course credit weight: ")]
        all[i] = {'assignment': assignment_mark, 
                  'lab': lab_mark, 
                  'IA': IA_mark, 
                  'credit': credit
                  }
    return all

assert get_