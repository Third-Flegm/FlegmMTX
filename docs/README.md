# flegmmtx

Small, practical helpers for working with numeric 2D matrices in Python.

## Installation

Install the package from PyPI when published:

```powershell
python -m pip install flegmmtx
```

Else if unpublished:
```powershell
python -m pip install git+https://github.com/Third-Flegm/FlegmMTX
```

For local development, install the current project in editable mode:

```powershell
python -m pip install -e .
```

The package requires Python 3.10 or newer.

## Commands

Install the library from the project directory:

```bash
python -m pip install -e .
```

Show the command-line help:

```bash
flegmmtx --help
```

Show the installed version:

```bash
flegmmtx --version
```

Copy all documentation files into the current folder:

```bash
flegmmtx --docs
```

Copy all documentation files into a custom folder. The folder is created when
it does not exist:

```bash
flegmmtx --docs my-docs
```

Overwrite documentation files that already exist:

```bash
flegmmtx --docs --force
flegmmtx --docs my-docs --force
```

Run the basic example:

```bash
python examples/1.py
```

Run the layered-data example:

```bash
python examples/3d.py
```

The `--docs` command copies `README.md`, `USES.md`, and `SYNTAX.md`.
Existing files are protected unless `--force` is provided.

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

For a closer explanation of Python matrix syntax, dimensions, and operation
rules, see [SYNTAX.md](SYNTAX.md). For examples of real-world uses, see
[USES.md](USES.md).

## Available helpers

- `shape(matrix)` returns the row and column count as `(rows, columns)`.
- `transpose(matrix)` exchanges rows and columns.
- `zeros(rows, columns)` creates a matrix filled with zeroes.
- `ones(rows, columns)` creates a matrix filled with ones.
- `identity(size)` creates a square identity matrix.
- `add(left, right)` adds matrices with matching dimensions.
- `multiply(left, right)` performs matrix multiplication.
- `scale(matrix, factor)` multiplies every value by a number.

Matrices must be non-empty, rectangular, 2D sequences containing numeric
values. Invalid matrices raise `ValueError` or `TypeError` with a message
describing the problem.

## 3D note

The current API does not support `layers x rows x columns` arrays. It can still
represent 3D graphics transformations as ordinary 4x4 matrices, because a 4x4
matrix is still a 2D matrix. Layered 3D arrays require tensor operations that
are outside the current API.

