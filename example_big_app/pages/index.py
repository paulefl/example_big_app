import reflex as rx
from ..templates import template

@template(route="/index", title="index")
def index():
    return rx.text("Root Page")