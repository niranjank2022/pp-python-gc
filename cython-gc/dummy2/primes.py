import timeit


def primes_python(nb_primes):
    p = []
    n = 2
    while len(p) < nb_primes:
        for i in p:
            if n % i == 0:
                break

        else:
            p.append(n)
        n += 1
    return p


def caller():
    n = 1000
    primes_python(n)


if __name__ == '__main__':
    times = 10
    execution_time = timeit.timeit(caller, number=times)
    print(f"Time taken: {execution_time / times:.6f}")
