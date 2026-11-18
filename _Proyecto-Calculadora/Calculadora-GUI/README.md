# 🧮 Calculadora de Tablas de Verdad y Lógica Difusa

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?logo=tkinter)](https://docs.python.org/3/library/tkinter.html)
[![Estado](https://img.shields.io/badge/Estado-Completado-brightgreen)](https://github.com/)
[![Curso - Introducción a la IA](https://img.shields.io/badge/Curso-Introducción%20a%20la%20IA-orange)](https://ucn.edu.co/)
[![Tecnologías](https://img.shields.io/badge/Tablas%20de%20Verdad%20%7C%20Lógica%20Difusa-Fundamentos%20IA-purple)](https://github.com/)
[![Autor](https://img.shields.io/badge/Autor-Luis%20Valencia-blueviolet)](https://github.com/)
[![Licencia](https://img.shields.io/badge/Licencia-Educativa-lightgrey)](https://github.com/)

## 📄 Descripción

Proyecto de interfaz gráfica (GUI) minimalista desarrollado con **Tkinter** para Python que combina dos herramientas para enseñar los fundamentos de la **Introducción a la Inteligencia Artificial**:

1. **Calculadora de tablas de verdad** — visualiza las tablas de los conectivos lógicos clásicos (negación, conjunción, disyunción y bicondicional).
2. **Lógica difusa** — operaciones con valores de verdad continuos entre 0 y 1 (AND, OR, NOT), base de los sistemas difusos en IA.

Diseño de usuario **minimalista**: interfaz limpia, pocos elementos, colores neutros y navegación por pestañas.

## 🛠️ Tecnologías

| Tecnología | Uso |
|------------|-----|
| **Python 3.x** | Lenguaje de programación |
| **Tkinter** | Interfaz gráfica de usuario (estándar de Python) |
| **itertools.product** | Generación de combinaciones de valores de verdad |
| **Lógica difusa** | Operadores mín/máx y complemento (1 - x) |

## 📂 Estructura del proyecto

```
Calculadora-GUI/
├── venv/                      # Entorno virtual de Python
├── calculadora_gui.py         # Aplicación GUI principal (Tkinter)
└── README.md                  # Este archivo
```

## 🚀 Instalación y ejecución

### 1. Activar el entorno virtual

El entorno virtual ya está incluido en la carpeta `venv/`.

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

### 2. Ejecutar la aplicación

```bash
python calculadora_gui.py
```

## 🖥️ Uso

### Pestaña: Tablas de Verdad
Seleccione uno de los botones para ver la tabla de verdad correspondiente:
- Negación (`~p`)
- Conjunción (`p AND q`)
- Disyunción (`p OR q`)
- Bicondicional (`p IFF q`)
- Mostrar todas

### Pestaña: Lógica Difusa
Ingrese dos valores entre **0 y 1** (representan grados de verdad) y seleccione una operación:
- **AND** → resultado = `mínimo(A, B)`
- **OR** → resultado = `máximo(A, B)`
- **NOT A** → resultado = `1 - A`
- **NOT B** → resultado = `1 - B`

## ✍️ Autoría

Este proyecto fue **realizado por Luis Valencia** como parte del curso de Introducción a la Inteligencia Artificial (UCN).

## 📄 Licencia

Proyecto con propósito educativo.

---