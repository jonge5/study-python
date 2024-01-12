def check(*, key: str, value: str) -> dict:  # check 함수를  dict형태로 key와 value값을 str 형태로 만들어준다
    for bank in Bank.banks:  # Bank클래스에 banks 리스트를 bank만큼 반복한다.
        for user in bank:  # bank에서 사용자만큼 반복한다.
            if user[key] == value:  # 사용자의 key값이 value와 같다면
                return user  # 사용자를 반환한다.

    return None  #사용자를 찾지 못하면 None을 반환한다.


class Bank:
    total_count = 3
    banks = [[] for i in range(total_count)]  # 은행들을 담을 리스트를 생성한다.

    def __init__(self, owner: str, account_number: str, phone: str, password: str, money: int):
        self.object = self  # 현재 객체를 설정한다?
        self.owner = owner  # 예금주 이름
        self.account_number = account_number  # 계좌 번호
        self.phone = phone  # 핸드폰 번호
        self.password = password  # 비밀번호
        self.money = money  # 통장 잔고

    @classmethod
    def open_account(cls, bank_choice, **kwargs):  # 은행에서 계좌를 개설하는 메서드
        user = [ShinHan, KookMin, KaKao][bank_choice - 1](**kwargs)  # 선택한 은행 객체를 생성한다.
        cls.banks[bank_choice - 1].append(user.__dict__)  # 해당 은행의 리스트에 계좌 정보를 추가한다.
        return user

    @staticmethod
    def check_account_number(account_number: str) -> dict:  # 계좌 번호에 해당하는 사용자 정보를 확인하는 정적 메서드이다.
        return check(key='account_number', value=account_number)  # check 함수로 계좌번호를 확인하고 리턴해준다.

    @staticmethod
    def check_phone(phone: str) -> dict:  # 핸드폰 번호에 해당하는 사용자 정보를 확인하는 정적 메서드이다.
        return check(key='phone', value=phone)  # 핸드폰 번호를 확인하고 리턴해준다.

    def deposit(self, money: int):
        self.money += money  # 입력된 금액만큼 통장 잔고에 추가한다.

    def withdraw(self, money: int):
        self.money -= money  # 입력된 금액만큼 통장 잔고에서 차감한다.

    def balance(self):
        return self.money  # 현재 통장 잔고를 리턴한다.

    def __str__(self):  # 객체를 문자열로 나타내기위한 메서드이다.
        return f'{self.owner}, {self.account_number}, {self.phone}, {self.password}, {self.money}'


class ShinHan(Bank):
    def deposit(self, money: int):  # 신한은행에 입금될 때 수수료를 적용한 메서드이다.
        money //= 2  # 절반만 입금된다.
        super().deposit(money)  # 부모 클래스의 입금 메서드를 호출한다.


class KookMin(Bank):
    def withdraw(self, money: int):  # 국민 은행에 출금될때 수수료가 적용된 메서드이다.
        money *= 1.5  # 출금금액에 1.5를 곱한다.
        super().withdraw(int(money))  # 부모클래스의 출금 메서드를 호출한다.


class KaKao(Bank):
    def balance(self):  # 카카오 계좌 잔액 조회시 잔액이 반으로 줄어드는 메서드
        self.money //= 2  # 잔고를 반으로 줄인다.
        return super().balance()  # 부모 클래스에서 잔액 조회메서드를 호출한다.
