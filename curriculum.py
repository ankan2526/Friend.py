"""
curriculum.py — Predefined Python learning topics with detailed lessons.
Spec ref: docs/specs.md Section 3
"""

TOPICS = [
    {
        "id": "01_variables",
        "title": "Variables & Data Types",
        "lesson": """
## 📦 Variables & Data Types

A **variable** is a named container that stores a value in memory. Think of it like a labelled box — you can put something in, look at it, or replace it.

```python
name = "Alice"   # str
age = 25         # int
height = 1.68    # float
is_student = True  # bool
```

---

### The Four Core Types

#### 1. `int` — Whole Numbers
```python
year = 2024
score = -10
big_number = 1_000_000  # underscores for readability
```

#### 2. `float` — Decimal Numbers
```python
pi = 3.14159
temperature = -2.5
price = 9.99
```
> ⚠️ Floats can have tiny rounding errors: `0.1 + 0.2 == 0.30000000000000004`

#### 3. `str` — Text (Strings)
Strings are sequences of characters, always wrapped in quotes.
```python
single = 'hello'
double = "world"
both   = "it's fine"  # single quote inside double quotes
```

#### 4. `bool` — True or False
```python
is_raining = False
logged_in = True
```
Booleans are the result of comparisons:
```python
print(5 > 3)    # True
print(10 == 9)  # False
```

---

### Checking the Type
Use `type()` to inspect a variable's type at any time:
```python
x = 42
print(type(x))       # <class 'int'>
print(type("hello")) # <class 'str'>
print(type(3.14))    # <class 'float'>
print(type(True))    # <class 'bool'>
```

---

### Type Conversion (Casting)
Convert between types using built-in functions:
```python
age_str = "25"
age_int = int(age_str)      # "25" → 25
price_str = str(9.99)       # 9.99 → "9.99"
pi_int = int(3.99)          # 3.99 → 3 (truncates, doesn't round)
flag = bool(0)              # 0 → False, any non-zero → True
```

---

### Variable Naming Rules
| Rule | Example |
|------|---------|
| Use letters, numbers, underscores | `first_name`, `score2` |
| Cannot start with a number | ~~`2score`~~ ❌ |
| Case-sensitive | `Name` ≠ `name` |
| Use `snake_case` by convention | `phone_number`, not `phoneNumber` |
| Reserved words are forbidden | ~~`if`, `for`, `class`~~ ❌ |

---

### Multiple Assignment
```python
x = y = z = 0          # all three get 0
a, b, c = 1, 2, 3      # unpacking — a=1, b=2, c=3
first, *rest = [1, 2, 3, 4]  # first=1, rest=[2,3,4]
```

---

### Arithmetic with Variables
```python
a = 10
b = 3

print(a + b)   # 13  — addition
print(a - b)   # 7   — subtraction
print(a * b)   # 30  — multiplication
print(a / b)   # 3.333... — true division (always float)
print(a // b)  # 3   — floor division (integer result)
print(a % b)   # 1   — modulo (remainder)
print(a ** b)  # 1000 — exponentiation (10³)
```
""",
        "challenge": "Create variables for your name (str), age (int), height in metres (float), and whether you are a student (bool). Print each variable along with its type using `type()`.",
        "starter_code": "# Challenge: Variables & Types\n# Create a variable for each: name, age, height, is_student\n\nname = \nage = \nheight = \nis_student = \n\n# Print each value AND its type\nprint(name, type(name))\n"
    },
    {
        "id": "02_strings",
        "title": "String Formatting",
        "lesson": """
## ✏️ String Formatting

Strings are one of the most used data types. Python gives you powerful tools to work with and display them.

---

### Creating Strings
```python
single    = 'Hello'
double    = "Hello"
multiline = \"\"\"Line 1
Line 2
Line 3\"\"\"
raw       = r"C:\\Users\\Alice"  # raw string — backslashes are literal
```

---

### String Concatenation
```python
first = "Alice"
last  = "Smith"
full  = first + " " + last   # "Alice Smith"
```

> ⚠️ You cannot concatenate a string with a non-string directly:
> ```python
> age = 25
> print("Age: " + age)       # ❌ TypeError
> print("Age: " + str(age))  # ✅ "Age: 25"
> ```

---

### f-strings (Recommended ✅)
Introduced in Python 3.6. The cleanest and fastest way to embed variables:
```python
name = "Alice"
age  = 25
city = "Bangalore"

print(f"Hello, {name}! You are {age} years old.")
print(f"Next year you'll be {age + 1}.")  # expressions work too!
print(f"Name has {len(name)} characters.")
```

You can format numbers directly inside f-strings:
```python
price = 9.5
print(f"Price: ₹{price:.2f}")   # ₹9.50  (2 decimal places)
print(f"Score: {0.875:.1%}")     # 87.5%
print(f"|{'left':<10}|")         # left-aligned in 10-char field
print(f"|{'right':>10}|")        # right-aligned
```

---

### Essential String Methods
```python
text = "  Hello, World!  "

text.upper()          # "  HELLO, WORLD!  "
text.lower()          # "  hello, world!  "
text.strip()          # "Hello, World!"   (removes whitespace)
text.lstrip()         # "Hello, World!  " (left only)
text.rstrip()         # "  Hello, World!" (right only)
text.replace("World", "Python")  # "  Hello, Python!  "
text.split(",")       # ["  Hello", " World!  "]
",".join(["a","b","c"])  # "a,b,c"
```

---

### Searching Inside Strings
```python
s = "the quick brown fox"

s.startswith("the")   # True
s.endswith("fox")     # True
s.find("quick")       # 4  (index), -1 if not found
"fox" in s            # True (membership test)
s.count("o")          # 2
```

---

### String Slicing
Strings are indexed sequences — you can slice them like lists:
```python
word = "Python"
#       0 1 2 3 4 5
#      -6-5-4-3-2-1  (negative indices go from the end)

print(word[0])      # "P"
print(word[-1])     # "n"
print(word[0:3])    # "Pyt"  (start inclusive, end exclusive)
print(word[2:])     # "thon"
print(word[:4])     # "Pyth"
print(word[::-1])   # "nohtyP"  (reverse!)
```

---

### Checking String Content
```python
"123".isdigit()   # True — all digits
"abc".isalpha()   # True — all letters
"abc123".isalnum() # True — letters or digits
"  ".isspace()    # True — only whitespace
"Hello".istitle() # True — Title Case
```
""",
        "challenge": "Given the string `'  python programming is fun!  '`, write code that: strips the whitespace, capitalizes the first letter of every word (Title Case), replaces 'Fun' with 'Awesome', and prints the final result along with its length.",
        "starter_code": "# Challenge: String manipulation\n\ntext = '  python programming is fun!  '\n\n# Step 1: Strip whitespace\n\n# Step 2: Title case\n\n# Step 3: Replace 'Fun' with 'Awesome'\n\n# Step 4: Print result and its length\n"
    },
    {
        "id": "03_lists",
        "title": "Lists & Tuples",
        "lesson": """
## 📋 Lists & Tuples

### Lists — Ordered, Mutable Sequences

A list stores multiple values in a single variable. Items are ordered, can be of mixed types, and can be changed (mutable).

```python
fruits   = ["apple", "banana", "cherry"]
numbers  = [10, 20, 30, 40, 50]
mixed    = [1, "hello", 3.14, True]
nested   = [[1, 2], [3, 4], [5, 6]]  # list of lists
empty    = []
```

---

### Indexing & Slicing
```python
fruits = ["apple", "banana", "cherry", "mango", "grape"]
#          0         1          2         3        4
#         -5        -4         -3        -2       -1

print(fruits[0])     # "apple"
print(fruits[-1])    # "grape"
print(fruits[1:4])   # ["banana", "cherry", "mango"]
print(fruits[:2])    # ["apple", "banana"]
print(fruits[2:])    # ["cherry", "mango", "grape"]
print(fruits[::2])   # ["apple", "cherry", "grape"]  (every 2nd)
print(fruits[::-1])  # reversed list
```

---

### Modifying Lists
```python
fruits = ["apple", "banana"]

# Add items
fruits.append("cherry")         # ["apple", "banana", "cherry"]
fruits.insert(1, "mango")       # ["apple", "mango", "banana", "cherry"]
fruits.extend(["grape", "kiwi"]) # adds multiple items

# Remove items
fruits.remove("banana")   # removes first occurrence by value
popped = fruits.pop()     # removes and returns last item
popped = fruits.pop(0)    # removes and returns item at index 0
del fruits[1]             # deletes item at index 1
fruits.clear()            # empties the list

# Modify in place
fruits[0] = "strawberry"  # replace by index
```

---

### Useful List Methods & Functions
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

numbers.sort()           # sorts in-place: [1, 1, 2, 3, 4, 5, 6, 9]
numbers.sort(reverse=True)  # descending
sorted(numbers)          # returns NEW sorted list, original unchanged
numbers.reverse()        # reverses in-place
numbers.count(1)         # 2 — how many times 1 appears
numbers.index(5)         # index of first occurrence of 5

len(numbers)             # 8 — length
min(numbers)             # 1
max(numbers)             # 9
sum(numbers)             # 31
```

---

### List Comprehensions — Pythonic One-liners
```python
# Traditional way
squares = []
for x in range(1, 6):
    squares.append(x ** 2)

# List comprehension — same result, one line
squares = [x ** 2 for x in range(1, 6)]   # [1, 4, 9, 16, 25]

# With a condition (filter)
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

---

### Tuples — Ordered, Immutable Sequences

Tuples are like lists, but they **cannot be changed** after creation. Use them for data that should not be modified.

```python
coordinates = (10.5, 20.3)
rgb          = (255, 128, 0)
single_item  = (42,)          # note the trailing comma!
person       = ("Alice", 25, "Bangalore")

# Access works the same
print(coordinates[0])   # 10.5
print(person[-1])       # "Bangalore"

# Unpacking
name, age, city = person
print(name)  # "Alice"

# Tuples are IMMUTABLE — this raises TypeError:
# coordinates[0] = 99  ❌
```

#### When to use tuples vs lists?
| Use **list** when | Use **tuple** when |
|---|---|
| Data may change | Data is fixed (constants) |
| You need to add/remove items | You want to protect data from modification |
| Order of items may change | Coordinates, RGB values, function returns |
""",
        "challenge": "Create a list of 5 numbers. Without using `sort()`, find and print the minimum and maximum values using only `min()` and `max()`. Then create a sorted copy using `sorted()` and print it. Finally, print the original list to prove it was unchanged.",
        "starter_code": "# Challenge: List operations\n\nnumbers = [42, 7, 19, 3, 55]\n\n# Find min and max\n\n# Create a sorted copy (without modifying original)\n\n# Print original to prove it's unchanged\n"
    },
    {
        "id": "04_dicts",
        "title": "Dictionaries",
        "lesson": """
## 📖 Dictionaries

A **dictionary** stores data as **key-value pairs**. Think of a real dictionary — you look up a word (key) to find its definition (value). Keys must be unique and immutable (strings, numbers, tuples). Values can be anything.

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "Bangalore",
    "hobbies": ["reading", "coding"]
}
```

---

### Accessing Values

```python
# By key — raises KeyError if key doesn't exist
print(person["name"])    # "Alice"

# .get() — safe access, returns None (or a default) if missing
print(person.get("email"))          # None
print(person.get("email", "N/A"))   # "N/A"
```

---

### Adding, Updating & Deleting

```python
d = {"x": 1, "y": 2}

# Add a new key
d["z"] = 3                   # {"x": 1, "y": 2, "z": 3}

# Update an existing key
d["x"] = 99                  # {"x": 99, "y": 2, "z": 3}

# Update multiple keys at once
d.update({"x": 10, "w": 4})  # {"x": 10, "y": 2, "z": 3, "w": 4}

# Delete
del d["z"]                   # removes "z"
value = d.pop("w")           # removes "w" and returns its value (4)
d.clear()                    # empties the dict
```

---

### Iterating Over a Dictionary

```python
scores = {"Alice": 95, "Bob": 82, "Charlie": 78}

# Iterate keys (default)
for name in scores:
    print(name)

# Iterate values
for score in scores.values():
    print(score)

# Iterate key-value pairs (most common)
for name, score in scores.items():
    print(f"{name}: {score}")
```

---

### Useful Methods & Operations

```python
d = {"a": 1, "b": 2, "c": 3}

d.keys()     # dict_keys(['a', 'b', 'c'])
d.values()   # dict_values([1, 2, 3])
d.items()    # dict_items([('a', 1), ('b', 2), ('c', 3)])

"a" in d     # True  — membership check on keys
"z" in d     # False

len(d)       # 3 — number of key-value pairs
```

---

### Nested Dictionaries

```python
students = {
    "alice": {"grade": "A", "score": 95},
    "bob":   {"grade": "B", "score": 82},
}

print(students["alice"]["score"])    # 95
students["bob"]["score"] = 85        # update nested value
```

---

### Dictionary Comprehensions

```python
# Build a dict of squares
squares = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter — keep only passing scores
scores = {"Alice": 90, "Bob": 45, "Charlie": 70}
passed = {name: s for name, s in scores.items() if s >= 60}
# {"Alice": 90, "Charlie": 70}
```

---

### Counting with Dictionaries

A very common pattern — count occurrences:
```python
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)  # {"apple": 3, "banana": 2, "cherry": 1}
```
""",
        "challenge": "Create a dictionary of 5 countries and their capitals. Write code that: (1) prints all capitals using `.values()`, (2) prints each country-capital pair in a nice format, (3) lets the user 'look up' a country using `.get()` and prints 'Not found' if it doesn't exist.",
        "starter_code": "# Challenge: Countries & Capitals\n\ncountries = {\n    # Add 5 country: capital pairs\n}\n\n# 1. Print all capitals\n\n# 2. Print each pair nicely\n\n# 3. Look up a country (try one that exists and one that doesn't)\ncountry_to_find = \"India\"\nresult = countries.get(country_to_find, \"Not found\")\nprint(result)\n"
    },
    {
        "id": "05_conditionals",
        "title": "Conditionals (if/else)",
        "lesson": """
## 🔀 Conditionals — Making Decisions

Conditionals allow your program to take different paths based on whether a condition is `True` or `False`.

---

### The Basic `if` / `elif` / `else`

```python
age = 20

if age >= 18:
    print("You can vote!")
elif age >= 16:
    print("Almost there!")
else:
    print("Too young to vote.")
```

Only one block runs — the **first one whose condition is `True`**. If none match, `else` runs.

---

### Comparison Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal | `5 != 3` | `True` |
| `>` | Greater than | `10 > 5` | `True` |
| `<` | Less than | `3 < 1` | `False` |
| `>=` | Greater or equal | `5 >= 5` | `True` |
| `<=` | Less or equal | `4 <= 3` | `False` |

---

### Logical Operators: `and`, `or`, `not`

```python
x = 15

# and — BOTH must be True
if x > 10 and x < 20:
    print("x is between 10 and 20")   # ✅ prints this

# or — AT LEAST ONE must be True
if x < 5 or x > 10:
    print("x is outside 5-10 range")  # ✅ prints this

# not — flips True/False
if not x == 100:
    print("x is not 100")             # ✅ prints this
```

#### Short-circuit evaluation
- `and`: stops as soon as it finds `False` (no need to check the rest)
- `or`: stops as soon as it finds `True`

---

### Truthy & Falsy Values

Python evaluates these as `False` (Falsy):
- `False`, `0`, `0.0`, `""`, `[]`, `{}`, `()`, `None`

Everything else is `True` (Truthy):
```python
name = ""
if name:
    print("Got a name")
else:
    print("Name is empty")  # ← this runs

numbers = [1, 2, 3]
if numbers:
    print("List is not empty")  # ← this runs
```

---

### The Ternary Operator (One-liner `if`)

```python
# Normal if/else
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Ternary — same thing in one line
status = "adult" if age >= 18 else "minor"
print(status)
```

---

### `in` and `not in` Operators

```python
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("Found it!")

if "mango" not in fruits:
    print("No mango here.")

# Works on strings too
email = "user@example.com"
if "@" in email:
    print("Looks like a valid email")
```

---

### Nested Conditionals

```python
score = 85

if score >= 60:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    else:
        grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")   # Grade: B
```

> 💡 **Tip:** Avoid deeply nested `if`s — it makes code hard to read. Prefer `elif` chains or `and`/`or` logic.
""",
        "challenge": "Write a program that uses a `score` variable (try different values). Print the letter grade: A (90+), B (80-89), C (70-79), D (60-69), F (below 60). Also print whether the student passed (score >= 60) using a ternary operator.",
        "starter_code": "# Challenge: Grade calculator\n\nscore = 75  # Try changing this!\n\n# Print the letter grade using if/elif/else\n\n# Print pass/fail using a ternary operator\nresult = \nprint(f\"Result: {result}\")\n"
    },
    {
        "id": "06_loops",
        "title": "Loops (for / while)",
        "lesson": """
## 🔁 Loops — Repeating Actions

Loops let you run the same block of code many times without copying it.

---

### `for` Loop — Iterating Over a Sequence

```python
# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterate over a string
for char in "Python":
    print(char)     # P, y, t, h, o, n
```

---

### `range()` — Generating Number Sequences

```python
range(5)          # 0, 1, 2, 3, 4
range(1, 6)       # 1, 2, 3, 4, 5
range(0, 10, 2)   # 0, 2, 4, 6, 8  (step = 2)
range(10, 0, -1)  # 10, 9, 8, ... 1  (countdown)

for i in range(1, 6):
    print(f"{i} squared = {i**2}")
```

---

### `enumerate()` — Index + Value Together

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# Start counting from 1
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
```

---

### `zip()` — Iterate Two Lists Together

```python
names  = ["Alice", "Bob", "Charlie"]
scores = [90,      85,    78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

---

### `while` Loop — Keep Going Until Condition is False

```python
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1      # ⚠️ Always move towards the exit condition!
```

> 🚨 Forgetting to update the condition causes an **infinite loop**! Use `Ctrl+C` to stop one.

```python
# Countdown example
n = 10
while n > 0:
    print(n)
    n -= 1
print("Blast off!")
```

---

### `break` — Exit the Loop Immediately

```python
for i in range(10):
    if i == 5:
        break   # stop the loop at 5
    print(i)    # prints 0, 1, 2, 3, 4
```

---

### `continue` — Skip to the Next Iteration

```python
for i in range(10):
    if i % 2 == 0:
        continue   # skip even numbers
    print(i)       # prints 1, 3, 5, 7, 9
```

---

### `else` on a Loop

The `else` block runs if the loop finished **without** a `break`:
```python
for i in range(5):
    print(i)
else:
    print("Loop finished normally!")

# But with break, else does NOT run:
for i in range(5):
    if i == 3:
        break
else:
    print("This won't print!")
```

---

### Nested Loops

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end=" ")
    print()   # newline after each row
# (1,1) (1,2) (1,3)
# (2,1) (2,2) (2,3)
# (3,1) (3,2) (3,3)
```
""",
        "challenge": "Use a `for` loop with `enumerate()` to print a numbered list of 5 of your favourite movies. Then use a `while` loop to print a countdown from 10 to 1, then print 'Go!'.",
        "starter_code": "# Challenge: Loops\n\nmovies = [\"Movie 1\", \"Movie 2\", \"Movie 3\", \"Movie 4\", \"Movie 5\"]\n\n# 1. Print numbered list using enumerate()\n\n\n# 2. Countdown from 10 to 1, then print 'Go!'\n"
    },
    {
        "id": "07_functions",
        "title": "Functions",
        "lesson": """
## ⚙️ Functions — Reusable Blocks of Code

A function is a named block of code that performs a task. Define it once, call it as many times as you need. Functions are the foundation of clean, maintainable code.

---

### Defining and Calling

```python
def greet():            # define — no parameters
    print("Hello!")

greet()                 # call — runs the block
greet()                 # call it again!
```

---

### Parameters & Arguments

```python
def greet(name):           # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Alice")             # "Alice" is the argument → Hello, Alice!
greet("Bob")               # Hello, Bob!
```

Multiple parameters:
```python
def add(a, b):
    return a + b           # 'return' sends a value back to the caller

result = add(3, 5)
print(result)   # 8
```

---

### Return Values

A function can return any value — or nothing (implicitly returns `None`).

```python
def square(n):
    return n * n

print(square(4))    # 16
x = square(7)       # store the result
print(x)            # 49

# Multiple return values (returned as a tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 9, 2, 7])
print(low, high)    # 1 9
```

---

### Default Parameters

Provide a fallback value when an argument isn't supplied:
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))           # Hello, Alice!
print(greet("Bob", "Hi"))       # Hi, Bob!
print(greet("Charlie", "Hey"))  # Hey, Charlie!
```

> ⚠️ Default parameters must come **after** required parameters.

---

### Keyword Arguments

Call a function using `name=value` syntax — order doesn't matter:
```python
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet(animal="cat", name="Whiskers")
describe_pet(name="Rex", animal="dog")    # same result!
```

---

### `*args` — Variable Number of Arguments

```python
def total(*numbers):       # numbers becomes a tuple
    return sum(numbers)

print(total(1, 2, 3))        # 6
print(total(10, 20, 30, 40)) # 100
```

---

### Scope — Local vs Global

Variables defined inside a function are **local** — they don't exist outside:
```python
def my_func():
    x = 10       # local variable
    print(x)

my_func()        # 10
# print(x)       # ❌ NameError — x doesn't exist out here
```

```python
y = 100          # global variable

def my_func():
    print(y)     # ✅ can READ globals

my_func()        # 100
```

---

### Docstrings — Documenting Your Functions

```python
def add(a, b):
    \"\"\"
    Add two numbers and return the result.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b
    \"\"\"
    return a + b

help(add)        # prints the docstring
print(add.__doc__)
```
""",
        "challenge": "Write a function `celsius_to_fahrenheit(c)` that converts a Celsius temperature to Fahrenheit (formula: `F = c * 9/5 + 32`). Give it a default parameter of `c=0`. Call it with several values including no argument, and print each result formatted to 1 decimal place.",
        "starter_code": "# Challenge: Temperature converter function\n\ndef celsius_to_fahrenheit(c=0):\n    \"\"\"Convert Celsius to Fahrenheit.\"\"\"\n    # Your formula here\n    pass\n\n# Test with: 0, 100, 37, and no argument\nprint(celsius_to_fahrenheit(100))\nprint(celsius_to_fahrenheit(37))\nprint(celsius_to_fahrenheit())     # uses default\n"
    },
    {
        "id": "08_error_handling",
        "title": "Error Handling (try/except)",
        "lesson": """
## 🛡️ Error Handling

When Python encounters a problem it cannot recover from, it raises an **exception**. Without handling, exceptions crash your program with a traceback. Error handling lets you respond gracefully.

---

### Reading a Traceback

```
Traceback (most recent call last):
  File "app.py", line 3, in <module>
    result = 10 / 0
ZeroDivisionError: division by zero
```

Key parts:
- **File & line number** — where the error happened
- **Exception type** — `ZeroDivisionError`
- **Message** — what went wrong

---

### `try` / `except` — Basic Pattern

```python
try:
    number = int("hello")       # this will fail
except ValueError:
    print("That's not a valid number!")

# Program continues normally here
print("Still running!")
```

The `except` block only runs if the specified exception is raised.

---

### Catching Multiple Exceptions

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    except TypeError:
        print("Both arguments must be numbers!")
        return None
    return result

print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # Cannot divide by zero! → None
print(safe_divide(10, "x"))  # Both arguments must be numbers! → None
```

---

### Catching Any Exception

```python
try:
    risky_operation()
except Exception as e:
    print(f"An error occurred: {e}")
```

> ⚠️ Catching bare `Exception` hides bugs. Always prefer specific exception types when you know what to expect.

---

### `else` — Runs Only If No Exception

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division failed!")
else:
    print(f"Success! Result = {result}")   # ← runs because no error occurred
```

---

### `finally` — Always Runs (Cleanup Code)

```python
try:
    f = open("data.txt")
    data = f.read()
except FileNotFoundError:
    print("File not found!")
finally:
    f.close()   # ← runs whether or not an error occurred
    print("File closed.")
```

---

### Raising Exceptions Yourself

```python
def set_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(e)    # Age cannot be negative: -5
```

---

### Common Built-in Exceptions

| Exception | Common Cause |
|-----------|-------------|
| `ValueError` | `int("abc")`, wrong value type |
| `ZeroDivisionError` | `x / 0` |
| `TypeError` | Wrong type for operation |
| `IndexError` | `lst[100]` on a short list |
| `KeyError` | `d["missing"]` on a dict |
| `FileNotFoundError` | Opening a file that doesn't exist |
| `AttributeError` | Calling `.upper()` on an int |
| `NameError` | Using a variable before defining it |
""",
        "challenge": "Write a function `safe_list_access(lst, index)` that returns the element at the given index. Handle `IndexError` by returning `'Index out of range'` and `TypeError` (if index is not an int) by returning `'Index must be an integer'`.",
        "starter_code": "# Challenge: Safe list access with error handling\n\ndef safe_list_access(lst, index):\n    try:\n        pass  # Your code here\n    except IndexError:\n        pass\n    except TypeError:\n        pass\n\n# Test cases\nmy_list = [10, 20, 30, 40, 50]\nprint(safe_list_access(my_list, 2))     # 30\nprint(safe_list_access(my_list, 99))    # Index out of range\nprint(safe_list_access(my_list, \"two\")) # Index must be an integer\n"
    },
    {
        "id": "09_oop",
        "title": "Basic OOP (Classes)",
        "lesson": """
## 🏗️ Object-Oriented Programming

**OOP** is a programming style that organises code around **objects** — entities that bundle together related data (attributes) and behaviour (methods). Python is fully object-oriented.

---

### Classes and Objects

A **class** is a blueprint; an **object** (or instance) is a concrete thing built from that blueprint.

```python
class Dog:                          # class definition
    def __init__(self, name, breed):  # constructor
        self.name = name            # instance attribute
        self.breed = breed          # instance attribute

    def bark(self):                 # instance method
        return f"{self.name} says: Woof!"

    def describe(self):
        return f"{self.name} is a {self.breed}"

# Create objects (instances)
rex   = Dog("Rex", "Labrador")
bella = Dog("Bella", "Poodle")

print(rex.bark())        # Rex says: Woof!
print(bella.describe())  # Bella is a Poodle
```

---

### `__init__` — The Constructor

`__init__` is called automatically when you create a new object. Use it to set up the initial state.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius        # every Circle gets its own radius

c1 = Circle(5)
c2 = Circle(10)
print(c1.radius)   # 5
print(c2.radius)   # 10
```

---

### `self` — The Instance Reference

`self` refers to the specific object the method is being called on. It's always the first parameter of instance methods, but you don't pass it — Python does automatically.

```python
class Counter:
    def __init__(self):
        self.count = 0           # each Counter starts at 0

    def increment(self):
        self.count += 1          # modifies THIS object's count

    def reset(self):
        self.count = 0

c = Counter()
c.increment()
c.increment()
c.increment()
print(c.count)   # 3
c.reset()
print(c.count)   # 0
```

---

### Class Attributes vs Instance Attributes

```python
class Dog:
    species = "Canis familiaris"   # class attribute — shared by ALL dogs

    def __init__(self, name):
        self.name = name           # instance attribute — unique per dog

print(Dog.species)                 # "Canis familiaris"
rex = Dog("Rex")
print(rex.species)                 # "Canis familiaris"
print(rex.name)                    # "Rex"
```

---

### `__str__` — Friendly String Representation

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person({self.name}, {self.age})"

p = Person("Alice", 25)
print(p)     # Person(Alice, 25)  — uses __str__
print(str(p))  # same
```

---

### Inheritance — Reusing Code

A child class **inherits** everything from a parent class and can add or override behaviour.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):             # Dog inherits from Animal
    def speak(self):           # override the method
        return f"{self.name} says: Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"

animals = [Dog("Rex"), Cat("Whiskers"), Dog("Buddy")]
for animal in animals:
    print(animal.speak())
```

---

### `super()` — Calling the Parent's Method

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call Animal's __init__
        self.breed = breed       # add Dog-specific attribute
```
""",
        "challenge": "Create a `BankAccount` class with: an `__init__` that takes `owner` and sets `balance = 0`; a `deposit(amount)` method; a `withdraw(amount)` method that raises a `ValueError` if amount exceeds balance; and a `__str__` that returns `'Account(owner, balance)'`. Test it.",
        "starter_code": "# Challenge: BankAccount class\n\nclass BankAccount:\n    def __init__(self, owner):\n        self.owner = owner\n        self.balance = 0\n\n    def deposit(self, amount):\n        pass  # increase balance\n\n    def withdraw(self, amount):\n        pass  # decrease balance, raise ValueError if overdraft\n\n    def __str__(self):\n        pass  # return friendly string\n\n# Test it\nacc = BankAccount(\"Alice\")\nacc.deposit(1000)\nprint(acc)                  # Account(Alice, 1000)\nacc.withdraw(250)\nprint(acc)                  # Account(Alice, 750)\nacc.withdraw(9999)          # Should raise ValueError\n"
    },
    {
        "id": "10_putting_together",
        "title": "Putting It All Together",
        "lesson": """
## 🎓 Putting It All Together

You've covered all the core building blocks of Python. This final lesson shows how they combine into a real, working program — and points you towards what's next.

---

### Recap of What You've Learned

| Topic | Key Concepts |
|-------|-------------|
| Variables & Types | `int`, `float`, `str`, `bool`, `type()`, casting |
| String Formatting | f-strings, methods (`.strip()`, `.upper()`, etc.), slicing |
| Lists & Tuples | Indexing, slicing, `.append()`, `.sort()`, comprehensions |
| Dictionaries | Key-value pairs, `.get()`, `.items()`, comprehensions |
| Conditionals | `if`/`elif`/`else`, comparison ops, ternary, truthy/falsy |
| Loops | `for`, `while`, `range()`, `enumerate()`, `break`, `continue` |
| Functions | `def`, parameters, `return`, defaults, `*args`, scope |
| Error Handling | `try`/`except`, `else`, `finally`, `raise`, built-in exceptions |
| OOP | Classes, `__init__`, `self`, inheritance, `__str__` |

---

### A Complete Mini-Project — Contact Book

```python
# contact_book.py — uses: dicts, lists, functions, loops, error handling, OOP

class ContactBook:
    def __init__(self):
        self._contacts = {}        # {name: phone}

    def add(self, name: str, phone: str):
        if name in self._contacts:
            raise ValueError(f"'{name}' already exists.")
        self._contacts[name] = phone
        print(f"✅ Added {name}")

    def find(self, name: str) -> str:
        return self._contacts.get(name, "Contact not found.")

    def remove(self, name: str):
        if name not in self._contacts:
            raise KeyError(f"'{name}' not found.")
        del self._contacts[name]
        print(f"🗑️ Removed {name}")

    def list_all(self):
        if not self._contacts:
            print("📒 No contacts yet.")
            return
        for i, (name, phone) in enumerate(sorted(self._contacts.items()), 1):
            print(f"{i}. {name}: {phone}")

    def __str__(self):
        return f"ContactBook({len(self._contacts)} contacts)"


# Usage
book = ContactBook()
book.add("Alice",   "9876543210")
book.add("Bob",     "1234567890")
book.add("Charlie", "5555555555")

book.list_all()
print(book.find("Alice"))
print(book.find("Zara"))   # not found

try:
    book.add("Alice", "0000000000")  # duplicate!
except ValueError as e:
    print(f"Error: {e}")

book.remove("Bob")
print(book)
```

---

### Understanding the Code

This single script uses **everything** you learned:
- **Classes & OOP** — `ContactBook` class with `__init__` and `__str__`
- **Dictionaries** — store contacts as `{name: phone}`
- **Functions/Methods** — `add`, `find`, `remove`, `list_all`
- **Loops** — `for` loop with `enumerate()` and `sorted()`
- **Conditionals** — `if name in self._contacts`
- **Error Handling** — `raise ValueError`, `try/except`
- **Type Hints** — `name: str`, `-> str`

---

### What's Next?

Now that you know Python fundamentals, here's your learning roadmap:

#### Immediate Next Steps
1. **Modules & Packages** — `import math`, `import random`, using `pip`
2. **File I/O** — reading/writing files with `open()`, `with` statements
3. **List Comprehensions & Generators** — more Pythonic patterns

#### Practical Projects
- 📝 **CLI Todo App** — file storage, menus
- 🌐 **Web Scraper** — `requests` + `BeautifulSoup`
- 📊 **Data Analysis** — `pandas` + `matplotlib`

#### Career Paths
| Path | Libraries to Learn |
|------|--------------------|
| Web Dev | `Flask`, `FastAPI`, `Django` |
| Data Science | `numpy`, `pandas`, `scikit-learn` |
| AI/ML | `PyTorch`, `TensorFlow`, Hugging Face |
| Automation | `selenium`, `pyautogui`, `schedule` |

---

**You've built a real foundation. Keep coding — every project teaches you something new! 🚀**
""",
        "challenge": "Extend the ContactBook class: add a `search(keyword)` method that returns all contacts whose name contains the keyword (case-insensitive). Test it by adding 5 contacts and searching for a partial name.",
        "starter_code": "# Challenge: Extend ContactBook with search()\n\nclass ContactBook:\n    def __init__(self):\n        self._contacts = {}\n\n    def add(self, name, phone):\n        self._contacts[name] = phone\n\n    def search(self, keyword):\n        \"\"\"Return list of (name, phone) tuples where name contains keyword.\"\"\"\n        pass  # Your code here\n\n    def list_all(self):\n        for name, phone in self._contacts.items():\n            print(f\"{name}: {phone}\")\n\n# Add 5 contacts and test search\nbook = ContactBook()\n# ... add contacts ...\n# ... test search ...\n"
    }
]
