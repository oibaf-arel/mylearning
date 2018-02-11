import time
import webbrowser

breaks = 0
print "This program started at " + time.ctime()
while breaks < 3:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=L-5M1_DKvb0")
    breaks = breaks + 1
    print "You have taken " + str(breaks) + " break(s)" 
