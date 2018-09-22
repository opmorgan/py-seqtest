from threading import Timer


class Timer:

    def __init__(self, interval, function, args=[], kwargs={}):
        self._interval = interval
        self._function = function
        self._args = args
        self._kwargs = kwargs

    def start(self):
        t = Timer(self._interval, self._function, *self._args, **self._kwargs)
        t.start()
