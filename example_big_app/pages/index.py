import reflex as rx
from reflex_monaco import monaco
from ..templates import template
from ..state import state
from typing import Dict, List, Any
import logging
import json
import reflex_chakra as rc


@template(route="/index", title="index")
def index()-> rx.Component:
    return rx.container(
        rx.text("Root Page"),
        monaco( 
            default_value=State2.json_spec_2,
            on_change=State2.monaco_edit,
            width="100%",
            height="200px",
        ),
        rc.grid(
            sidebar("HomeState"),
            grid_template_columns="1fr 2fr 1fr",
            h="100vh",
            gap=4,
        ),
        rc.table_container(
            rc.table(
            headers=["Name", "Age", "Location"],
            rows=[
                ("John", 30, "New York"),
                ("Jane", 31, "San Francisco"),
                ("Joe", 32, "Los Angeles")
            ],
            footers=["Footer 1", "Footer 2", "Footer 3"],
            variant='striped'
           )
        )
    )

def sidebar(HomeState):
    """The sidebar displayed on the right."""
    return rc.vstack(
        rx.text(HomeState),
    )

class State2(rx.State):
    """The app state."""

    spec_airport: Dict[str, Any] = {'layer': [{'data': {'format': {'feature': 'states', 'type': 'topojson'} } }]}

    def monaco_edit(self, value):
        try:
            tmp = json.loads(value)
            self.spec_airport = tmp
        except Exception as e:
            logging.error(e)

    @rx.vars.base.computed_var(cache=True)
    def json_spec_2(self) -> str:
        return json.dumps(self.spec_airport, indent=2)
    
    def logout(self) -> str:
        return "Hello"