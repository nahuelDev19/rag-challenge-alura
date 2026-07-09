import gradio as gr
from consulta import respuesta

def chat(message, history):
    return respuesta(message)

gr.ChatInterface(
    fn=chat,
    title="🤖 Asistente BimBam Buy",
    description="Preguntá sobre BimBam Buy utilizando la documentación disponible."
).launch()