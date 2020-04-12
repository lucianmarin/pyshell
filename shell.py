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


def rs(cmd):
    # run subprocess or run split
    subprocess.run(cmd.split())


def ld(path='.'):
    contents = os.listdir(path)
    for content in contents:
        print(content)


def tree(path='.'):
    abspath = os.path.abspath(path)
    alen = len(abspath.split(os.sep))
    for root, dirs, files in os.walk(abspath):
        rlen = len(root.split(os.sep))
        print((rlen - alen) * "---", os.path.basename(root))
        for file in sorted(files):
            print((rlen - alen + 1) * "---", file)
