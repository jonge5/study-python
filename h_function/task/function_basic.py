# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupon, count)를 전달받은 뒤,
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.

# 주문 금액 pay
#
# 쿠폰의 할인율 coupon
#
# 쿠폰 개수 count
#
# 1. coupon을 pay에 순차 적용하는 함수 제작
#
# 2. 할인율이 적용된 금액(discounted_price)은 정수로 리턴 된다.
#
# 조건
# 할인율은 백분율
# 쿠폰 개수 > 주문 개수
# comprehension을 사용

# 입력 예시1
# [2000, 4000, 5000]
# coupon=50
# count=2

# 출력 예시1
# [1000, 2000]

# 입력 예시2
# [1000, 4000, 5000]
# coupon=30
# count=100

# 출력 예시2
# [700, 2800, 3500]

# def coupon_used(*args, **kwargs):
#     # 주문 금액 리스트를 만든다.
#     pay = args[0]
#     # args의 길이가 1보다 크면 두번째 위치 args를 할인율로, 아니면 kwargs에서 coupon의 키값을 할인율로 설정한다.
#     coupon = args[1] if len(args) > 1 else kwargs.get('coupon', 0)
#     # args의 길이가 2보다 크면 세번쨰 위치 args를 할인율로, 아니면 kwargs에서 coupon의 키값을 주문 개수로 설정한다.
#     count = args[2] if len(args) > 2 else kwargs.get('count', len(pay))
#
#     discounted_prices = []   # 할인율이 적용된 금액의 리스트를 만들어준다.
#     discounted_prices = [int(price * (1 - (coupon / 100))) for price in pay[:count]]  # price에 할인율을 적용해 준다.
#
#     return discounted_prices
#
# # 입력 예시
# pay = [7000, 4000, 5000]
# coupon = 30
# count = 2
#
# result = coupon_used(pay, coupon, count)
# print(result)



# 강사님 코드
# =====================================================================================================================
def use_coupon(*pay, **kwargs):
    '''

    :param pay: 주문 금액들
    :param kwargs: {coupon: 할인율, count: 쿠폰의 개수}
    :return: 할인율이 적용된 주문 금액들
    '''
    if 'coupon' in kwargs:
        return [
            int((1 - kwargs.get('coupon') * 0.01) * pay[i])
            for i in
            range(kwargs.get('count') if kwargs.get('count') <= len(pay) else len(pay))
        ]

    return None


help(use_coupon)
result = use_coupon(1000, 2000, 3000, coupon=50, count=100)

if result:
    print(result)
else:
    print('쿠폰이 없습니다.')

