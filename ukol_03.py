import json
with open('body.json', encoding='utf-8') as file:
    pisemka = json.load(file)
#print(pisemka)

hodnoceni = {}
for student in pisemka:
    if pisemka[student] >= 60:
        hodnoceni[student] = "Pass"
    else:
        hodnoceni[student] = "Fail"

# print(hodnoceni)

with open('prospech.json', mode='w', encoding='utf-8') as out_file:
    json.dump(hodnoceni, out_file, indent=4, ensure_ascii=False)

# Bonus
with open('bonusy.json', encoding='utf-8') as file:
    bonusove_body = json.load(file)

#print(bonusove_body)

body_celkem = {}
for student in pisemka:
    if student in bonusove_body:
        body_celkem[student] = pisemka[student] + bonusove_body[student]
    else:
        body_celkem[student] = pisemka[student]

#print(body_celkem)

znamky_studentu = {}
for student in body_celkem:
    if body_celkem[student] <= 29:
        znamky_studentu[student] = 5
    elif body_celkem[student] <= 49:
        znamky_studentu[student] = 4
    elif body_celkem[student] <= 69:
        znamky_studentu[student] = 3
    elif body_celkem[student] <= 89:
        znamky_studentu[student] = 2
    else:
        znamky_studentu[student] = 1 

#print(znamky_studentu)

with open('znamky.json', mode='w', encoding='utf-8') as out_file:
    json.dump(znamky_studentu, out_file, indent=4, ensure_ascii=False)