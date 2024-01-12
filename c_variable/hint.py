from typing import List, Dict, Set, Tuple, Union, Final

data: Final[int] = 10
print(data)

class A:
    pass

class B:
    @staticmethod
    def test(data: Union[int, str], number: int | float, data1: A, datas: List[int], data_dict: Dict[int, str]) -> int:
        return 10

