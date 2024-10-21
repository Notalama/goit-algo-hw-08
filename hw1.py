import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)
        cost = cable1 + cable2
        total_cost += cost
        heapq.heappush(cables, cost)

    return total_cost

cables = [2, 3, 4, 5, 6]
min_cost = min_cost_to_connect_cables(cables)
print("Мінімальна вартість з'єднання кабелів:", min_cost)  # Виведе 45