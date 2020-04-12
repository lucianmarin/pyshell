# pyshell

pyshell turns (i)Python into a shell using functional programming.

pyshell is useful on remote environments were your favorite shell can't be installed, but python and pip are available for development.

pyshell was worked on and commited using pyshell and helper runargs.

## Functions

`cd()`, `cp()`, `mv()`, `pwd()`, `run()` are available in `shell.py`.

Some helping run arguments are available in `runargs.py`. You can create a local `runargs.py` where you define your command line shortcuts.

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

In [20]: def gc(msg): return ['git', 'commit', '-am', msg]

In [21]: run(gc('initial version'))
[master 7d64e23] initial version
 3 files changed, 81 insertions(+), 1 deletion(-)
 rewrite README.md (100%)
 create mode 100644 runargs.py
 create mode 100644 shell.py
```
