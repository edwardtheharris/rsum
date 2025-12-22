import version_query

try:
    __version__ = version_query.query_version_str()
except Exception as exc:
    print(exc)
    __version__ = "0.0.1"
