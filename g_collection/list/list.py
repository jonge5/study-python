# animals = ["dog", "cat", "bird", "fish"]
# print(animals)
# print(type(animals))
#
# # 인덱스로 접근
# print(animals[1])
# print(animals[2])
#
# # 음수 인덱스 기능(가장 마지막부터 순서대로 앞으로 이동한다.)
# print(animals[-1])
# print(animals[-2])
#
# # len()
# print(len(animals))
#
# # append()
# animals.append("hamster")
# print(len(animals))
# print(animals)
#
# animals.append("cat") #list는 중복을 신경쓰지 않는다.
# print(animals)
#
# # insert()
# animals.insert(1, "dog")
# print(animals)
#
# # remove()
# animals.remove('fish')
# print(animals)
#
# # del()
# del animals[1]
# print(animals)
#
# # claer()
# # animals.clear()
# # print(animals)
#
# # index()
# print(animals.index('bird'))
# # print(animals.index('tiger'))
#
# # 수정
# index = animals.index('bird')
# animals[index] = 'lion'
# print(animals)
#
# # 그 외
# animals = ["dog", "cat", "bird", "fish"]
# print(animals * 2)
#
# print("dog" in animals) #이런식으로 검색해도 된다.
# print("tiger" in animals)
#
# for animal in animals:
#     print(animal, end='')
#
#
# 실습
# 1~90까지 list에 담고 출력
# list1 = list(range(1, 91))
# print(list1)
#
# ===================강사님 코드==========================
# number_list = [0] * 90
# for i in range(len(number_list)):
#     number_list[i] = i + i
#
#
# 1~100까지 중 짝수만 list에 담고 출력
# list1 = list(range(2,101,2))
# print(list1)
#
# ===================강사님 코드==========================
# number_list = [0] * 50
#
# for i in range(len(number_list)):
#     number_list[i] = (i + 1) * 2
# print(number_list)
#
#
# 1~10까지 list에 담은 후 짝수만 출력
# ===================강사님 코드==========================
# number_list = []
# for i in range(10):
#     number_list.append(i + 1)
#
# print(number_list)
# even_list = [0] * (len(number_list) / 2)
# even_list = []
# for i in range(len(number_list)):
#     if number_list[i] % 2 == 0:
#         even_list.append(number_list[i])
#
# print(even_list)
#
#
#
# 4명의 회원 정보를 list에 담은 뒤 두번째 회원의 이름을 변경하고 마지막 회원은 삭제
#
# information_mumber = ['홍길동', '김수빈', '조은종', '안효성']
# information_mumber[1] = '황수빈'
# del information_mumber[3]
# print(information_mumber)
#
# ===================강사님 코드==========================
# 1. 두번째 회원의 이름 수정
# 2. 마지막 회원 삭제
#
# names = ['한동석', '홍길동', '이순신', '장보고']
# # 1.
# names[1] = '서경덕'
# print(names)
#
# # 2.
# # names.remove(names[-1])
# # print(names)
#
# del names[-1]
# print(names)
#
# # list안에 list
# number_list = [[1, 3, 5], [2, 4, 6]]
# # print(number_list[0][0])
#
# for i in range(len(number_list)):
#     for j in range(len(number_list[i])):
#         print(number_list[i][j])
#
