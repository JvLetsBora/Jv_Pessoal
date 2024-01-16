extends Node2D


enum elevador{
	ANDANDO,
	PARADO
}

var andares = {
	PRIMEIRO = Vector2(334,310),
	SEGUNDO = Vector2(334, 273),
	TERCEIRO = Vector2(334, 237),
	QUARTO = Vector2(334, 202),
	QUINTO = Vector2(334,168),
	SEXTO = Vector2(334,134),
	SETIMO = Vector2(334, 100),
	OITAVO = Vector2(334, 65),
	NONO = Vector2(334,34)
}

var andar = ""

var adares_on = []

func _ready():
	pass # Replace with function body.



func _process(delta):
	pass


func andarTeck(andar):
	var a = []
	for i in adares_on:
		if !(i in a):
			 a.append(i)
	print(a)
	return andar in a

func add_Andar(_andar, obj):
	obj.modulate = Color(1, 0.490196, 0.490196)
	adares_on.append(_andar)
	andarTeck(andar)

func _on_btn_3_pressed():
	add_Andar(andares.TERCEIRO, $Andar_buttons/btn_3)

func _on_btn_2_pressed():
	add_Andar(andares.SEGUNDO, $Andar_buttons/btn_2)

func _on_btn_1_pressed():
	add_Andar(andares.PRIMEIRO, $Andar_buttons/btn_1)

func _on_btn_6_pressed():
	add_Andar(andares.SEXTO, $Andar_buttons/btn_6)

func _on_btn_5_pressed():
	add_Andar(andares.QUINTO, $Andar_buttons/btn_5)

func _on_btn_4_pressed():
	add_Andar(andares.QUARTO, $Andar_buttons/btn_4)

func _on_btn_9_pressed():
	add_Andar(andares.NONO, $Andar_buttons/btn_9)

func _on_btn_8_pressed():
	add_Andar(andares.OITAVO, $Andar_buttons/btn_8)

func _on_btn_7_pressed():
	add_Andar(andares.SETIMO, $Andar_buttons/btn_7)
