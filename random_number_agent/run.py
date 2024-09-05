#!/usr/bin/env python
from naptha_sdk.utils import get_logger, load_yaml
import random
from random_number_agent.schemas import InputSchema
import time

logger = get_logger(__name__)

class RandomParticipant():
    """A fake participant who generates number randomly."""

    def __init__(
        self,
        name: str,
        max_value: int = 100,
        sleep_time: float = 1.0,
    ) -> None:
        """Initialize the participant."""
        self.max_value = max_value
        self.sleep_time = sleep_time

    def generate_random_response(self) -> str:
        """generate a random int"""
        time.sleep(self.sleep_time)
        return str(random.randint(0, self.max_value))


def run(inputs, worker_nodes=None, orchestrator_node=None, flow_run=None, cfg=None):
    logger.info(f"Inputs: {inputs}")
    agent = RandomParticipant(name=inputs.agent_name)
    response = agent.generate_random_response()
    return response

if __name__ == "__main__":
    cfg_path = "random_number_agent/component.yaml"
    cfg = load_yaml(cfg_path)
    inputs = InputSchema(agent_name="agent_1")
    response = run(inputs, cfg=cfg)
    logger.info(f"Response: {response}")