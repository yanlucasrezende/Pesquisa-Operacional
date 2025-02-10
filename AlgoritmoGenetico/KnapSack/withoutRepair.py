import random

NUMBER_GENS = 6
SIZE_POPULATION = 4
BENEFIT_ARRAY = [ 10, 6, 11, 6, 9]
COST_ARRAY = [ 4, 2, 6, 3, 5]
MAX_WEIGHT = 14
CHOICES_SIZE = 5
TAXA_CROSSOVER = 0.9
TAXA_MUTATION = 0.1

# Esta implementacao do algoritmo genetico nao se da com reparo, ou seja,
# quando um individuo gerado nao atender as restricoes ele sera podera
# ter filhos porem nao sera inserido como melhor escolha caso nao haja solucao
# que atenda as restricoes

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
    for col in range(SIZE_POPULATION):
        pularParaProximaIteracao = False
        if pularParaProximaIteracao:
            continue
        if row == 0:
            indiv = Individuo([sortearValorPosicao() for i in range(CHOICES_SIZE)])
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

                if filho1.get_beneficio() > BEST_CHOICE.get_beneficio() and filho1.get_custo() <= MAX_WEIGHT:
                    BEST_CHOICE = filho1
                if filho2.get_beneficio() > BEST_CHOICE.get_beneficio() and filho2.get_custo() <= MAX_WEIGHT:
                    BEST_CHOICE = filho2

                matriz[row][indicesCasais[0]] = filho1
                matriz[row][indicesCasais[1]] = filho2
            else:
                matriz[row][col] = pai1
                matriz[row][col] = mae1

            if random.uniform(0, 1) <= TAXA_CROSSOVER:
                pontoCorte = random.randint(0, CHOICES_SIZE)
                filho3 = Individuo(pai2.get_escolha()[:pontoCorte] + mae2.get_escolha()[pontoCorte:])
                filho4 = Individuo(mae2.get_escolha()[:pontoCorte] + pai2.get_escolha()[pontoCorte:])

                if filho3.get_beneficio() > BEST_CHOICE.get_beneficio() and filho3.get_custo() <= MAX_WEIGHT:
                    BEST_CHOICE = filho3
                if filho4.get_beneficio() > BEST_CHOICE.get_beneficio() and filho4.get_custo() <= MAX_WEIGHT:
                    BEST_CHOICE = filho4

                matriz[row][indicesCasais[2]] = filho3
                matriz[row][indicesCasais[3]] = filho4
            else:
                matriz[row][col] = pai2
                matriz[row][col] = mae2
        pularParaProximaIteracao = True

print("Melhor escolha: ", BEST_CHOICE.get_escolha())
print("Beneficio: ", BEST_CHOICE.get_beneficio())
print("Custo: ", BEST_CHOICE.get_custo())
