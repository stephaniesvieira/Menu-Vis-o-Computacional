import cv2
import time
import os
import numpy as np

# Cria a pasta para imagens modificadas se não existir
if not os.path.exists('Imagens Modificadas'):
    os.makedirs('Imagens Modificadas')

def salvar_imagem(nome_arquivo, imagem):
    """Função auxiliar para salvar imagens na pasta de modificadas"""
    caminho = os.path.join('Imagens Modificadas', nome_arquivo)
    cv2.imwrite(caminho, imagem)
    print(f"Imagem salva em: {caminho}")

def abrir_imagem():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Erro ao carregar a imagem 'img1.jpg'")
        return
    cv2.imshow('Imagem', imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def separar_canais():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Erro ao carregar a imagem 'img1.jpg'")
        return
    b, g, r = cv2.split(imagem)
    
    cv2.imshow('Canal Azul', b)
    cv2.imshow('Canal Verde', g)
    cv2.imshow('Canal Vermelho', r)
    
    # Salva os canais separados
    salvar_imagem('canal_azul.jpg', b)
    salvar_imagem('canal_verde.jpg', g)
    salvar_imagem('canal_vermelho.jpg', r)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def juntar_canais():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Erro ao carregar a imagem 'img1.jpg'")
        return
    b, g, r = cv2.split(imagem)
    imagem_resultado = cv2.merge((b, g, r))
    cv2.imshow('Imagem Original', imagem)
    cv2.imshow('Imagem Resultado', imagem_resultado)
    
    salvar_imagem('imagem_reconstruida.jpg', imagem_resultado)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def copiar_imagem():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Erro ao carregar a imagem 'img1.jpg'")
        return
    cv2.imshow('Imagem Original', imagem)
    imagem2 = imagem.copy()
    cv2.imshow('Imagem Copia', imagem2)
    
    salvar_imagem('imagem_copi.jpg', imagem2)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def converter_para_cinza():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Erro ao carregar a imagem 'img1.jpg'")
        return
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Imagem em Tons de Cinza', gray)
    
    salvar_imagem('imagem_cinza.jpg', gray)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def converter_rgb_para_hsv():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Erro ao carregar a imagem 'img1.jpg'")
        return
        
    cv2.imshow('Imagem Original (RGB)', imagem)
    
    imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    cv2.imshow('Imagem Convertida (HSV)', imagem_hsv)
    
    salvar_imagem('imagem_hsv.jpg', imagem_hsv)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def aplicar_blur():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Erro ao carregar a imagem 'img1.jpg'")
        return
    blurred = cv2.GaussianBlur(imagem, (15, 15), 0)
    cv2.imshow('Imagem Original', imagem)
    cv2.imshow('Imagem com Blur', blurred)
    
    salvar_imagem('imagem_blur.jpg', blurred)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def detectar_bordas():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Erro ao carregar a imagem 'img1.jpg'")
        return
    edges = cv2.Canny(imagem, 50, 150)
    cv2.imshow('Imagem Original', imagem)
    cv2.imshow('Bordas Detectadas', edges)
    
    salvar_imagem('bordas_detectadas.jpg', edges)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def mostrar_propriedades():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Erro ao carregar a imagem 'img1.jpg'")
        return
    cv2.imshow('Imagem', imagem)
    print("\nPropriedades da Imagem:")
    print("Altura (height): %d pixels" % (imagem.shape[0]))
    print("Largura (width): %d pixels" % (imagem.shape[1]))
    print("Canais (channels): %d" % (imagem.shape[2]))
    print("Tipo de dados:", imagem.dtype)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def capturar_cor_de_pixel():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Erro ao carregar a imagem 'img1.jpg'")
        return
    
    cv2.imshow('Imagem - Clique em qualquer lugar e pressione uma tecla', imagem)

    def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            (b, g, r) = imagem[y, x]
            print(f"\nCor do pixel na coordenada ({x}, {y}):")
            print(f"Vermelho: {r}, Verde: {g}, Azul: {b}")
    
    cv2.setMouseCallback('Imagem - Clique em qualquer lugar e pressione uma tecla', mouse_callback)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def modificar_cor_de_pixel():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Erro ao carregar a imagem 'img1.jpg'")
        return
    
    imagem_original = imagem.copy()
    imagem[0, 0] = (255, 0, 0)
    imagem[5:20, 5:20] = (0, 0, 255)
    
    print("Modificações realizadas:")
    print("- Pixel (0,0) alterado para Azul (B=255, G=0, R=0)")
    print("- Região retangular (5:20, 5:20) alterada para Vermelho (B=0, G=0, R=255)")
    
    cv2.imshow('Imagem Original', imagem_original)
    cv2.imshow('Imagem Modificada', imagem)
    
    salvar_imagem('imagem_pixel_modificada.jpg', imagem)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def recortar_regiao():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Erro ao carregar a imagem 'img1.jpg'")
        return
    ROI1 = imagem[0:30, 20:80]
    cv2.imshow("Imagem Original", imagem)
    cv2.imshow("Regiao Recortada", ROI1)
    
    salvar_imagem("regiao_recortada.jpg", ROI1)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def redimensionar_imagem():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Erro ao carregar a imagem 'img1.jpg'")
        return
        
    cv2.imshow('Imagem Original', imagem)
    width = int(imagem.shape[1] * 0.5)
    height = int(imagem.shape[0] * 0.5)
    dimensoes = (width, height)
    resized = cv2.resize(imagem, dimensoes, interpolation=cv2.INTER_AREA)
    cv2.imshow('Imagem Redimensionada', resized)
    
    salvar_imagem('imagem_redimensionada.jpg', resized)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def aplicar_sobel():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Erro ao carregar a imagem 'img1.jpg'")
        return
    
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobelx = cv2.convertScaleAbs(sobelx)
    sobely = cv2.convertScaleAbs(sobely)
    sobel_combinado = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
    
    cv2.imshow('Imagem Original', imagem)
    cv2.imshow('Sobel X (Bordas Verticais)', sobelx)
    cv2.imshow('Sobel Y (Bordas Horizontais)', sobely)
    cv2.imshow('Sobel Combinado', sobel_combinado)
    
    salvar_imagem('sobel_x.jpg', sobelx)
    salvar_imagem('sobel_y.jpg', sobely)
    salvar_imagem('sobel_combinado.jpg', sobel_combinado)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print('\nMenu de Opcoes:')
        print('1 - Abrir imagem')
        print('2 - Separar canais de cor')
        print('3 - Juntar canais de cor')
        print('4 - Copiar imagem')
        print('5 - Converter para tons de cinza')
        print('6 - Converter RGB para HSV')
        print('7 - Aplicar efeito blur')
        print('8 - Detectar bordas (Canny)')
        print('9 - Mostrar propriedades da imagem')
        print('10 - Capturar cor de pixel')
        print('11 - Modificar cor de pixel')
        print('12 - Recortar região da imagem')
        print('13 - Redimensionar imagem')
        print('14 - Aplicar filtro Sobel (detecção de bordas)')
        print('0 - Sair')
        
        try:
            opcao = int(input('\nEscolha uma opcao: '))
            
            if opcao == 1:
                abrir_imagem()
            elif opcao == 2:
                separar_canais()
            elif opcao == 3:
                juntar_canais()
            elif opcao == 4:
                copiar_imagem()
            elif opcao == 5:
                converter_para_cinza()
            elif opcao == 6:
                converter_rgb_para_hsv()
            elif opcao == 7:
                aplicar_blur()
            elif opcao == 8:
                detectar_bordas()
            elif opcao == 9:
                mostrar_propriedades()
            elif opcao == 10:
                capturar_cor_de_pixel()
            elif opcao == 11:
                modificar_cor_de_pixel()
            elif opcao == 12:
                recortar_regiao()
            elif opcao == 13:
                redimensionar_imagem()
            elif opcao == 14:
                aplicar_sobel()
            elif opcao == 0:
                print("Saindo do programa...")
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Opcao invalida, tente novamente.')
                time.sleep(2)
                
            os.system('cls' if os.name == 'nt' else 'clear')
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Entrada invalida. Por favor, digite um numero.")
            time.sleep(2)

if __name__ == "__main__":
    main()