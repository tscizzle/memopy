"""
Decorator for adding memoization to a function
"""


from collections import defaultdict
from functools import wraps


def memoify(func):
    """
    store past answers in a dict of the form
    {hashable_args: [(unhashable_args, result),
                     (unhashable_args, result),
                     ... ],
     ... }
    """
    memo_dict = defaultdict(list)
    @wraps(func)
    def memo_func(*args, **kwargs):
        arg_tuple = tuple(args) + tuple(kwargs.items())
        hashables = tuple(arg for arg in arg_tuple if is_hashable(arg))
        non_hashables = tuple(arg for arg in arg_tuple if not is_hashable(arg))
        if hashables in memo_dict:
            for past_non_hashables, past_answer in memo_dict[hashables]:
                if past_non_hashables == non_hashables:
                    return past_answer
        answer = func(*args, **kwargs)
        ## TODO: handling catching, storing, and raising exceptions
        memo_dict[hashables].append((non_hashables, answer))
        return answer
    memo_func.clear = memo_dict.clear
    return memo_func


def is_hashable(obj):
    try:
        hash(obj)
    except:
        return False
    else:
        return True
