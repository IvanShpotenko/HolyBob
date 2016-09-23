#!/usr/bin/python
import os

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python3.5/site-packages')
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    with open(virtenv) as f:
        code = compile(f.read(), virtenv, 'exec')
        exec(code, dict(__file__=virtualenv))
except IOError:
    pass

from HolyBob import app as application