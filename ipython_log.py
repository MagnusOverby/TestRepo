# IPython log file

a = 1 
'a' in _ip.user_ns
'a' in _ip.user_ns
def foo(x,y,z):
    return (x+y)/z
2 ** 27
_
fo = 'bar'
fo
_i27
_i9
exec _i8
get_ipython().magic(u'logstart')
get_ipython().system(u'python')
ip_info = get_ipython().getoutput(u'ifconfig eth0 | grep "inet "')
ip_info
ip_info[0].strip()
foo = 'test*'
foo
get_ipython().system(u'ls $foo')
get_ipython().magic(u'alias ll ls -l')
get_ipython().system(u'ls -F --color -l /usr')
get_ipython().magic(u'alias test_alias (cd ch08; ls; cd..)')
get_ipython().system(u'(cd ch08; ls; cd..) ')
get_ipython().magic(u'run ch03/ipython_bug.pyu')
get_ipython().magic(u'run ch03/ipython_bug.py')
get_ipython().system(u'ls -F --color ')
get_ipython().magic(u'cd IPython/')
emacs ipython_bug.py
vim ipython_bug.py
emacs ipython_bug.py &
emacs
.\emacs
vim
./vim
./emacs
emacs ipython_bug.py
get_ipython().magic(u'run ipython_bug.py')
get_ipython().magic(u'run ipython_bug.py')
Magnus(2)
get_ipython().magic(u'run ipython_bug.py')
get_ipython().magic(u'run ipython_bug.py in throws_an_exception()')
get_ipython().magic(u'debug')
strings = ['foo','foobar','baz','qux','python','Guido Van Rossum']*100000
method1 = [x for x in strings if x.startswith('foo')]
method2 = [x for x in strings if x[:3] == 
'foo']
method2
get_ipython().magic(u'time method1')
get_ipython().magic(u'time method2;')
get_ipython().magic(u'time method1;')
get_ipython().magic(u"timeit [x for x strings if x.startwith('foo')]")
get_ipython().magic(u'pinfo %timeit')
get_ipython().magic(u"timeit [x for x in strings if x.startswith('foo')]")
get_ipython().magic(u"timeit [x for x in strings if x[:3]=='foo']")
x = 'foobar'
get_ipython().magic(u"timeit x.startswith('foo')")
get_ipython().magic(u'timeit x[:3] == y')
y = 'foo'
get_ipython().magic(u'timeit x[:3] == y')
get_ipython().magic(u'run linalg.py')
python -m cProfile linalg.py
matrix = randn(100,100)
matrix
get_ipython().magic(u'lprun -f add_and_sum add_and_sum(x,y)')
get_ipython().magic(u'lprun -f add_and_sum add_and_sum(x,y)')
get_ipython().magic(u'lprun -f add_and_sum add_and_sum(x,y)')
get_ipython().magic(u'lprun -f add_and_sum add_and_sum(x,y)')
