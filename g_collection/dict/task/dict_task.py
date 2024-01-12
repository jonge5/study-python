# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
data_dict = {}

title = "또와 과일"
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

result_message = ""
append_error_message = "추가 실패(중복된 상품명)"
update_error_message1 = "수정 실패(존재하지 않는 상품명)"
update_error_message2 = "수정 실패(중복된 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."

while True:
    # 사용자에게 메뉴를 보여주고 선택한 번호를 choice에 저장
    choice = int(input(title + '\n' + menu))

    # 추가
    if choice == 1:
        # 사용자에게 상품명과 가격을 동시에 입력받는다(구분점은 공백문자).
        new_name, new_price = input(append_message).split()
        # 입력한 상품명이 기존 상품과 중복되지 없다면,
        if new_name not in data_dict:
            data_dict[new_name] = int(new_price)
            continue
        else:
            # 입력한 상품명이 기존 상품과 중복되었다면,
            # 알맞은 메세지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
            result_message = append_error_message

    # 수정
    elif choice == 2:
        # 수정할 상품의 이름을 입력합니다.
        name = input(search_name_message_for_update)
        # 목록에 해당 상품이 있는 경우에는,
        if name in data_dict:
            new_name, new_price = input(update_message).split()
            if new_name not in data_dict:
                del data_dict[name]
                data_dict[new_name] = int(new_price)
                continue
            else:
                data_dict[new_name] = int(new_price)
        else:
            # 업데이트할 상품이 목록에 없는 경우 error_message1를 출력합니다.
            result_message = update_error_message1

    # 삭제
    elif choice == 3:
        # 삭제할 상품의 이름을 입력합니다.
        name = input(delete_message)
        # 목록에 해당 상품이 있는 경우
        if name in data_dict:

            del data_dict[name]

            continue

        else:
            # 삭제할 상품이 목록에 없는 경우 아래 메시지를 출력합니다.
            result_message = delete_error_message

    # 검색
    elif choice == 4:
        # 검색 메뉴를 선택합니다.
        choice = int(input(search_menu))

        # 상품명으로 검색
        if choice == 1:
            # 검색할 상품의 이름을 입력합니다.
            keyword = input(search_name_message)
            # 목록에 해당 상품이 있는경우
            if keyword in data_dict:
                for name, price in data_dict.items():
                    if keyword == name:
                        print(f'{name}, {price}')
                continue

            else:
                # 검색할 상품이 없는 경우 search_name_error_message를 출력합니다
                result_message = search_name_error_message

        # 가격으로 검색
        elif choice == 2:
            check = False
            # 검색할 가격을 입력합니다.
            price = int(input(search_price_message))
            # 최소값을 계산한다.
            min = price * 0.5
            # 최대값을 계산합니다.
            max = price * 1.5
            # 가격 범위 내에서 상품의 인덱스를 찾습니다.
            for name, price in data_dict.items():
                if min <= price <= max:
                    check = True
                    print(f'{name}, {price}')

            if check:
                continue

            if not check:
                result_message = search_error_message

    # 목록
    elif choice == 5:
        # 상품 목록이 비어있는 경우에
        if len(data_dict) == 0:
            # 목록이 비어있음을 알려줍니다.
            result_message = no_item_message
            continue
        else:
            # 아닌 경우
            for name, price in data_dict.items():
                # 상품명과 가격을 출력합니다.
                print(f'{name}, {price}')


    # 나가기
    elif choice == 6:
        # 반복문을 종료하고 나갑니다.
        break

    # 그 외
    else:
        result_message = error_message
    # result_message로 일괄처리해서 출력한다.
    print(result_message)
    # 다음 반복을 위해 결과 메세지를 초기화 합니다.
    result_message = ""


