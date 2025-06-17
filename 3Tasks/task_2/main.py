from collections import defaultdict


students = {
        'Alice': {'math': 80, 'physics': 90},
        'Bob': {'math': 75, 'physics': 85, 'chemistry': 95},
        'Charlie': {'math': 60, 'physics': 70},
        'Dima':{'math': 75, 'physics': 85, 'chemistry': 95}
    }


def get_highest_object(dict:dict):
    count = defaultdict(int)
    sum = defaultdict(int)
    for i in dict.values():
        for j in i.keys():
            count[j] += 1
            for g in i.values():
                sum[j] += g
    obj_avg = defaultdict(int)
    for i in sum.keys():
        for j in count.keys():
            obj_avg[i] = sum[i] / count[j]
    max_avg = 0
    for i in obj_avg.values():
        if i > max_avg:
            max_avg = i
    for i in obj_avg.keys():
        for j in obj_avg.values():
            if j == max_avg:
                return i


def calc_avg_score(dict: dict) -> float:
    sum = 0
    for i in dict.values():
        sum += i
    avg_score = sum / len(dict)
    return avg_score


def find_highest_avg_score(list:list):
    max_avg = [0,0]
    int_students = ''
    for i in list:
        if calc_avg_score(students[i]) > max_avg[1]:
            max_avg = (i,calc_avg_score(students[i]))
        elif calc_avg_score(students[i]) == max_avg[1]:
            int_students += "," + i
    if(int_students != 0):
        print(f'{max_avg[0]}{int_students} has maximum avg score:{max_avg[1]}')
    else:
        print(f'{max_avg[0]} has maximum avg score:{max_avg[1]}')


def main():
    student_name = input('Enter the required name ').title()
    try:
        if student_name in students.keys():
            print('')
        else:
            return
    except KeyError:
        print('Name not found')
    print(f'{calc_avg_score(students[student_name])}')
    find_highest_avg_score(list(students))
    print(f'Highest score object {get_highest_object(students)}')

if __name__ == '__main__':
    main()