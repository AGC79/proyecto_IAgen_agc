# 🛡️ CyberAI - Security Tactical Agent

CyberAI es una plataforma de inteligencia táctica para ciberseguridad que utiliza modelos de lenguaje avanzados para análisis de amenazas, pentesting ético y hardening. Diseñada con una arquitectura de microservicios y desplegada de forma profesional en una infraestructura elástica de **AWS**.

## 🚀 Arquitectura del Proyecto

El sistema se basa en una arquitectura de servicios contenerizados:
- **Frontend:** Interfaz táctica en tiempo real con autodetección de IP dinámica.
- **Backend:** API REST en Python con integración de LangChain (Llama 3.3) y persistencia de datos.
- **Base de Datos:** PostgreSQL para el almacenamiento histórico de las consultas y respuestas.
- **Gestión:** pgAdmin4 integrado para administración de datos en la nube.

## 🛠️ Tecnologías Utilizadas

- **IA Engine:** LangChain + Groq (Llama 3.3 70B).
- **Frontend:** HTML5, Tailwind CSS, JavaScript (Async/Fetch).
- **Backend:** Flask, Flask-CORS, SQLAlchemy.
- **Infraestructura:** Docker & Docker Compose.
- **Cloud:** AWS EC2 (Ubuntu 24.04 LTS).

## 📦 Despliegue en AWS (Workflow 2026)

Este proyecto utiliza un flujo de despliegue basado en contenedores a través de Docker Hub:

1.  **Construcción y Push:** Las imágenes se compilan localmente y se suben al registro:
    ```bash
    docker build -t agc79/cyber-chatbot-frontend:latest .
    docker push agc79/cyber-chatbot-frontend:latest
    ```
2.  **Despliegue en EC2:** Gestión de la instancia de Amazon para la descarga y ejecución de servicios:
    ```bash
    ssh -i "clave.pem" ubuntu@13.60.3.132
    cd ~/cyber_app
    docker compose pull && docker compose up -d
    ```

## 🌐 Acceso a la Plataforma

Puedes acceder a las distintas interfaces de la infraestructura (Enero 2026):

*   **Aplicación CyberAI (Chatbot):** <a href="http://13.60.3.132:3000" target="_blank">Abrir Chatbot</a>
*   **Gestión de Datos (pgAdmin):** <a href="http://13.60.3.132:8080" target="_blank">Abrir pgAdmin</a>
*   **API Health Check:** <a href="http://13.60.3.132:5000/raiz_api" target="_blank">Ver Status API</a>


> **Nota:** El acceso está sujeto a las reglas de entrada (Inbound Rules) del **Security Group** de AWS para los puertos 3000, 5000 y 8080.

## ⚙️ Configuración del Sistema

### Variables de Entorno (.env)
Configuración requerida en el servidor para la conectividad de los servicios:
- `GROQ_API_KEY`: Llave de API de Groq para el procesamiento de IA.
- `DB_HOST`: Host de la base de datos (`chatbot_db`).
- `POSTGRES_PASSWORD`: Credenciales de seguridad de la base de datos.

### Lógica de Interacción
- El Frontend detecta automáticamente la IP del servidor mediante `window.location.hostname`.
- Las consultas se procesan de forma atómica y se almacenan cronológicamente en PostgreSQL.
- El historial lateral permite la recuperación de interacciones individuales almacenadas en el backend.

## 🔒 Seguridad
- **Firewall:** Control de tráfico mediante `UFW` en el servidor y `Security Groups` en la infraestructura de AWS.
- **Acceso SSH:** Autenticación mediante llaves RSA (.pem) con permisos de seguridad restringidos.
- **Network:** Red interna bridge de Docker para la comunicación aislada entre la API y la base de datos.

---
**Status:** `v1.0 Connected` | **Última actualización:** 14 de Enero, 2026.
