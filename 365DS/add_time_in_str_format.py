"""
This is a script to add all the duration in string format and then convert back to hour:min:sec format
* Split text and convert them to numbers again
"""
duration = ["2h 06m 18s",
            "2h 32m 07s",
            "1h 29m 44s",
            "1h 06m 51s",
            "0h 51m 56s",
            "0h 59m 38s",
            "2h 12m 22s",
            "0h 56m 35s",
            "1h 13m 10s",
            "2h 03m 30s",
            "0h 49m 28s",
            "1h 42m 49s",
            "1h 13m 07s",
            "1h 19m 52s",
            "1h 19m 24s",
            "1h 28m 45s",
            "1h 17m 24s",
            "0h 12m 00s",
            "1h 36m 13s",
            "1h 52m 23s",
            "2h 26m 52s",
            "1h 51m 16s",
            "2h 29m 02s",
            "1h 01m 06s",
            "0h 32m 07s",
            "0h 42m 11s",
            "0h 56m 31s",
            "1h 22m 16s"]
total_time = 0
for time in duration:
    h, m, s = time.split()
    total_time += int(h[:-1]) * 60 + int(m[:-1]) + int(s[:-1])/60

min = float(str(total_time/60)[str(total_time/60).index('.'):])*60
seconds = round(float(str(min)[str(min).index('.'):])*60)
print(f'{int(total_time)// 60}h {int(total_time%60)}m {seconds}s')
