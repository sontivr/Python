import sys
#import calendar
#from datetime import datetime, tzinfo, timezone, timedelta
from datetime import datetime

def time_delta(t1, t2):
    # Complete this function
    return abs(int((datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z") - datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")).total_seconds()))

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1, t2)
        print(delta)
        #t1_month = int([print(k) for k, v in enumerate(calendar.month_abbr) if v == t1[2]])
        #t2_month = int([print(k) for k, v in enumerate(calendar.month_abbr) if v == t2[2]])
        #{print(k, v) for k, v in enumerate(calendar.month_abbr)}
        #t = datetime(int(t1[3]), t1_month, int(t1[1]), time(t1[4]).hours, 
        #t10 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
        #t20 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
        #print(t1[2])
        #print(t1_month)
        #print(t10)


#Sun 10 May 2015 13:54:36 -0700
#Sun 10 May 2015 13:54:36 -0000
