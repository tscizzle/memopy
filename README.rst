MemoPy
======

.. image:: https://travis-ci.org/tscizzle/memopy.svg?branch=master
    :target: https://travis-ci.org/tscizzle/memopy

.. image:: https://coveralls.io/repos/github/tscizzle/memopy/badge.svg?branch=master
    :target: https://coveralls.io/github/tscizzle/memopy?branch=master

.. image:: https://badge.fury.io/py/memopy.svg
    :target: https://badge.fury.io/py/memopy

Store results of functions calls so that subsequent calls with the same arguments do not have to redo work.

This strategy of memoizing past results is only fully correct with "pure functions". Pure functions (https://en.wikipedia.org/wiki/Pure_function) are functions that, when run with the same arguments, always return the same result. They should not have any side effects (e.g. modifying global variables, writing to an external database), or depend on anything besides the parameters (e.g. a random number generator, reading from an external database). Typically any mathematically-defined function (fibonacci, factorial, sine, cosine, etc.) is a pure function.

But MemoPy can be useful with impure functions, too, when perfect correctness is not required. For example, it can be used to cache the results of network calls to external API's, to avoid repeating expensive network requests (but the cache should be cleared when it is necessary to get completely up to date information).

Use
---

Import the memoify decorator::

    from memopy.memopy import memoify

Apply the ``memoify`` decorator to a function to turn that function into a memo function::

    @memoify
    def multiply(x, y):
        return x * y

Subsequent calls to ``multiply`` with the same args will not perform the multiplication, but rather look up the past answer.

Multiplying numbers is not a typical use case, so take a look at a function which is inherently reused on the same arguments a lot::

    @memoify
    def fibo(n):
        if n in [0, 1]:
            return n
        return fibo(n-1) + fibo(n-2)

Without memoization, some values of the fibonacci sequence would be computed an exponential number of times. With the single line ``@memoify``, for a given ``n`` every computation after the first will be replaced with a lookup.

Function arguments are not *required* to be hashable, but they should be for best (fastest) results. If they are not, the memoizing version of the function could become slower than the original under special circumstances (depending on the runtime of the original function, and the number and nature of different arguments the memoizing version has been called with).

MemoPy was not designed with concurrency in mind. So multiple runs of the same function in different threads at the same time is advised against as it has not been thoroughly thought through what would happen.

Documentation
-------------

The tests found on Github at https://github.com/tscizzle/memopy/tree/master/tests give some examples and showcase the library's functionality.

Installation
------------

If you don't have pip, get pip at: https://pip.pypa.io/en/stable/installing

Run the command ``pip install memopy`` in your terminal to get the MemoPy library.

To test your installation, start a Python interpreter with the ``python`` command in your terminal and make sure you can run ``import memopy`` in it without getting an error.

Contribute
----------

Find the code on Github at: https://github.com/tscizzle/memopy

Support
-------

Contact me (Tyler Singer-Clark) at tscizzle@gmail.com with any questions or concerns.

License
-------

The project is licensed under the MIT license.
