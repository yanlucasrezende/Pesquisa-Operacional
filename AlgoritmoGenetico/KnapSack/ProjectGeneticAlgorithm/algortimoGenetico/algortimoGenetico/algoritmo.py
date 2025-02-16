import random
from itertools import product

MAX_WEIGHT = 14
BENEFIT_ARRAY = [10, 6, 11, 6, 9]
COST_ARRAY = [4, 2, 6, 3, 5]

def algoritmo_forca_bruta():
    class Individuo:
        def __init__(self, choice):
            self.choice = choice
            self.beneficio = self.fitnessFunction()
            self.custo = self.calcularCusto()
        
        def get_beneficio(self):
            return self.beneficio

        def get_custo(self):
            return self.custo

        def get_escolha(self):
            return self.choice
        
        def recalcular_individuo(self):
            self.beneficio = self.fitnessFunction()
            self.custo = self.calcularCusto()
        
        def __str__(self):
            itens = [
                f"Item {i+1}: {'Sim' if val == 1 else 'Não'}"
                for i, val in enumerate(self.choice)
            ]
            return (
                f"Escolha: [ {', '.join(itens)} ]\n"
                f"Benefício: {self.beneficio}\n"
                f"Custo: {self.custo}"
            )

        def fitnessFunction(self):
            return sum(BENEFIT_ARRAY[i] for i, val in enumerate(self.choice) if val == 1)

        def calcularCusto(self):
            return sum(COST_ARRAY[i] for i, val in enumerate(self.choice) if val == 1)

    melhor_individuo = Individuo([0, 0, 0, 0, 0])
    # Esse product funciona testando todas as combinacoes entre [0,1] para 5 posicoes, evitar for aninhado
    for combinacao in product([0, 1], repeat=5):
        indiv = Individuo(list(combinacao))
        
        if indiv.custo <= MAX_WEIGHT:
            if (indiv.beneficio > melhor_individuo.beneficio or 
                (indiv.beneficio == melhor_individuo.beneficio and indiv.custo < melhor_individuo.custo)):
                melhor_individuo = indiv
    
    return str(melhor_individuo)

if __name__ == "__main__":
    print(algoritmo_forca_bruta())