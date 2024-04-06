# Rust vs Python Module Benchmark

Though easy to use, Python is notoriously slow. On the other hand, Python allows you to create modules in C. You can avoid manual pointer manipulation by using Rust. This enables you to create Python-based solutions while building performance-sensitive modules in Rust.

## Setup

    make setup
    make install

## Build Rust Module

    source env/bin/activate
    cd fibonacci_rust
    maturin develop
    cd ..

## Run

    make run

Graph is stored at line_graph.png

## Sample Results

![Graph](line_graph.png)