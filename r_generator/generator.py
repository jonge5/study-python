# import os
# import psutil
#
# process_object = psutil.Process(os.getpid())
# momory_before = process_object.memory_info().rss / 1024 / 1024
#
# data_list = [i ** 2 for i in range(100)]
# print(data_list)
#
# memory_after = process_object.memory_info().rss / 1024 / 1024
# print({f'memory: {momory_before} -> {memory_after}'})
#
# # ===========================================================================
#
# momory_before = process_object.memory_info().rss / 1024 / 1024
#
# data_generator = (i ** 2 for i in range(100))
# print(next(data_generator))
#
# memory_after = process_object.memory_info().rss / 1024 / 1024
# print({f'memory: {momory_before} -> {memory_after}'})

def increase(number: int = 0):
    while True:
        number += 1
        yield number # 리턴의 기능

result = increase()
while True:
    data = input("Y/n >> ")
    if data == "Y":
        print(next(result))
    else:
        break