# FlegmMTX Syntax Guide

FlegmMTX uses ordinary Python lists. A matrix is written as a list of rows,
and every row is written as a list of numbers.

## A matrix literal

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]
```

This matrix has 2 rows and 3 columns, so its shape is `(2, 3)`:

```python
from flegmmtx import shape

print(shape(matrix))
# (2, 3)
```

The indentation is only for readability. The important syntax is the nested
square brackets:

```python
matrix = [[1, 2, 3], [4, 5, 6]]
```

Both forms create the same matrix.

## Values and rows

Values must be numbers, such as integers or decimals:

```python
numbers = [
    [1, 2],
    [3.5, 4.75],
]
```

Rows must all have the same number of values. This is valid:

```python
valid = [[1, 2], [3, 4], [5, 6]]
```

This is invalid because the rows have different lengths:

```python
invalid = [[1, 2], [3]]
```

Matrices also cannot be empty:

```python
# Invalid: []
# Invalid: [[], []]
```

The library raises `ValueError` for empty or non-rectangular matrices and
`TypeError` when rows or values have the wrong type.

## Importing functions

Import the functions you need from `flegmmtx`:

```python
from flegmmtx import add, multiply, scale, shape, transpose
```

You can also import constructors:

```python
from flegmmtx import identity, ones, zeros
```

## Checking a shape

```python
from flegmmtx import shape

matrix = [[1, 2, 3], [4, 5, 6]]
rows, columns = shape(matrix)

print(rows)     # 2
print(columns)  # 3
```

`shape()` validates the matrix before returning its dimensions.

## Creating matrices

```python
from flegmmtx import identity, ones, zeros

empty_values = zeros(2, 3)
# [[0, 0, 0], [0, 0, 0]]

same_values = ones(2, 2)
# [[1, 1], [1, 1]]

unchanged = identity(3)
# [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

The dimensions are passed as integers: `zeros(rows, columns)` and
`ones(rows, columns)`. Dimensions must be positive.

## Transposing

`transpose()` exchanges rows and columns:

```python
from flegmmtx import transpose

matrix = [
    [1, 2, 3],
    [4, 5, 6],
]

result = transpose(matrix)
# [[1, 4], [2, 5], [3, 6]]
```

The original matrix is not modified. The returned matrix has shape `(3, 2)`.

## Adding matrices

`add(left, right)` adds values in matching positions. Both matrices must have
the same shape:

```python
from flegmmtx import add

left = [[1, 2], [3, 4]]
right = [[10, 20], [30, 40]]

result = add(left, right)
# [[11, 22], [33, 44]]
```

The operation is element by element:

```text
result[row][column] = left[row][column] + right[row][column]
```

## Scaling

`scale(matrix, factor)` multiplies every value by one number:

```python
from flegmmtx import scale

matrix = [[1, 2], [3, 4]]
result = scale(matrix, 10)
# [[10, 20], [30, 40]]
```

The factor can be an integer or decimal.

## Matrix multiplication

`multiply(left, right)` uses standard matrix multiplication. The number of
columns in the left matrix must equal the number of rows in the right matrix.

For an `m x n` matrix multiplied by an `n x p` matrix, the result is `m x p`:

```python
from flegmmtx import multiply

left = [
    [1, 2, 3],
    [4, 5, 6],
]                       # 2 x 3

right = [
    [7, 8],
    [9, 10],
    [11, 12],
]                       # 3 x 2

result = multiply(left, right)    # 2 x 2
# [[58, 64], [139, 154]]
```

Each result value is a dot product. For example, the top-left value is:

```text
(1 * 7) + (2 * 9) + (3 * 11) = 58
```

In Python-style indexing, the rule is:

```text
result[row][column] = sum(
    left[row][index] * right[index][column]
    for index in range(left_columns)
)
```

Matrix multiplication is not generally commutative. `multiply(a, b)` and
`multiply(b, a)` may have different results or only one order may be valid.

## 3D syntax and current limits

A nested value such as this has three dimensions:

```python
layers = [
    [
        [1, 2],
        [3, 4],
    ],
    [
        [5, 6],
        [7, 8],
    ],
]
```

Its conceptual shape is `2 layers x 2 rows x 2 columns`. The current FlegmMTX
functions accept 2D matrices only, so passing `layers` directly to them raises a
validation error. For small data, process each layer separately:

```python
from flegmmtx import scale

scaled_layers = [scale(layer, 2) for layer in layers]
# [[[2, 4], [6, 8]], [[10, 12], [14, 16]]]
```

For 3D graphics, a 4x4 transformation matrix is still a normal 2D matrix and
can be used directly:

```python
from flegmmtx import multiply

translation = [
    [1, 0, 0, 3],
    [0, 1, 0, 2],
    [0, 0, 1, 5],
    [0, 0, 0, 1],
]
point = [[1], [4], [-2], [1]]

moved_point = multiply(translation, point)
# [[4], [6], [3], [1]]
```

## Running an example

From the project directory:

```bash
python -m pip install -e .
python examples/1.py
```

The `examples/3d.py` file demonstrates the layer representation, but layered
3D operations must currently be written as a loop over 2D matrices.
