# Chatbot de Restaurante Andy 🍕🍜
Este proyecto es una aplicación de chatbot desarrollada con Streamlit que interactúa con los usuarios proporcionando respuestas automáticas sobre un restaurante de comida asiática y española. La aplicación se conecta a los servicios de Azure AI para obtener respuestas a las preguntas planteadas por los usuarios.

El chatbot es capaz de proporcionar respuestas a diversas consultas como: menús degustación, opciones de entrega a domicilio, menús para personas con alergias alimentarias, entre otras.

## Requisitos
Antes de ejecutar la aplicación, asegúrate de tener las siguientes dependencias instaladas:

- Python 3.7 o superior
- Streamlit
- python-dotenv
- azure-ai-language

Puedes instalar las dependencias con pip:
```bash
pip install streamlit python-dotenv azure-ai-language
```

## Configuración
Para poder interactuar con el servicio de Azure, necesitarás configurar un proyecto de Question Answering en Azure Cognitive Services. A continuación, debes definir tus credenciales en un archivo `.env` en el mismo directorio del proyecto.

Crea un archivo `.env` y añade las siguientes variables de entorno:
```bash
AI_SERVICE_ENDPOINT=your_azure_endpoint
AI_SERVICE_KEY=your_azure_key
QA_PROJECT_NAME=your_project_name
QA_DEPLOYMENT_NAME=your_deployment_name
```

AI_SERVICE_ENDPOINT: El endpoint de tu servicio de Azure Cognitive Services.
AI_SERVICE_KEY: La clave de acceso a tu servicio de Azure.
QA_PROJECT_NAME: El nombre del proyecto de Question Answering.
QA_DEPLOYMENT_NAME: El nombre del despliegue de Question Answering.

Ejecución
Para ejecutar la aplicación, simplemente corre el siguiente comando en tu terminal:
```bash
streamlit run app.py
```

Esto abrirá la aplicación en tu navegador web. Desde ahí, podrás interactuar con el chatbot y realizar preguntas sobre el restaurante.

Funcionamiento
Interfaz de Usuario:

El chatbot muestra una interfaz en la que el usuario puede escribir preguntas.
Algunas preguntas sugeridas incluyen temas como menús degustación, opciones de entrega a domicilio o menús para personas con alergias alimentarias.
Procesamiento de la Pregunta:

El chatbot procesa las preguntas enviadas por el usuario utilizando el servicio de Azure para obtener respuestas desde un modelo entrenado.
Las respuestas obtenidas se muestran junto con su nivel de confianza y la fuente de donde se extrajo la respuesta.
Historial de Conversación:

Cada pregunta realizada por el usuario, junto con la respuesta recibida, se guarda en un historial visible en la misma interfaz de la aplicación.
Borrar Historial:

Hay un botón que permite al usuario borrar el historial de preguntas y respuestas, reiniciando la conversación.

### Notas
Confianza: Si deseas mostrar el nivel de confianza de cada respuesta, descomenta la línea correspondiente en el código donde se encuentra la variable answer.confidence.

Fuentes: Si deseas mostrar las fuentes de las respuestas, también puedes descomentar la línea correspondiente en el código donde se encuentra answer.source.