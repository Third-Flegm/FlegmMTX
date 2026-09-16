# flegmmtx

Small, practical helpers for working with numeric matrices in Python.

## Installation

Install the package locally from the project directory:

```bash
python -m pip install -e .
```

The package requires Python 3.10 or newer.

## Quick start

```python
from flegmmtx import add, multiply, scale, shape, transpose

left = [
	[1, 2, 3],
	[4, 5, 6],
]
right = [
	[7, 8],
	[9, 10],
	[11, 12],
]

print(shape(left))
# (2, 3)

print(transpose(left))
# [[1, 4], [2, 5], [3, 6]]

print(add(left, left))
# [[2, 4, 6], [8, 10, 12]]

print(scale(left, 2))
# [[2, 4, 6], [8, 10, 12]]

print(multiply(left, right))
# [[58, 64], [139, 154]]
```

Matrix multiplication follows the standard rule: the number of columns in the
left matrix must equal the number of rows in the right matrix.

## Available helpers

- `shape(matrix)` returns the row and column count.
- `transpose(matrix)` exchanges rows and columns.
- `zeros(rows, columns)` creates a matrix filled with zeroes.
- `ones(rows, columns)` creates a matrix filled with ones.
- `identity(size)` creates a square identity matrix.
- `add(left, right)` adds matrices with matching dimensions.
- `multiply(left, right)` performs matrix multiplication.
- `scale(matrix, factor)` multiplies every value by a number.

Matrices must be non-empty, rectangular, and contain numeric values. Invalid
matrices raise `ValueError` or `TypeError` with a message describing the
problem.

## Example

Run the included example from the project directory:

```bash
python -m pip install -e .
python examples/1.py
```
