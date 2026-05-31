# 🚀 TaskForge API v2.0.0

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.12-yellow)
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-green)
![OpenAPI](https://img.shields.io/badge/OpenAPI-3.0-brightgreen)
![License](https://img.shields.io/badge/License-MIT-red)

---

## 📋 Tabla de Contenidos

* [📖 Descripción](#-descripción)
* [🎯 Objetivo del Proyecto](#-objetivo-del-proyecto)
* [✨ Características](#-características)
* [⚙️ Tecnologías Utilizadas](#️-tecnologías-utilizadas)
* [📦 Requisitos Previos](#-requisitos-previos)
* [🔧 Instalación](#-instalación)
* [▶️ Ejecución](#️-ejecución)
* [📚 Documentación de la API](#-documentación-de-la-api)
* [🌐 Endpoints Disponibles](#-endpoints-disponibles)
* [📄 Ejemplo de Uso](#-ejemplo-de-uso)
* [📁 Estructura del Proyecto](#-estructura-del-proyecto)
* [🔄 Control de Versiones](#-control-de-versiones)
* [📜 Licencia](#-licencia)
* [👨‍💻 Autor](#-autor)

---

# 📖 Descripción

**TaskForge API** es una API REST desarrollada en **Python** utilizando **FastAPI**, diseñada para la gestión de tareas personales.

La aplicación permite realizar operaciones CRUD (*Create, Read, Update y Delete*) sobre tareas, facilitando la organización y seguimiento de actividades mediante una interfaz basada en servicios REST.

Este proyecto fue desarrollado con fines académicos para aplicar conocimientos relacionados con:

* Desarrollo de APIs REST.
* Programación en Python.
* Documentación técnica.
* OpenAPI y Swagger UI.
* Control de versiones con Git y GitHub.
* Metodologías ágiles.
* Gestión de proyectos mediante Jira y Confluence.

---

# 🎯 Objetivo del Proyecto

Desarrollar una API REST para la administración de tareas personales utilizando Python y FastAPI, aplicando buenas prácticas de desarrollo de software, documentación técnica y control de versiones.

---

# ✨ Características

✅ Gestión de tareas personales.

✅ Operaciones CRUD completas.

✅ Arquitectura REST.

✅ Respuestas en formato JSON.

✅ Documentación automática mediante Swagger UI.

✅ Compatibilidad con OpenAPI 3.0.

✅ Proyecto preparado para GitHub, Jira y Confluence.

---

# ⚙️ Tecnologías Utilizadas

| Tecnología  | Descripción               |
| ----------- | ------------------------- |
| Python 3.12 | Lenguaje principal        |
| FastAPI     | Framework para APIs REST  |
| Uvicorn     | Servidor ASGI             |
| OpenAPI 3.0 | Especificación de la API  |
| Swagger UI  | Documentación interactiva |
| Git         | Control de versiones      |
| GitHub      | Gestión del repositorio   |

---

# 📦 Requisitos Previos

Antes de ejecutar el proyecto asegúrese de tener instalado:

* Python 3.10 o superior.
* Git.
* Visual Studio Code (opcional).

Verificar versión instalada:

```bash
python --version
```

---

# 🔧 Instalación

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/taskforge-api.git
```

### 2️⃣ Ingresar al directorio del proyecto

```bash
cd taskforge-api
```

### 3️⃣ Crear entorno virtual

```bash
python -m venv venv
```

### 4️⃣ Activar entorno virtual

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / MacOS

```bash
source venv/bin/activate
```

### 5️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# ▶️ Ejecución

Iniciar el servidor local:

```bash
uvicorn main:app --reload
```

La aplicación estará disponible en:

```text
http://127.0.0.1:8000
```

---

# 📚 Documentación de la API

Una vez iniciado el servidor, FastAPI genera automáticamente la documentación interactiva.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### OpenAPI JSON

```text
http://127.0.0.1:8000/openapi.json
```

---

# 🌐 Endpoints Disponibles

| Método | Endpoint      | Descripción                    |
| ------ | ------------- | ------------------------------ |
| GET    | `/tasks`      | Obtener todas las tareas       |
| POST   | `/tasks`      | Crear una nueva tarea          |
| PUT    | `/tasks/{id}` | Actualizar una tarea existente |
| DELETE | `/tasks/{id}` | Eliminar una tarea             |

---

# 📄 Ejemplo de Uso

### Solicitud

```json
{
  "title": "Estudiar FastAPI",
  "completed": false
}
```

### Respuesta

```json
{
  "id": 1,
  "title": "Estudiar FastAPI",
  "completed": false
}
```

---

# 📁 Estructura del Proyecto

```text
TaskForgeAPI/
│
├── main.py
├── README.md
├── CHANGELOG.md
├── LICENSE
├── .gitignore
├── requirements.txt
└── api-spec.yaml
```

---

# 🔄 Control de Versiones

## 🏷️ Versión Actual

**v1.0.0**

## 📌 Cambios Iniciales

* Creación de la API REST.
* Implementación de endpoints CRUD.
* Integración con Swagger UI.
* Configuración de OpenAPI.
* Estructuración inicial del proyecto.

---

# 📜 Licencia

Este proyecto se distribuye bajo la licencia **MIT**.

Consulte el archivo `LICENSE` para más información.

---

# 👨‍💻 Autores

**Guillermo Carpio**
**Jandry Cordova**

🎓 Proyecto académico desarrollado para la asignatura de Desarrollo de Software y Documentación Técnica.

⭐ Gracias por visitar este proyecto.
