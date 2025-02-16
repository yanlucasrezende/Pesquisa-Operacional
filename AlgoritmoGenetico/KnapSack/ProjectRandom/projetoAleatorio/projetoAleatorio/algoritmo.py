import random

BENEFIT_ARRAY = [10, 6, 11, 6, 9]
COST_ARRAY = [4, 2, 6, 3, 5]

def algoritmo_random():
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
            # Formata a lista de escolhas com Sim/Não
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

    def sortearValorPosicao():
        return 1 if random.uniform(0, 1) > 0.5 else 0

    # Gera a lista de escolhas
    escolhas = [sortearValorPosicao() for _ in range(5)]
    indiv = Individuo(escolhas)
    
    return str(indiv)

if __name__ == "__main__":
    print(algoritmo_random())