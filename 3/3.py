from typing import List, Union, Any

def function_name(search: str, status: bool, *args: Any, **kwargs: Any) -> Union[List[int], str]:
    result: List[int] = []
    result_2: str = ""
    
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f" {i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += f" Key: {k}, Value: {v}; "
        return result_2
    else:
        raise ValueError("Error for search")

# Пример использования функции:
print(function_name("args", True, 1, 2, "three", 4.0, 5))  # Вывод: [1, 2, 5]
print(function_name("args", False, 1, 2, "three", 4.0, 5))  # Вывод: " 1 2 three 4.0 5"
print(function_name("kwargs", False, key1="value1", key2="value2"))  # Вывод: " Key: key1, Value: value1;  Key: key2, Value: value2; "
