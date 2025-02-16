import random
from itertools import product

NUMBER_GENS = 6
SIZE_POPULATION = 4
BENEFIT_ARRAY = [ 10, 6, 11, 6, 9]
COST_ARRAY = [ 4, 2, 6, 3, 5]
MAX_WEIGHT = 14
CHOICES_SIZE = 5
TAXA_CROSSOVER = 0.9
TAXA_MUTATION = 0.1

def algoritmo_forca_bruta():
    class Individuo:
        def __init__(self, choice):
            self.choice = choice
            self.beneficio = fitnessFunction(self)
            self.custo = calcularCusto(self)
        
        def get_beneficio(self):
            return self.beneficio

        def get_custo(self):
            return self.custo

        def get_escolha(self):
            return self.choice
        
        def recalcular_individuo(self):
            self.beneficio = fitnessFunction(self)
            self.custo = calcularCusto(self)

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

    def fitnessFunction(individuo):
        beneficio = 0
        for valuePosi in range(len(individuo.choice)):
            if individuo.choice[valuePosi] == 1:
                beneficio += BENEFIT_ARRAY[valuePosi]
        return beneficio

    def calcularCusto(individuo):
        custo = 0
        for valuePosi in range(len(individuo.choice)):
            if individuo.choice[valuePosi] == 1:
                custo += COST_ARRAY[valuePosi]
        return custo

    def sortearValorPosicao():
        x = random.uniform(0, 1)
        return 1 if x > 0.5 else 0

    BEST_CHOICE = Individuo([0, 0, 0, 0, 0])

    matriz = [[None for _ in range(SIZE_POPULATION)] for _ in range(NUMBER_GENS)]


    for row in range(NUMBER_GENS):
        pularParaProximaIteracao = False
        for col in range(SIZE_POPULATION):
            if pularParaProximaIteracao:
                continue
            if row == 0:
                indiv = Individuo([sortearValorPosicao() for i in range(CHOICES_SIZE)])
                # REPARO
                while indiv.get_custo() > MAX_WEIGHT:
                    bitInversao = random.randint(0, CHOICES_SIZE-1)
                    if indiv.get_escolha()[bitInversao] == 1:
                        indiv.get_escolha()[bitInversao] = 0
                    indiv.recalcular_individuo()
                # FIM REPARO
                if indiv.get_beneficio() > BEST_CHOICE.get_beneficio() and indiv.get_custo() <= MAX_WEIGHT:
                    BEST_CHOICE = indiv
                matriz[row][col] = indiv
            else:
                indicesCasais = random.sample(range(SIZE_POPULATION), SIZE_POPULATION)
                pai1 = matriz[row-1][indicesCasais[0]]
                mae1 = matriz[row-1][indicesCasais[1]]

                pai2 = matriz[row-1][indicesCasais[2]]
                mae2 = matriz[row-1][indicesCasais[3]]

                if random.uniform(0, 1) <= TAXA_MUTATION:
                    indiceMutation = random.randint(0, CHOICES_SIZE-1)
                    pai1.get_escolha()[indiceMutation] = 1 if pai1.get_escolha()[indiceMutation] == 0 else 0
                
                if random.uniform(0, 1) <= TAXA_MUTATION:
                    indiceMutation = random.randint(0, CHOICES_SIZE-1)
                    mae1.get_escolha()[indiceMutation] = 1 if mae1.get_escolha()[indiceMutation] == 0 else 0

                if random.uniform(0, 1) <= TAXA_MUTATION:
                    indiceMutation = random.randint(0, CHOICES_SIZE-1)
                    pai2.get_escolha()[indiceMutation] = 1 if pai2.get_escolha()[indiceMutation] == 0 else 0

                if random.uniform(0, 1) <= TAXA_MUTATION:
                    indiceMutation = random.randint(0, CHOICES_SIZE-1)
                    mae2.get_escolha()[indiceMutation] = 1 if mae2.get_escolha()[indiceMutation] == 0 else 0
                
                if random.uniform(0, 1) <= TAXA_CROSSOVER:
                    pontoCorte = random.randint(0, CHOICES_SIZE)
                    filho1 = Individuo(pai1.get_escolha()[:pontoCorte] + mae1.get_escolha()[pontoCorte:])
                    filho2 = Individuo(mae1.get_escolha()[:pontoCorte] + pai1.get_escolha()[pontoCorte:])

                    # REPARO FILHO 1
                    while filho1.get_custo() > MAX_WEIGHT:
                        bitInversao = random.randint(0, CHOICES_SIZE-1)
                        if filho1.get_escolha()[bitInversao] == 1:
                            filho1.get_escolha()[bitInversao] = 0
                        filho1.recalcular_individuo()
                    # FIM REPARO FILHO 1

                    # REPARO FILHO 2
                    while filho2.get_custo() > MAX_WEIGHT:
                        bitInversao = random.randint(0, CHOICES_SIZE-1)
                        if filho2.get_escolha()[bitInversao] == 1:
                            filho2.get_escolha()[bitInversao] = 0
                        filho2.recalcular_individuo()
                    # FIM REPARO FILHO 2

                    if filho1.get_beneficio() > BEST_CHOICE.get_beneficio() and filho1.get_custo() <= MAX_WEIGHT:
                        BEST_CHOICE = filho1
                    if filho2.get_beneficio() > BEST_CHOICE.get_beneficio() and filho2.get_custo() <= MAX_WEIGHT:
                        BEST_CHOICE = filho2

                    matriz[row][indicesCasais[0]] = filho1
                    matriz[row][indicesCasais[1]] = filho2
                else:
                    matriz[row][indicesCasais[0]] = pai2
                    matriz[row][indicesCasais[1]] = mae2

                if random.uniform(0, 1) <= TAXA_CROSSOVER:
                    pontoCorte = random.randint(0, CHOICES_SIZE)
                    filho3 = Individuo(pai2.get_escolha()[:pontoCorte] + mae2.get_escolha()[pontoCorte:])
                    filho4 = Individuo(mae2.get_escolha()[:pontoCorte] + pai2.get_escolha()[pontoCorte:])

                    # REPARO FILHO 3
                    while filho3.get_custo() > MAX_WEIGHT:
                        bitInversao = random.randint(0, CHOICES_SIZE-1)
                        if filho3.get_escolha()[bitInversao] == 1:
                            filho3.get_escolha()[bitInversao] = 0
                        filho3.recalcular_individuo()
                    # FIM REPARO FILHO 3

                    # REPARO FILHO 4
                    while filho4.get_custo() > MAX_WEIGHT:
                        bitInversao = random.randint(0, CHOICES_SIZE-1)
                        if filho4.get_escolha()[bitInversao] == 1:
                            filho4.get_escolha()[bitInversao] = 0
                        filho4.recalcular_individuo()
                    # FIM REPARO FILHO 4

                    if filho3.get_beneficio() > BEST_CHOICE.get_beneficio() and filho3.get_custo() <= MAX_WEIGHT:
                        BEST_CHOICE = filho3
                    if filho4.get_beneficio() > BEST_CHOICE.get_beneficio() and filho4.get_custo() <= MAX_WEIGHT:
                        BEST_CHOICE = filho4

                    matriz[row][indicesCasais[2]] = filho3
                    matriz[row][indicesCasais[3]] = filho4
                else:
                    matriz[row][indicesCasais[2]] = pai2
                    matriz[row][indicesCasais[3]] = mae2
        pularParaProximaIteracao = True
    return str(BEST_CHOICE)

if __name__ == "__main__":
    print(algoritmo_forca_bruta())