Using virtualenv, pip, and ipython
##################################
:date: 2011-07-03 21:06
:author: reece
:slug: using-virtualenv-pip-and-ipython
:status: published

This page provides a quick synopsis on how to use three of my favorite
Python features together:

-  `virtualenv <http://www.virtualenv.org/>`__, which provides a
   standardized mechanism to isolate python environments (including in
   WSGI setups)
-  `pip <http://www.pip-installer.org/>`__, which facilitates packages
   installation in virtualenv environments or otherwise
-  `ipython <http://ipython.scipy.org/>`__, a terrific interactive shell
   with readline and debugging support

First, you'll need python, virtualenv, and ipython installed. These are
commonly available in most (all?) Linux distributions, or you can
install from source. On Ubuntu, try
``sudo apt-get install python python-virtualenv ipython``. You're on
your own for other systems.

| A virtualenv consists of a project directory with modified python,
  pip, and easy\_install executables. To create this directory, type the
  following in your shell:
| [shell]
| virtualenv myproject
| [/shell]
| This will create a ``myproject`` directory and install a base virtual
  environment.

| Take a moment to browse the myproject directory. You'll see that
  virtualenv also created ``myproject/bin/activate``, a shell script
  that sets up the environment to use this virtualenv. Unsurprisingly,
  ``activate`` is how you activate your virtualenv. Invoke ``activate``
  like this:
| [shell]
| apt12j$ source myproject/bin/activate
| (myproject)apt12j$
| [/shell]
| ``activate`` prepended myproject/bin to your PATH so that you will use
  myproject's versions of python, pip, and easy install. ``activate``
  also modifies your shell prompt so that it's clear that you're in a
  virtualenv. To revert your environment, type ``deactivate``.

| Now suppose we want to work with openpyxl, a package for reading and
  writing Microsoft Excel OpenXML files. Let's first install openpyxl
  into our virtualenv:
| [shell]
| (myproject)apt12j$ pip install openpyxl
| [/shell]

| Let's write a simple script called ``openpyxl-version`` that
  demonstrates how to write Python programs that use the virtualenv:
| [python]
| #!/usr/bin/env python
| import openpyxl
| print openpyxl.\_\_version\_\_
| [/python]
| (N.B. that's \_\_version\_\_, with two underscores before and two
  underscores after.)

Note the ``#!/usr/bin/env python`` at the top of the script. This
well-known trick causes the first python in your PATH to be used. In our
case, the first python is the one in myproject/bin.

| Make the script executable and run it:
| [text]
| (myproject)apt12j$ chmod 755 openpxyl-version
| (myproject)apt12j$ ./openpxyl-version
| 1.5.2
| [/text]

Et voilà! We've now got a working virtualenv.

--------------

And now how about ipython? There are lots of blog posts about modifying
the ipython startup scripts. While those work, there are two other
approaches that I find much easier. The first is so easy that it's
almost not worth mentioning... except that I've never seen it in any
posts or documentation. Get ready for the big let down: just type
``python /usr/bin/ipython``. When you've activate'd as above, that
python refers to your virtualenv python and /usr/bin/ipython is the
standard script that imports IPython and starts the interactive shell.

| The second way is to create a script called ``myprojects/bin/ipython``
  with the following:
| [shell]
| #!/bin/sh
| echo ===== Using virtualenv ipython =====
| exec $(dirname "$0")/python /usr/bin/ipython ${1:+"$@"}
| [/shell]
| (Don't forget to make it executable or you'll get some other ipython,
  if such exists.)

| Invoke the ipython script and import openpyxl:
| [text]
| (myproject)apt12j$ ipython
| In [1]: import openpyxl
| In [2]: openpyxl.\_\_version\_\_
| Out[2]: '1.5.2'
| [/text]

There you have it: a complete, isolated sandbox in which packages may be
installed without affecting other virtualenvs, your system libraries, or
other users. Furthermore, this can be accomplished without special
permissions in a user's directory.
