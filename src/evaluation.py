import pandas as pd

def calculate_ctr(recommended, clicked):
    if not recommended:
        return 0.0
    return len(clicked) / len(recommended)

def calculate_watch_time(watch_times):
    if not watch_times:
        return 0.0
    return sum(watch_times) / len(watch_times)