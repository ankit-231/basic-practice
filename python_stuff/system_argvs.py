"""
From [Lecture 2: Command-line Environment](https://www.youtube.com/watch?v=ccBGsPedE9Q)
"""

import sys

if __name__ == "__main__":
    print(sys.argv)

"""
➜ py python_stuff/system_argvs.py 
['python_stuff/system_argvs.py']

➜ py -m python_stuff.system_argvs                 
['/home/ankit/MyFiles/self_practice/basic-practice/python_stuff/system_argvs.py']


py python_stuff/system_argvs.py python_stuff/*.py

['python_stuff/system_argvs.py', 'python_stuff/about_str.py', 'python_stuff/boolean_values.py', 'python_stuff/complex_numbers.py', 'python_stuff/from_cmdline_docs.py', 'python_stuff/garbase_collection.py', 'python_stuff/hashing_tuple_and_list.py', 'python_stuff/identity_comparison.py', 'python_stuff/immutable_tuple.py', 'python_stuff/sequence_slicing.py', 'python_stuff/set_and_frozenset.py', 'python_stuff/system_argvs.py']
"""
