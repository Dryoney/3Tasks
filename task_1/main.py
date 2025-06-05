import os
from collections import defaultdict
from typing import Literal

LOG_FILE_NAME = 'log.txt'


def get_logs_count() -> int:
    with open(LOG_FILE_NAME, 'rt') as file:
        return len(file.readlines())

Topics = Literal ['INFO','ERROR','WARNING']
def get_topic_count(topic: Topics) -> int:
    topic_counter = defaultdict(int)
    with open(LOG_FILE_NAME, 'rt') as file:
        while True:
            line = file.readline()
            if not line:
                break
            if line.find(topic) != -1:
                topic_counter[topic] += 1
    return topic_counter[topic]


def find_users() -> set:
    logged_users = set()
    with open(LOG_FILE_NAME, 'rt') as file:
        for line in file:
            if 'logged in' in line.lower():
                parts = line.split()
                username = parts[4]
                logged_users.add(username)
    return logged_users


def main():
    if os.path.exists(LOG_FILE_NAME):
        topic = 'ERROR'
        logs_count = get_logs_count()
        topic_count = get_topic_count(topic)
        print(f'Количество строк: {logs_count}')
        print(f'Количество {topic}(s) {topic_count}')
        users = find_users()
        for user in users:
            print(user)
    else:
        print('Файл не найден')



if __name__ == '__main__':
    main()
