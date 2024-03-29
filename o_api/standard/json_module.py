import json

data = {'name': '책', 'price': 25_000, 'stock': 55}
print(data)


# ditc를 json으로 변환
# ensure_ascii: 한글을 유니코드가 아닌 원본으로 출력
# indent: 보기 좋게 바꿔주며, 전달한 값을 들여쓰기 공백 개수이다.
json_data = json.dumps(data, ensure_ascii=False, indent=4)
print(json_data)


# json을 dict로 변환
data_dict = json.loads(json_data)
print(data_dict)
