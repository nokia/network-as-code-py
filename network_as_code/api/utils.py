from datetime import datetime

def convert_from_timestamp(ts):
    return datetime.fromtimestamp(ts)

def convert_to_timestamp(dt_obj):
    if isinstance(dt_obj, datetime.datetime):
        return int(dt_obj.timestamp())