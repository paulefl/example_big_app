import reflex as rx
import json
from reflex_monaco import monaco
from typing import Dict, List, Any
import logging

class State(rx.State):
    """The app state."""

    spec_airport: Dict[str, Any] = {}

    def monaco_edit(self, value):
        try:
            tmp = json.loads(value)
            self.spec_airport = tmp
        except Exception as e:
            logging.error(e)

    @rx.vars.base.computed_var(cache=True)
    def json_spec_2(self) -> str:
        return json.dumps(self.spec_airport, indent=2)


