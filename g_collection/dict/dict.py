student = {
    "name": "한동석",
    "email": "tenhan@gmail.com"
}

print(student['name'])
print(student.get('name'))

# get()을 사용하면 key를 찾지 못했을 때 원하는 default 값으로 설정이 가능하며,
# default 값이 없을 때에는 None을 가져온다.
# print(student['phone']) # 오류
print(student.get('phone', '01012345678'))

# 'name' key 값이 이미 있기 때문에, 아래의 코드는 수정이다.
student['name'] = '홍길동'
print(student)

# 'phone' key 값이 없기 때문에, 아래의 코드는 '추가'이다.
student['phone'] = '01012345678'
print(student)

if 'email' in student:  # 수정
    student['email'] = 'hgd1234@gmail.com'
else:  # 추가
    student['email'] = 'hgd1234@gmail.com'

print(student)


my_dict = {
    1: '한동석',
    'two': '20살',
    False: [10, 20, 30],
    "row": [
        {'name': "ted", "age": 40},
        {'name': "jack", "age": 30},
        {'name': "john", "age": 20},
    ]
}

# row에 있는 회원 3명의 정보 출력
if "row" in my_dict:
    # print(type(my_dict["row"]))
    for data in my_dict["row"]:
        print(f'{data["name"]}: {data["age"]}')

# 1~10까지 중 홀수와 짝수가 있다.
# 사용자가 '짝수'를 입력하면 짝수만 출력하고
# '홀수'를 입력하면, 홀수만 출력한다.
# dict를 사용한다.

num_dict = {
    "홀수": [i * 2 + 1 for i in range(5)],
    "짝수": [(i + 1) * 2 for i in range(5)]
}

print(','.join(map(str, num_dict[input('짝수 혹은 홀수:')])))


student = {
    "name": "한동석",
    "email": "tenhan@gmail.com"
}
# key 분리
print(list(student.keys()))

# value 분리
print(list(student.values()))

# item 분리
print(list(student.items()))

for key, value in student.items():
    print(key, value)


