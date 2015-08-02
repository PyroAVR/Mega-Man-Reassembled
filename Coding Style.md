**Why?**
As a codebase grows, it becomes increasingly important to keep the code reasonable and readable.  This is mostly due to the increased difficulty of maintaining a large codebase.

**Python**
*Flow control should work like this:*
```python
if condition:
  statement
```
Not like this:
```python
if condition: statement
```

*Checking for validity should look like this:*
```python
if valid:
```
Not like this:
```python
if valid == True:
```

While python is dynamically typed, it is also strongly typed, and, if variables are only used such that no conversions are necessary, and that types are not reassigned, processing time is saved during interpretation, speeding up execution considerably. See rpython project.

Typing recap:
*Dynamic:* An object type can be changed within a given scope, therefore the following is valid:
```python
a = 5
a = '5'IS
```
*Static:* An object type cannot be changed without redefinition (in a different scope).  The following is therefore invalid:
```c++
int a = 5;
char a = '5'
```
*Strong:* An object cannot be compared with another object of a different type without an explicit conversion.  The following is produces an integer:
```python
print(5 + int(5))
10
```
The following produces an error:
FIX THIS
