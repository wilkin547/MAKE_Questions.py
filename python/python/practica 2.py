from typing import ItemsView, NewType


frase = input() + " "

def comprueba_verbs(frase):


    verbos = ["is","are","run","go","stay","swim"]

    for verb in verbos:

        if frase == verb + " ":
            return True

    return False
def encuentra_Pregunta(phrase):



    word = ""
    Question = []

    

    for letter in phrase:

        if  letter != " " :

            word += letter
        
        else: 

            Question.append(word + " ")
            word = ""
        

    return Question

def Make_Question_open(palabras):

    complento = ""
    sujeto = ""
    vervo = ""

    isSubect = True
    isComplemto = False
    isVerb = False
    

    for word in palabras:

        if   comprueba_verbs(word): 

            isSubect = False
            isVerb = True

        if isSubect :

            sujeto += word
            

        if isVerb :

            vervo += word
            isComplemto = True
            isVerb = False
            continue
            

        if isComplemto :

            complento += word


    texto_final =  "what " + vervo +  complento + "? " 
    return texto_final

def estructura_frase(palabras):
    complento = ""
    sujeto = ""
    vervo = ""

    isSubect = True
    isComplemto = False
    isVerb = False
    

    for word in palabras:


        if comprueba_verbs(word): 

            isSubect = False
            isVerb = True

        if isSubect :

            sujeto += word
            

        if isVerb :

            vervo += word
            isComplemto = True
            isVerb = False
            continue
            

        if isComplemto :

            complento += word


    texto = {
        "sujeto" : sujeto,
        "verbo"  : vervo,
        "complento" : complento
    }
    return texto

#hola mundo 
