class General():
    AVGS = []
    for i in range(2):
        n = float(input())
        sen, ghad, vazn = input().split(' '), input().split(' '), input().split(' ')
        kol = [sen, ghad, vazn]
        avg_kol = []
        for i in kol:
            sum = 0
            for j in i:
                sum += float(j)
            avg_kol.append(sum / n)
        AVGS.append(avg_kol)
    def avg(self):
        for i in self.AVGS:
            for j in i:
                print(j)
    def compare(self):
        if self.AVGS[0][1] > self.AVGS[1][1]:
            print('A')
        elif self.AVGS[0][1] < self.AVGS[1][1]:
            print('B')
        else:
            if self.AVGS[0][2] > self.AVGS[1][2]:
                print('B')
            elif self.AVGS[0][2] < self.AVGS[1][2]:
                print('A')
            else:
                print('Same')

x = General()
x.avg()
x.compare()