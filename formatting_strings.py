# use %
team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
count_team_members = f'"В команде {team1} участников: %d!"' % team1_num
count_team_members2 = '"Итого сегодня в командах участников: %d, %d!"' % (team1_num, team2_num)
# use format
score_1 = 40
score_2 = 42
count_score1 = '"Команда Мастера кода решила {} задач!"'.format(score_1)
count_score2 = '"Команда Волшебники данных решила задач: {}!"'.format(score_2)
team1_time = 1552.512
team2_time = 2153.31451
time_count1 = '"Мастера кода решили задачи за {} c!"'.format(round(team1_time, 1))
time_count2 = '"Волшебники данных решили задачи за {}c!"'.format(round(team2_time, 1))
# use f-строк
total_count_score = f'"Команды решили {score_1} и {score_2} задач.”'
task_total = score_1 + score_2
time_avg = (team1_time + team2_time)/task_total
time_avg1team = team1_time/ score_1
time_avg2team = team2_time/ score_2

if score_1 > score_2 or score_1 == score_2 and time_avg1team < time_avg2team:
    challenge_result = f'Победила команда {team1}!'
elif score_1 < score_2 or score_1 == score_2 and time_avg1team > time_avg2team:
    challenge_result = f'Победила команда {team2}!'
else:
    challenge_result = f'Ничья!'

task_total = score_1 + score_2
time_avg = (team1_time + team2_time)/task_total

print(count_team_members)
print(count_team_members2)
print(count_score1)
print(count_score2)
print(time_count1)
print(time_count2)
print(total_count_score)
print(challenge_result)
print(task_total, time_avg)
print(f'"Сегодня было решено всего {task_total} задачи, среднее время на решение одной задачи составило {time_avg}".')
