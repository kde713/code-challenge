from typing import List


def solution(interval_list: List[tuple]) -> List[tuple]:
    interval_list.sort()

    merged_list = []
    merged_interval = list(interval_list.pop(0))

    for current_interval in interval_list:
        if current_interval[0] <= merged_interval[1]:
            merged_interval[1] = max(merged_interval[1], current_interval[1])
        else:
            merged_list.append(tuple(merged_interval))
            merged_interval = list(current_interval)

    merged_list.append(tuple(merged_interval))

    return merged_list
