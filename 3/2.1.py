from typing import List, Union


def multiply_elements(
    elements: List[Union[int, float]], multiplier: Union[int, float] = 2
) -> List[Union[int, float]]:
    return [element * multiplier for element in elements]


elements = [1, 2, 3, 4, 5]
print(multiply_elements(elements, 3))
print(multiply_elements(elements))
