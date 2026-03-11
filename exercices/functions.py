def greet_users(names : list):
    if not isinstance(names, list):
        raise TypeError
    for name in names:
        print(f"Hello, {name}")

def sum_even(numbers: list):
    try:
        return sum([n for n in numbers if n %2 == 0])
    except Exception as e:
        raise e

def fibonacci(n : int):
    try:
        result = []
        i = 0
        for i in range(n):
            if i <= 1:
                result.append(i)
            else:
                result.append(result[i - 1] + result[i - 2])
            i += 1
        return result
    except Exception as e:
        raise e

if __name__ == "__main__":
    greet_users(["Thomas", "Beverly"])
    print(sum_even([2, 3, 4, 5]))
    print(fibonacci(10))