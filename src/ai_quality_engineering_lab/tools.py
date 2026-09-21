from pydantic import BaseModel, Field, TypeAdapter, field_validator
from typing import Annotated, Literal

class ClickArgs(BaseModel):
    element_ref: str = Field(pattern=r"^e\d+$")

class FinishArgs(BaseModel):
    status: Literal["success", "failure"]
    reason: str = Field(min_length=1)

    @field_validator("reason")
    def validate_reason(reason: str):
        if not reason.strip():
            raise ValueError("Reason must contain non-whitespace characters")

        return reason

class ClickAction(BaseModel):
    action: Literal["click"]
    arguments: ClickArgs

class FinishAction(BaseModel):
    action: Literal["finish"]
    arguments: FinishArgs

AgentAction = Annotated[
    ClickAction | FinishAction,
    Field(discriminator="action")
]
agent_action_adapter = TypeAdapter(AgentAction)