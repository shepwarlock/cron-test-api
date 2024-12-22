from datetime import datetime as dt

f = open("ok.txt", "a")
f.write(f"\n{dt.today()}")
f.close()
