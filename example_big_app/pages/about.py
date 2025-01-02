import reflex as rx
from ..templates import template

@template(route="/about", title="About")
def about():
    return rx.text("About Page")