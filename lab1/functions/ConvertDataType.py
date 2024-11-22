def ConvertNumTypes(nums):
    """
    Конвертує строкове представлення числа в числовий тип (int або float).

    Функція приймає рядок, який може містити числа з роздільником ',' або '.', 
    конвертує його у float, а якщо число ціле, повертає його у вигляді int.

    Args:
        nums (str): Рядок, що представляє число. 
                    Наприклад: '123', '45.67', '8,9'.

    Returns:
        int: Якщо число є цілим.
        float: Якщо число є дробовим.

    Raises:
        ValueError: Якщо рядок не може бути перетворений у число.

    Example:
        >>> ConvertNumTypes('123')
        123
        >>> ConvertNumTypes('45.67')
        45.67
        >>> ConvertNumTypes('8,9')
        8.9
        >>> ConvertNumTypes('invalid')
        ValueError: Invalid number: 'invalid'
    """
    nums = nums.replace(',', '.')
    try:
        number = float(nums)
        if number.is_integer():
            return int(number)
        return number
    except ValueError:
        raise ValueError(f"Invalid number: '{nums}'")
