from __future__ import annotations

import random
from dataclasses import dataclass

from environment import MazeEnvironment, Position


@dataclass
class RandomAgentResult:
    success: bool
    path: list[Position]
    steps: int
    total_reward: int


class RandomAgent:
    """Agente de referência que escolhe uma ação válida aleatoriamente."""

    def __init__(self, seed: int | None = None) -> None:
        self.random = random.Random(seed)

    def run(
        self,
        environment: MazeEnvironment,
        max_steps: int = 300,
    ) -> RandomAgentResult:
        environment.reset()
        path = [environment.agent_position]
        total_reward = 0

        for step_number in range(1, max_steps + 1):
            actions = environment.valid_actions()

            if not actions:
                return RandomAgentResult(
                    success=False,
                    path=path,
                    steps=step_number - 1,
                    total_reward=total_reward,
                )

            action = self.random.choice(actions)
            position, reward, done, _ = environment.step(action)

            total_reward += reward
            path.append(position)

            if done:
                return RandomAgentResult(
                    success=True,
                    path=path,
                    steps=step_number,
                    total_reward=total_reward,
                )

        return RandomAgentResult(
            success=False,
            path=path,
            steps=max_steps,
            total_reward=total_reward,
        )
