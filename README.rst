MemoPy
======

badges

Store results of functions calls so that subsequent calls with the same arguments do not have to redo work.
This strategy of memoizing past results is only fully correct with "pure functions". Pure functions (https://en.wikipedia.org/wiki/Pure_function) are functions that, when run with the same arguments, always return the same result. They should not have any side effects (e.g. modifying global variables, writing to an external database), or depend on anything besides the parameters (e.g. a random number generator, reading from an external database). Typically any mathematically-defined function (fibonacci, factorial, sine, cosine, etc.) is a pure function.
But MemoPy can be useful with impure functions, too, when perfect correctness is not required. For example, it can be used to cache the results of network calls to external API's, to avoid repeating expensive network requests (but the cache should be cleared when it is necessary to get completely up to date information).

Use
---

Apply the ``memoify`` decorator to a function to turn that function into a memo function.::

@memoify
def multiply(x, y):
    return x * y

Subsequent calls to ``multiply`` with the same args will not perform the multiplication, but rather look up the past answer.

Multiplying numbers is not a typical use case, so take a look at a function which is inherently reused on the same arguments a lot.

@memoify
def fibo(n):
    return n if n in [0, 1] else (fibo(n-1) + fibo(n-2))

Without memoization, some values of the fibonacci sequence would be computed an exponential number of times. With the single line ``@memoify``, every computation after the first will be replaced with a lookup.

Function arguments are not *required* to be hashable, but they should be for best (fastest) results. If they are not, the memoizing version of the function could become slower than the original under special circumstances (depending on the runtime of the original function, and the number of different arguments the memoizing version has been called with).

MemoPy was not designed with concurrency in mind. So multiple runs of a function at the same time is advised against as it has not been thoroughly thought through what would happen.

Documentation
-------------



Installation
------------



Contribute
----------



Support
-------



License
-------

The project is licensed under the MIT license.
