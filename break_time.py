import webbrowser
import time

total_breaks = 3
breaks = 0

print "This program starts at " + time.ctime()
while breaks < total_breaks:
	time.sleep(5)
	webbrowser.open("https://www.youtube.com/watch?v=jqPxJp5OJW0")
	breaks += 1