#!/usr/bin/env python
import logging
import random
import time
from typing import Dict
from random_number_agent.schemas import InputSchema
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


async def run(module_run: Dict, *args, **kwargs):
    module_run = AgentRunInput(**module_run)
    module_run.inputs = InputSchema(**module_run.inputs)
    random_agent = RandomParticipant(name=module_run.inputs.agent_name)
    response = random_agent.generate_random_response()
    return response


if __name__ == "__main__":
    cfg_path = "random_number_agent/component.yaml"
    cfg = load_yaml(cfg_path)
    inputs = InputSchema(agent_name="agent_1")
    response = run(inputs, cfg=cfg)
    logger.info(f"Response: {response}")