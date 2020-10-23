# -*- coding: utf-8 -*-

class Air:
    def __init__(self, temp):
        self.T = temp
    def getViscosity(self):
        return 1.72E-5*393/(self.T+120)*(self.T/273)**1.5
