import tkinter as tk
from tkinter import messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from plotter import draw_rgb_space
from utils import validate_inputs, check_point_inside

def build_gui(root):
    vars = {
        'R1': tk.StringVar(value="50"), 'R2': tk.StringVar(value="200"),
        'G1': tk.StringVar(value="30"), 'G2': tk.StringVar(value="180"),
        'B1': tk.StringVar(value="100"), 'B2': tk.StringVar(value="220"),
        'r': tk.StringVar(value="120"), 'g': tk.StringVar(value="100"), 'b': tk.StringVar(value="150"),
        'inside': tk.BooleanVar(),
        'figure': None
    }

    input_frame = tk.Frame(root)
    input_frame.pack(padx=10, pady=5)

    # Поля ввода
    for key in ['R1','R2','G1','G2','B1','B2','r','g','b']:
        tk.Label(input_frame, text=key).pack(side=tk.LEFT)
        tk.Entry(input_frame, textvariable=vars[key], width=5).pack(side=tk.LEFT, padx=2)

    # Кнопки
    tk.Button(input_frame, text="Построить", command=lambda: on_submit(vars, plot_frame, result_label)).pack(side=tk.LEFT, padx=10)
    tk.Checkbutton(input_frame, text="Проверить вхождение", variable=vars['inside']).pack(side=tk.LEFT)
    tk.Button(input_frame, text="Сохранить PNG", command=lambda: save_png(vars)).pack(side=tk.LEFT, padx=10)

    # Метка результата
    result_label = tk.Label(root, text="", font=("Arial", 12))
    result_label.pack()

    # Область под график
    plot_frame = tk.Frame(root)
    plot_frame.pack(fill=tk.BOTH, expand=True)

    vars['plot_frame'] = plot_frame
    vars['result_label'] = result_label

def on_submit(vars, plot_frame, result_label):
    try:
        values = {key: int(vars[key].get()) for key in ['R1','R2','G1','G2','B1','B2','r','g','b']}
        validate_inputs(values)
        for widget in plot_frame.winfo_children():
            widget.destroy()

        check = vars['inside'].get()
        inside = check_point_inside(values) if check else None
        result_label.config(text=f"Результат: {'Внутри' if inside else 'Снаружи'}", fg='green' if inside else 'red' if check else 'black')

        fig = draw_rgb_space(**values, check_inside=check)
        vars['figure'] = fig
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

def save_png(vars):
    fig = vars.get('figure')
    if fig:
        path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG файлы", "*.png")])
        if path:
            fig.savefig(path)
            messagebox.showinfo("Сохранено", f"Файл сохранён: {path}")
    else:
        messagebox.showwarning("Нет графика", "Сначала построй график.")
