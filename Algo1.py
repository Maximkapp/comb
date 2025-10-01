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