# 📘 Tabla de Verdad - Conectivos Lógicos

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Estado](https://img.shields.io/badge/Estado-Completado-green)](https://github.com/)
[![Usuarios - Introducción a la Inteligencia Artificial](https://img.shields.io/badge/Curso-Introducción%20a%20la%20Inteligencia%20Artificial-orange)](https://ucn.edu.co/)
[![Autor](https://img.shields.io/badge/Autor-Luis%20Valencia-blueviolet)](https://github.com/)
[![Licencia](https://img.shields.io/badge/Licencia-Educativa-lightgrey)](https://github.com/)

## 📄 Descripción

Este proyecto es un programa básico escrito en Python que permite **visualizar las tablas de verdad** de los conectivos lógicos fundamentales:

- **Negación** (`~p`)
- **Conjunción** (`p AND q`)
- **Disyunción** (`p OR q`)
- **Bicondicional** (`p IFF q`)

Incluye un **menú interactivo** que permite seleccionar un conectivo individual o mostrar todas las tablas de verdad a la vez.

### Archivo principal

- `tabla-de-verdad.py` — Contiene la lógica del programa con funciones independientes para cada conectivo y un menú principal de ejecución.

## 🛠️ Requisitos

- Python 3.x instalado.
- No requiere librerías externas (usa solo la librería estándar de Python: `itertools.product`).

## 🚀 Instalación y ejecución

### 1. Crear el entorno virtual

```bash
python -m venv venv
```

### 2. Activar el entorno virtual

**En Windows (PowerShell / CMD):**

```powershell
venv\Scripts\activate
```

> *Nota:* Si estás en PowerShell y te aparece un error de permisos de ejecución de scripts, puedes usar:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
> venv\Scripts\Activate.ps1
> ```

**En Linux/macOS:**

```bash
source venv/bin/activate
```

Una vez activado, verás el prefijo `(venv)` al inicio de la terminal.

---

### 3. Ejecutar el programa

Con el entorno virtual activado, ejecuta el archivo principal:

```bash
python tabla-de-verdad.py
```

Al ejecutar, se mostrará un menú con las opciones:

```
1. Negación (~p)
2. Conjunción (p AND q)
3. Disyunción (p OR q)
4. Bicondicional (p IFF q)
5. Mostrar todas las tablas
0. Salir
```

## ✍️ Ejemplo de salida

```
===================================
TABLA DE VERDAD - CONJUNCIÓN (p AND q)
===================================
  p   |  q   | p AND q
---------------------
  V   |  V   |    V
  V   |  F   |    F
  F   |  V   |    F
  F   |  F   |    F
```

## 👨‍💻 Autoría

Este proyecto fue **realizado por Luis Valencia** como parte del curso de Introducción a la Inteligencia Artificial (UCN).

## 📄 Licencia

Este proyecto tiene un propósito educativo.

---