# concept_name
Queue General

# Queue Step 1

## name
```
Queues
```

## md_content
```
A queue is a very important data structure in Python. It is essentially a list of elements in Python that we can use to work with data. It is a linear data structure that has a very flexible size and is very easy to add elements to. A queue is very similar to a stack, although the fundamental difference is that the queue follows the **FIFO rule - First in, First out**. 

You can think of a queue data structure as similar to a queue (i.e. a line) for a concert. The first person to enter the line, is the first person to leave the line and enter the concert. Similarly, when one is in line for a fast-food restaurant, the cashier attends the first person in line (**F**irst **I**n **F**irst **O**ut)!   

As we will see, queues are used in many algorithms and for the implementation of functions for many data structures. For example, queues are used in graph (another important data structure) algorithms such as Breadth-First Search.
```
# Queue Step 2

## name
```
Queue Function
```

## md_content
```

Queues, as a data structure, are essentially a class. We can create a Queue with the following code here. 

Just like a stack, we are able to add and remove items from a queue. 
```
## code_snippet
```Python
class Queue():
    def __init__(self):
        self.items = []
```

# Queue Step 3

## name
```
Rules for Queue
```

## md_content
```

1. Things to Remember
   1. The point of entry and exit are different in a Queue.
   2. **Enqueue** - Adding an element to a Queue
   3. **Dequeue** - Removing an element from a Queue
   4. Random access is not allowed - you cannot add or remove an element from the middle.
   
```
