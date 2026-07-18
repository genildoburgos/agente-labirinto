from __future__ import annotations

import argparse

from environment import MazeEnvironment
from heuristic_agent import HeuristicAgent
from metrics import (
    evaluate_agents,
    print_summary,
    save_metrics,
    summarize_metrics,
)


def run_astar_demo() -> None:
    environment = MazeEnvironment()
    agent = HeuristicAgent()
    result = agent.find_path(environment)

    print("\nDemonstração do agente heurístico A*")
    print("-" * 45)

    if not result.success:
        print("O agente não encontrou um caminho até o objetivo.")
        return

    print(f"Custo do caminho: {result.path_cost}")
    print(f"Estados explorados: {result.explored_states}")
    print(f"Quantidade de posições no caminho: {len(result.path)}")
    print("\nLabirinto:")
    environment.render_terminal(result.path)

    try:
        run_pygame_visualization(environment, result.path)
    except ModuleNotFoundError:
        print(
            "\nO Pygame não está instalado. "
            "A visualização textual foi executada normalmente."
        )


def run_pygame_visualization(
    environment: MazeEnvironment,
    path: list[tuple[int, int]],
) -> None:
    import pygame

    cell_size = 55
    width = environment.cols * cell_size
    height = environment.rows * cell_size

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Agente A* no Labirinto")
    clock = pygame.time.Clock()

    colors = {
        "background": (245, 245, 245),
        "grid": (190, 190, 190),
        "obstacle": (40, 40, 40),
        "start": (70, 160, 90),
        "goal": (210, 70, 70),
        "path": (100, 150, 230),
        "agent": (245, 180, 55),
    }

    running = True

    for current_position in path:
        if not running:
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(colors["background"])

        for row in range(environment.rows):
            for col in range(environment.cols):
                position = (row, col)
                rect = pygame.Rect(
                    col * cell_size,
                    row * cell_size,
                    cell_size,
                    cell_size,
                )

                if position in environment.obstacles:
                    pygame.draw.rect(screen, colors["obstacle"], rect)
                elif position in path:
                    pygame.draw.rect(screen, colors["path"], rect)

                if position == environment.start:
                    pygame.draw.rect(screen, colors["start"], rect)

                if position == environment.goal:
                    pygame.draw.rect(screen, colors["goal"], rect)

                pygame.draw.rect(screen, colors["grid"], rect, 1)

        agent_center = (
            current_position[1] * cell_size + cell_size // 2,
            current_position[0] * cell_size + cell_size // 2,
        )
        pygame.draw.circle(
            screen,
            colors["agent"],
            agent_center,
            cell_size // 3,
        )

        pygame.display.flip()
        clock.tick(5)

    wait_start = pygame.time.get_ticks()

    while running and pygame.time.get_ticks() - wait_start < 2500:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(30)

    pygame.quit()


def run_evaluation(executions: int, random_max_steps: int) -> None:
    print(
        f"\nExecutando {executions} avaliações por agente. "
        "Aguarde..."
    )

    metrics = evaluate_agents(
        executions=executions,
        random_max_steps=random_max_steps,
    )
    output_path = save_metrics(metrics)
    summary = summarize_metrics(metrics)

    print_summary(summary)
    print(f"\nMétricas salvas em: {output_path.resolve()}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Projeto de agente inteligente em um labirinto."
    )
    parser.add_argument(
        "--mode",
        choices=["demo", "evaluate"],
        default="demo",
        help=(
            "'demo' executa e exibe o A*. "
            "'evaluate' compara o A* com o agente aleatório."
        ),
    )
    parser.add_argument(
        "--executions",
        type=int,
        default=30,
        help="Número de execuções de cada agente na avaliação.",
    )
    parser.add_argument(
        "--random-max-steps",
        type=int,
        default=300,
        help="Limite de passos do agente aleatório.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()

    if args.mode == "demo":
        run_astar_demo()
    else:
        run_evaluation(
            executions=args.executions,
            random_max_steps=args.random_max_steps,
        )


if __name__ == "__main__":
    main()
