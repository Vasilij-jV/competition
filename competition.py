# -*- config: utf8 -*-

team1_num = 7
team2_num = 7
score_1 = 34
score_2 = 37
team1_time = 1350.95732456
team2_time = 1674.984567


def winnig_team():
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        return 'победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team2_time > team1_time:
        return 'победа команды Волшебники данных!'
    else:
        return 'Ничья!'


challenge_result = winnig_team()


def final_results():
    tasks_total1 = score_1 + score_2
    time_avg1 = (team1_time + team2_time) / tasks_total1
    return tasks_total1, time_avg1


tasks_total, time_avg = final_results()

file_name = 'out_1.txt'
with open(file_name, mode='w', encoding='utf8') as file:
    #  Использование %
    file.write('В команде Мастера кода участников: %d !\n' % (team1_num))
    file.write('Итого сегодня в команде участников: %d и %d !' % (team1_num, team2_num))
    file.write('\n\n')

    #  Использование format()
    file.write('Команда Волшебники данных решила задач: {score_2:3d} !\n'.format(score_2=score_2))
    file.write('Волшебники данных решили задачи за: {team2_time:10.2f} !'.format(team2_time=team2_time))
    file.write('\n\n')

    #  Использование f-строк
    file.write(f'Команды решили {score_1:^4d} и {score_2:^4d} задач\n')
    file.write(f'Результат битвы: {challenge_result}\n')
    file.write(f'Сегодня было решено {tasks_total:^4d} задач, в среднем по {time_avg:^6.1f} секунды за задачу')
