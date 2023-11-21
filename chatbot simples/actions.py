point_dict = {
    "martelo": ((0.0, 2.0, 0.0, 1.0, 0.0, 0.0),"Setor A"),
    "marreta": ((60.0, 0.0, 0.0, 1.0, 0.0, 0.0),"Setor B"),
    "prego": ((0.0, 0.2, 0.0, 1.0, 0.0, 0.0),"Setor A"),
    "porca": ((5.0, 0.0, 0.0, 1.0, 7.0, 0.0),"Setor D"),
    "chave de Fenda": ((0.0, 0.0, 0.0, 1.0, 0.0, 0.0),"Setor C"),
    "alicate": ((0.0, 0.2, 0.0, 1.0, 0.0, 0.0),"Setor A"),
    "chave Inglesa": ((6.0, 2.0, 0.0, 1.0, 0.0, 0.0),"Setor C"),
    "parafuso": ((0.0, 0.0, 0.0, 1.0, 0.0, 7.0),"Setor A"),
    "serra": ((6.0, 0.2, 0.0, 1.0, 0.0, 0.0),"Setor B"),
    "lixa": ((5.0, 0.4, 0.0, 1.0, 0.0, 7.0),"Setor D"),
}




def control(a):
    if a in point_dict:
        print(f"{(str(a)[-1]).upper()} '{a}' se enconta no {point_dict[a][1]}: {point_dict[a][0]}")
    else:
        print(f"Esse ponto não está cadastrado: {a}")
   
    