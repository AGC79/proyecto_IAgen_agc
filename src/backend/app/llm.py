from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from config_env import Config

# Configuración del modelo Llama 3.3 de Groq
llm = ChatGroq(
    groq_api_key=Config.GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0.2  # Baja temperatura para respuestas técnicas precisas
)

# Prompt de sistema para definir el rol de ciberseguridad
prompt = ChatPromptTemplate.from_messages([
    ("system", (
        "Eres un Agente Experto en Ciberseguridad de élite (Red Team y Blue Team). "
        "Tu propósito es asistir en pentesting ético, análisis de logs, hardening y cumplimiento. "
        "Reglas: 1. Respuestas técnicas rigurosas. 2. Usa estándares MITRE ATT&CK y OWASP. "
        "3. Siempre advierte sobre el uso ético en comandos ofensivos."
    )),
    ("human", "{input}"),
])

# Cadena de ejecución (LCEL)
chain = prompt | llm

def get_answer(question: str) -> str:
    """Procesa la pregunta con el agente de ciberseguridad."""
    try:
        response = chain.invoke({"input": question})
        return response.content
    except Exception as e:
        return f"Error en el motor de IA: {str(e)}"
