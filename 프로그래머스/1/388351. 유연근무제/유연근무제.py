def solution(schedules, timelogs, startday):
    answer = 0
    number = len(schedules)
    for i in range(number):
        day = startday
        count = 0
        for j in range(7):
            ## 날짜 정하기            
            if day > 7:
                day = day - 7
            if 1<=day<=5:
               # t_l = timelogs[i][j]//100
               # scheduel = schedules[i]//100
               #  if t_l == scheduel:
               #      timelogs[i][j] - scheduel <=10:
               #      count +=1
               #  elif : t_l < scheduel:
               #      count +=1
               #  elif t_l
                if schedules[i] % 100 >= 50:
                    if timelogs[i][j]-schedules[i] <= 50:
                        count +=1
                else:
                    if timelogs[i][j]-schedules[i] <= 10:
                        count +=1
                ## scheduels 의나머지가 50이상이면
                
            day += 1
        print(count)
        if count == 5:
            answer += 1
    return answer