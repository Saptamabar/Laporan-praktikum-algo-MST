import tkinter as tk
import math

def draw_vertices(canvas, vertices):
    
    for vertex in vertices:
        if vertex == vertices[0]:
            x, y = vertex
            canvas.create_oval(x-5, y-5, x+5, y+5, fill='green')
        else:
            x, y = vertex
            canvas.create_oval(x-5, y-5, x+5, y+5, fill='red')

def generate_minimum_spanning_tree(vertices):
    edges = []
    connected_vertices = [vertices[0]]
    unconnected_vertices = vertices[1:]
    
    while unconnected_vertices:
        min_distance = math.inf
        min_edge = None
        for connected_vertex in connected_vertices:
            for unconnected_vertex in unconnected_vertices:
                distance = calculate_distance(connected_vertex, unconnected_vertex)
                if distance < min_distance:
                    min_distance = distance
                    min_edge = (connected_vertex, unconnected_vertex)
        
        connected_vertex, unconnected_vertex = min_edge
        edges.append(min_edge)
        connected_vertices.append(unconnected_vertex)
        unconnected_vertices.remove(unconnected_vertex)
    
    return edges

def calculate_distance(vertex1, vertex2):
    x1, y1 = vertex1
    x2, y2 = vertex2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def draw_edges(canvas, edges):
    for edge in edges:
        start, end = edge
        canvas.create_line(start[0], start[1], end[0], end[1], fill='blue')

def masukan_fakultas():
    Jumlah_fakultas = tk.Tk()
    def fakultas(jumlah):
        def tambah():
            a.append((int(entry_fakultas.get()), int(entry_fakultas1.get())))
            Fakultas.destroy()

        for i in range(jumlah):
            Fakultas = tk.Tk()
            input_label = tk.Label(Fakultas, text="Masukan koordinat Fakultas (50 - 350)")
            input_label.pack()
            input_labels = tk.Label(Fakultas, text="Masukkan koordinat x: ")
            input_labels.pack()

            entry_fakultas = tk.Entry(Fakultas, width=30)
            entry_fakultas.pack(pady=10)

            input_label1 = tk.Label(Fakultas, text="Masukkan koordinat y: ")
            input_label1.pack()

            entry_fakultas1 = tk.Entry(Fakultas, width=30)
            entry_fakultas1.pack(pady=10)

            button = tk.Button(Fakultas, text="Ambil Input", command=tambah)
            button.pack()
            Fakultas.mainloop()

    def get_input():
        global input_text
        input_text = entry.get()
        Jumlah_fakultas.destroy()

    input_label = tk.Label(Jumlah_fakultas, text="Masukan jumlah fakultas : ")
    input_label.pack()

    entry = tk.Entry(Jumlah_fakultas, width=30)
    entry.pack(pady=10)

    button = tk.Button(Jumlah_fakultas, text="Ambil Input", command=get_input)
    button.pack()

    Jumlah_fakultas.mainloop()
    fakultas(int(input_text))

def masukan_koordinat():
    def get_input():
        global a
        a = []
        input_text = entry.get()
        input_text1 = entry1.get()
        a.append((int(input_text),int(input_text1)))
        UPPTI.destroy()
        masukan_fakultas()

    UPPTI = tk.Tk()
    UPPTI.title("Masukan koordinat UPPTI (50 - 350)")

    input_label = tk.Label(UPPTI, text="Masukan koordinat UPPTI (50 - 350)")
    input_label.pack()
    input_labels = tk.Label(UPPTI, text="Masukkan koordinat x: ")
    input_labels.pack()

    entry = tk.Entry(UPPTI, width=30)
    entry.pack(pady=10)

    input_label1 = tk.Label(UPPTI, text="Masukkan koordinat y: ")
    input_label1.pack()

    entry1 = tk.Entry(UPPTI, width=30)
    entry1.pack(pady=10)

    button = tk.Button(UPPTI, text="Ambil Input", command=get_input)
    button.pack()

    UPPTI.mainloop()
    return a
    
def main():
    
    vertices = masukan_koordinat()
    root = tk.Tk()
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()
    
    draw_vertices(canvas, vertices)
    input_label = tk.Label(root, text="Hijau = UPPTI")
    input_label1 = tk.Label(root, text="Merah = Fakultas")
    input_label.pack()
    input_label1.pack()

    def buat_edged():
        edges = generate_minimum_spanning_tree(vertices)
        draw_edges(canvas, edges)
    button = tk.Button(root, text="Buat edges", command=buat_edged)
    button.pack()
    
    root.mainloop()

if __name__ == "__main__":
    main()

