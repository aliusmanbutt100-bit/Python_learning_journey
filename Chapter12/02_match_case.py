def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case 500:
            return "Internal server error"
        case _:
            return "unknown error"
print(http_status(200))
print(http_status(404))
print(http_status(500))
print(http_status(700))
