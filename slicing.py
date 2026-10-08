t = (10, 20, 30, 40, 50)

t[0]       # 10      first
t[-1]      # 50      last
t[1:4]     # (20, 30, 40)
t[:3]      # (10, 20, 30)
t[2:]      # (30, 40, 50)
t[::2]     # (10, 30, 50)    step
t[::-1]    # (50, 40, 30, 20, 10)   reversed
t[10]      # IndexError
t[10:20]   # ()  slicing never raises an error