import heapq
from typing import List
# Як останнє завдання, використався підхід з ООП :)
class CableMerger:
    def __init__(self, cable_lengths: List[int]):
        self.cable_lengths = cable_lengths

    def minimize_connection_cost(self) -> int:
        heapq.heapify(self.cable_lengths)
        total_cost = 0

        while len(self.cable_lengths) > 1:
            first_cable = heapq.heappop(self.cable_lengths)
            second_cable = heapq.heappop(self.cable_lengths)
            connection_cost = first_cable + second_cable
            total_cost += connection_cost
            heapq.heappush(self.cable_lengths, connection_cost)

        return total_cost

    @staticmethod
    def merge_k_lists(lists: List[List[int]]) -> List[int]:
        min_heap = []
        for index, sorted_list in enumerate(lists):
            if sorted_list:
                heapq.heappush(min_heap, (sorted_list[0], index, 0))
        
        merged_list = []
        while min_heap:
            value, list_index, element_index = heapq.heappop(min_heap)
            merged_list.append(value)
            if element_index + 1 < len(lists[list_index]):
                next_value = lists[list_index][element_index + 1]
                heapq.heappush(min_heap, (next_value, list_index, element_index + 1))

        return merged_list


cable_lengths = [1, 2, 10, 45, 12, 3, 14]
merger = CableMerger(cable_lengths)
print("Загальні витрати на з’єднання кабелів:", merger.minimize_connection_cost())

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = CableMerger.merge_k_lists(lists)
print("Відсортований список:", merged_list)