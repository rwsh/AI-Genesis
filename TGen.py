# -*- coding: utf-8 -*-
"""
AI.Lector.ru

Автор: Р.В. Шамин
"""

import random as rnd

import numpy as np

class THrom():
    def __init__(self, N, Hrom):
        if Hrom == None:
            self.N = N
            self.Gen = list()
            for i in range(N):
                self.Gen.append(0)
        else:
            self.N = Hrom.N
            self.Gen = list()
            for i in range(N):
                self.Gen.append(Hrom.Gen[i])

    def Calc(self):
        x = self.Gen[0]
        y = self.Gen[1]
        z = self.Gen[2]

        return (1 - np.abs(x) + y - np.abs(z)) / (1 + x * x + y * y + z * z)
        
class TGenesis():
    def __init__(self, M):
        self.M = M
        self.Hroms = list()
        
        Hrom = THrom(3, None)
        Hrom.Gen = [0, 1, 2]
        self.Hroms.append(Hrom)

        Hrom = THrom(3, None)
        Hrom.Gen = [1, 2, 0]
        self.Hroms.append(Hrom)

        Hrom = THrom(3, None)
        Hrom.Gen = [2, 0, 1]
        self.Hroms.append(Hrom)

        Hrom = THrom(3, None)
        Hrom.Gen = [1, 0, 2]
        self.Hroms.append(Hrom)

        Hrom = THrom(3, None)
        Hrom.Gen = [2, 1, 0]
        self.Hroms.append(Hrom)
        
    def Calcs(self):
        F = list()
        i = 0
        for Hrom in self.Hroms:
            F.append([Hrom.Calc(), Hrom, i])
            i = i + 1
        
        rate = 1
        while(len(F) > 0):
            m = -1000
            for f in F:
                if f[0] > m:
                    m = f[0]
                    fd = f
            fd[1].rate = rate
            F.remove(fd)
            rate = rate + 1
            
    def GetHrom(self, rate, Num):
        for Hrom in self.Hroms:
            if Hrom.rate == rate:
                return Hrom.Gen[Num]
            
    def Generate(self):
        Hroms = list()
        
        Hrom = THrom(3, None)
        Hrom.Gen = [self.GetHrom(1, 0), self.GetHrom(2, 1), self.GetHrom(1, 2)]
        Hroms.append(Hrom)
        
        Hrom = THrom(3, None)
        Hrom.Gen = [self.GetHrom(2, 0), self.GetHrom(1, 1), self.GetHrom(1, 2)]
        Hroms.append(Hrom)
        
        Hrom = THrom(3, None)
        Hrom.Gen = [self.GetHrom(1, 0), self.GetHrom(1, 1), self.GetHrom(2, 2)]
        Hroms.append(Hrom)

        Hrom = THrom(3, None)
        Hrom.Gen = [self.GetHrom(2, 0), self.GetHrom(3, 1), self.GetHrom(4, 2)]
        Hroms.append(Hrom)
        
        Hrom = THrom(3, None)
        
        r1 = (rnd.random() - 0.5) / 1.0
        r2 = (rnd.random() - 0.5) / 1.0
        r3 = (rnd.random() - 0.5) / 1.0
        
        Hrom.Gen = [self.GetHrom(3, 0) + r1, self.GetHrom(2, 1) + r2, self.GetHrom(3, 2) + r3]
        Hroms.append(Hrom)
        
        self.Hroms = list()
        for Hrom in Hroms:
            self.Hroms.append(Hrom)
        
    def Type(self):
        for Hrom in self.Hroms:
            sol = Hrom.Calc()
            if Hrom.rate == 1:
                res = sol
            print(Hrom.rate.__str__() + ": x=" \
                  + Hrom.Gen[0].__str__() + " y=" + Hrom.Gen[1].__str__() + \
                  " z=" + Hrom.Gen[2].__str__() + " res =" + sol.__str__())
        return res
        

            
            
            