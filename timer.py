from datetime import datetime, timedelta
from threading import Timer, Lock

# A reusable thread safe timer implementation
class RepeatableTimer(object):
    

    def __init__(self, interval_sec, function, *args, **kwargs):

        #Create a timer object which can be restarted
        self._interval_sec = interval_sec
        self._function = function
        self._args = args
        self._kwargs = kwargs
        # Locking is needed since the '_timer' object might be replaced in a different thread
        self._timer_lock = Lock()
        self._timer = None
        self._now = datetime.today()
        self._time_started = None
        self._elapsed_time = None

    # Starts the timer and returns this object [e.g. my_timer = TimerEx(10, my_func).start()]
    # param restart_if_alive: 'True' to start a new timer if current one is still alive
    # return: This timer object (i.e. self)
    def start(self, restart_if_alive=True):
        with self._timer_lock:
            # Current timer still running
            if self._timer is not None:
                if not restart_if_alive:
                    # Keep the current timer
                    return self
                # Cancel the current timer
                self._timer.cancel()
            # Create new timer
            self._timer = Timer(self._interval_sec, self._function) 
            self._timer.start()
            self._time_started = datetime.today()
            self._elapsed_time = self._time_started + timedelta(seconds=self._interval_sec)
            # Alternative timer is time.perf_counter() to check if how much your code to run
        # Return this object to allow single line timer start
        return self

    # Cancels the current timer if alive
    def cancel(self):
        with self._timer_lock:
            if self._timer is not None:
                self._timer.cancel()
                self._timer = None

    # return: True if current timer is alive (i.e not elapsed yet)
    def is_alive(self):
        with self._timer_lock:
            if self._timer is not None:
                return self._timer.is_alive()
        return False
        
    def get_remaining_time(self):
        self._remaining_time = self._elapsed_time - datetime.today()
        return round(self._remaining_time.total_seconds())