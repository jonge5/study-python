# # [종합 실습]
# # 은행
# #    예금주
# #    계좌번호(중복 없음)
# #    핸드폰번호(중복 없음)
# #    비밀번호
# #    통장잔고
# #
# # 신한
# #    입금 시 수수료 50%
# # 국민
# #    출금 시 수수료 50%
# # 카카오
# #    잔액조회 재산 반토막
# #
# # 은행은 3개를 선언한다.
# # 모든 은행 고객을 관리하는 DB를 2차원 list로 선언한다.
# # 모든 은행은 출금, 입금, 잔액조회, 계좌개설, 계좌번호 중복검사, 로그인, 핸드폰 번호 중복검사 서비스가 있다.
# # 화면쪽 메뉴는 "계좌개설, 입금하기, 출금하기, 잔액조회, 계좌번호 찾기(새로운 계좌 설정, 핸드폰 번호로 서비스 이용가능), 나가기"로 구성되어 있다.
#
# def check(check_number, list_number):
#     if check_number not in list_number:
#         check_number.append(list_number)
#     else:
#         print('다시 입력하세요.')
#
#
# # 모든 은행은 출금, 입금, 잔액조회, 계좌개설, 계좌번호 중복검사, 로그인, 핸드폰 번호 중복검사 서비스가 있다.
# class Bank:
#     total_count = 3
#     banks = []
#
# # 은행
# # 예금주
# # 계좌번호(중복 없음)
# # 핸드폰번호(중복 없음)
# # 비밀번호
# # 통장잔고
#     def __init__(self, bank, account_holder, account_number, phone_number, password, account_balance):
#         self.banks = bank
#         self.account_holder = account_holder
#         self.account_number = account_number
#         self.phone_number = phone_number
#         self.password = password
#         self.account_balance = account_balance
#
#     # 계좌 개설
#     @classmethod
#     def open_account(cls, bank):
#         if bank == 'ShinHan':
#             bank.account_holder = ShinHan
#
#         if bank == 'KookMin':
#             bank.account_number = KookMin
#
#         if bank == 'KaKao':
#             bank.account_number = KaKao
#
#     # 계좌 번호 중복 검사
#     @staticmethod
#     def check_account_number(check):
#         check()
#
#     # 핸드폰 번호 중복 검사
#     @staticmethod
#     def check_phone(check):
#         check()
#
#     #  입금
#     def deposit(self, bank):
#         bank.append(bank.account_balance)
#
#     # 출금
#     def withdraw(self, bank):
#         bank.remove(bank.account_balance)
#
#     # 잔액 조회
#     def balance(self, bank):
#         bank.account_balance = self.account_balance
#
#     def __str__(self, bank):
#         return f'Bank: {self.bank}'
#
#
# class ShinHan(Bank):
#     ShinHan_bank = []
#
#     def __init__(self, account_holder, account_number, phone_number, password, account_balance):
#         self.account_holder = account_holder
#         self.account_number = account_number
#         self.phone_number = phone_number
#         self.password = password
#         self.account_balance = account_balance
#
# #    입금 시 수수료 50%
#     def deposit_fee(self, account_balance, deposit):
#             account_balance += deposit * 0.5
#
# class KookMin(Bank):
#     KookMin_bank = []
#
#     def __init__(self, account_holder, account_number, phone_number, password, account_balance):
#         self.account_holder = account_holder
#         self.account_number = account_number
#         self.phone_number = phone_number
#         self.password = password
#         self.account_balance = account_balance
#
#     # 출금 시 수수료 50%
#     def withdraw_fee(self, account_balance, withdraw):
#         account_balance -= withdraw * 0.5
#
# class KaKao(Bank):
#     KaKao_bank = []
#
#     def __init__(self, account_holder, account_number, phone_number, password, account_balance):
#         self.account_holder = account_holder
#         self.account_number = account_number
#         self.phone_number = phone_number
#         self.password = password
#         self.account_balance = account_balance
#
#     # 잔액조회 재산 반토막
#     def whitdraw_cut_in_half(self, bank):
#         bank.account_balance / 2
#
#
# if __name__ == '__main__':
#     bank_menu = "1. 신한 은행\n" \
#                 "2. 국민 은행\n" \
#                 "3. 카카오 뱅크\n" \
#                 "4. 나가기\n"
#
#     menu = "1. 개설\n" \
#            "2. 입금\n" \
#            "3. 출금\n" \
#            "4. 잔액\n" \
#            "5. 은행 선택 메뉴로 돌아가기\n"
#
#     owner_message = "예금주: "
#     account_number_message = "계좌번호: "
#     phone_message = "핸드폰 번호: "
#     password_message = "비밀번호(4자리): "
#     money_message = "예치금: "
#     deposit_message = "입금액: "
#     withdraw_message = "출금액: "
#     error_message = "다시 시도해주세요"
#
#     while True:
#         # 은행 메뉴
#         if __name__ == '__main__':
#             print(bank_menu)
#             if bank_menu == "1":
#                 pass
#         while True:
#             # 서비스 메뉴
#             pass
#

