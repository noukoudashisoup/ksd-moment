import time

class ContextTimer(object):
    """
    A class used to time an execution of a code snippet. 
    Use it with with .... as ...
    For example, 

        with ContextTimer() as t:
            # do something 
        time_spent = t.secs

    From https://www.huyng.com/posts/python-performance-analysis
    """

    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start 
        if self.verbose:
            print('elapsed time: %f ms' % (self.secs*1000))

# end class ContextTimer

