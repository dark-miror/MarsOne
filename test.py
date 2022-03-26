from requests import get, post
from pprint import pprint

# print(get('http://localhost:5000/api/jobs').json())
#
# print(get('http://localhost:5000/api/jobs/1').json())
#
# print(get('http://localhost:5000/api/jobs/999').json())
#
# print(get('http://localhost:5000/api/jobs/q').json())

# пустой запрос
print(post('http://localhost:5000/api/jobs').json())

# не все поля указаны
print(post('http://localhost:5000/api/jobs',
           json={'job': 'Работа'}).json())

# такой id уже существует
print(post('http://localhost:5000/api/jobs',
           json={'id': 1,
                 'team_leader': '5',
                 'job': 'gym',
                 'work_size': 1,
                 'collaborators': '2, 3, 4',
                 'is_finished': False}).json())

# верное добавление
print(post('http://localhost:5000/api/jobs',
           json={'id': 2,
                 'team_leader': '5',
                 'job': 'gym',
                 'work_size': 1,
                 'collaborators': '2, 3, 4',
                 'is_finished': False}).json())

# проверим, что работа добавилась
pprint(get('http://localhost:5000/api/jobs').json())
