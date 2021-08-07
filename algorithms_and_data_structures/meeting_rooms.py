"""
Meeting Rooms  - CodePro problem 34 (www.techseries.dev)
"""
import heapq


def are_overlapping(time_range_1, time_range_2):
    """
    not overlapping case 1:
            *---*
      *---*
    not overlapping case 2:
        *---*
              *---*

    :return not case 1 and not case 2
    """
    return not time_range_1[0] >= time_range_2[1] and not time_range_1[1] <= time_range_2[0]


def get_rooms_needed(schedules):
    booked = set()
    rooms_count = 1
    for s in schedules:
        for b in booked:
            if are_overlapping(b, s):
                rooms_count += 1
                break
        booked.add(s)
    return rooms_count


print(get_rooms_needed([(0, 10), (10, 20)]))
# 1
print(get_rooms_needed([(0, 50), (10, 21), (20, 30)]))
# 2


def meeting_rooms(meetings):
    meetings.sort(key=lambda x: x[0])
    print(meetings)
    meeting_ends = []
    max_rooms = 0

    for meeting in meetings:
        while meeting_ends and meeting_ends[0] <= meeting[0]:
            heapq.heappop(meeting_ends)
        heapq.heappush(meeting_ends, meeting[1])
        max_rooms = max(max_rooms, len(meeting_ends))
        print(meeting_ends, max_rooms)
    return max_rooms


print(meeting_rooms([[0, 10], [10, 20]]))
# 1

print(meeting_rooms([[20, 30], [10, 21], [0, 50]]))
# 3
