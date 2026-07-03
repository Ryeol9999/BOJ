def solution(n):
    answer = 0
    three = ""
    while(n>0) :
        x = n%3 
        three += str(x)
        n = n//3
    for i in range(len(three)):
        answer += (3**((len(three)-1)-i)) * int(three[i])
    return answer