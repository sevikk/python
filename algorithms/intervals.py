# Write a function that will take 2 segments as coordinates of their start and end on the plane (e.g. [[[0, 2], [3, 4]], [[10, 20], [-1, 3]]]) and return the coordinates of their intersection or, if the segments do not intersect, return 'No intersection'

def intersectionIntervals(intervals):
    intervals_list = intervals[0] + intervals[1]

    intervals_list.sort()

    result = [intervals_list[0]]

    for index, key in enumerate(intervals_list):

        current = intervals_list[index + 1]
        previous = result[len(result) - 1]

        if (current[0] <= previous[1]):
            return [previous, current]
        else:
            result = [current]
            continue
    return False


try:
    print(intersectionIntervals([[[0, 0], [3, 3]], [[4, 4], [6, 6]]]))
except IndexError as e:
    print("No intersection")
finally:
    print("Finally we are here")


# [[[0, 2], [3, 4]], [[10, 20], [-1, 3]]]#

# const segment1 = [[[0, 0], [4, 4]], [[4, 4], [6, 6]]]);
