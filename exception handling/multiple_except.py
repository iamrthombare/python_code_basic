try:
    d = {}
    d["x"]
except KeyError:
    print("specific")
except Exception:
    print("general")

#  Catching several types in one block
# except (ValueError, TypeError) as e:
#     print(e)
