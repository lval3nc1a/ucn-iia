# 📘 Proyecto IA - Tablas de Verdad y Lógica Difusa

Este proyecto contiene dos implementaciones para enseñar fundamentos de Introducción a la Inteligencia Artificial:

| Implementación | Carpeta | Descripción |
|----------------|---------|-------------|
| **CLI** (línea de comandos) | `Calculadora-CLI/` | Menú interactivo en consola con tablas de verdad de conectivos lógicos. |
| **GUI** (interfaz gráfica) | `Calculadora-GUI/` | Ventana con Tkinter (tema oscuro) que muestra tablas de verdad y operaciones de lógica difusa en popups. |

---

## 📂 Estructura del proyecto

```
_Proyecto-Calculadora/
├── README.md                    # Este archivo (resumen general)
├── Calculadora-CLI/             # Versión consola
│   ├── README.md                # Instrucciones específicas de la CLI
│   ├── tabla-de-verdad.py       # Programa principal de tablas de verdad
│   └── venv/                    # Entorno virtual de Python
└── Calculadora-GUI/             # Versión gráfica (Tkinter)
    ├── README.md                # Instrucciones específicas de la GUI
    ├── calculadora_gui.py       # Aplicación GUI principal
    └── venv/                    # Entorno virtual de Python
```

---

## 🚀 Uso rápido

### 1. Calculadora de Tablas de Verdad (CLI)

```powershell
# Desde la raíz del proyecto
Calculadora-CLI\venv\Scripts\Activate.ps1
python Calculadora-CLI\tabla-de-verdad.py
```

O directamente dentro de la carpeta:

```powershell
cd Calculadora-CLI
venv\Scripts\activate
python tabla-de-verdad.py
```

### 2. Calculadora con Interfaz Gráfica (GUI)

```powershell
# Desde la raíz del proyecto
Calculadora-GUI\venv\Scripts\Activate.ps1
python Calculadora-GUI\calculadora_gui.py
```

O directamente dentro de la carpeta:

```powershell
cd Calculadora-GUI
venv\Scripts\activate
python calculadora_gui.py
```

---

## 📋 Requisitos

- Python 3.x
- No requiere librerías externas (usa solo la librería estándar de Python: `itertools`, `tkinter`).

---

## 👨‍💻 Autoría

Este proyecto fue realizado por **Luis Valencia** como parte del curso de **Introducción a la Inteligencia Artificial** (UCN). Proyecto con propósito educativo.

---

## 📄 Licencia

Educativa.
