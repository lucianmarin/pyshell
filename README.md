# pyshell

Turning Python into a shell using functional programming.

## Usage

```
Python 3.7.7 (default, Mar 10 2020, 15:43:03)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.13.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from shell import *

In [2]: pwd()
/Users/lucian/Git/pyshell

In [3]: pwd('..')
/Users/lucian/Git

In [4]: pwd('shell.py')
/Users/lucian/Git/pyshell/shell.py

In [5]: run('ls')
README.md	__init__.py	__pycache__	shell.py

In [6]: pwd()
/Users/lucian/Git/pyshell

In [7]: run('pwd')
/Users/lucian/Git/pyshell

In [11]: gs = ['git', 'status']

In [12]: run(gs)
On branch master
Your branch is up to date with 'origin/master'.

In [17]: gA = ['git', 'add', '-A']

In [18]: run(gA)

In [19]: run(gs)
On branch master
Your branch is up to date with 'origin/master'.
```

## Functions

cd, cp, mv, pwd, run are available in shell.py
