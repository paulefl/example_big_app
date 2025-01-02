import reflex as rx
from ..templates import template

@template(route="/custom", title="Custom")
def custom():
    return rx.text("Custom Route")