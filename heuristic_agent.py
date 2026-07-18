from __future__ import annotations

import heapq
from dataclasses import dataclass

from environment import MazeEnvironment, Position


@dataclass
class SearchResult:
    success: bool
    path: list[Position]
    explored_states: int
    path_cost: int


class HeuristicAgent:
    """Agente que utiliza o algoritmo A* com distância de Manhattan."""

    def manhattan_distance(self, current: Position, goal: Position) -> int:
        return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

    def find_path(self, environment: MazeEnvironment) -> SearchResult:
        start = environment.start
        goal = environment.goal

        frontier: list[tuple[int, int, Position]] = []
        counter = 0

        heapq.heappush(
            frontier,
            (self.manhattan_distance(start, goal), counter, start),
        )

        came_from: dict[Position, Position | None] = {start: None}
        cost_so_far: dict[Position, int] = {start: 0}
        explored_states = 0

        while frontier:
            _, _, current = heapq.heappop(frontier)
            explored_states += 1

            if current == goal:
                path = self._reconstruct_path(came_from, goal)
                return SearchResult(
                    success=True,
                    path=path,
                    explored_states=explored_states,
                    path_cost=len(path) - 1,
                )

            for neighbor in environment.valid_neighbors(current):
                new_cost = cost_so_far[current] + 1

                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + self.manhattan_distance(neighbor, goal)
                    counter += 1
                    heapq.heappush(frontier, (priority, counter, neighbor))
                    came_from[neighbor] = current

        return SearchResult(
            success=False,
            path=[],
            explored_states=explored_states,
            path_cost=0,
        )

    def _reconstruct_path(
        self,
        came_from: dict[Position, Position | None],
        goal: Position,
    ) -> list[Position]:
        path = [goal]
        current = goal

        while came_from[current] is not None:
            current = came_from[current]  # type: ignore[assignment]
            path.append(current)

        path.reverse()
        return path
