def is_odd(number):
    if number % 2 ==0:
        return False
    return True


def is_prime(num):
    if num > 1:
        for i in range(2, (num // 2) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

def is_perfect(Input_Number):
    Sum = 0
    for i in range(1, Input_Number):
        if (Input_Number % i == 0):
            Sum = Sum + i
    if (Sum == Input_Number):
       return True
    else:
        return False

def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit)**num_digits for digit in num_str)
    return sum_of_powers == num
def digit_sum(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_digit = sum(int(digit) for digit in num_str)
    return sum_of_digit
def find_property(num):
    num_property = []
    if is_armstrong(num):
        num_property.append("armstrong")
    if is_odd(num):
        num_property.append("odd")
    else:
        num_property.append("even")
    return num_property



