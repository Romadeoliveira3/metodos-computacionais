from memory_profiler import profile

@profile

def big_array():
    x = [1] * (10 ** 5)
    y = [2] * (2 * 10 ** 7)
    del y
    return x

if __name__ == '__main__':
    big_array()