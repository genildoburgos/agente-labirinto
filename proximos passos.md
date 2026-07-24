# Próximos Passos (Planejamento) 🚀

## O códigoestá basicamente pronto. Os próximos passos devem ser focados em refinamento e na preparação para a entrega.

**Passo A:** Pequenas melhorias no código (Opcional, mas recomendado)

Nas limitações do README, vocês citam que "o labirinto atual é fixo" e "não há geração automática". Para enriquecer a comparação e a avaliação:

Poderíamos criar um gerador de obstáculos aleatórios no MazeEnvironment, permitindo avaliar a média de performance do A\* em, por exemplo, 5 mapas diferentes (com sementes aleatórias fixas).

**Passo B:** Finalizar o Repositório

- Adicionar os nomes de vocês no final do README.md.  
- Garantir que o repositório no GitHub esteja público.  
- Adicionar o link do vídeo gravado no topo do README antes da entrega.

**Passo C:** Roteiro e Gravação do Vídeo (A tarefa principal agora)

O professor pede um vídeo em formato de conversa técnica entre a dupla (máx 20 min). Todos os itens do tópico "5. Conteúdo obrigatório do vídeo" devem ser abordados. Aqui está uma sugestão de roteiro baseada no projeto de vocês:

1. **Apresentação e IA Generativa (Item 1):** Apresentem-se e comecem explicando que usaram IA (eu) para revisar o código, estruturar o boilerplate inicial e organizar o README, mas que vocês validaram toda a lógica do A\* e as métricas geradas.  
2. **O Ambiente (Item 2 e 6):** Mostrem o código do environment.py. Expliquem a grade 10x10, o que é o estado (a tupla (linha, coluna)), as ações permitidas, os obstáculos e a condição de sucesso (bater a posição atual com a posição do objetivo).  
3. **Conexão Agente-Ambiente (Item 3):** Mostrem o método find\_path e step. Expliquem que no caso do A\*, o agente usa o modelo do ambiente (valid\_neighbors) para planejar offline antes de agir. Mostrem rapidamente a lógica de recompensa que deixaram preparada (-1 por passo, \+100 vitória).  
4. **Teoria do A e Heurística (Item 4 e 7):** Essa é a parte mais importante. Expliquem como o A funciona. Mostrem a função manhattan\_distance no código. Justifiquem por que usaram Manhattan (movimentos em grade) e não Euclidiana. Falem sobre a fila de prioridade.  
5. **Visualização (Item 5 e 10):** Rodem o python main.py \--mode demo. Mostrem o terminal e a janelinha do Pygame. Expliquem o agente achando o caminho ótimo.  
6. **Avaliação e Comparação (Item 8):** Rodem o python main.py \--mode evaluate. Mostrem os resultados impressos no terminal. Discutam por que o A\* tem 100% de sucesso e o menor caminho possível, enquanto o agente aleatório falha ou dá milhares de voltas (devido à falta de conhecimento e plano).  
7. **Limitações (Item 9):** Leiam a seção de limitações do README de vocês (falem sobre o mapa fixo e que o A\* precisa conhecer tudo desde o início, diferentemente de um agente de aprendizado por reforço).