# -*- coding: utf-8 -*-
"""
Calculadora de Tablas de Verdad y Lógica Difusa

Interfaz gráfica minimalista desarrollada con Tkinter para explicar los
fundamentos de la Introducción a la Inteligencia Artificial.

Autor: Luis Valencia
"""

import tkinter as tk
from tkinter import ttk
from itertools import product


# ----------------------------------------------------------------
# Paleta de colores oscuro (dark theme)
# ----------------------------------------------------------------
COLOR_FONDO = "#121212"      # Fondo principal (casi negro)
COLOR_PANEL = "#1e1e1e"      # Paneles y pestañas (gris muy oscuro)
COLOR_PRIMARIO = "#3d3d3d"   # Gris oscuro para botones (acorde a dark theme)
COLOR_PRIMARIO_HOVER = "#505050"
COLOR_TEXTO = "#e0e0e0"      # Texto principal (gris claro)
COLOR_TEXTO_SUAVE = "#a0a0a0" # Texto secundario (gris medio)
COLOR_BORDE = "#333333"      # Bordes y separadores
COLOR_FONDO_AREA = "#121212" # Fondo de áreas de texto
COLOR_INSERT = "#ffffff"     # Color del cursor en entradas


# Colores de acento y estados
COLOR_TAB_ACTIVO_TXT = "#38bdf8"    # Celeste/cian brillante que resalta claramente en el tab activo
COLOR_TAB_INACTIVO_TXT = "#707070"  # Atenuado para diferenciar claramente el tab inactivo
COLOR_TAB_ACTIVO_LINEA = "#38bdf8"  # Línea superior de pestaña activa
COLOR_BTN_NORMAL = "#2d2d2d"        # Fondo normal del botón
COLOR_BTN_HOVER = "#404040"         # Efecto hover visible al pasar el cursor
COLOR_BTN_ACTIVE = "#525252"        # Efecto al hacer clic
COLOR_BTN_BORDER = "#3a3a3a"        # Borde sutil del botón


class BotonRedondeado(tk.Canvas):
    """Botón con bordes redondeados y efecto hover interactivo."""
    def __init__(
        self,
        master,
        text,
        command=None,
        bg_normal=COLOR_BTN_NORMAL,
        bg_hover=COLOR_BTN_HOVER,
        bg_active=COLOR_BTN_ACTIVE,
        border_color=COLOR_BTN_BORDER,
        fg=COLOR_TEXTO,
        font=("Segoe UI", 10),
        radius=10,
        height=38,
        **kwargs,
    ):
        super().__init__(
            master,
            height=height,
            bg=master["bg"],
            highlightthickness=0,
            cursor="hand2",
            **kwargs,
        )
        self.text = text
        self.command = command
        self.bg_normal = bg_normal
        self.bg_hover = bg_hover
        self.bg_active = bg_active
        self.border_color = border_color
        self.current_bg = bg_normal
        self.current_border = border_color
        self.fg = fg
        self.font = font
        self.radius = radius

        self.bind("<Configure>", self._dibujar)
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<Button-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _dibujar(self, event=None):
        self.delete("all")
        w = self.winfo_width()
        h = self.winfo_height()
        if w <= 4 or h <= 4:
            return

        r = self.radius
        points = [
            r, 2,  w - r, 2,  w - 2, 2,  w - 2, r,
            w - 2, h - r,  w - 2, h - 2,  w - r, h - 2,
            r, h - 2,  2, h - 2,  2, h - r,
            2, r,  2, 2
        ]
        self.create_polygon(
            points,
            smooth=True,
            fill=self.current_bg,
            outline=self.current_border,
            width=1,
        )
        self.create_text(
            w / 2,
            h / 2,
            text=self.text,
            fill=self.fg,
            font=self.font,
        )

    def _on_enter(self, event):
        self.current_bg = self.bg_hover
        self.current_border = "#555555"
        self._dibujar()

    def _on_leave(self, event):
        self.current_bg = self.bg_normal
        self.current_border = self.border_color
        self._dibujar()

    def _on_press(self, event):
        self.current_bg = self.bg_active
        self.current_border = "#666666"
        self._dibujar()

    def _on_release(self, event):
        self.current_bg = self.bg_hover
        self.current_border = "#555555"
        self._dibujar()
        if self.command:
            self.command()


