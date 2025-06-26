# API Test Challenge - Pytest + POM

Este proyecto automatiza pruebas para una API de importación utilizando **Pytest** y el patrón **POM (Page Object Model)** adaptado para testing de APIs.

Incluye:

- Validación de respuesta exitosa (Happy Path)
- Validación de error esperado (Sad Path)
- Verificación en base de datos de la inserción del `personId`

---

## Estructura del proyecto

```
api_test_challenge/
├── pages/              # Lógica de la API encapsulada (POM)
│   └── import_api.py
├── db/                 # Validaciones contra base de datos
│   └── db_utils.py
├── tests/              # Casos de prueba automatizados
│   └── test_import.py
├── conftest.py         # Fixtures para pytest
├── requirements.txt
```

---

## Requisitos

- Python 3.8 o superior
- pip (Python package manager)

---

## Instalación

1. Clonar o descomprimir este proyecto.
2. Crear un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv venv
   venv/Scripts/activate   # Windows
   # o
   source venv/bin/activate  # macOS/Linux
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

---

## Ejecución de los tests

Desde la raíz del proyecto:

```bash
pytest -s
```

El parámetro `-s` permite ver mensajes `print()` en la consola, útiles para verificar las validaciones.

---

## Casos de prueba incluidos

| Test              | Descripción                                               |
| ----------------- | --------------------------------------------------------- |
| `test_happy_path` | Envía un `personId` válido y espera `200 OK`              |
| `test_sad_path`   | Envía un `personId` vacío y espera error `401`            |
| `test_happy_path` | Verifica en base de datos que el `personId` fue insertado |

---

## Configuración

- En `conftest.py`: reemplazar `"xxx"` por un token real.
- En `db/db_utils.py`: configurar acceso a la base (host, usuario, etc.).
