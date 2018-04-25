import calendar

if __name__ == '__main__':
  #cal = calendar.Calendar()
  #class calendar.TextCalendar([firstweekday])
  m, d, y = list(map(int, input().split()))

  print("{} {} {}".format(m, d, y))
  #print(calendar.TextCalendar(firstweekday=6).formatyear(y))
  print(calendar.day_name[calendar.weekday(y, m, d)].upper())
  #c = calendar.TextCalendar(calendar.SUNDAY)
  #c.prmonth(2017, 7)