class TabsHeader(tk.Frame):
    """Cabecera de pestañas con esquinas superiores redondeadas y misma altura."""
    def __init__(self, master, tabs, on_change, bg=COLOR_FONDO, height=44, **kwargs):
        super().__init__(master, bg=bg, **kwargs)
        self.tabs = tabs
        self.on_change = on_change
        self.tab_height = height
        self.selected_index = 0
        self.canvases = []

        for i, title in enumerate(tabs):
            c = tk.Canvas(
                self,
                width=175,
                height=self.tab_height,
                bg=bg,
                highlightthickness=0,
                cursor="hand2",
            )
            c.pack(side="left", padx=(0, 6))
            c.bind("<Button-1>", lambda e, idx=i: self.select(idx))
            c.bind("<Enter>", lambda e, idx=i: self._on_hover(idx, True))
            c.bind("<Leave>", lambda e, idx=i: self._on_hover(idx, False))
            self.canvases.append({"canvas": c, "title": title, "hover": False})

        self.redraw()

    def _on_hover(self, index, is_hover):
        if self.selected_index != index:
            self.canvases[index]["hover"] = is_hover
            self.redraw()

    def select(self, index):
        if self.selected_index != index:
            self.selected_index = index
            for item in self.canvases:
                item["hover"] = False
            self.redraw()
            self.on_change(index)

    def redraw(self):
        for i, item in enumerate(self.canvases):
            c = item["canvas"]
            title = item["title"]
            hover = item["hover"]
            c.delete("all")

            w = 175
            h = self.tab_height
            r = 12
            is_sel = (i == self.selected_index)

            if is_sel:
                fill_bg = COLOR_PANEL
                outline_col = "#383838"
                text_col = COLOR_TAB_ACTIVO_TXT
                font = ("Segoe UI", 10, "bold")
            elif hover:
                fill_bg = "#181818"
                outline_col = "#2a2a2a"
                text_col = "#b0b0b0"
                font = ("Segoe UI", 10)
            else:
                fill_bg = "#131313"
                outline_col = "#202020"
                text_col = COLOR_TAB_INACTIVO_TXT
                font = ("Segoe UI", 10)

            # Esquinas superiores redondeadas, parte inferior recta a ras del panel
            pts = [
                2, h,
                2, r,
                2, 2,
                r, 2,
                w - r, 2,
                w - 2, 2,
                w - 2, r,
                w - 2, h,
            ]
            c.create_polygon(
                pts,
                smooth=True,
                fill=fill_bg,
                outline=outline_col,
                width=1,
            )
            # Cubrir el borde inferior para conectar limpiamente con el panel
            c.create_line(2, h, w - 2, h, fill=fill_bg, width=2)

            if is_sel:
                # Línea superior de acento para mayor distinción visual
                c.create_line(r, 2, w - r, 2, fill=COLOR_TAB_ACTIVO_LINEA, width=2)

            c.create_text(
                w / 2,
                h / 2,
                text=title,
                fill=text_col,
                font=font,
            )


class CalculadoraApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora - Tablas de Verdad y Lógica Difusa")
        self.geometry("700x520")
        self.configure(bg=COLOR_FONDO)

        # Estilo para Scrollbar oscuro minimalista y visible
        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.style.configure(
            "Dark.Vertical.TScrollbar",
            troughcolor="#1e1e1e",
            background="#444444",
            bordercolor="#1e1e1e",
            darkcolor="#3a3a3a",
            lightcolor="#555555",
            arrowcolor="#aaaaaa",
            gripcount=0,
            borderwidth=0,
        )
        self.style.map(
            "Dark.Vertical.TScrollbar",
            background=[("active", "#666666"), ("pressed", "#777777")],
            arrowcolor=[("active", "#ffffff"), ("pressed", "#ffffff")],
        )

        self._construir_interfaz()

    # ------------------------------------------------------------
    # Interfaz
    # ------------------------------------------------------------
    def _construir_interfaz(self):
        contenedor = tk.Frame(self, bg=COLOR_FONDO)
        contenedor.pack(fill="both", expand=True, padx=24, pady=24)

        # Encabezado
        encabezado = tk.Frame(contenedor, bg=COLOR_FONDO)
        encabezado.pack(fill="x", pady=(0, 16))

        tk.Label(
            encabezado,
            text="Fundamentos de IA",
            font=("Segoe UI", 11, "bold"),
            fg=COLOR_TEXTO,
            bg=COLOR_FONDO,
        ).pack(side="left")
        tk.Label(
            encabezado,
            text="  ·  Tablas de verdad y lógica difusa",
            font=("Segoe UI", 10),
            fg=COLOR_TEXTO_SUAVE,
            bg=COLOR_FONDO,
        ).pack(side="left")

        # Pestañas personalizadas con esquinas redondeadas
        self.header_tabs = TabsHeader(
            contenedor,
            tabs=["Tablas de Verdad", "Lógica Difusa"],
            on_change=self._cambiar_pestaña,
            bg=COLOR_FONDO,
        )
        self.header_tabs.pack(fill="x")

        # Contenedor de contenido de las pestañas
        self.cuerpo_tabs = tk.Frame(contenedor, bg=COLOR_PANEL, bd=1, relief="solid")
        self.cuerpo_tabs.pack(fill="both", expand=True)

        self.pestaña_tabla = tk.Frame(self.cuerpo_tabs, bg=COLOR_PANEL)
        self.pestaña_difusa = tk.Frame(self.cuerpo_tabs, bg=COLOR_PANEL)

        self._construir_pestaña_tabla()
        self._construir_pestaña_difusa()

        # Mostrar la primera pestaña por defecto
        self._cambiar_pestaña(0)

        # Pie de página
        pie = tk.Frame(contenedor, bg=COLOR_FONDO)
        pie.pack(fill="x", pady=(16, 0))
        tk.Label(
            pie,
            text="Realizado por Luis Valencia - Introducción a la Inteligencia Artificial",
            font=("Segoe UI", 9),
            fg=COLOR_TEXTO_SUAVE,
            bg=COLOR_FONDO,
        ).pack(side="right")

    def _cambiar_pestaña(self, index):
        if index == 0:
            self.pestaña_difusa.pack_forget()
            self.pestaña_tabla.pack(fill="both", expand=True)
        else:
            self.pestaña_tabla.pack_forget()
            self.pestaña_difusa.pack(fill="both", expand=True)

    # ------------------------------------------------------------
    # Pestaña: Tablas de Verdad
    # ------------------------------------------------------------
    def _construir_pestaña_tabla(self):
        panel = tk.Frame(self.pestaña_tabla, bg=COLOR_PANEL)
        panel.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(
            panel,
            text="Seleccione un conectivo lógico:",
            font=("Segoe UI", 10, "bold"),
            fg=COLOR_TEXTO,
            bg=COLOR_PANEL,
        ).pack(anchor="w", pady=(0, 12))

        botones = [
            ("Negación (~p)", self._mostrar_negacion),
            ("Conjunción (p AND q)", self._mostrar_conjuncion),
            ("Disyunción (p OR q)", self._mostrar_disyuncion),
            ("Bicondicional (p IFF q)", self._mostrar_bicondicional),
            ("Mostrar todas", self._mostrar_todas),
        ]

        for texto, comando in botones:
            btn = BotonRedondeado(
                panel,
                text=texto,
                command=comando,
                height=38,
                radius=9,
            )
            btn.pack(fill="x", pady=4)

        tk.Label(
            panel,
            text="Haga clic en un conectivo para ver su tabla de verdad en una ventana emergente.",
            font=("Segoe UI", 9),
            fg=COLOR_TEXTO_SUAVE,
            bg=COLOR_PANEL,
        ).pack(anchor="w", pady=(16, 0))

    def _mostrar_popup(self, titulo, lineas, ancho=560, alto=420):
        """Muestra el contenido en una ventana emergente con scrollbar (tema oscuro)."""
        popup = tk.Toplevel(self)
        popup.title(titulo)
        popup.configure(bg=COLOR_FONDO)
        popup.transient(self)

        # Definir tamaño mínimo proporcional y dimensiones iniciales
        popup.minsize(max(200, int(ancho * 0.8)), max(140, int(alto * 0.7)))

        # Posicionar centrado sobre la ventana principal
        self.update_idletasks()
        pos_x = self.winfo_rootx() + (self.winfo_width() // 2) - (ancho // 2)
        pos_y = self.winfo_rooty() + (self.winfo_height() // 2) - (alto // 2)
        popup.geometry(f"{ancho}x{alto}+{max(0, pos_x)}+{max(0, pos_y)}")

        contenedor = tk.Frame(popup, bg=COLOR_FONDO)
        contenedor.pack(fill="both", expand=True, padx=16, pady=16)

        # Área de texto con scrollbar vertical
        frame_texto = tk.Frame(contenedor, bg=COLOR_PANEL, bd=1, relief="solid")
        frame_texto.pack(fill="both", expand=True)

        scrollbar = ttk.Scrollbar(
            frame_texto,
            orient="vertical",
            style="Dark.Vertical.TScrollbar",
        )
        scrollbar.pack(side="right", fill="y")

        texto = tk.Text(
            frame_texto,
            font=("Consolas", 11),
            bg=COLOR_FONDO_AREA,
            fg="#ffffff",
            insertbackground="#ffffff",
            relief="flat",
            padx=14,
            pady=14,
            yscrollcommand=scrollbar.set,
            wrap="none",
        )
        texto.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=texto.yview)

        texto.insert("1.0", "\n".join(lineas))
        texto.configure(state="disabled")

        # Botón cerrar con esquinas redondeadas y efecto hover
        btn_cerrar = BotonRedondeado(
            contenedor,
            text="Cerrar",
            command=popup.destroy,
            font=("Segoe UI", 10),
            height=34,
            radius=8,
        )
        btn_cerrar.pack(pady=(12, 0))

        # Asegurar que el popup aparezca al frente y tenga el foco
        popup.deiconify()
        popup.lift()
        popup.focus_force()

    def _formato_valor(self, v):
        return "V" if v else "F"

    def _mostrar_negacion(self):
        lineas = [
            "TABLA DE VERDAD - NEGACIÓN (~p)",
            "=" * 30,
            f"{'p':^5} | {'~p':^5}",
            "-" * 13,
        ]
        for p in (True, False):
            linea = f"{self._formato_valor(p):^5} | {self._formato_valor(not p):^5}"
            lineas.append(linea)
        self._mostrar_popup("Negación (~p)", lineas)

    def _mostrar_conjuncion(self):
        lineas = [
            "TABLA DE VERDAD - CONJUNCIÓN (p AND q)",
            "=" * 34,
            f"{'p':^5} | {'q':^5} | {'p AND q':^9}",
            "-" * 23,
        ]
        for p, q in product((True, False), repeat=2):
            linea = (
                f"{self._formato_valor(p):^5} | {self._formato_valor(q):^5} | "
                f"{self._formato_valor(p and q):^9}"
            )
            lineas.append(linea)
        self._mostrar_popup("Conjunción (p AND q)", lineas)

    def _mostrar_disyuncion(self):
        lineas = [
            "TABLA DE VERDAD - DISYUNCIÓN (p OR q)",
            "=" * 33,
            f"{'p':^5} | {'q':^5} | {'p OR q':^8}",
            "-" * 23,
        ]
        for p, q in product((True, False), repeat=2):
            linea = (
                f"{self._formato_valor(p):^5} | {self._formato_valor(q):^5} | "
                f"{self._formato_valor(p or q):^8}"
            )
            lineas.append(linea)
        self._mostrar_popup("Disyunción (p OR q)", lineas)

    def _mostrar_bicondicional(self):
        lineas = [
            "TABLA DE VERDAD - BICONDICIONAL (p IFF q)",
            "=" * 36,
            f"{'p':^5} | {'q':^5} | {'p IFF q':^9}",
            "-" * 23,
        ]
        for p, q in product((True, False), repeat=2):
            linea = (
                f"{self._formato_valor(p):^5} | {self._formato_valor(q):^5} | "
                f"{self._formato_valor(p == q):^9}"
            )
            lineas.append(linea)
        self._mostrar_popup("Bicondicional (p IFF q)", lineas)

    def _mostrar_todas(self):
        """Muestra todas las tablas de verdad en una sola ventana emergente."""
        lineas = []
        bloques = []

        # Negación
        bloques.append(("TABLA DE VERDAD - NEGACIÓN (~p)", "-" * 13))
        bloques.append((f"{'p':^5} | {'~p':^5}", None))
        for p in (True, False):
            bloques.append(
                (
                    f"{self._formato_valor(p):^5} | {self._formato_valor(not p):^5}",
                    None,
                )
            )
        bloques.append(("", None))

        # Conjunción
        bloques.append(("TABLA DE VERDAD - CONJUNCIÓN (p AND q)", "-" * 23))
        bloques.append((f"{'p':^5} | {'q':^5} | {'p AND q':^9}", None))
        for p, q in product((True, False), repeat=2):
            bloques.append(
                (
                    f"{self._formato_valor(p):^5} | {self._formato_valor(q):^5} | "
                    f"{self._formato_valor(p and q):^9}",
                    None,
                )
            )
        bloques.append(("", None))

        # Disyunción
        bloques.append(("TABLA DE VERDAD - DISYUNCIÓN (p OR q)", "-" * 23))
        bloques.append((f"{'p':^5} | {'q':^5} | {'p OR q':^8}", None))
        for p, q in product((True, False), repeat=2):
            bloques.append(
                (
                    f"{self._formato_valor(p):^5} | {self._formato_valor(q):^5} | "
                    f"{self._formato_valor(p or q):^8}",
                    None,
                )
            )
        bloques.append(("", None))

        # Bicondicional
        bloques.append(("TABLA DE VERDAD - BICONDICIONAL (p IFF q)", "-" * 23))
        bloques.append((f"{'p':^5} | {'q':^5} | {'p IFF q':^9}", None))
        for p, q in product((True, False), repeat=2):
            bloques.append(
                (
                    f"{self._formato_valor(p):^5} | {self._formato_valor(q):^5} | "
                    f"{self._formato_valor(p == q):^9}",
                    None,
                )
            )

        for texto, _ in bloques:
            lineas.append(texto)

        self._mostrar_popup("Todas las tablas de verdad", lineas)

    # ------------------------------------------------------------
    # Pestaña: Lógica Difusa
    # ------------------------------------------------------------
    def _construir_pestaña_difusa(self):
        panel = tk.Frame(self.pestaña_difusa, bg=COLOR_PANEL)
        panel.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(
            panel,
            text="Lógica Difusa - Valores entre 0 y 1",
            font=("Segoe UI", 10, "bold"),
            fg=COLOR_TEXTO,
            bg=COLOR_PANEL,
        ).pack(anchor="w", pady=(0, 12))

        # Entradas
        entradas = tk.Frame(panel, bg=COLOR_PANEL)
        entradas.pack(fill="x", pady=(0, 12))

        tk.Label(
            entradas, text="Valor A:", font=("Segoe UI", 10), fg=COLOR_TEXTO,
            bg=COLOR_PANEL,
        ).grid(row=0, column=0, sticky="w", padx=(0, 8))
        self.entrada_a = tk.Entry(
            entradas,
            font=("Segoe UI", 10),
            width=12,
            relief="solid",
            bd=1,
            bg=COLOR_PANEL,
            fg=COLOR_TEXTO,
            insertbackground=COLOR_INSERT,
            highlightbackground=COLOR_BORDE,
            highlightcolor=COLOR_PRIMARIO,
        )
        self.entrada_a.grid(row=0, column=1, padx=(0, 16))
        self.entrada_a.insert(0, "0.7")

        tk.Label(
            entradas, text="Valor B:", font=("Segoe UI", 10), fg=COLOR_TEXTO,
            bg=COLOR_PANEL,
        ).grid(row=0, column=2, sticky="w", padx=(0, 8))
        self.entrada_b = tk.Entry(
            entradas,
            font=("Segoe UI", 10),
            width=12,
            relief="solid",
            bd=1,
            bg=COLOR_PANEL,
            fg=COLOR_TEXTO,
            insertbackground=COLOR_INSERT,
            highlightbackground=COLOR_BORDE,
            highlightcolor=COLOR_PRIMARIO,
        )
        self.entrada_b.grid(row=0, column=3)
        self.entrada_b.insert(0, "0.4")

        # Botones de operación
        ops = [
            ("AND (mínimo)", self._difusa_and),
            ("OR (máximo)", self._difusa_or),
            ("NOT A", self._difusa_not_a),
            ("NOT B", self._difusa_not_b),
        ]
        for texto, comando in ops:
            btn = BotonRedondeado(
                panel,
                text=texto,
                command=comando,
                height=38,
                radius=9,
            )
            btn.pack(fill="x", pady=4)

        tk.Label(
            panel,
            text="Seleccione una operación para ver el resultado en una ventana emergente.",
            font=("Segoe UI", 9),
            fg=COLOR_TEXTO_SUAVE,
            bg=COLOR_PANEL,
        ).pack(anchor="w", pady=(16, 0))

    def _leer_valores(self):
        try:
            a = float(self.entrada_a.get())
            b = float(self.entrada_b.get())
            if not (0 <= a <= 1 and 0 <= b <= 1):
                raise ValueError
            return a, b
        except ValueError:
            self._mostrar_popup(
                "Error",
                ["Ingrese valores numéricos entre 0 y 1."],
                ancho=480,
                alto=240,
            )
            return None, None

    def _difusa_and(self):
        a, b = self._leer_valores()
        if a is None:
            return
        resultado = min(a, b)
        self._mostrar_popup(
            "Lógica Difusa - AND",
            [f"A AND DIFUSA B = min({a}, {b}) = {resultado:.2f}"],
            ancho=480,
            alto=240,
        )

    def _difusa_or(self):
        a, b = self._leer_valores()
        if a is None:
            return
        resultado = max(a, b)
        self._mostrar_popup(
            "Lógica Difusa - OR",
            [f"A OR DIFUSA B = max({a}, {b}) = {resultado:.2f}"],
            ancho=480,
            alto=240,
        )

    def _difusa_not_a(self):
        a, _ = self._leer_valores()
        if a is None:
            return
        resultado = 1 - a
        self._mostrar_popup(
            "Lógica Difusa - NOT A",
            [f"NOT DIFUSA A = 1 - {a} = {resultado:.2f}"],
            ancho=480,
            alto=240,
        )

    def _difusa_not_b(self):
        _, b = self._leer_valores()
        if b is None:
            return
        resultado = 1 - b
        self._mostrar_popup(
            "Lógica Difusa - NOT B",
            [f"NOT DIFUSA B = 1 - {b} = {resultado:.2f}"],
            ancho=480,
            alto=240,
        )


if __name__ == "__main__":
    app = CalculadoraApp()
    app.mainloop()
