from bank_module import *
from message_module import *

if __name__ == '__main__':
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
