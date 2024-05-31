from typing import List, Union

multiply_elements_lambda = lambda elements, multiplier=2: [
    element * multiplier for element in elements
]


elements = [1, 2, 3, 4, 5]
print(multiply_elements_lambda(elements, 3))
print(multiply_elements_lambda(elements))
