def str2bool(v) -> bool:
    if v and isinstance(v, str):
        return v.lower() in ("yes", "true", "t", "1", "True")
    return False