# 강사님 코드
# ============================================================================================================

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


if __name__ == '__main__':
    bank_menu = "1. 신한 은행\n" \
                "2. 국민 은행\n" \
                "3. 카카오 뱅크\n" \
                "4. 나가기\n"

    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 계좌 번호 재설정\n" \
           "6. 은행 선택 메뉴로 돌아가기\n"

    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요"

    while True:
        # 은행 메뉴
        bank_choice = int(input(bank_menu))  # 은행 메뉴에서 은행을 선택한다.
        if bank_choice == 4:
            break  # 4를 선택하면 프로그램을 종료한다.

        if bank_choice < 1 or bank_choice > len(Bank.banks):
            continue


        while True:
            # 서비스 메뉴
            menu_choice = int(input(menu))  # 서비스 메뉴에서 서비스를 선택한다.
            if menu_choice == 6:
                break  # 5를 선택하면 서비스 메뉴로 돌아간다.

            # 개설
            if menu_choice == 1:
                owner = input(owner_message)

                while True:
                    account_number = input(account_number_message)
                    if Bank.check_account_number(account_number) is None:
                        break  # 중복되지 않는 계좌번호를 입력받는다.

                while True:
                    phone = input(phone_message)
                    if Bank.check_phone(phone) is None:
                        break  # 중복되지 않는 핸드폰 번호를 입력받는다.

                while True:
                    password = input(password_message)
                    if len(password) == 4:
                        break  # 4자리 수의 비밀번호를 입력 받는다.

                money = int(input(money_message))
                # 입력한 정보로 새 계좌를 개설하고 해당 정보를 출력한다.
                user = Bank.open_account(bank_choice, owner=owner, account_number=account_number, phone=phone,
                                         password=password, money=money)
                print(user)

            # 입금
            # 개설한 은행에서만 입금 가능
            elif menu_choice == 2:
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:  # 사용자가 None이 아니고
                    if user['password'] == input(password_message):  # password가 일치하면
                        if isinstance(user.get('object'), ShinHan):
                            if bank_choice != 1:
                                print("개설한 은행에서만 입금 서비스를 사용하실 수 있습니다.")
                                continue



                        deposit_money = int(input(deposit_message))
                        user['object'].deposit(deposit_money)  # 해당 은행에 입금을 한다.

                else:
                    print(error_message)  # 아니면 error 메시지를 출력한다.

            # 출금
            elif menu_choice == 3:
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
                    if user['password'] == input(password_message):
                        withdraw_money = int(input(withdraw_message))
                        # 사용자의 object가 국민은행이면 출금 금액에 1.5배를 해주고 아니면 1배 해준다. 그 금액이 사용자 잔고보다 작으면
                        if withdraw_money * (1.5 if isinstance(user['object'], KookMin) else 1) <= user['money']:
                            user['object'].withdraw(withdraw_money)  # 출금이 가능하다.
                        else:
                            print(error_message)

                else:
                    print(error_message)

            # 잔액 조회
            elif menu_choice == 4:
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
                    if user['password'] == input(password_message):
                        print(f'현재 잔액: {user["object"].balance()}')  # 계좌의 잔액을 출력해준다.
                        continue

                else:
                    print(error_message)

            # 계좌 번호 재설정 기능
            # 핸드폰 번호와 비밀번호를 입력 받고,
            # 정확하면 해당 회원의 계좌번호를 재설정합니다 (다시 입력받음).
            elif menu_choice == 5:
                phone = input(phone_message)
                user = Bank.check_phone(phone)
                if user is not None:
                    if user['password'] == input(password_message):
                        while True:
                            account_number = input(account_number_message)
                            if Bank.check_account_number(account_number) is None:
                                break
                        user.get('object').account_number = account_number
                        continue

                print('핸드폰 번호 혹은 비밀번호를 다시 확인해주세요.')

            else:
                print(error_message)


