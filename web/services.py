from massagemanager.redis import get_redis_client


def filter_sessions(sessions_qs, filters: dict):
    if filters["date"]:
        sessions_qs = sessions_qs.filter(session_date__gte=filters["date"])

    if filters["index"]:
        sessions_qs = sessions_qs.filter(session_index=filters["index"])

    if filters["type"]:
        sessions_qs = sessions_qs.filter(massage_type=filters["type"])

    return sessions_qs


def get_stat():
    redis = get_redis_client()
    keys = redis.keys("stat_*")
    return [
        (key.decode().replace("stat_", ""), redis.get(key).decode()) for key in keys
    ]
