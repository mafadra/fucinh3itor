import time

class handle_time:
    @staticmethod
    def convert_seconds_to_hms(seconds):
        from datetime import timedelta
        time_delta = timedelta(seconds=seconds)
        hours, remainder = divmod(time_delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return hours, minutes, seconds

    def estimated_time_fucinh3itor_consult(result_list_size, timeout):
        total_estimated_time = result_list_size * timeout
        return handle_time.convert_seconds_to_hms(total_estimated_time)

    def current_time(datetime_format):
        from datetime import datetime
        return datetime.now().strftime(datetime_format)

class timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.interval = self.end - self.start
    
    @property
    def fucinh3itor_execution_time_in_seconds(self):
        return int(self.interval)
