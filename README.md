# 🧬 Algoritmo Genético — Problema das 8 Rainhas (Codificação Binária)

Este projeto implementa um **algoritmo genético em Python** para resolver o clássico **Problema das Oito Rainhas**, utilizando **codificação binária** para representar indivíduos e os seguintes parâmetros:

---

## ✅ Requisitos Atendidos

### ✳️ Representação
- Cada indivíduo representa uma solução como uma string de **32 bits** (8 rainhas × 4 bits por posição).
- Cada rainha está posicionada em uma linha, e seu valor binário indica a **coluna (0 a 15)**. Apenas valores **0 a 7** são válidos. Valores maiores são penalizados.

---

### ⚙️ Parâmetros do Algoritmo

| Parâmetro                  | Valor                                  |
|---------------------------|----------------------------------------|
| Tamanho da população      | 20                                     |
| Representação             | Codificação binária (32 bits)          |
| Seleção dos pais          | Roleta (Roleta Viciada)                |
| Cruzamento                | Um ponto de corte                      |
| Taxa de cruzamento        | 80%                                    |
| Mutação                   | Bit flip                               |
| Taxa de mutação           | 3%                                     |
| Seleção de sobreviventes  | Elitismo (2 melhores por geração)      |
| Critérios de parada       | Solução ótima ou 1000 gerações         |

---

## 🎯 Função Objetivo

A **função de aptidão** (fitness) avalia o número de **colisões entre rainhas**. O número máximo de pares possíveis entre 8 rainhas é 28. O objetivo é **minimizar as colisões**, portanto:
fitness = 28 - número de colisões

---

## 📈 Estatísticas Geradas

Durante a execução, o algoritmo:
- Roda **50 vezes**.
- Calcula:
  - Média e desvio padrão do número de gerações até convergência.
  - Média e desvio padrão do tempo de execução.
- Armazena as **cinco melhores soluções distintas** encontradas (com 0 colisões).

---

## 📦 Estrutura do Código

- `random_individual()`: gera um indivíduo de 32 bits.
- `decode(ind)`: converte o binário em posições de coluna.
- `fitness(ind)`: calcula número de colisões.
- `roulette_selection()`: implementa seleção dos pais por roleta.
- `crossover()`: faz cruzamento de um ponto.
- `mutate()`: faz mutação bit a bit com 3% de chance.
- `genetic_algorithm()`: roda o algoritmo completo até o critério de parada.

---

## ▶️ Como Executar

### Pré-requisitos

- Python 3.x
- Nenhuma biblioteca externa necessária.

### Rodar o algoritmo

```bash
python q2.py
