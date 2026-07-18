from __future__ import annotations

import csv
import time
from dataclasses import asdict, dataclass
from pathlib import Path

from environment import MazeEnvironment
from heuristic_agent import HeuristicAgent
from random_agent import RandomAgent


@dataclass
class ExecutionMetric:
    agent: str
    execution: int
    success: bool
    steps: int
    path_cost: int
    explored_states: int
    total_reward: int
    execution_time_seconds: float


def evaluate_agents(
    executions: int = 30,
    random_max_steps: int = 300,
) -> list[ExecutionMetric]:
    if executions <= 0:
        raise ValueError("O número de execuções deve ser maior que zero.")

    metrics: list[ExecutionMetric] = []

    for execution in range(1, executions + 1):
        environment = MazeEnvironment()
        heuristic_agent = HeuristicAgent()

        start_time = time.perf_counter()
        result = heuristic_agent.find_path(environment)
        elapsed_time = time.perf_counter() - start_time

        metrics.append(
            ExecutionMetric(
                agent="A*",
                execution=execution,
                success=result.success,
                steps=max(len(result.path) - 1, 0),
                path_cost=result.path_cost,
                explored_states=result.explored_states,
                total_reward=100 - result.path_cost if result.success else 0,
                execution_time_seconds=elapsed_time,
            )
        )

        environment = MazeEnvironment()
        random_agent = RandomAgent(seed=execution)

        start_time = time.perf_counter()
        random_result = random_agent.run(
            environment,
            max_steps=random_max_steps,
        )
        elapsed_time = time.perf_counter() - start_time

        metrics.append(
            ExecutionMetric(
                agent="Aleatório",
                execution=execution,
                success=random_result.success,
                steps=random_result.steps,
                path_cost=random_result.steps,
                explored_states=0,
                total_reward=random_result.total_reward,
                execution_time_seconds=elapsed_time,
            )
        )

    return metrics


def save_metrics(
    metrics: list[ExecutionMetric],
    output_path: str | Path = "resultados/metricas.csv",
) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=list(asdict(metrics[0]).keys()),
        )
        writer.writeheader()

        for metric in metrics:
            writer.writerow(asdict(metric))

    return path


def summarize_metrics(metrics: list[ExecutionMetric]) -> dict[str, dict[str, float]]:
    summary: dict[str, dict[str, float]] = {}

    for agent_name in sorted({metric.agent for metric in metrics}):
        agent_metrics = [
            metric for metric in metrics if metric.agent == agent_name
        ]
        successful_metrics = [
            metric for metric in agent_metrics if metric.success
        ]

        summary[agent_name] = {
            "executions": float(len(agent_metrics)),
            "success_rate": (
                len(successful_metrics) / len(agent_metrics)
                if agent_metrics
                else 0.0
            ),
            "average_steps": (
                sum(metric.steps for metric in agent_metrics)
                / len(agent_metrics)
                if agent_metrics
                else 0.0
            ),
            "average_time_seconds": (
                sum(metric.execution_time_seconds for metric in agent_metrics)
                / len(agent_metrics)
                if agent_metrics
                else 0.0
            ),
            "average_path_cost_on_success": (
                sum(metric.path_cost for metric in successful_metrics)
                / len(successful_metrics)
                if successful_metrics
                else 0.0
            ),
            "average_explored_states": (
                sum(metric.explored_states for metric in agent_metrics)
                / len(agent_metrics)
                if agent_metrics
                else 0.0
            ),
        }

    return summary


def print_summary(summary: dict[str, dict[str, float]]) -> None:
    print("\nResumo das métricas")
    print("-" * 72)

    for agent, values in summary.items():
        print(f"Agente: {agent}")
        print(f"Execuções: {int(values['executions'])}")
        print(f"Taxa de sucesso: {values['success_rate'] * 100:.2f}%")
        print(f"Média de movimentos: {values['average_steps']:.2f}")
        print(
            "Custo médio do caminho nas execuções bem-sucedidas: "
            f"{values['average_path_cost_on_success']:.2f}"
        )
        print(
            "Tempo médio de execução: "
            f"{values['average_time_seconds']:.6f} s"
        )
        print(
            "Média de estados explorados: "
            f"{values['average_explored_states']:.2f}"
        )
        print("-" * 72)
