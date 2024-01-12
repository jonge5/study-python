# 중복이 없고, 순서가 없다. -> 값을 가져올 수가 없다 : 값이 있는지 없는지 검사하기 위해서 사용

world_set = {'korea', 'america', 'japan', 'china'}  # 중괄호에 콤마로 연결되어있음
print(type(world_set))
print(len(world_set))
# print(world_set[1]) 오류남 순서X
world_set.add('korea')  # 중복된 값은 들어갈 수 없다.
print(world_set)  # set을 다른 자료구조로 바꿔서 가져오는 것이다.

# 중복된 값을 제거하기 위해서 사용한다.
datas = [1, 2, 2, 1, 3, 4, 2, 1, 2]
print(list(set(datas)))
print(set(list(datas)))


