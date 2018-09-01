import time
import webbrowser


break_count = 0
total_break = 3

print ("this program started on "+time.ctime())
while break_count < total_break:
    break_count += 1
    time.sleep(1)
    webbrowser.open("http://www.youtube.com")
    
