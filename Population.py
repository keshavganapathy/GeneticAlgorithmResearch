from Individual import Individual
import numpy
import random


class Population:
    popSize = 0
    individuals = []
    fittestScore = 0

    def __init__(self, popsize):
        self.popSize = popsize
        self.individuals = numpy.empty(popsize, dtype=Individual)

    def selectFittest(self):
        total = 0
        for i in range(len(self.individuals)):
            total = total + self.individuals[i].getFitness()
        arr = numpy.empty(100, dtype=object)
        holder = 0
        for individual in self.individuals:
            for x in range(int(individual.getFitness() * 100 / total)):
                arr[holder] = individual.getFitness()
                holder = holder + 1
        winnerIndex = random.randrange(0, 99)
        fit = arr[winnerIndex]
        self.fittestScore = self.individuals[self.getIndex(fit)].getFitness()
        return self.individuals[self.getIndex(fit)]

    def selectSecondFittest(self):
        total = 0
        for i in range(len(self.individuals)):
            if(self.individuals[i].getFitness() != self.fittestScore):
                total = total + self.individuals[i].getFitness()
        arr = numpy.empty(100, dtype=object)
        holder = 0
        for individual in self.individuals:
            if individual.getFitness() != self.fittestScore:
                for x in range(int(individual.getFitness() * 100 / total)):
                    arr[holder] = individual.getFitness()
                    holder = holder + 1
        winnerIndex = random.randrange(0, 99)
        fit = arr[winnerIndex]
        return self.individuals[self.getIndex(fit)]

    def getLeastFittestIndex(self):
        minFitVal = self.individuals[0].getFitness()
        minFitIndex = 0
        for i in range(len(self.individuals)):
            if minFitVal >= self.individuals[i].getFitness():
                minFitVal = self.individuals[i].getFitness()
                minFitIndex = i
        return minFitIndex

    def getIndex(self, fitness):
        for i in range(len(self.individuals)):
            if self.individuals[i].getFitness() == fitness:
                return i
        return 0

    def getFittestIndex(self):
        maxFit = 0
        maxFitIndex = 0
        for i in range(len(self.individuals)):
            if maxFit <= self.individuals[i].getFitness():
                maxFit = self.individuals[i].getFitness()
                maxFitIndex = i
        return maxFitIndex

    def getPopSize(self):
        return self.popSize

    def setPopSize(self, popsize):
        self.popSize = popsize

    def getIndividuals(self):
        return self.individuals

    def getFittestScore(self):
        return self.fittestScore

    def setFittestScore(self):
        self.fittestScore = 0
        for individual in self.individuals:
            if individual.getFitness() > self.fittestScore:
                self.fittestScore = individual.getFitness()
