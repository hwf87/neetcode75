# Neetcode Blind 75
This is a repository for coding practices.
* Ref1: [link](https://neetcode.io/practice)
* Ref2: [link](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)
---

### 1. Array and Hash
* 

### 2. Two Pointer
*

### 3. Sliding Window
* Template to solve most of Sliding Window question
```python
class Solution:
    def foo(self, s: str, k: int) -> int:
        # Use a hash map or a set for question that ask about repeating
        # Use a max count or min count for question ask about longest/shortest substring
        # A variable for the start of our window
		
        for windowEnd in range(len(s)):
            # Perform something to our map/set or anything that'll be used for the result
            # Condition to stop our window and move to the next window
            # Calculate the window max/min length if question asking about length, sum if question about sum and so on
			
        # Return what the question want
```

### 4. Stack
* Stack type follow "last-in, first-out" principle
* Which is using list.append() first, then list.pop() later

### 5. Binary Search
* TC = O(Log N)

### 6. Linked List
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        new_node = ListNode(val)
        # if head is None, which means the first Node
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
```



---
### Test Case Template
```python
# Unit Test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("input, expect", \
                             [(),()]
                            )
    def test_foo(self, input, expect):
        '''
        '''
        answer = self.foo(input)
        assert answer == expect
```

### Time Complexity in Python

#### Lists: 
Operation     | Example      | Complexity| Notes
| ----------- |:------------:| ---------:|-------------:| 
Index         | l[i]         | O(1)	     |
Store         | l[i] = 0     | O(1)	     |
Length        | len(l)       | O(1)	     |
Append        | l.append(5)  | O(1)	     | mostly: ICS-46 covers details
Pop	      | l.pop()      | O(1)	     | same as l.pop(-1), popping at end
Clear         | l.clear()    | O(1)	     | similar to l = []
Slice         | l[a:b]       | O(b-a)	     | l[1:5]:O(l)/l[:]:O(len(l)-0)=O(N)
Extend        | l.extend(...)| O(len(...))   | depends only on len of extension
Construction  | list(...)    | O(len(...))   | depends on length of ... iterable
check ==, !=  | l1 == l2     | O(N)          |
Insert        | l[a:b] = ... | O(N)	     | 
Delete        | del l[i]     | O(N)	     | depends on i; O(N) in worst case
Containment   | x in/not in l| O(N)	     | linearly searches list 
Copy          | l.copy()     | O(N)	     | Same as l[:] which is O(N)
Remove        | l.remove(...)| O(N)	     | 
Pop	      | l.pop(i)     | O(N)	     | O(N-i): l.pop(0):O(N) (see above)
Extreme value | min(l)/max(l)| O(N)	     | linearly searches list for value
Reverse	      | l.reverse()  | O(N)	     |
Iteration     | for v in l:  | O(N)          | Worst: no return/break in loop
Sort          | l.sort()     | O(N Log N)    | key/reverse mostly doesn't change
Multiply      | k*l          | O(k N)        | 5*l is O(N): len(l)*l is O(N**2)

#### Dict:
Operation     | Example      | Complexity| Notes
| ----------- |:------------:| ---------:|-------------:| 
Index         | d[k]         | O(1)	     |
Store         | d[k] = v     | O(1)	     |
Length        | len(d)       | O(1)	     |
Delete        | del d[k]     | O(1)	     |
get/setdefault| d.get(k)     | O(1)	     |
Pop           | d.pop(k)     | O(1)	     | 
Pop item      | d.popitem()  | O(1)	     | popped item "randomly" selected
Clear         | d.clear()    | O(1)	     | similar to s = {} or = dict()
View          | d.keys()     | O(1)	     | same for d.values()
Construction  | dict(...)    | O(len(...))   | depends # (key,value) 2-tuples
Iteration     | for k in d:  | O(N)          | all forms: keys, values, items

#### Set:
Operation     | Example      | Complexity| Notes
| ----------- |:------------:| ---------:|-------------:| 
Length        | len(s)       | O(1)	     |
Add           | s.add(5)     | O(1)	     |
Containment   | x in/not in s| O(1)	     | compare to list/tuple - O(N)
Remove        | s.remove(..) | O(1)	     | compare to list/tuple - O(N)
Discard       | s.discard(..)| O(1)	     | 
Pop           | s.pop()      | O(1)	     | popped value "randomly" selected
Clear         | s.clear()    | O(1)	     | similar to s = set()
Construction  | set(...)     | O(len(...))   | depends on length of ... iterable
check ==, !=  | s != t       | O(len(s))     | same as len(t); False in O(1) if the lengths are different
Union         | s | t        | O(len(s)+len(t))
Intersection  | s & t        | O(len(s)+len(t))
Difference    | s - t        | O(len(s)+len(t))
Symmetric Diff| s ^ t        | O(len(s)+len(t))
Iteration     | for v in s:  | O(N)          | Worst: no return/break in loop
Copy          | s.copy()     | O(N)	     |
