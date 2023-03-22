import sys

print(sys.argv)

def test(*args, **kwargs):
    print(args, kwargs)

test('hello mr',11)
