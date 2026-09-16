"""Small helpers for working with numeric matrices."""

from __future__ import annotations

from collections.abc import Sequence
from numbers import Number
from typing import TypeAlias


Matrix: TypeAlias = list[list[Number]]


def _validate_matrix(matrix: Sequence[Sequence[Number]]) -> tuple[int, int]:
	"""Validate a non-empty rectangular matrix and return its dimensions."""
	if not matrix:
		raise ValueError("matrix must not be empty")
	if any(not isinstance(row, Sequence) or isinstance(row, (str, bytes)) for row in matrix):
		raise TypeError("matrix rows must be sequences")

	column_count = len(matrix[0])
	if column_count == 0:
		raise ValueError("matrix rows must not be empty")
	if any(len(row) != column_count for row in matrix):
		raise ValueError("matrix must be rectangular")
	if any(not isinstance(value, Number) for row in matrix for value in row):
		raise TypeError("matrix values must be numbers")
	return len(matrix), column_count


def shape(matrix: Sequence[Sequence[Number]]) -> tuple[int, int]:
	"""Return the number of rows and columns in ``matrix``."""
	return _validate_matrix(matrix)


def transpose(matrix: Sequence[Sequence[Number]]) -> Matrix:
	"""Return a matrix with its rows and columns exchanged."""
	_validate_matrix(matrix)
	return [list(column) for column in zip(*matrix)]


def zeros(rows: int, columns: int) -> Matrix:
	"""Create a matrix filled with zeroes."""
	_validate_dimensions(rows, columns)
	return [[0 for _ in range(columns)] for _ in range(rows)]


def ones(rows: int, columns: int) -> Matrix:
	"""Create a matrix filled with ones."""
	_validate_dimensions(rows, columns)
	return [[1 for _ in range(columns)] for _ in range(rows)]


def identity(size: int) -> Matrix:
	"""Create a square identity matrix of ``size``."""
	_validate_dimensions(size, size)
	return [[1 if row == column else 0 for column in range(size)] for row in range(size)]


def add(left: Sequence[Sequence[Number]], right: Sequence[Sequence[Number]]) -> Matrix:
	"""Add two matrices with the same dimensions."""
	left_rows, left_columns = _validate_matrix(left)
	right_rows, right_columns = _validate_matrix(right)
	if (left_rows, left_columns) != (right_rows, right_columns):
		raise ValueError("matrices must have the same dimensions")
	return [
		[left[row][column] + right[row][column] for column in range(left_columns)]
		for row in range(left_rows)
	]


def multiply(left: Sequence[Sequence[Number]], right: Sequence[Sequence[Number]]) -> Matrix:
	"""Multiply two matrices using the standard dot-product operation."""
	left_rows, left_columns = _validate_matrix(left)
	right_rows, right_columns = _validate_matrix(right)
	if left_columns != right_rows:
		raise ValueError(
			"the left matrix column count must match the right matrix row count"
		)

	return [
		[
			sum(left[row][index] * right[index][column] for index in range(left_columns))
			for column in range(right_columns)
		]
		for row in range(left_rows)
	]


def scale(matrix: Sequence[Sequence[Number]], factor: Number) -> Matrix:
	"""Multiply every value in ``matrix`` by ``factor``."""
	_validate_matrix(matrix)
	if not isinstance(factor, Number):
		raise TypeError("factor must be a number")
	return [[value * factor for value in row] for row in matrix]


def _validate_dimensions(rows: int, columns: int) -> None:
	if not isinstance(rows, int) or not isinstance(columns, int):
		raise TypeError("matrix dimensions must be integers")
	if rows <= 0 or columns <= 0:
		raise ValueError("matrix dimensions must be positive")
