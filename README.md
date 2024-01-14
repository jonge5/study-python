# Python - 프로그래밍 언어

- **컴퓨터와 소통하기 위해 사용하는 언어**입니다.
- **소스코드**는 명령어를 작성해 놓은 것으로, 개발자와 컴퓨터가 소통할 내용을 글로 작성해 놓은 것입니다.

## 주요 용어

### 소스코드
- 명령어를 작성해 놓은 것.

### 소스파일
- 소스코드가 작성되어 있는 파일.

### 컴파일
- 사람의 언어를 컴퓨터 언어로 바꿔주는 작업.

### 컴파일러
- 컴파일을 해주는 프로그램 또는 명령어.

### 인터프리터
- 인터프리트를 해주는 프로그램 또는 명령어.
- 파이썬은 인터프리터 안에 컴파일러를 내장하고 있습니다.

## 프로그램

### 일반 프로그램
```
프로그램
OS(운영체제): 하드웨어에 적절한 전기신호를 흘려주는 역할.
하드웨어
```

### Python 프로그램
```
프로그램
PVM: Python 프로그램을 OS에 맞게 번역한다.
OS(운영체제): 하드웨어에 적절한 전기신호를 흘려주는 역할.
하드웨어
```

- Python 프로그램은 이식성이 좋습니다.

## 콘솔, 터미널, 쉘

### 콘솔
- 개발자가 내 컴퓨터(로컬)와 직접 소통할 수 있는 입출력장치(입력: 키보드, 출력: 모니터).

### 터미널
- 내 컴퓨터(로컬)뿐만 아니라 다른 컴퓨터에 원격으로도 접속할 수 있는 콘솔을 구현한 프로그램.

### 쉘
- 명령어 해석기.

- **서식문자**를 사용하여 변수나 값을 따옴표 안에서 사용해야 합니다.

```python
print("서식문자 예시: %d, %f, %s" % (10, 3.14, "Hello"))
```

## 변수와 자료형

- **변수**는 값을 담는 저장공간입니다.
- **자료형**은 저장공간의 종류를 나타냅니다.
- Python은 동적 바인딩을 지원하며, 값에 따라 자료형이 동적으로 결정됩니다.

### 자료형(type)과 값의 예시
- 정수(int): 0, 10, -187, ...
- 실수(float): 0.0, 10.58, -77.568, ...
- 문자열(str): '0', "0.0", """한동석""", '''Python''', ...
- 리스트(list): [1, 2, 3], [0], [3,], ...
- 튜플(tuple): (1, 2), (), 1, 2, 3, (1,), ...
- 딕셔너리(dict): {key:value,}, ...
- 집합(set): {1, 2, 3}, {1}, ...
- 불린(bool): True, False

## 변수명 주의사항

- 변수명은 문자로 시작해야 합니다.
- 특수문자는 사용할 수 없습니다. 단, _는 허용됩니다.
- 변수명은 소문자로 시작해야 합니다.
- 공백을 사용할 수 없습니다.
- 되도록 한글은 사용하지 않도록 합니다.
- 명사로 사용하고 뜻이 있는 단어를 선택합니다.

## 변수의 선언과 사용

1. **선언**: 대입 연산자를 사용하여 변수에 값을 할당합니다. (값으로 보지 말 것!)
2. **사용**: 대입 연산자 없이 변수를 참조하여 사용합니다.

## 표기법

- 파스칼 표기법(PascalCase): 대문자로 시작하고 이어지는 단어의 시작도 대문자로 작성합니다.
- 카멜 표기법(camelCase): 소문자로 시작하고 이어지는 단어의 시작은 대문자로 작성합니다.
- 스네이크 표기법(snake_case): 단어 사이에 언더스코어(_)를 사용합니다.
- 케밥 표기법(kebab-case): 단어 사이에 하이픈(-)을 사용합니다.

## 서식문자

- 서식문자는 따옴표 안에서 변수나 값을 사용해야 할 때 사용합니다.

```python
print("서식문자 예시: %d, %f, %s" % (10, 3.14, "Hello"))
```

## 변수를 사용하는 이유

1. 반복되는 값을 쉽게 관리하고자 할 때
2. 값에 의미 부여를 할 때 (자료구조)

## 알고리즘과 자료구조

