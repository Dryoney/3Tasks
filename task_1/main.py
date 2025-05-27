LOG_FILE_NAME = 'log.txt'


def count_lines():
    with open(LOG_FILE_NAME, 'rt') as file:
        return len(file.readlines())


def count_topic(topic):
    topic_counter = 0
    with open(LOG_FILE_NAME, 'rt') as file:
        while True:
            line = file.readline()
            if not line:
                break
            if line.find(topic) != -1:
                topic_counter += 1
    return topic_counter


def find_users():
    logged_users = set()
    with open(LOG_FILE_NAME, 'rt') as file:
        for line in file:
            if 'logged in' in line.lower():  # Проверяем наличие фразы в строке.
                parts = line.split()  # Разделяем строку на части.
                username = parts[4]
                logged_users.add(username)
    return logged_users


def main():
    try:
        open(LOG_FILE_NAME, 'rt')
    except FileNotFoundError:
        print('Файл не найден')
    topic = 'ERROR'
    print(f'Количество строк: {count_lines()}')
    print(f'Количество {topic}(s) {count_topic(topic)}')
    users = find_users()
    for user in users:
        print(user)


if __name__ == '__main__':
    main()
