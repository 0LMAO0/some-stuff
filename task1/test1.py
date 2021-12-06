import unittest


def analyse(programm: list[tuple[str, int]]) -> int:
    cnt = 0
    srtd_prog = sorted(programm, key= lambda package: package[1])               # сортировка списка по номеру контейнера
    for i in range(0, len(srtd_prog)-1):                                        # сортировка контейнеров по принципу: принять выгрузить номер
        for j in range(len(srtd_prog)-1):
            if (srtd_prog[j][0] == srtd_prog[j+1][0])\
            or (srtd_prog[j-1][1] == srtd_prog[j+1][1]):
                c = srtd_prog[j]
                srtd_prog[j] = srtd_prog[j+1]
                srtd_prog[j+1] = c
            
    for i in range(0,len(srtd_prog)-1):                                         # дополнительная сортировка для проверки
        for j in range(len(srtd_prog)-1):
            if srtd_prog[j][0] == srtd_prog[j+1][0] and \
                srtd_prog[j][1] > srtd_prog[j+1][1]:
                c = srtd_prog[j+1]
                srtd_prog[j+1] = srtd_prog[j]
                srtd_prog[j] = c

    for i in range(len(srtd_prog)):                                             # подсчет единиц энергии
        if srtd_prog[i][0] == "принять":
            cnt += 1
        elif srtd_prog[i][0] == "выгрузить":
            if srtd_prog[i][1] == srtd_prog[i-1][1]:
                cnt +=1           
    return cnt


class TestCase(unittest.TestCase):
    def test_analyse1(self):
        truth = analyse([('принять', 46),('выгрузить', 46),('принять', 21),
        ('выгрузить', 21),])
        self.assertEqual(truth, 4)
    def test_analyse2(self):
        truth = analyse([('принять', 1),('принять', 2),('выгрузить', 1),
        ('принять', 3),('принять', 4),('выгрузить', 3),])
        self.assertEqual(truth, 6)



if __name__ == "__main__":
    unittest.main()