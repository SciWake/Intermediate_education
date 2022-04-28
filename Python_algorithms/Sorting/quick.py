import random

# Генерация массива

mass = [i for i in range(20, 0, -1)]


# РЕАЛИЗАЦИЯ 1 -  Данная версия требует дополнительной памяти

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = random.choice(array)
    s_ar = []
    m_ar = []
    l_ar = []

    for item in array:

        if item < pivot:
            s_ar.append(item)
        elif item > pivot:
            l_ar.append(item)
        elif item == pivot:
            m_ar.append(item)
        else:
            raise Exception(f'Необычный элемент {item}')

    return quick_sort(s_ar) + m_ar + quick_sort(l_ar)

# python -m timeit -n 1000 "import quick" "quick.quick_sort(quick.mass)"
# 1000 loops, best of 5: 33.6 usec per loop
