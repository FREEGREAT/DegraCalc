def ConvertNumberType(nums):
    nums = nums.replace(',', '.')
    try:
        number = float(nums)
        if number.is_integer():
            return int(number)
        return number
    except ValueError:
        raise ValueError(f"Invalid number: '{nums}'")
