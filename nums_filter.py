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