#given intervals of time i.e start time and end time in minutes (to_minutes("15:35") # 15*60 + 35 = 935
#find minimum no. of rooms required so meetings don't overlap in one room
def min_meeting_rooms(lst):
    if not lst or not lst[0]:
        return None
    #sort starts and ends separate
    starts = sorted(t[0] for t in lst)
    ends = sorted(t[1] for t in lst)
    s, e = 0, 0
    rooms, max_rooms = 0, 0
    #while starts are there, if curr start > previous end room is vacated else room is needed
    while s < len(starts):
        if starts[s] < ends[e]:
            rooms += 1
            s += 1
            max_rooms = max(rooms, max_rooms)
        else:
            rooms -= 1
            e += 1
    return max_rooms
time_intervals = eval(input('Enter a nested list of time intervals: '))
print(min_meeting_rooms(time_intervals))

#TC: O(NlogN) : creating starts ref take O(N) + O(NlogN) + creating ends ref take O(N) + O(NlogN), s takes O(N) + e takes O(N)
#SC: O(N) : starts store sorted start times O(N), ends store sorted end times O(N), rest all store constant space O(1)