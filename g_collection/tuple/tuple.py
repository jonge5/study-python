# mutable: 변할 수 있는
data_list1 = [1, 2, 3, 4]
data_list2 = data_list1
data_list2[0] = 10
print(data_list2)
print(data_list1)


# immutable : 변할 수 없는
data_tuple1 = (1, 2, 3, 4)
data_tuple2 = data_tuple1

test = list(data_tuple2)
test[0] = 10
print(test)

data_tuple2 = data_tuple1 + (5, 6)
print(data_tuple2)
print(data_tuple1)

datas = 1, 2   # ()없이 사용할 수 있음
print(type(datas))
print(datas[0])

# 다른 개발자들이 만들어놓은 것을 이해하기 위해서 알아야됨. (튜플이라서 수정이 안는되구나)

ERROR_CODE = 1,
print(type(ERROR_CODE))  # 개발자들 끼리 약속 : 대문자는 값을 변경할 수 없는 값이다.



