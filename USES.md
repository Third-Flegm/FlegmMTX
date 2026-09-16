# What Are Matrices Used For?

A matrix is a rectangular grid of numbers. It is more than a table: the
numbers can describe a transformation, a collection of data, or a system of
equations. Matrix operations give us a consistent way to combine and transform
that information.

FlegmMTX is a small, dependency-free Python library for the everyday 2D
matrix operations that make these ideas practical.

## Why matrices matter

Matrices are useful whenever many related values need to be processed by the
same rules.

- **Geometry and graphics:** rotate, resize, move, and project points.
- **3D graphics and games:** combine camera, object, and world transformations.
- **Systems of equations:** represent coefficients and solve or manipulate
  related equations.
- **Data and statistics:** store observations, features, images, or tables of
  measurements.
- **Machine learning:** represent batches, weights, activations, and other
  numerical data.
- **Simulations:** update positions, velocities, and other state values.
- **Image processing:** treat an image as a grid of pixel values and apply
  filters or other transformations.

The main benefit is composition. Instead of writing separate code for every
coordinate, a matrix can describe one operation and matrix multiplication can
combine several operations into one.

## What FlegmMTX provides

The package accepts non-empty, rectangular, 2D sequences containing numeric
values. It checks inputs and reports invalid shapes instead of silently
producing surprising results.

```python
from flegmmtx import add, identity, multiply, ones, scale, shape, transpose, zeros
```

Available helpers:

| Helper | Purpose |
| --- | --- |
| `shape(matrix)` | Return `(rows, columns)`. |
| `transpose(matrix)` | Exchange rows and columns. |
| `zeros(rows, columns)` | Create a matrix filled with zeroes. |
| `ones(rows, columns)` | Create a matrix filled with ones. |
| `identity(size)` | Create a square matrix that leaves values unchanged when multiplied. |
| `add(left, right)` | Add matrices with matching dimensions. |
| `multiply(left, right)` | Perform standard matrix multiplication. |
| `scale(matrix, factor)` | Multiply every value by the same number. |

## A small example

```python
from flegmmtx import add, multiply, scale, shape, transpose

measurements = [
    [10, 12, 9],
    [8, 11, 13],
]

print(shape(measurements))       # (2, 3)
print(transpose(measurements))   # [[10, 8], [12, 11], [9, 13]]
print(scale(measurements, 2))    # [[20, 24, 18], [16, 22, 26]]
print(add(measurements, measurements))
```

For multiplication, the inner dimensions must match. An `m x n` matrix can be
multiplied by an `n x p` matrix, producing an `m x p` matrix:

```python
from flegmmtx import multiply

left = [[1, 2, 3], [4, 5, 6]]       # 2 x 3
right = [[7, 8], [9, 10], [11, 12]] # 3 x 2

result = multiply(left, right)      # 2 x 2
# [[58, 64], [139, 154]]
```

## Using FlegmMTX for 3D graphics

A 3D point has three coordinates, but 3D graphics commonly use a **4x4
homogeneous transformation matrix**. The extra coordinate makes translation
work with the same multiplication operation as rotation and scaling.

A point `(x, y, z)` is written as `[x, y, z, 1]`. A 4x4 matrix can then apply a
transformation to that point. FlegmMTX already supports the required 4x4
matrix operations.

### Translation

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

The first three values are the transformed `(x, y, z)` coordinates. The final
value stays `1` for an ordinary position.

### Scaling and rotation

A scale matrix changes the size of an object:

```python
scale_3d = [
    [2, 0, 0, 0],
    [0, 3, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 1],
]
```

A rotation around the z-axis by an angle `theta` is represented by:

```python
from math import cos, sin

theta = 0.5
rotation_z = [
    [cos(theta), -sin(theta), 0, 0],
    [sin(theta), cos(theta), 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]
```

Transformations can be composed. The order matters: applying `scale_3d`
then `translation` is different from applying them in the opposite order.

```python
from flegmmtx import multiply

world_transform = multiply(translation, multiply(rotation_z, scale_3d))
world_point = multiply(world_transform, point)
```

This is the usual pattern for a 3D object:

```text
world_point = world_matrix * object_point
camera_point = view_matrix * world_point
screen_point = projection_matrix * camera_point
```

Each named matrix is a normal 4x4 matrix, so it can be created and combined
with FlegmMTX today.

## What about a 3D matrix?

The phrase "3D matrix" can mean two different things:

1. A matrix used for 3D geometry. This is usually a 4x4 matrix, and FlegmMTX
   supports it because it supports arbitrary rectangular 2D matrices.
2. A 3D array, such as `layers x rows x columns`. This is technically a tensor
   rather than a single 2D matrix, and FlegmMTX does not currently provide
   tensor operations or a 3D `shape()` result.

For a small 3D dataset, keep each layer as a normal matrix and process the
layers with Python:

```python
from flegmmtx import scale

layers = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
]

brighter_layers = [scale(layer, 2) for layer in layers]
# [[[2, 4], [6, 8]], [[10, 12], [14, 16]]]
```

For large tensors, broadcasting, fast numerical routines, or neural-network
work, a specialized package such as NumPy is a better fit. FlegmMTX is most
useful when you want a small, readable matrix API without adding a dependency.

## Common mistakes

- **Adding different shapes:** matrix addition is element by element, so both
  matrices must have the same dimensions.
- **Mixing up multiplication and element-wise multiplication:** `multiply()` is
  standard matrix multiplication, not value-by-value multiplication.
- **Using the wrong order:** matrix multiplication is not generally commutative;
  `multiply(a, b)` can differ from `multiply(b, a)`.
- **Forgetting homogeneous coordinates:** a 3D translation matrix expects a
  point written with a fourth coordinate, normally `1`.
- **Calling a tensor a matrix:** a collection of 2D layers needs different
  operations from a single 2D matrix.

## Installation and next steps

From the project directory:

```bash
python -m pip install -e .
```

Then import the helpers from `flegmmtx`. The included `examples/1.py` shows the
basic package layout, while the examples in this document demonstrate how the
same operations extend to 3D transformation math.
