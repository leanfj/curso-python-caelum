def test_args_kwargs(*args, **kwargs):
    # print('Arg1: {}'.format(arg1))
    # print('Arg2: {}'.format(arg2))
    # print('Arg3: {}'.format(arg3))

    for item in args:
        print(item)

    for key, value in kwargs.items():
        print(key, value)


args = (3, 'Um', 2, 4)

test_args_kwargs(*args)

kwargs = {'arg3': 3, 'arg2': 'dois', 'arg1': 'um', 'arg0': 'Zero'}

test_args_kwargs(**kwargs)
