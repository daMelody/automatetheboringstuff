def a():
    print('a() starts')
    b()
    d()
    print('a() returns')


#! cannot call a() here
#? why not?
# TODO: call a() on the next line and look at the error message


def b():
    print('b() starts')
    c()
    print('b() returns')


def c():
    print('c() starts')
    print('c() returns')


def d():
    print('d() starts')
    print('d() returns')


a()  #* can call a() here
