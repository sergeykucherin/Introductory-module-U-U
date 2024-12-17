team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'
team1_name = "Мастера кода"
team2_name = "Волшебники данных"

"""
Использование %:
"""
# информацию на экран выводим в двойных кавычках как указано в примере решения к задаче
print('"В команде %s участников: %s!"' % (team1_name,team1_num))        # 1-й вариант записи кода
print('"В команде %s участников: %s%s"' % (team1_name,team1_num, '!')) # 2-й вариант записи кода
print('"Итого сегодня в командах участников: %s и %s!"' % (team1_num, team2_num))
# если при выводе на экран необходим пробел перед знаком ! - то для этого ставим пробел после %s, а также можно
# записать всё выражение другим способом %()s (c добавлением после % скобок и значений в них), которое до сих пор можно
#  встретить в написанных кодах:
print('"Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s !"' % {'team1_num': 5, 'team2_num': 6})

"""
Использование format():
"""
print('"Команда {} решила задач: {}!"'.format(team2_name, score_2))
print('"{team2_name} решили задачи за {team2_time}с !"'.format(team2_name="Волшебники данных", team2_time=2153.31451))

"""
Использование f-строк:
"""
print(f'"Команды решили {score_1} и {score_2} задач.”')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = "Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = "Победа команды Волшебники Данных!"
else:
    result = "Ничья!"
print(f'"результат битвы: {challenge_result.replace('Победа', 'победа')}"')
print(f'"Сегодня было решено {score_1 + score_2} задач, в среднем по {round((team1_time + team2_time) / 
                                                                        (score_1 + score_2), 1)} секунды на задачу!."')