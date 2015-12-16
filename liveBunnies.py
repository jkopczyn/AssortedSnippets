def answer(meetings):
    meetings.sort(None, lambda x: x[1])
    highest = 0
    most = 0
    for start, end in meetings:
        if start >= highest:
            most +=1
            highest = end
    return most
