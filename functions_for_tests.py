def filter_positive_even_numbers(numbers: list[int]) -> list[int]:

    if not isinstance(numbers, list):
        raise TypeError('Not list')
    
    result = []

    for num in numbers:
    
        if isinstance(num, bool) or isinstance(num, str):    
            raise ValueError(f"All elements must be integers, got {type(num).__name__}")
        
        if not isinstance(num, int):
            continue
        
        if num > 0 and num%2 == 0:
            result.append(int(num))


    return result    

def merge_and_count(dict1: dict, dict2: dict) -> dict:

    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise TypeError('Not list')
    
    for key,val in dict1.items():
    
        if not isinstance(key, str):    
                raise ValueError(f"Keys must be str, got {type(key).__name__}")
        if not isinstance(val, int):    
                raise ValueError(f"Value must be int, got {type(val).__name__}")
    
    result = dict1.copy()
    
    for key,val in dict2.items():
    
        if not isinstance(key, str):    
                raise ValueError(f"Keys must be str, got {type(key).__name__}")
        if not isinstance(val, int):    
                raise ValueError(f"Value must be int, got {type(val).__name__}")
        
        if key in result:
            result[key] += val
        else:
             result[key] = val    

    return result       
    