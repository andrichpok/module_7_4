team_1 = 'Мастера кода'
team_2 = 'Волшебники данных'

def num(team1_num = 0, team2_num = 0):
    print('В команде %s участников: %s!' % (team_1, team1_num))
    print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

score_1 = 0
score_2 = 0
def score(team1_time = 0, team2_time = 0):
    print('Команда {} решила задач: {}!'.format (team_2, score_2))
    print('{} решили задачи за {} c!'.format (team_2, team2_time))



def challenge_result(tasks_total = 0, time_avg = 0):
    print(f'Команды решили {score_1} и {score_2} задач.')
    if score_1 > score_2:
        print(f'Результат битвы: победа команды {team_1}!')
    elif score_1 == score_2:
        print(f'Результат битвы: Ничья!')
    else:
        print(f'Результат битвы: победа команды {team_2}!')

    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу')


num(team1_num = 5,team2_num = 6)
score_1 = 40
score_2 = 42
score(team1_time = 1552.512, team2_time = 2153.31451)
challenge_result(tasks_total = 82, time_avg = 45.2)
#challenge_result = 'Победа команды Волшебники данных!'

