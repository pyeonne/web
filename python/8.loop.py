members = ['egoing', 'duru']
for member in members:
    print('member', member)
    
members2 = [
    ['egoing', 'seoul', 'programmer'],
    ['duru', 'daegu', 'dba']
]
print(members2[0][0])
for member in members2:
    for info in member:
        print(info)

egoing1 = ['egoing', 'seoul', 'programmer']
egoing2 = {'name': 'egoing', 'city': 'seoul', 'job': 'programmer'} # 사전형
print(egoing2['city'])
for name in egoing2:
    print(egoing2[name])
    
members3 = [
    {'name': 'egoing', 'city': 'seoul', 'job': 'programmer'},
    {'name': 'duru', 'city': 'daegu', 'job': 'dba'}
]
for member in members3:
    for value in member:
        print(member[value])

def sum(a, b):
    return a + b
print(f'result: {sum(10, 20)}')

todo_list = list(map(str, input('할일을 입력해주세요').split()))
print(todo_list)

