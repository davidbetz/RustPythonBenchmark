use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

fn fib(n: u64) -> u64 {
    if n <= 1 {
        return n;
    } else {
        return fib(n - 1) + fib(n - 2);
    }
}

#[pyfunction]
fn fibonacci(n: u64) -> PyResult<u64> {
    Ok(fib(n))
}

#[pymodule]
fn fibonacci_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fibonacci, m)?)?;
    Ok(())
}
