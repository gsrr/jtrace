# jtrace
[Reference]

1. http://code.activestate.com/recipes/576515/

2. https://pymotw.com/2/sys/tracing.html

[Installation]

python setup.py install

[usage]

1. Import the module 

2. Call listen() at any point during startup.

3. For a debugger to support multiple threads, it must be registered using settrace() for each thread being debugged.

4. send signal : kill -SIGUSR1 $pid  