1. **알고리즘이란** 문제가 발생했을 때 해결할 수 있는 절차입니다.
   - 예: 두 정수의 합을 출력하는 알고리즘.

   ```python
   # 알고리즘 예시
   num1 = 3
   num2 = 1
   result = num1 + num2
   print("두 정수의 합:", result)
   ```

2. **자료구조란** 의미 없는 값을 하나의 정보로 변환하고 이

는 저장공간의 종류를 의미합니다.
   - 예: 리스트를 사용하여 여러 정수를 빠르게 가져오는 서비스 제작.

   ```python
   # 자료구조 예시
   numbers = [1, 2, 3]
   for num in numbers:
       print(num)
   ```

## 형변환

- `bin()`, `oct()`, `hex()`, `int()`, `float()`, `str()`, `bool()` 등의 함수를 사용하여 형변환이 가능합니다.

## 연산자

1. **산술 연산자**

   | 연산자 | 예시   | 설명          |
   | ------ | ------ | ------------- |
   | +      | 3 + 5  | 더하기        |
   | -      | 3 - 5  | 빼기          |
   | *      | 3 * 5  | 곱하기        |
   | /      | 3 / 5  | 나누기        |
   | **     | 3 ** 5 | 제곱          |
   | //     | 3 // 5 | 몫            |
   | %      | 3 % 5  | 나머지        |

2. **대입(allocation) 연산자**

   ```python
   data = 10  # 좌항에 우항을 대입
   data += 10  # data = data + 10
   data -= 10  # data = data - 10
   data *= 10  # data = data * 10
   data /= 10  # data = data / 10
   ```

3. **비교 연산자**

   ```python
   data == 10  # 같으면 True, 같지 않으면 False
   data != 10  # 같지 않으면 True, 같으면 False
   data > 5    # 보다 크다
   data < 5    # 보다 작다
   data >= 5   # 이상
   data <= 5   # 이하
   ```

4. **논리 연산자**

   ```python
   a == b and c == d  # 조건식 둘 다 True일 경우 True
   a == b or c == d   # 조건식 둘 중 하나라도 True일 경우 True
   not (a == b)        # True를 False로, False를 True로 변경
   ```

5. **멤버 연산자**

   ```python
   "a" in "abc"       # 좌항이 우항에 포함되었다면 True, 아니면 False
   2 in [1, 2, 3]     # 좌항이 우항에 포함되었다면 True, 아니면 False
   "a" not in "abc"   # 좌항이 우항에 포함되어 있지 않다면 True, 포함되면 False
   2 not in [1, 2, 3] # 좌항이 우항에 포함되어 있지 않다면 True, 포함되면 False
   ```

6. **식별 연산자**

   ```python
   a is b             # 두 객체 모두 같은 주소일 경우 True, 아니면 False
   a is not b         # 두 객체 모두 같은 주소일 경우 True, 아니면 False
   ```

## 입력과 제어문

- **입력 상태**: 커서가 깜빡이고 있는 상태, 항상 입력 전에 출력을 해서 사용자가 정확한 값을 입력할 수 있도록 합니다.
- **입력 함수**: `input()` 함수를 사용하여 사용자로부터 입력을 받습니다.

```python
user_input = input("출력할 메세지: ")
print("사용자 입력:", user_input)
```

## 제어문

### 조건문 (if문)

1.
   ```python
   if 조건식:
       실행할 문장
   if 조건식:
       실행할 문장
   if 조건식:
       실행할 문장
   ```

2.
   ```python
   if 조건식:
       실행할 문장
   elif 조건식:
       실행할 문장
   else:
       실행할 문장
   ```

### 반복문

#### for문

```python
for 변수명 in range(inclusive_start, exclusive_end, step):
    실행할 문장
```

#### while문

```python
while 조건식:
    실행할 문장
```

## **Dictionary (dict)**

- 한 쌍으로 저장되어 관리
- 두 개의 자료구조가 합쳐져서 만들어짐
- `len()`를 사용하면 한 쌍을 1로 카운트
- 키 값은 중복이 불가능하지만 값은 중복이 가능
- 키 값을 주면 그 키의 값을 가져옴

### Dictionary 선언

```python
dict_name = {key1: value1, key2: value2, ...}
```

