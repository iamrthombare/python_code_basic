# Problem: Pattern matching (Python 3.10+)
# Match a command and execute appropriate action

command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "restart":
        print("Restarting...")
    case _:
        print("Unknown command")