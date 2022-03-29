id = input('아이디를 입력해주세요.')
pw = input('비밀번호를 입력해주세요.')
if id == 'pyeonne':
    if pw == '1234':
        print(f'{id}님 안녕하세요!')
    else:
        print('비밀번호가 다릅니다.')
else:
    print('누구임?')