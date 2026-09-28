# Library Basics — Q&A Log

---

## Q: What is a Python library?

A **Python library** is a collection of pre-written code that you can reuse in your own programs so you don't have to write everything yourself.

### The pieces

- **Module**: a single `.py` file with functions, classes, or variables.
- **Package**: a folder of modules (it usually has an `__init__.py` file).
- **Library**: a general term for a module or package, or a group of them, built for some purpose, such as math, web requests or data analysis.

### Two kinds

**1. The standard library** comes with Python, so you don't install anything:
```python
import math
import random
from collections import deque   # handy for DSA work (queues and stacks)

print(math.sqrt(16))        # 4.0
print(random.randint(1, 10))
```

**2. Third-party libraries** are written by others. You install them with `pip`:
```
pip install numpy
```
```python
import numpy as np
arr = np.array([1, 2, 3])
print(arr * 2)   # [2 4 6]
```

### Popular examples
| Library | Used for |
|---|---|
| `numpy` | Fast arrays and math |
| `pandas` | Tables and data analysis |
| `requests` | Making HTTP calls |
| `matplotlib` | Plotting charts |
| `flask` / `django` | Building websites |

**An analogy:** a library is like a toolbox. You can build your own hammer, but it's usually faster to use one that's already made and well tested.

Since you're working on arrays, the most useful ones to know are the built-in `list`, the standard-library modules `collections` and `bisect`, and `numpy`.

---

## Q: Make a Library_basic MD file in this folder and write every response into it.

I created `Library_basic.md` in this folder. It holds the previous answer, and I'll add each new question and answer to the end of it for the rest of this conversation.

---

## Q: What does `__init__.py` do? What is its significance?

`__init__.py` is a special file inside a folder that tells Python: **"this folder is a package, so you can import from it."**

### Example structure
```
my_library/
├── __init__.py
├── arrays.py
└── strings.py
```
Now you can write:
```python
from my_library import arrays
from my_library.strings import reverse
```

### What it does

**1. Marks a folder as a package.**
In old Python (before 3.3), a folder *without* `__init__.py` could not be imported at all. Modern Python can import such folders anyway (they're called "namespace packages"), but a regular package still uses `__init__.py`, and it's still the standard practice.

**2. Runs when the package is imported.**
The code inside `__init__.py` runs **once**, the first time you import the package. You can use it for setup:
```python
# my_library/__init__.py
print("my_library loaded!")
```

**3. Makes imports shorter.**
You can bring things up to the package level so users don't need to know the internal file layout:
```python
# my_library/__init__.py
from .arrays import binary_search
from .strings import reverse
```
Now users can write:
```python
from my_library import binary_search   # instead of my_library.arrays.binary_search
```

**4. Controls `from package import *`.**
The `__all__` list decides what gets imported with `*`:
```python
# my_library/__init__.py
__all__ = ["binary_search", "reverse"]
```

**5. Holds package-level info.**
For example, a version number:
```python
__version__ = "1.0.0"
```

### Key points
- It **can be empty**, and an empty file is perfectly fine and very common.
- Its name must be exactly `__init__.py` (two underscores on each side).
- Think of it as the **front door** of the package: it decides what visitors see first and what happens when they walk in.

---
