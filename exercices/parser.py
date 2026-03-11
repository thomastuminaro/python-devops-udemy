def parse_log_line(log_line: str) -> dict | None:
    try:
        splitted = log_line.split(" ")
        timestamp = splitted[0]
        level = splitted[1]
        msg = splitted[2:]
        if not timestamp or not level or not msg:
            return None
        elif level[0] != "[" or level[-1] != "]":
            return None
        else:
            return {
                'timestamp': timestamp,
                'log_level': level.strip("[]"),
                'message': (" ").join(msg)
            }
    except Exception as e:
        return None

if __name__ == "__main__":
    log = "2024-05-20T14:00:05Z [ERROR] Failed to connect to database." 
    print(parse_log_line(log))
