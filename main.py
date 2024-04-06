import matplotlib.pyplot as plt
import time
from fibonacci_rust import fibonacci as fibonacci_rust


def fibonacci_python(n):
    if n <= 1:
        return n
    else:
        return fibonacci_python(n-1) + fibonacci_python(n-2)


def benchmark(n):
    start_time = time.time()
    result_python = fibonacci_python(n)
    end_time = time.time()
    py = round(end_time - start_time, 3)

    start_time = time.time()
    result_rust = fibonacci_rust(n)
    end_time = time.time()
    rs = round(end_time - start_time, 3)
    print(f"Python/Rust: {py}s/{rs}s")
    assert result_python == result_rust
    return py, rs


def run(start, count):
    inputs = []
    pyresults = []
    rsresults = []
    for n in range(count):
        i = start+n
        py, rs = benchmark(i)
        inputs.append(i)
        pyresults.append(py)
        rsresults.append(rs)
    return inputs, pyresults, rsresults


n, py, rs = run(20, 25)

plt.plot(n, py, label='Python')
plt.plot(n, rs, label='Rust')

plt.xlabel('n')
plt.ylabel('Seconds')
plt.title('Fibonacci Times')
plt.legend()
plt.savefig('line_graph.png')
