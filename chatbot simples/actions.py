point_dict = {
    "Martelo": (0.0, 0.0, 0.0, 1.0, 0.0, 0.0),
    "Marreta": (0.0, 1.0, 0.0, 1.0, 0.0, 0.0),
    "Prego": (0.0, 3.0, 0.0, 1.0, 0.0, 0.0),
    "Porca": (0.0, 0.0, 0.0, 1.0, 0.0, 0.0),
    "Chave de Fenda": (1.0, 1.0, 1.0, 0.0, 0.0, 1.0),
    "Alicate": (-1.0, -1.0, -1.0, 0.0, 1.0, 0.0),
    "Chave Inglesa": (2.0, 2.0, 2.0, 0.0, 1.0, 1.0),
    "Parafuso": (-2.0, -2.0, -2.0, 1.0, 0.0, 0.0),
    "Serra": (3.0, 3.0, 3.0, 1.0, 1.0, 1.0),
    "Lixa": (-3.0, -3.0, -3.0, 1.0, 1.0, 0.0),
}







def go_to(point):
    if point in point_dict:
        print(f"Indo para '{point}': {point_dict[point]}")
    else:
        print("Esse ponto não está cadastrado: {point}")


def control():
    print("teste")
    pass