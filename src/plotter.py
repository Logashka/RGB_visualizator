import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def draw_rgb_space(R1, R2, G1, G2, B1, B2, r, g, b, check_inside=False):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Вершины и грани
    v = lambda x, y, z: [x, y, z]
    vertices = [v(R1,G1,B1), v(R2,G1,B1), v(R2,G2,B1), v(R1,G2,B1),
                v(R1,G1,B2), v(R2,G1,B2), v(R2,G2,B2), v(R1,G2,B2)]
    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],
        [vertices[4], vertices[5], vertices[6], vertices[7]],
        [vertices[0], vertices[1], vertices[5], vertices[4]],
        [vertices[2], vertices[3], vertices[7], vertices[6]],
        [vertices[1], vertices[2], vertices[6], vertices[5]],
        [vertices[4], vertices[7], vertices[3], vertices[0]]
    ]
    cube = Poly3DCollection(faces, alpha=0.3, facecolor='gray', edgecolor='black')
    ax.add_collection3d(cube)

    # Точка
    ax.scatter([r], [g], [b], color=(r/255, g/255, b/255), s=100, label=f'Точка ({r}, {g}, {b})')

    # Оси и подписи
    ax.set_xlim(0, 255); ax.set_ylim(0, 255); ax.set_zlim(0, 255)
    ax.quiver(0, 0, 0, 255, 0, 0, color='red', arrow_length_ratio=0.02)
    ax.quiver(0, 0, 0, 0, 255, 0, color='green', arrow_length_ratio=0.02)
    ax.quiver(0, 0, 0, 0, 0, 255, color='blue', arrow_length_ratio=0.02)
    ax.set_xlabel('R', color='red'); ax.set_ylabel('G', color='green'); ax.set_zlabel('B', color='blue')

    legend_items = [
        f"R1={R1}, R2={R2} — диапазон RED",
        f"G1={G1}, G2={G2} — диапазон GREEN",
        f"B1={B1}, B2={B2} — диапазон BLUE",
        f"r={r}, g={g}, b={b} — координаты точки"
    ]
    ax.legend(
        title="Обозначения:\n" + "\n".join(legend_items),
        loc='upper left',
        bbox_to_anchor=(-0.45, 1.0),
        fontsize='small',
        borderaxespad=0.5
    )

    ax.set_title("RGB-пространство")
    return fig
