#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)

```python
    a = 0 #O(1)
    while (a < n * n * n): #O(1)
      a = a + n * n #O(1)
```

This will be constant O because every input will be constant without having to do change of rate while running.

b)

```python
    sum = 0   #O(1)
    for i in range(n): # *** O(n)
      j = 1 #O(1)
      while j < n: #(1)
        j *= 2 #(1)
        sum += 1 #(1)
```

This will be linear because bigger the input will increase the rate of change.

c)

```python
    def bunnyEars(bunnies):
      if bunnies == 0: #O(1)
        return 0#O(1)

      return 2 + bunnyEars(bunnies-1) #O(1)
```

This one will be constant because it will increment by two, not depend on the input that wont change any of rate of change.

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

Answer:

I would use binaray tree
find the middle of the floor in the list, and if the egg broke as trying, it will return -1 and going left a time. if the egg survives then it will return 1 and going right a time. Through laying out the returns of each index, will be able to identify which floor will be safe floor.
Since this algorithm depends on amount of inputs, the running time can grow or shorten linearly so therefore it will be linear.
