area_dict = {
    "setor a": (0.0, 2.0, 0.0, 1.0, 0.0, 0.0),
     "setor b": (60.0, 0.0, 0.0, 1.0, 0.0, 0.0),
    "setor c": (0.0, 0.2, 0.0, 1.0, 0.0, 0.0),
     "setor d": (5.0, 0.0, 0.0, 1.0, 7.0, 0.0)
}


point_dict = {
    r"martelo": (area_dict['setor a'],"Setor A"),
    r"marreta": (area_dict['setor b'],"Setor B"),
    r"prego": (area_dict["setor a"],"Setor A"),
    r"porca": (area_dict["setor d"],"Setor D"),
    r"chave de Fenda": (area_dict["setor c"],"Setor C"),
    r"alicate": (area_dict["setor a"],"Setor A"),
    r"chave Inglesa": (area_dict["setor c"],"Setor C"),
    r"parafuso": (area_dict["setor a"],"Setor A"),
    r"serra": (area_dict['setor b'],"Setor B"),
    r"lixa": (area_dict["setor d"],"Setor D"),
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
   
    