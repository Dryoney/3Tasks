import re
def count_lines():
    with open('log.txt','rt') as log:
        lines = log.readlines()
        print(str(len(lines))+": количество строк")
def count_errors():
    with open('log.txt','rt') as log:
        counter_errors = 0
        while True:
            line = log.readline()
            if not line:
                break
            if line.find('ERROR') != -1:
                counter_errors += 1
        print('Количество ошибок:'+str(counter_errors))
def find_users():
    logged_users = set()
    with open('log.txt','rt') as file:
        for line in file:
            if "logged in" in line:  # Проверяем наличие фразы в строке
                parts = line.split()  # Разделяем строку на части
                username = parts[4]
                logged_users.add(username)
    return logged_users
def main():
    count_lines()
    count_errors()
    users = find_users()
    for user in users:
        print(user)
if __name__ == "__main__":
    main()