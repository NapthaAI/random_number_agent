from pydantic import BaseModel, Field

class InputSchema(BaseModel):
    agent_name: str = Field(..., title="Agent name")
