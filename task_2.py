from typing import List, Dict
from dataclasses import dataclass


@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int


@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int


def find_most_priority_job(print_jobs: List[Dict]) -> int:
    if len(print_jobs) == 1:
        return 0
    index = 0
    max_priority_job = print_jobs[index]["priority"]
    min_volume = print_jobs[index]["volume"]

    for i in range(1, len(print_jobs)):
        if print_jobs[i]["priority"] < max_priority_job:
            max_priority_job = print_jobs[i]["priority"]
            min_volume = print_jobs[i]["volume"]
            index = i
        if (
            print_jobs[i]["priority"] == max_priority_job
            and print_jobs[i]["volume"] < min_volume
        ):
            min_volume = print_jobs[i]["volume"]
            index = i

    return index


def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    """
    Оптимізує чергу 3D-друку згідно з пріоритетами та обмеженнями принтера

    Args:
        print_jobs: Список завдань на друк
        constraints: Обмеження принтера

    Returns:
        Dict з порядком друку та загальним часом
    """
    current_print_jobs = print_jobs.copy()
    total_time = 0
    total_volume = 0
    print_order = []

    while total_volume <= constraints["max_volume"] or len(current_print_jobs) >= 1:
        current_job_index = find_most_priority_job(current_print_jobs)
        if (
            total_volume + current_print_jobs[current_job_index]["volume"]
            > constraints["max_volume"]
        ):
            break
        print_order.append(current_print_jobs[current_job_index]["id"])
        total_time += current_print_jobs[current_job_index]["print_time"]
        total_volume += current_print_jobs[current_job_index]["volume"]
        current_print_jobs.pop(current_job_index)

    return {"print_order": print_order, "total_time": total_volume}


# Тестування
def test_printing_optimization():
    # Тест 1: Моделі однакового пріоритету
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150},
    ]

    # Тест 2: Моделі різних пріоритетів
    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},  # лабораторна
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},  # дипломна
        {
            "id": "M3",
            "volume": 120,
            "priority": 3,
            "print_time": 150,
        },  # особистий проєкт
    ]

    # Тест 3: Перевищення обмежень об'єму
    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120},
    ]

    constraints = {"max_volume": 300, "max_items": 2}

    print("Тест 1 (однаковий пріоритет):")
    result1 = optimize_printing(test1_jobs, constraints)
    print(f"Порядок друку: {result1['print_order']}")
    print(f"Загальний час: {result1['total_time']} хвилин")

    print("\nТест 2 (різні пріоритети):")
    result2 = optimize_printing(test2_jobs, constraints)
    print(f"Порядок друку: {result2['print_order']}")
    print(f"Загальний час: {result2['total_time']} хвилин")

    print("\nТест 3 (перевищення обмежень):")
    result3 = optimize_printing(test3_jobs, constraints)
    print(f"Порядок друку: {result3['print_order']}")
    print(f"Загальний час: {result3['total_time']} хвилин")


if __name__ == "__main__":
    test_printing_optimization()
