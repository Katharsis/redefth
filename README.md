redefth v0.2
============

Redefines each theorems in single or multiple files or the all *.miz in MML base.

How to use:
===========
For the first 10 files:
<pre>python redefth.py 10</pre>

For the all files from MML directory:
<pre>python redefth.py -a</pre>

For the single file (without *.miz extension):
<pre>python redefth.py -f filename</pre>

Remember to set up mmlPath, everylabPath and textPath inside of the script.

Requirments:
============
[Mizar 7.12+](http://mizar.org/), [Python 2.5+](http://python.org/), [lxml 2.3+](http://lxml.de/), everylab (which is not included with Mizar binary files)
