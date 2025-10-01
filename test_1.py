import random
import time


def gale_shapley(men_preferences, women_preferences):
    n = len(men_preferences)
    men_free = [True] * n
    women_free = [True] * n
    women_partner = [-1] * n  # Индексы партнеров для женщин (-1 - нет партнера)
    men_partner = [-1] * n  # Индексы партнеров для мужчин (-1 - нет партнера)

    # Для каждой женщины, индексы мужчин, которых она предпочитает
    women_ranking = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            women_ranking[i][women_preferences[i][j]] = j

    while any(men_free):
        for i in range(n):
            if men_free[i]:
                # Выбираем женщину с наибольшим приоритетом, которой еще не предложили
                for j in range(n):
                    woman = men_preferences[i][j]
                    if women_partner[woman] == -1:  # Если женщина свободна
                        # Связываем мужчину и женщину
                        women_partner[woman] = i
                        men_partner[i] = woman
                        men_free[i] = False
                        break
                    else:
                        current_partner = women_partner[woman]
                        # Если женщина предпочитает текущего партнера
                        if women_ranking[woman][i] < women_ranking[woman][current_partner]:
                            # Женщина отклоняет текущего партнера и выбирает нового
                            women_partner[woman] = i
                            men_partner[i] = woman
                            men_free[i] = False
                            men_free[current_partner] = True
                            break
    return men_partner, women_partner


def generate_random_preferences(n):
    """Генерация случайных предпочтений для мужчин и женщин."""
    men_preferences = [random.sample(range(n), n) for _ in range(n)]
    women_preferences = [random.sample(range(n), n) for _ in range(n)]
    return men_preferences, women_preferences


def test_basic_case():
    """Тест с минимальными данными."""
    men_preferences = [[1, 0]]
    women_preferences = [[0, 1]]

    men_partner, women_partner = gale_shapley(men_preferences, women_preferences)

    print("Тест с минимальными данными:")
    print(f"Мужчины: {men_partner}")
    print(f"Женщины: {women_partner}")
    print()


def test_medium_case():
    """Тест с 4 мужчинами и 4 женщинами."""
    men_preferences = [[1, 0, 2, 3], [0, 1, 2, 3], [2, 1, 0, 3], [3, 0, 1, 2]]
    women_preferences = [[0, 1, 2, 3], [1, 0, 3, 2], [2, 3, 1, 0], [3, 0, 1, 2]]

    men_partner, women_partner = gale_shapley(men_preferences, women_preferences)

    print("Тест с 4 участниками:")
    print(f"Мужчины: {men_partner}")
    print(f"Женщины: {women_partner}")
    print()


def test_large_case(n=1000):
    """Тест с большими данными (1000 мужчин и женщин)."""
    men_preferences, women_preferences = generate_random_preferences(n)

    start_time = time.time()
    men_partner, women_partner = gale_shapley(men_preferences, women_preferences)
    end_time = time.time()

    print(f"Тест с {n} участниками:")
    print(f"Время выполнения: {end_time - start_time:.4f} секунд")
    print()


# Выполнение тестов
test_basic_case()
test_medium_case()
test_large_case(1000)