# f(x) = 2x+1

# def 함수명(매개변수, ...):
#     실행할 문장
#     return 리턴값

# def f(x):
#     return 2 * x + 1
#
# result = f(2)
# print(result)

# 두 정수의 곱셈 함수
def f(num1, num2):
    return num1 * num2

result = f(2, 3)
print(result)

# 두 정수의 나눗셈 후 몫과 나머지 구하는 함수
def divide(number1, number2):
    if number2 != 0:
        return number1 // number2, number1 % number2
    return None

result = divide(10, 3)
if result:
    value, rest = result
    print(f'몫: {value}, 나머지: {rest}')
else:
    print('0으로 나눌 수 없습니다.')

# 1~10까지 print()로 출력하는 함수
def print_from1_to10():
    for i in range(10):
        print(i + 1, end=' ')

print_from1_to10()


# 이름을 n번 print()로 출력하는 함수
def print_from1_to10():
    for i in range(10):
        print(i + 1, end=' ')


# # 1~n까지의 합을 구해주는 함수
def sum(x):
    total = 0
    for i in range(x):
        total += i + 1
    return total
result = sum(4)
print(result)


# 1~100까지 중 n의 배수를 print()로 출력하는 함수
def print_time_from1_to100(time):
    for i in range(100):
        if (i + 1) % time == 0:
            print(i + 1)

# 세 정수의 뺄셈 함수
def subtract(num1,num2,num3):
    return num1 - num2 - num3
result = subtract(4,2,-4)
print(result)

# 문자열을 입력받고 원하는 문자의 개수를 구해주는 함수
def get_count_of_result(target, keyword):
    # return len([i for i in target if i == keyword])
    count = 0
    for i in target:
        if i == keyword:
            count += 1
    return count


'''
    문자열과 문자를 입력받은 뒤 해당 문자가 몇 번째 인덱스에 있는 지 검사하고,
    만약 해당 문자가 없으면 -1을 리턴하는 함수
'''

message1 = '문자열을 입력하세요.'
message2 = '문자를 입력하세요.'

string_1 = input(message1)
string_2 = input(message2)

def check_string(string_1, string_2):
    return string_1.find(string_2)

print(check_string(string_1, string_2))

