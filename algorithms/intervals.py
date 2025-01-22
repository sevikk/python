# Write a function that will take 2 segments as coordinates of their start and end on the plane
# (e.g. [[[0, 2], [3, 4]], [[10, 20], [-1, 3]]])
# and return the coordinates of their intersection or, if the segments do not intersect, return 'No intersection'

def intervalsIntersection(intervals):
    intervals_list = intervals[0] + intervals[1]

    intervals_list.sort()

    result = [intervals_list[0]]

    for index, key in enumerate(intervals_list):
        if len(intervals_list) <= index:
            current = intervals_list[index + 1]
            previous = result[len(result) - 1]

            if current[0] <= previous[1]:
                return [previous, current ]
            else:
                result = [current]
    return "No intersection"


print(intervalsIntersection([[[0, 0], [3, 3]], [[4, 4], [6, 6]]]))


# [[[0, 2], [3, 4]], [[10, 20], [-1, 3]]]#

#const segment1 = [[[0, 0], [4, 4]], [[4, 4], [6, 6]]]);
