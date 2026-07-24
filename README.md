# Agente Inteligente em Labirinto

Projeto desenvolvido para a disciplina de Inteligência Artificial do curso de
Bacharelado em Ciência da Computação.

O projeto utiliza um ambiente próprio em formato de labirinto bidimensional.
O agente principal utiliza o algoritmo de busca heurística A* e é comparado
com um agente que escolhe movimentos aleatoriamente.

## Objetivo

Fazer um agente sair de uma posição inicial e chegar ao objetivo, evitando
obstáculos e buscando um caminho de baixo custo.

## Agentes implementados

### Agente heurístico

O agente principal utiliza o algoritmo A*.

A função de avaliação é:

```text
f(n) = g(n) + h(n)
```

- `g(n)`: custo acumulado desde o estado inicial;
- `h(n)`: estimativa de distância até o objetivo;
- `f(n)`: custo total estimado.

A heurística utilizada é a distância de Manhattan:

```text
h(n) = |x_atual - x_objetivo| + |y_atual - y_objetivo|
```

### Agente aleatório

O agente aleatório escolhe uma ação válida a cada passo. Ele é utilizado como
estratégia de referência para comparar o desempenho do A*.

## Representação do problema

### Estado

O estado é composto por:

- posição atual do agente;
- posição do objetivo;
- posições dos obstáculos;
- dimensões da grade.

### Ações

O agente pode executar quatro ações:

- cima;
- baixo;
- esquerda;
- direita.

### Condição de sucesso

O agente obtém sucesso quando alcança a célula objetivo.

### Recompensas

Na simulação do agente aleatório:

- `+100` ao alcançar o objetivo;
- `-1` por movimento válido;
- `-5` por tentativa de movimento inválido.

O agente aleatório escolhe somente ações válidas, mas a penalidade permanece
implementada no ambiente para permitir outros experimentos.

## Métricas

O projeto coleta:

- taxa de sucesso;
- quantidade de movimentos;
- custo do caminho;
- número de estados explorados;
- recompensa total;
- tempo de execução.

Os resultados são salvos em:

```text
resultados/metricas.csv
```

## Estrutura do projeto

```text
agente-labirinto/
├── assets/
├── resultados/
│   └── metricas.csv
├── main.py
├── environment.py
├── heuristic_agent.py
├── random_agent.py
├── metrics.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Requisitos

- Python 3.10 ou superior;
- Pygame 2.6.1.

## Instalação

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
cd agente-labirinto
```

Crie um ambiente virtual:

### Linux ou macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

### Demonstração do agente A*

```bash
python main.py
```

ou:

```bash
python main.py --mode demo
```

A demonstração mostra o labirinto no terminal e, caso o Pygame esteja
instalado, abre uma janela com a animação do caminho.

### Comparação entre os agentes

```bash
python main.py --mode evaluate
```

Por padrão, cada agente será executado 30 vezes.

Para alterar a quantidade de execuções:

```bash
python main.py --mode evaluate --executions 50
```

Para alterar o limite de movimentos do agente aleatório:

```bash
python main.py --mode evaluate --random-max-steps 500
```

## Legenda da visualização textual

```text
S = início
G = objetivo
# = obstáculo
* = caminho encontrado
A = agente
. = célula livre
```

## Protocolo de avaliação

1. Executar o agente A* e o agente aleatório no mesmo labirinto.
2. Realizar pelo menos 30 execuções de cada agente.
3. Limitar o agente aleatório a 300 movimentos por execução.
4. Registrar as métricas em arquivo CSV.
5. Comparar taxa de sucesso, movimentos e tempo de execução.
6. Discutir as limitações do experimento.

## Limitações

- o labirinto atual é fixo;
- o ambiente utiliza uma grade pequena;
- o agente aleatório pode repetir posições;
- o A* conhece completamente o mapa;
- ainda não há geração automática de diferentes labirintos;
- a comparação utiliza apenas uma estratégia de referência simples.

## Uso de IA generativa

Ferramentas de IA generativa foram utilizadas como apoio na estruturação
inicial do código e da documentação. O código deve ser testado, revisado,
compreendido e validado pelos integrantes antes da entrega. Os integrantes
devem ser capazes de explicar e modificar todas as partes do projeto.

## Integrantes

- Douglas Filipe Severo Batista
- Genildo Burgos Barros

---

## Repositório

**GitHub:** https://github.com/genildoburgos/agente-labirinto

---

## Vídeo de apresentação

**Link do vídeo:** https://www.youtube.com/
