from playwright.sync_api import Locator, Page
from pydantic import BaseModel

class InteractiveElement(BaseModel):
    ref: str
    role: str
    name: str

class Observation(BaseModel):
    url: str
    title: str
    elements: list[InteractiveElement]

class ObservationContext:
    def __init__(self, observation: Observation, grounding: dict[str, Locator]):
        self.observation = observation
        self.grounding = grounding
    

def build_observation(page: Page) -> ObservationContext:
    links = page.get_by_role("link")

    elements: list[InteractiveElement] = []
    grounding: dict[str, Locator] = {}

    for i in range(links.count()):
        link = links.nth(i)
        ref = f"e{i + 1}" 

        element = InteractiveElement(
            ref=ref,
            role="link",
            name=link.inner_text().strip()
        )

        elements.append(element)
        grounding[ref]=link


    observation = Observation(
        url=page.url,
        title=page.title(),
        elements=elements,
    )

    return ObservationContext(observation, grounding)