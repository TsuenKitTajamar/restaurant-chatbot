import streamlit as st
from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient

# Cargar las variables de entorno
load_dotenv()
ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
ai_key = os.getenv('AI_SERVICE_KEY')
ai_project_name = os.getenv('QA_PROJECT_NAME')
ai_deployment_name = os.getenv('QA_DEPLOYMENT_NAME')

# Crear cliente usando endpoint y key
credential = AzureKeyCredential(ai_key)
ai_client = QuestionAnsweringClient(endpoint=ai_endpoint, credential=credential)

# Función para obtener respuestas
def get_answer(question):
    response = ai_client.get_answers(
        question=question,
        project_name=ai_project_name,
        deployment_name=ai_deployment_name
    )
    return response.answers

# Configurar la aplicación de Streamlit
st.title("Chatbot de Restaurante Andy 🍕🍜")
st.write("""Esto es un chatbot para un restaurante de comida asiática y española. Si tiene alguna consulta, no dudes en preguntar. 🍣🥗  
    Por ejemplo:  
    - ¿Ofrecen opciones de menús degustación?    
    - ¿Ofrecen servicio de entrega a domicilio?    
    - ¿Ofrecen opciones para personas con alergias alimentarias?   
    - ¿Dónde puedo obtener más información sobre alergias alimentarias?    
    - ¿Dónde puedo consultar los derechos del consumidor?   
""")

# Historial de conversación
if 'history' not in st.session_state:
    st.session_state.history = []

# Controlar el input de texto usando st.session_state
if 'user_question' not in st.session_state:
    st.session_state.user_question = ""  # Inicializar la pregunta

# Entrada de usuario (usando el componente chat_input)
user_question = st.chat_input("Pregunta", key="chat_input")

# Procesar la pregunta del usuario
if user_question:
    if user_question.strip():  # Solo si la pregunta no está vacía
        answers = get_answer(user_question)
        st.session_state.history.append((user_question, answers))


# Mostrar historial de conversación
for i, (question, answers) in enumerate(st.session_state.history):
    st.write(f"**Pregunta {i+1}:** {question}")
    for answer in answers:
        st.write(f"- **Respuesta:** {answer.answer}")
        # st.write(f"  **Confianza:** {answer.confidence:.2f}") # Para sacar el nivel de confianza de la respuesta
        # st.write(f"  **Fuente:** {answer.source}") # Para sacar la fuente de la respuesta

# Botón para borrar el historial
if st.button("Borrar historial"):
    st.session_state.history = []  # Borra el historial
    st.rerun()  # Fuerza la actualización de la interfaz
