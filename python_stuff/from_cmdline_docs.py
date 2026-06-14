def sys_argv_func():
    """
    https://docs.python.org/3/using/cmdline.html#interface-options
    """
    import sys

    arguments = sys.argv
    print(arguments)

    # from docs: (sys.argv[0]), is a string reflecting the program’s source.
    first_arg = arguments[0]
    print(first_arg)
    # .../basic-practice/python_stuff/from_cmdline_docs.py


def dash_c_command():
    """
    https://docs.python.org/3/using/cmdline.html#cmdoption-c
    """
    cmd = """
        python -c "import sys; print(sys.argv)"
        """

    # it gives: ['-c']


if __name__ == "__main__":
    sys_argv_func()
