from requests import get, post, delete, put
from pprint import pprint

# print(get('http://localhost:5000/api/jobs').json())
#
# print(get('http://localhost:5000/api/jobs/1').json())
#
# print(get('http://localhost:5000/api/jobs/999').json())
#
# print(get('http://localhost:5000/api/jobs/q').json())

# # пустой запрос
# print(post('http://localhost:5000/api/jobs').json())
#
# # не все поля указаны
# print(post('http://localhost:5000/api/jobs',
#            json={'job': 'Работа'}).json())
#
# # такой id уже существует
# print(post('http://localhost:5000/api/jobs',
#            json={'id': 1,
#                  'team_leader': '5',
#                  'job': 'gym',
#                  'work_size': 1,
#                  'collaborators': '2, 3, 4',
#                  'is_finished': False}).json())
#
# # верное добавление
# print(post('http://localhost:5000/api/jobs',
#            json={'id': 2,
#                  'team_leader': '5',
#                  'job': 'gym',
#                  'work_size': 1,
#                  'collaborators': '2, 3, 4',
#                  'is_finished': False}).json())
#
# # проверим, что работа добавилась
# pprint(get('http://localhost:5000/api/jobs').json())

# # верное добавление
# print(post('http://localhost:5000/api/jobs',
#            json={'id': 2,
#                  'team_leader': '5',
#                  'job': 'gym',
#                  'work_size': 1,
#                  'collaborators': '2, 3, 4',
#                  'is_finished': False}).json())
#
# # проверим, что работа добавилась
# pprint(get('http://localhost:5000/api/jobs').json())
#
# # работы с id = 999 нет в базе
# print(delete('http://localhost:5000/api/jobs/999').json())
#
# # верное удаление
# print(delete('http://localhost:5000/api/jobs/2').json())
#
# # проверим, что работа удалилась
# pprint(get('http://localhost:5000/api/jobs').json())

# пустой запрос
print(put('http://localhost:5000/api/jobs').json())

# не все поля указаны
print(put('http://localhost:5000/api/jobs', json={'job': 'Работа'}).json())

# такой id не существует
print(put('http://localhost:5000/api/jobs',
          json={'id': 999,
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

# верное изменение
print(put('http://localhost:5000/api/jobs',
           json={'id': 2,
                 'team_leader': '5',
                 'job': 'gym',
                 'work_size': 2,
                 'collaborators': '2, 3',
                 'is_finished': False}).json())

# проверим, что работа изменилась
pprint(get('http://localhost:5000/api/jobs').json())
