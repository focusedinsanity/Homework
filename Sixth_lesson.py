import sys


def my_func(x):
    my_float_list = []

    for elem in x:
        if len(elem) > 5:
            print('Bigger than five: ', elem)

        try:
            my_float_list.append(float(elem))
        except:
            pass
    return print('Сумма числовых параметров: ',sum(my_float_list)), print('Уникальные параметры: ', (set(x)))


print(my_func(sys.argv[1:]))
