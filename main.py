#pip install reactpy
#pip install "uvicorn[standard]"
#pip install reactpy[fastapi]
#unicorn main:app --relaod

from reactpy import component, html, hooks
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

@component
def Item(text, initial_done=False):
    done, set_done = hooks.use_state(initial_done)

    def handle_click(evento):
        set_done(not done)

    attrs = {"style": {"color": "green"}} if done else{}

    if done:
        return html.li(attrs,text)
    else:
        return html.li(
            html.span(attrs,text),
            html.button({"on_click": handle_click}, "Hecho!!!")
        )


@component
def HolaMundo():
    return html.div(
        html.h1("Hola amigos FullStack!!!!"),
        html.h2("Lista de Tareas!"),
        html.ul(
                Item("Hacer Proyecto"),
                Item("Terminar Video"),
                Item("Preparar pitch"),
                Item("Hacer la presentacion", initial_done=False),
        )


    )

app = FastAPI()
configure(app,HolaMundo)