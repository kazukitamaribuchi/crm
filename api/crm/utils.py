import pytz


def utc_to_jst(timestamp_utc):
    datetime_jst = timestamp_utc.astimezone(pytz.timezone('Asia/Tokyo'))
    return datetime_jst
