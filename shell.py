import os
import shutil
import subprocess


def cd(*args, **kwargs):
    os.chdir(*args, **kwargs)


def pwd(path='.'):
    print(os.path.abspath(path))


def cp(*args, **kwargs):
    shutil.copy2(*args, **kwargs)


def mv(*args, **kwargs):
    shutil.move(*args, **kwargs)


def run(*args, **kwargs):
    subprocess.run(*args, **kwargs)
