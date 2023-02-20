from to_do import TODO


def task5(value_for_a, value_for_b):
    a = value_for_a
    b = value_for_b
    temp = a
    a = value_for_b
    b = temp

    print(f"a is {a} and b is {b} ")
    return a, b

if __name__ == "__main__":

    print(task5(value_for_a= 125 ,value_for_b=645))