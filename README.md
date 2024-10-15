# Algorithms

## Setup (Windows)
Build Docker Container
```bash
docker build -t algos:1 .
```

Run docker image
```bash
docker run -v ${PWD}:/usr/src/app -it algos:1
```

Now connect using VSCode Remote Connect functionality. Verify that the local folder is linked to the container folder by creating a new file and verifying that its created both inside container an in local filesystem.


## Time complexity of built in Functions - Python
[Link](https://wiki.python.org/moin/TimeComplexity)

## DS Notes
### Linked List
[Python Linked Lists: Tutorial With Examples](https://www.datacamp.com/tutorial/python-linked-lists)
It contains a series of nodes that are stored at random locations in memory, allowing for efficient memory management.
Benefits of linked list:
- **Ease of insertion and deletion (O(1) vs O(n)):** In lists, inserting or deleting an element at any position other than the end requires shifting all the subsequent items to a different position. This process has a time complexity of O(n). The linked list structure allows to add or remove elements at any position by simply modifying the links to include a new element or bypass the deleted one. Once the position of the element is identified and there is direct access to the point of insertion or deletion, adding or removing nodes can be achieved in O(1) time.
- **Dynamic Size:** Python lists are dynamic arrays, which means that they provide the flexibility to modify size. However, this process involves a series of complex operations, including reallocating the array to a new, larger memory block. Such reallocation is inefficient since elements are copied over to a new block, potentially allocating more space than is immediately necessary. Linked lists can grow and shrink dynamically without the need for reallocation or resizing.
- **Memory Efficiency:** Linked lists allocate memory for each element separately. There is no need of over allocating memory in the case of lists.

| Pros | Cons |
| ---- | ---- |
| Dynamic Size | Doesn't allow for direct access to elements (accessing an element requires sequential traversal) |
| Memory Efficiency | Higher memory usage per element (since you need to store pointer to next element) |

Use when:
- You need to frequently insert and delete many elements
- The data size is unpredictable or likely to change frequently
- Direct access to elements is not a requirement
- The dataset contains large elements or structures

Types of linked list:
- Singly Linked List
- Doubly Linked List
- Circular Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data  # Assigns the given data to the node
        self.next = None  # Initialize the next attribute to null

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)  # Create a new node 
        new_node.next = self.head  # Next for new node becomes the   current head
        self.head = new_node  # Head now points to the new node
    
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If the list is empty, make the new node the head
            return
        last = self.head 
        while last.next:  # Otherwise, traverse the list to find the last node
            last = last.next
        last.next = new_node  # Make the new node the next node of the last node
    
    def deleteFromBeginning(self):
        if self.head is None:
            return "The list is empty" # If the list is empty, return this string
        self.head = self.head.next  # Otherwise, remove the head by making the next node the new head
    
    def deleteFromEnd(self):
        if self.head is None:
            return "The list is empty" 
        if self.head.next is None:
            self.head = None  # If there's only one node, remove the head by making it None
            return
        temp = self.head
        while temp.next.next:  # Otherwise, go to the second-last node
            temp = temp.next
        temp.next = None  # Remove the last node by setting the next pointer of the second-last node to None
    
    def search(self, value):
        current = self.head  # Start with the head of the list
        position = 0  # Counter to keep track of the position
        while current: # Traverse the list
            if current.data == value: # Compare the list's data to the search value
                return f"Value '{value}' found at position {position}" # Print the value if a match is found
            current = current.next
            position += 1
        return f"Value '{value}' not found in the list" 

    def printList(self):
        temp = self.head # Start from the head of the list
        while temp:
            print(temp.data,end=' ') # Print the data in the current node
            temp = temp.next # Move to the next node
        print()  # Ensures the output is followed by a new line
```

## Python Notes
### Modules
#### [6.0) Modules](https://docs.python.org/3.9/tutorial/modules.html)

Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. Such a file is called a module; definitions from a module can be imported into other modules or into the main module.

A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable \_\_name__.
```python
>>> import fibo
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.__name__
'fibo'
```

#### 6.1) More on Modules
A module can contain executable statements as well as function definitions. These statements are intended to initialize the module. They are executed only the first time the module name is encountered in an import statement. 1 (They are also run if the file is executed as a script.)

Each module has its own private symbol table, which is used as the global symbol table by all functions defined in the module. Thus, the author of a module can use global variables in the module without worrying about accidental clashes with a user’s global variables.

##### Executing modules as scripts
When you run a Python module with

```bash
python fibo.py <arguments>
```

the code in the module will be executed, just as if you imported it, but with the \_\_name__ set to "\_\_main__". That means that by adding this code at the end of your module:

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

you can make the file usable as a script as well as an importable module, because the code that parses the command line only runs if the module is executed as the “main” file:

```bash
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```

If the module is imported, the code is not run:

```bash
>>>
>>> import fibo
>>>
```
This is often used either to provide a convenient user interface to a module, or for testing purposes (running the module as a script executes a test suite).


##### The module search paths
When a module named spam is imported, the interpreter first searches for a built-in module with that name. These module names are listed in ```sys.builtin_module_names```. If not found, it then searches for a file named spam.py in a list of directories given by the variable ```sys.path```.

```bash
>>> import sys
>>> sys.builtin_module_names
('_abc', '_ast', '_codecs', '_collections', '_functools', '_imp', '_io', '_locale', '_operator', '_signal', '_sre', '_stat', '_string', '_symtable', '_thread', '_tokenize', '_tracemalloc', '_typing', '_warnings', '_weakref', 'atexit', 'builtins', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'posix', 'pwd', 'sys', 'time')
>>> sys.path
['', '/usr/local/lib/python312.zip', '/usr/local/lib/python3.12', '/usr/local/lib/python3.12/lib-dynload', '/usr/local/lib/python3.12/site-packages']
```

```sys.path``` is initialized from these locations:
- The directory containing the input script (or the current directory when no file is specified).
- PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
- The installation-dependent default (by convention including a site-packages directory, handled by the site module).

#### 6.4) Packages
Packages are a way of structuring Python’s module namespace by using “dotted module names”. For example, the module name A.B designates a submodule named B in a package named A. 

Suppose you want to design a collection of modules (a “package”) for the uniform handling of sound files and sound data
```bash
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

When importing the package, Python searches through the directories on sys.path looking for the package subdirectory.

The \_\_init__.py files are required to make Python treat directories containing the file as packages. In the simplest case, \_\_init__.py can just be an empty file, but it can also execute initialization code for the package or set the \_\_all__ variable, described later.

Importing modules
```python
import sound.effects.echo
from sound.effects import echo # alternative
from sound.effects.echo import echofilter # function directly
```

**Importing * From a Package**
Now what happens when the user writes from sound.effects import *? Ideally, one would hope that this somehow goes out to the filesystem, finds which submodules are present in the package, and imports them all. **This takes a long time**. The import statement uses the following convention: if a package’s \_\_init__.py code defines a list named \_\_all__, it is taken to be the list of module names that should be imported when from package import * is encountered. For example, the file sound/effects/\_\_init__.py could contain the following code:
```python
__all__ = ["echo", "surround", "reverse"] # This would 
# mean that from sound.effects import * would import the 
# # three named submodules of the sound.effects package.
```

If \_\_all__ is not defined, the statement from sound.effects import * does not import all submodules from the package sound.effects into the current namespace; it only ensures that the package sound.effects has been imported (possibly running any initialization code in \_\_init__.py) and then imports whatever names are defined in the package.

**Intra-package References**
When packages are structured into subpackages (as with the sound package in the example), you can use absolute imports to refer to submodules of siblings packages. For example, if the module sound.filters.vocoder needs to use the echo module in the sound.effects package, it can use ``` from sound.effects import echo.```

You can also write relative imports, with the from module import name form of import statement. These imports use leading dots to indicate the current and parent packages involved in the relative import. From the surround module for example, you might use:
```python
from . import echo
from .. import formats
from ..filters import equalizer
```

Note that relative imports are based on the name of the current module. Since the name of the main module is always "\_\_main__", modules intended for use as the main module of a Python application must always use absolute imports.

---

#### [5) The import system](https://docs.python.org/3/reference/import.html)

Python defines two types of packages, regular packages and namespace packages. 
- Regular Packages: A regular package is typically implemented as a directory containing an \_\_init__.py file. When a regular package is imported, this \_\_init__.py file is implicitly executed, and the objects it defines are bound to names in the package’s namespace. Importing parent.one will implicitly execute parent/\_\_init__.py and parent/one/\_\_init__.py. Subsequent imports of parent.two or parent.three will execute parent/two/\_\_init__.py and parent/three/\_\_init__.py respectively.
```python
parent/
    __init__.py
    one/
        __init__.py
    two/
        __init__.py
    three/
        __init__.py
```

- Namespace Packages: A namespace package is a composite of various portions, where each portion contributes a subpackage to the parent package. Portions may reside in different locations on the file system. Portions may also be found in zip files, on the network, or anywhere else that Python searches during import. Namespace packages may or may not correspond directly to objects on the file system; they may be virtual modules that have no concrete representation.

### 'is' vs ==

**Equality Operator (==):** Checks if the values of two objects are equal.
```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True because the contents of a and b are the same
```

**Identity Operator (is):**  Checks if two variables point to the same object in memory.
```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)  # False because a and b are two different objects in memory
```