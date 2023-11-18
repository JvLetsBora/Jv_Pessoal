point_dict = {
    r"martelo": ((0.0, 2.0, 0.0, 1.0, 0.0, 0.0),"Setor A"),
    r"marreta": ((60.0, 0.0, 0.0, 1.0, 0.0, 0.0),"Setor B"),
    r"prego": ((0.0, 0.2, 0.0, 1.0, 0.0, 0.0),"Setor A"),
    r"porca": ((5.0, 0.0, 0.0, 1.0, 7.0, 0.0),"Setor D"),
    r"chave de Fenda": ((0.0, 0.0, 0.0, 1.0, 0.0, 0.0),"Setor C"),
    r"alicate": ((0.0, 0.2, 0.0, 1.0, 0.0, 0.0),"Setor A"),
    r"chave Inglesa": ((6.0, 2.0, 0.0, 1.0, 0.0, 0.0),"Setor C"),
    r"parafuso": ((0.0, 0.0, 0.0, 1.0, 0.0, 7.0),"Setor A"),
    r"serra": ((6.0, 0.2, 0.0, 1.0, 0.0, 0.0),"Setor B"),
    r"lixa": ((5.0, 0.4, 0.0, 1.0, 0.0, 7.0),"Setor D"),
}

area_dict = {
    "setor a": (0.0, 2.0, 0.0, 1.0, 0.0, 0.0),
     "setor b": (60.0, 0.0, 0.0, 1.0, 0.0, 0.0),
    "setor c": (0.0, 0.2, 0.0, 1.0, 0.0, 0.0),
     "setor d": (5.0, 0.0, 0.0, 1.0, 7.0, 0.0)
}





def go_to(point):
    if point in area_dict:
        print(f"Indo para '{point}': {area_dict[point]}")
    else:
        print(f"Esse ponto não está cadastrado: {point}")


def control(a):
    if a in point_dict:
        print(f"{(str(a)[-1]).upper()} '{a}' se enconta no {point_dict[a][1]}: {point_dict[a][0]}")
    else:
        print(f"Esse ponto não está cadastrado: {a}")
   
    