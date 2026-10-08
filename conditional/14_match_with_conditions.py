# Problem: Match with guards (conditions in match-case)
# Python 3.10+

score = 85

match score:
    case s if s >= 90:
        print("Excellent")
    case s if s >= 70:
        print("Good")
    case s if s >= 50:
        print("Average")
    case _:
        print("Needs improvement")