### Dictionary 사용

- **추가, 수정**
  ```python
  dict_name[key] = value
  ```
  키 값이 기존에 있으면 수정, 없으면 추가

- **삭제**
  ```python
  del dict_name[key]
  ```

- **검사**
  ```python
  key in dict_name  # 키가 있으면 참
  key not in dict_name  # 키가 없으면 참
  ```

## **List**

- 여러 개의 저장공간이 나열된 것

### 사용 목적

1. 여러 번 선언하지 않고 한 번만 선언하기 위해
2. 규칙성 없는 값에 규칙성을 부여하기 위해 사용

### List 선언

- 어떤 값을 넣을 지 알 때
  ```python
  list_name = [value1, value2, ...]
  ```

- 어떤 값인 지는 모르지만, 칸 수는 알 때
  ```python
  list_name = [value] * count  # 몇 개의 값인지 알고 있는 경우
  ```

- 어떤 값인 지 모르고, 칸 수도 모를 때
  ```python
  list_name = []
  ```

### List 길이

```python
len(list_name)
```

### List 사용

```python
data_list = [1, 2, 3]

- **값 넣기 (추가)**
  ```python
  list_name.append(value)
  ```

- **값 넣기 (삽입)**
  ```python
  list_name.insert(index, value)
  ```

- **값 삭제**
  ```python
  list_name.remove(value)  # 중복 시 먼저 나온 값(낮은 인덱스 값)이 삭제
  del list_name[index]  # 인덱스로 삭제
  list_name.clear()  # 모든 값 삭제

- **값 검색**
  ```python
  list_name.index(value)  # 값이 들어 있는 저장공간의 인덱스 번호, 중복 시 먼저 나온 값의 인덱스 번호
  ```

- **값 수정**
  ```python
  list_name[index] = new_value
  ```

## **Collection - 자료구조**

- list: 인덱스
- tuple: 값을 수정할 수 없다.
- set: 중복 제거
- dict: 서버 간 데이터 교환

## **함수**

- 이름 뒤에 소괄호, 작성된 코드의 주소 값을 담고 있는 저장공간

```python
# 함수 선언
def function_name(parameters, ...):
    # 실행할 문장
    return return_value

# 함수 사용
function_name(value1, ...)
```

### **함수를 사용하는 목적**

1. 재사용
2. 간결화

### **매개변수 선언 방법**

1. **Packing(args)**
   여러 개의 값을 마구잡이로 받을 때 사용

2. **kwargs**
   여러 개의 값을 key=value 형식으로 받음

3. **Unpacking**
   매개변수에 *로 시작하면 kwargs 형식과 동일, 그냥 매개변수가 나열되어 있으면 값만 전달

## **클로저(Closure, 폐쇄)**

- 함수 안에 함수, 모듈화
- 함수가 정의된 시점의 변수를 기억하고, 이 변수를 나중에 참조 혹은 변경 가능
- 데이터 은닉과 지속성을 가지고 있다.

### **클로저 구현 코드**

```python
def outer(arg):
    local_variable = value

    def inner(arg):
        # read local_variable
        value = operate_something
        return value

    return inner
```

## **데코레이터(Decorator, 장식)**

- 주로 로직에만 집중할 수 있게 해주는 기능
- 보안, 로그, 트랜잭션, 예외처리와 같이 로직과 직접적인 관련이 없는 부분을 처리

### **데코레이터 동작 코드**

1. 
```python
def decorator_name(original_function):
    def wrapper_function(*args, **kwargs):
        enhanced_code = peripheral_logic
        original_function(enhanced_code)
    return wrapper_function
```

2. 
```python
def decorator_name(original_function):
    def wrapper_function(*args, **kwargs):
        peripheral_logic
        original_function(*args, **kwargs)
    return wrapper_function
```

## **클래스(Class) - 반**

- 공통 요소를 한 번만 선언

### **클래스 선언**

```python
class ClassName:
    # Fields (변수, 메소드)
```

### **클래스의 필드 사용**

1. 객체화 (instance)
   - 객체 (instance variable)를 만드는 작업. 추상적인 개념을 구체화
2. 생성자

### **생성자**

- 클래스 이름 뒤에 소괄호가 있는 형태. 메소드와 기능이 똑같지만 메소드라고 부르지 않음

