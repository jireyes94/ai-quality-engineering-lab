from ai_quality_engineering_lab.observation import ObservationContext
from ai_quality_engineering_lab.tools import ClickAction
from pydantic import BaseModel

class UnknownElementReferenceError(Exception):
    pass

class ActionExecutionResult(BaseModel):
    pass

def execute_click(action: ClickAction, context: ObservationContext):
    element_ref = action.arguments.element_ref
    locator = context.grounding.get(element_ref)

    if locator is None:
        raise UnknownElementReferenceError(
            f"Element reference {element_ref!r} does not exist in the current observation."
        )

    locator.click()