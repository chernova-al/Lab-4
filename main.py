# 7 вариант
# используем "жадный алгоритм"
bag = []
curr_count = float(2*4) # место в рюкзаке
points = 15 # исходное кол-во очков выживания
items = {'r': [3, 25],
         'p': [2, 15],
         'a': [2, 15],
         'm': [2, 20],
         'i': [1, 5],
         'k': [1, 15],
         'x': [3, 20],
         't': [1, 25],
         'f': [1, 15],
         'd': [1, 10],
         's': [2, 20],
         'c': [2, 20]
         }
for key in items:
    items[key].append(items[key][1]/items[key][0])
items = sorted(items.items(), key=lambda x: x[1][2])
items = items[::-1]
for key in items:
    if (curr_count - float(key[1][0])) >= 0:
        bag.append(key[0])
        curr_count = curr_count - float(key[1][0])
        points += float(key[1][1])
    else:
        points -= float(key[1][1])
print('Итоговые очки выживания:', int(points))
print(bag)
