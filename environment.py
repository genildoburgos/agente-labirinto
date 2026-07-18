from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

Position = tuple[int, int]


@dataclass(frozen=True)
class MazeConfig:
    rows: int = 10
    cols: int = 10
    start: Position = (0, 0)
    goal: Position = (9, 9)


class MazeEnvironment:
    """Representa um labirinto em grade com obstáculos fixos."""

    ACTIONS: dict[str, Position] = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }

    def __init__(
        self,
        config: MazeConfig | None = None,
        obstacles: Iterable[Position] | None = None,
    ) -> None:
        self.config = config or MazeConfig()
        self.start = self.config.start
        self.goal = self.config.goal

        default_obstacles = {
            (1, 1), (1, 2), (1, 3),
            (2, 3), (3, 3), (4, 3),
            (4, 4), (4, 5), (4, 6),
            (5, 6), (6, 6), (7, 6),
            (7, 7), (7, 8),
            (2, 7), (3, 7),
            (6, 1), (6, 2),
        }

        self.obstacles = set(obstacles) if obstacles is not None else default_obstacles

        if not self.is_inside(self.start):
            raise ValueError("A posição inicial está fora da grade.")
        if not self.is_inside(self.goal):
            raise ValueError("A posição objetivo está fora da grade.")
        if self.start in self.obstacles:
            raise ValueError("A posição inicial não pode ser um obstáculo.")
        if self.goal in self.obstacles:
            raise ValueError("A posição objetivo não pode ser um obstáculo.")

        self.agent_position = self.start

    @property
    def rows(self) -> int:
        return self.config.rows

    @property
    def cols(self) -> int:
        return self.config.cols

    def reset(self) -> Position:
        """Reinicia o ambiente e devolve o estado inicial."""
        self.agent_position = self.start
        return self.agent_position

    def is_inside(self, position: Position) -> bool:
        row, col = position
        return 0 <= row < self.rows and 0 <= col < self.cols

    def is_valid_position(self, position: Position) -> bool:
        return self.is_inside(position) and position not in self.obstacles

    def valid_neighbors(self, position: Position) -> list[Position]:
        neighbors: list[Position] = []
        for delta_row, delta_col in self.ACTIONS.values():
            candidate = (position[0] + delta_row, position[1] + delta_col)
            if self.is_valid_position(candidate):
                neighbors.append(candidate)
        return neighbors

    def valid_actions(self, position: Position | None = None) -> list[str]:
        current = position if position is not None else self.agent_position
        actions: list[str] = []

        for action, (delta_row, delta_col) in self.ACTIONS.items():
            candidate = (current[0] + delta_row, current[1] + delta_col)
            if self.is_valid_position(candidate):
                actions.append(action)

        return actions

    def step(self, action: str) -> tuple[Position, int, bool, dict[str, bool]]:
        """
        Executa uma ação.

        Recompensa:
        - 100 ao chegar ao objetivo;
        - -1 por movimento válido;
        - -5 por movimento inválido.
        """
        if action not in self.ACTIONS:
            raise ValueError(f"Ação inválida: {action}")

        delta_row, delta_col = self.ACTIONS[action]
        candidate = (
            self.agent_position[0] + delta_row,
            self.agent_position[1] + delta_col,
        )

        invalid_move = not self.is_valid_position(candidate)

        if not invalid_move:
            self.agent_position = candidate

        done = self.agent_position == self.goal
        reward = 100 if done else (-5 if invalid_move else -1)

        return self.agent_position, reward, done, {"invalid_move": invalid_move}

    def action_between(self, current: Position, next_position: Position) -> str:
        delta = (
            next_position[0] - current[0],
            next_position[1] - current[1],
        )

        for action, action_delta in self.ACTIONS.items():
            if delta == action_delta:
                return action

        raise ValueError("As posições informadas não são vizinhas.")

    def render_terminal(self, path: list[Position] | None = None) -> None:
        """Exibe uma representação textual do labirinto."""
        path_set = set(path or [])

        for row in range(self.rows):
            symbols: list[str] = []

            for col in range(self.cols):
                position = (row, col)

                if position == self.start:
                    symbol = "S"
                elif position == self.goal:
                    symbol = "G"
                elif position == self.agent_position:
                    symbol = "A"
                elif position in self.obstacles:
                    symbol = "#"
                elif position in path_set:
                    symbol = "*"
                else:
                    symbol = "."

                symbols.append(symbol)

            print(" ".join(symbols))
