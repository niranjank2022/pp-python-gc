import timeit
import cython


def primes_pure_python(nb_primes: cython.int):
    i: cython.int
    p: cython.int[2500]

    if nb_primes > 2500:
        nb_primes = 2500

    if not cython.compiled:
        p = [0] * 2500

    len_p: cython.int = 0
    n: cython.int = 2

    while len_p < nb_primes:
        for i in p[:len_p]:
            if n % i == 0:
                break
        else:
            p[len_p] = n
            len_p += 1
        n += 1

    result_as_list = [prime for prime in p[:len_p]]
    return result_as_list


def caller():
    n = 1000
    primes_pure_python(n)


if __name__ == '__main__':
    times = 10
    execution_time = timeit.timeit(caller, number=times)
    print(f"Time taken: {execution_time / times:.6f}")