### **기본 생성자**

- 매개변수가 없는 생성자. 클래스 선언 시 자동으로 선언됨. 사용자가 직접 생성자를 선언하면 자동으로 선언되지 않음.

### **self**

- 필드에 접근한 객체가 누구인지 알아야 해당 필드에 접근 가능. 객체가 가지고

 있는 필드의 주소값이 self에 자동으로 넘어감.

### **상속**

1. 기존에 선언된 클래스의 필드를, 새롭게 만들 클래스의 필드로 사용하고자 할 때
2. 겹치는 필드가 있을 경우 부모 클래스를 선언한 뒤 겹치는 필드를 구성하고 각 자식 클래스에 상속

### **상속 문법**

```python
class A:
    # A 필드

class B(A):
    # A, B 필드
```

- A: 부모 클래스, 상위 클래스, 슈퍼 클래스, 기반 클래스
- B: 자식 클래스, 하위 클래스, 서브 클래스, 파생 클래스

### **super().__init__()**

- 자식 객체로 부모 필드에 접근 가능. 자식 생성자만 호출하지만, 자식 생성자에는 항상 부모 생성자를 호출하기 때문에 자식 필드만 메모리에 할당된 것처럼 보임.
- 실제로는 자식 생성자 호출 시 부모와 자식 필드 모두 메모리에 할당됨. 부모 생성자 호출은 `super().__init__()`로 수행하며, 직접 작성하지 않아도 자동으로 추가됨.

### **오버라이딩(Overriding, 재정의)**

- 부모 필드에서 선언한 메소드를 자식 필드에서 수정하고자 할 때 사용
- 자식에서 부모 필드의 메소드와 동일한 이름으로 선언하는 문법
- 접근한 객체와 가까운 곳부터 찾기 때문에, 자식 필드에 해당 메소드가 있다면 재정의된 메소드가 실행됨.



## **매직 메소드**
클래스 안에 재정의할 수 있는 스페셜 메소드입니다.

| 연산자 | 메소드 | 설명 |
| --- | --- | --- |
| + | `__add__(self, other)` | 덧셈 |
| * | `__mul__(self, other)` | 곱셈 |
| - | `__sub__(self, other)` | 뺄셈 |
| / | `__truediv__(self, other)` | 나눗셈 |
| // | `__floordiv__(self, other)` | 몫 |
| % | `__mod__(self, other)` | 나머지 |
| ** | `__pow__(self, other[, modulo])` | 제곱 |
| >> | `__lshift__(self, other)` | 우쉬프트 |
| << | `__rshift__(self, other)` | 좌쉬프트 |
| & | `__and__(self, other)` | 논리곱 |
| ^ | `__xor__(self, other)` | 배타논리합 |
| \| | `__or__(self, other)` | 논리합 |
| += | `__iadd__(self, other)` | 누적 더하기 |
| -= | `__isub__(self, other)` | 누적 빼기 |
| *= | `__imul__(self, other)` | 누적 곱하기 |
| /= | `__idiv__(self, other)` | 누적 나누기 |
| //= | `__ifloordiv__(self, other)` | 누적 몫 |
| %= | `__imod__(self, other)` | 누적 나머지 |
| **= | `__ipow__(self, other)` | 누적 제곱 |
| >>= | `__irshift__(self, other)` | 누적 우쉬프트 |
| <<= | `__ilshift__(self, other)` | 누적 좌쉬프트 |
| &= | `__iand__(self, other)` | 누적 논리합 |
| ^= | `__ixor__(self, other)` | 누적 배타논리합 |
| \| = | `__ior__(self, other)` | 누적 논리합 |
| < | `__lt__(self, other)` | 작다(미만) |
| <= | `__le__(self, other)` | 작거나 같다(이하) |
| == | `__eq__(self, other)` | 같다 |
| != | `__ne__(self, other)` | 같지 않다 |
| > | `__gt__(self, other)` | 크다(초과) |
| >= | `__ge__(self, other)` | 크거나 같다(이상) |
| [i] | `__getitem__(self, index)` | 인덱스 연산자 |
| in | `__contains__(self, value)` | 멤버 확인 |
| len | `__len__(self)` | 요소 길이 |
| str | `__str__(self)` | 문자열 표현 |

