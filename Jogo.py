import random

def escolher_palavra():
    palavras = ["programacao", "tecnologia", "computador", "python", "algoritmo", "desenvolvimento", "software", "hardware", "logica", "tendencias"]
    return random.choice(palavras)


def exibir_forca(tentativas):
    estagios = [
        """
            -----
            |   |
            |   
            |  
            |  
            |  
        """,
        """
            -----
            |   |
            |   O
            |  
            |  
            |  
        """,
        """
            -----
            |   |
            |   O
            |   |
            |  
            |  
        """,
        """
            -----
            |   |
            |   O
            |  /|
            |  
            |  
        """,
        """
            -----
            |   |
            |   O
            |  /|\\
            |  
            |  
        """,
        """
            -----
            |   |
            |   O
            |  /|\\
            |  / 
            |  
        """,
        """
            -----
            |   |
            |   O
            |  /|\\
            |  / \\
            |  
        """
    ]
    print(estagios[tentativas])


def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ["_" for _ in palavra]
    tentativas = 0
    letras_tentadas = set()
    
    print("Bem-vindo ao jogo da forca!")
    print("Vamos começar...")
    exibir_forca(tentativas)
    print(" ".join(palavra_oculta))
    

    while tentativas < 6 and "_" in palavra_oculta:
        try:
            letra = input("Digite uma letra: ").lower()
            if len(letra) != 1 or not letra.isalpha():
                raise ValueError("Por favor, digite uma única letra.")
            if letra in letras_tentadas:
                print("Você já tentou essa letra. Tente uma diferente.")
                continue

            letras_tentadas.add(letra)

            if letra in palavra:
                for i, char in enumerate(palavra):
                    if char == letra:
                        palavra_oculta[i] = letra
            else:
                tentativas += 1
            
            exibir_forca(tentativas)
            print(" ".join(palavra_oculta))
            print(f"Letras tentadas: {', '.join(letras_tentadas)}")
        
        except ValueError as e:
            print(e)


    if "_" not in palavra_oculta:
        print("Parabéns, você ganhou!")
    else:
        print(f"Você perdeu! A palavra era '{palavra}'.")

    print("Obrigado por jogar! Até a próxima.")

if __name__ == "__main__":
    jogar()