meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "Random": "Algo aleatorio o inesperado.",

"Mood":  "Se usa para expresar identificación con una emoción o situación.",

"Bro": "Amigo (equivalente a parce, mano, etc.).",

"F" : "Para mostrar respeto o lamento (viene de los videojuegos).",

"Tóxico/a": "Alguien que causa problemas o drama.",

"Flexear":  "Presumir algo.",

"Shippear": " Querer que dos personas estén juntas (de relationship)." ,

"Spoiler" : "Revelar algo importante de una serie, película, etc." ,

"LOL" :  "Reírse (Laugh Out Loud)." ,

"Fake": "Falso, poco auténtico."}
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("la palabra no esta en el diccionario ")
