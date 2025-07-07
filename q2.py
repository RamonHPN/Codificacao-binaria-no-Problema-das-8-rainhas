import random
import time
from statistics import mean, stdev

# Parâmetros do Algoritmo Genético
POP_SIZE = 20
GENE_SIZE = 32  # 8 rainhas * 4 bits por coluna
NUM_QUEENS = 8
MAX_GENERATIONS = 1000
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.03
MAX_NO_COLLISIONS = 28  # Máximo de pares de rainhas que não se atacam

# Gera um indivíduo binário aleatório (32 bits)
def random_individual():
    return ''.join(random.choice('01') for _ in range(GENE_SIZE))

# Converte o indivíduo binário em uma lista de colunas (0 a 15)
def decode(ind):
    return [int(ind[i:i+4], 2) for i in range(0, GENE_SIZE, 4)]

# Avalia a aptidão (fitness) de um indivíduo com base nas colisões
def fitness(ind):
    board = decode(ind)
    conflicts = 0
    for i in range(NUM_QUEENS):
        for j in range(i + 1, NUM_QUEENS):
            if board[i] > 7 or board[j] > 7:  # penalidade se valor > 7
                conflicts += 1
            elif board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return MAX_NO_COLLISIONS - conflicts

# Seleção dos pais por roleta
def roulette_selection(pop, fits):
    total_fit = sum(fits)
    pick = random.uniform(0, total_fit)
    current = 0
    for ind, fit in zip(pop, fits):
        current += fit
        if current >= pick:
            return ind
    return pop[-1]

# Cruzamento de ponto único
def crossover(p1, p2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, GENE_SIZE - 1)
        return p1[:point] + p2[point:], p2[:point] + p1[point:]
    return p1, p2

# Mutação por bit flip
def mutate(ind):
    return ''.join(
        bit if random.random() > MUTATION_RATE else '1' if bit == '0' else '0'
        for bit in ind
    )

# Algoritmo Genético completo
def genetic_algorithm():
    population = [random_individual() for _ in range(POP_SIZE)]
    start = time.time()

    for generation in range(1, MAX_GENERATIONS + 1):
        fits = [fitness(ind) for ind in population]

        if MAX_NO_COLLISIONS in fits:
            best = population[fits.index(MAX_NO_COLLISIONS)]
            elapsed = time.time() - start
            return generation, elapsed, best

        # Elitismo: mantém os dois melhores
        sorted_pop = [ind for _, ind in sorted(zip(fits, population), reverse=True)]
        next_generation = sorted_pop[:2]

        # Reproduz até preencher a população
        while len(next_generation) < POP_SIZE:
            parent1 = roulette_selection(population, fits)
            parent2 = roulette_selection(population, fits)
            child1, child2 = crossover(parent1, parent2)
            next_generation.append(mutate(child1))
            if len(next_generation) < POP_SIZE:
                next_generation.append(mutate(child2))

        population = next_generation

    # Se não encontrou a solução ótima
    fits = [fitness(ind) for ind in population]
    best = population[fits.index(max(fits))]
    return MAX_GENERATIONS, time.time() - start, best

# Rodando 50 execuções
iterations = []
times = []
solutions = []

for _ in range(50):
    gen, exec_time, sol = genetic_algorithm()
    iterations.append(gen)
    times.append(exec_time)
    if sol not in solutions:
        solutions.append(sol)
    if len(solutions) >= 5:
        break

# Estatísticas
print("\n Estatísticas:")
print(f"Média de gerações: {mean(iterations):.2f}")
print(f"Desvio padrão das gerações: {stdev(iterations):.2f}")
print(f"Média do tempo: {mean(times):.4f} s")
print(f"Desvio padrão do tempo: {stdev(times):.4f} s")

# Mostrando as 5 melhores soluções distintas
print("\n 5 Melhores Soluções Distintas:")
for i, sol in enumerate(solutions[:5]):
    decoded = decode(sol)
    print(f"{i+1}: {sol} → {decoded}")
