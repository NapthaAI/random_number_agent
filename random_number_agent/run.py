#!/usr/bin/env python
import logging
import random
from random_number_agent.schemas import InputSchema
import time
from naptha_sdk.utils import load_yaml
from naptha_sdk.schemas import AgentRunInput

logger = logging.getLogger(__name__)

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


def run(agent_run: AgentRunInput, *args, **kwargs):
    logger.info(f"Inputs: {agent_run.inputs}")
    agent = RandomParticipant(name=agent_run.inputs.agent_name)
    response = agent.generate_random_response()
    return response

if __name__ == "__main__":
    cfg_path = "random_number_agent/component.yaml"
    cfg = load_yaml(cfg_path)
    inputs = InputSchema(agent_name="agent_1")
    response = run(inputs, cfg=cfg)
    logger.info(f"Response: {response}")