import streamlit as st
from fpdf import FPDF

st.title("Encuesta: Impacto de ChatGPT en la Educación")

st.write("Responde las siguientes afirmaciones usando la escala de Likert.")

# Opciones de la escala Likert
likert_options = [
    "Totalmente de acuerdo",
    "De acuerdo",
    "Ni de acuerdo ni en desacuerdo",
    "En desacuerdo",
    "Totalmente en desacuerdo"
]

# Lista de preguntas
questions = [
    "ChatGPT facilita la creación de actividades educativas innovadoras.",
    "ChatGPT mejora la eficiencia en la planeación de clases.",
    "ChatGPT es una herramienta útil para generar ideas educativas basadas en problemas reales.",
    "ChatGPT contribuye a diversificar las estrategias de enseñanza utilizadas en clase.",
    "ChatGPT contribuye a personalizar el aprendizaje según las necesidades de los estudiantes.",
    "ChatGPT fomenta el desarrollo del pensamiento crítico en los estudiantes.",
    "ChatGPT promueve la autonomía en el aprendizaje de los estudiantes.",
    "ChatGPT mejora la comprensión de los conceptos en estudiantes con dificultades de aprendizaje.",
    "ChatGPT estimula la curiosidad y la creatividad en los estudiantes.",
    "Considero que ChatGPT tiene un impacto positivo en la enseñanza y el aprendizaje.",
    "Los beneficios de usar ChatGPT superan sus limitaciones en el contexto educativo.",
    "ChatGPT me motiva a explorar nuevas formas de enseñar y aprender.",
    "Recomendaría el uso de ChatGPT a otros docentes para mejorar los escenarios educativos."
]

# Diccionario para guardar respuestas
responses = {}

# Mostrar preguntas
for i, question in enumerate(questions):
    response = st.radio(f"{i+1}. {question}", likert_options, key=i)
    responses[question] = response

# Función para generar PDF
def generar_pdf(respuestas):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Resultados de la Encuesta", ln=True, align="C")
    pdf.ln(10)

    for i, (pregunta, respuesta) in enumerate(respuestas.items(), start=1):
        pdf.multi_cell(0, 10, f"{i}. {pregunta}\n   Respuesta: {respuesta}")
        pdf.ln(2)

    pdf_output = "respuestas_encuesta.pdf"
    pdf.output(pdf_output)
    return pdf_output

# Botón para generar PDF
if st.button("Generar PDF con respuestas"):
    pdf_file = generar_pdf(responses)
    with open(pdf_file, "rb") as f:
        st.download_button(
            label="Descargar PDF",
            data=f,
            file_name="respuestas_encuesta.pdf",
            mime="application/pdf"
        )