- `__init__`: 생성자
- `__del__`: 소멸자
- `__new__`: 할당자
- `__repr__(self)`: `__str__`을 정의하지 않을 경우, `__repr__`이 대신 쓰인다. 객체를 표현(객체의 주소)하는 목적으로 사용한다.

# 모듈(부품)
변수와 함수, 클래스 등을 모아 놓은 파이썬 파일입니다.

## 모듈 사용
- `import [모듈명]`: 사용할 함수의 소속을 직접 코드에 작성하고 모든 필드를 사용하고자 할 때
- `import [모듈명] as [사용할 이름]`: 모듈명이 길거나 복잡할 때 원하는 이름으로 설정해서 사용
- `from [모듈명] import [필드명,...]`: 모듈명을 직접 코드에 작성하지 않고 필드를 바로 사용하고자 할 때
- `from [모듈명] import*`: 모듈 안에 있는 모든 필드를 바로 사용하고자 할 때

# 패키지
폴더를 생성하여 .py 또는 .ipynb 파일을 관리하고자 할 때 해당 폴더를 패키지라고 합니다.
`__init__.py` 파일을 생성해야 패키지로 인식되지만, 상위 버전(3.3 부터)에서는 `__init__.py` 파일이 없어도 패키지로 인식됩니다.
하지만, 하위(3.3 미만)에서도 인식되기 위해서는 직접 생성해 놓는 것이 좋습니다.

**주의 사항:** 모듈을 사용할 파일의 이름이 모듈과 같으면 사용이 불가능합니다.

# API(Application Programming Interface)
선배 개발자들이 미리 작성해놓은 틀(소스코드)입니다.

1. **내부 API(기본 API)**
   - Python 설치 시 다운로드되었던 모듈. 바로 사용할 수 있는 API.
   
2. **외부 API**
   - 해당 기업에서 배포한 코드를 다운로드 받은 뒤 사용할 수 있는 모듈. 기본으로 제공되지 않는 API.

# 예외 처리
프로그램 실행 중 오류 발생 시 강제 종료되기 때문에 이를 막기 위하여 예외 처리를 작성합니다.

**try, except 문**

1. 
```python
try:
    # 오류가 발생할 수 있는 문장
except 발생오류 as 오류객체:
    # 오류 발생 시 실행할 문장
```

2. 
```python
try:
    # 오류가 발생할 수 있는 문장
except 발생오류:
    # 오류 발생 시 실행할 문장
```

3. 
```python
try:
    # 오류가 발생할 수 있는 문장
except:


    # 오류 발생 시 실행할 문장
finally:
    # 오류 발생 여부와 상관없이 실행
```

**예외 발생시키기**
심각한 문제가 발생하기 전에 일부러 프로그램을 강제 종료할 때 사용합니다. 예외를 한 곳에서 묶어서 처리하기 위해 사용합니다.

```python
raise 발생오류
```

**예외 만들기**
```python
class 오류명(Exception):
    def __str__(self):
        return "오류 메세지"
```

# 파일
외부에 파일을 생성하거나 내용을 작성할 수 있으며, 기존의 내용도 읽어올 수 있습니다.

**파일 생성하기**
파일을 열고 작성할 때 사용합니다. 'w'를 작성해서 운영체제에게 파일을 여는 목적을 알려줘야 하며, 이 때 'w'를 작성합니다.

```python
open(path, 'w')
```

**내용 추가하기**
기존의 내용을 없애지 않고, 아래에 내용을 추가합니다. 이 때에는 추가 모드인 'a'를 작성합니다.

```python
open(path, 'a')
```

**파일 읽기**
기존의 내용을 한 줄씩 읽어올 때 'r'을 작성하여 읽기 모드로 파일을 열어줍니다.

```python
open(path, 'r')
```

# 제너레이터(Generator)
한 번에 하나씩 구성 요소를 반환해주는 객체로, 대용량 데이터 및 많은 반복이 필요한 코드에서 메모리를 적게 사용할 수 있는 고성능 방법입니다. 필요할 때마다 하나씩 가져오기 때문에 무거운 객체를 다룰 때 사용됩니다.

# List Comprehension
```python
[operate for variable in range(end)]
```

# Generator Expression
```python
(operate for variable in range(end))
```

