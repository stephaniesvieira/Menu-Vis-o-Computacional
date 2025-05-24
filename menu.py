import cv2
import time
import os
import numpy as np
import pyfiglet
import time
import shutil
import matplotlib.pyplot as plt

# Cria a pasta para imagens modificadas se não existir
if not os.path.exists('Imagens Modificadas'):
    os.makedirs('Imagens Modificadas')

def tela_boas_vindas():
    os.system('cls' if os.name == 'nt' else 'clear')

    terminal_largura = shutil.get_terminal_size().columns
    banner = pyfiglet.figlet_format("VisionToolbox")
    banner_centralizado = "\n".join(line.center(terminal_largura) for line in banner.split("\n"))

    mensagem = "Seja bem-vindo!"
    mensagem_centralizada = mensagem.center(terminal_largura)
    print(banner_centralizado)
    print(mensagem_centralizada)
    time.sleep(5)

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

def converter_hsv_para_rgb():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Erro ao carregar a imagem 'img1.jpg'")
        return
    
    # Primeiro converte para HSV
    imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    # Depois converte de volta para RGB
    imagem_rgb = cv2.cvtColor(imagem_hsv, cv2.COLOR_HSV2BGR)
    
    cv2.imshow('Imagem Original (BGR)', imagem)
    cv2.imshow('Imagem HSV', imagem_hsv)
    cv2.imshow('Imagem Convertida de HSV para RGB', imagem_rgb)
    
    salvar_imagem('imagem_hsv_para_rgb.jpg', imagem_rgb)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def converter_para_ycrcb():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Erro ao carregar a imagem 'img1.jpg'")
        return
        
    imagem_ycrcb = cv2.cvtColor(imagem, cv2.COLOR_BGR2YCrCb)
    
    cv2.imshow('Imagem Original (BGR)', imagem)
    cv2.imshow('Imagem YCrCb', imagem_ycrcb)
    
    # Separando os canais Y, Cr e Cb
    y, cr, cb = cv2.split(imagem_ycrcb)
    cv2.imshow('Canal Y (Luminância)', y)
    cv2.imshow('Canal Cr (Crominância Vermelho)', cr)
    cv2.imshow('Canal Cb (Crominância Azul)', cb)
    
    salvar_imagem('imagem_ycrcb.jpg', imagem_ycrcb)
    salvar_imagem('canal_y.jpg', y)
    salvar_imagem('canal_cr.jpg', cr)
    salvar_imagem('canal_cb.jpg', cb)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def converter_para_lab():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Erro ao carregar a imagem 'img1.jpg'")
        return
        
    imagem_lab = cv2.cvtColor(imagem, cv2.COLOR_BGR2LAB)
    
    cv2.imshow('Imagem Original (BGR)', imagem)
    cv2.imshow('Imagem LAB', imagem_lab)
    
    # Separando os canais L, A e B
    l, a, b = cv2.split(imagem_lab)
    cv2.imshow('Canal L (Luminância)', l)
    cv2.imshow('Canal A (Verde-Magenta)', a)
    cv2.imshow('Canal B (Azul-Amarelo)', b)
    
    salvar_imagem('imagem_lab.jpg', imagem_lab)
    salvar_imagem('canal_l.jpg', l)
    salvar_imagem('canal_a.jpg', a)
    salvar_imagem('canal_b.jpg', b)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def carregar_video():
    print("\nCarregar vídeo de arquivo")
    nome_video = input("Digite o nome do arquivo de vídeo (ex: meuVideo.mp4): ")
    
    video = cv2.VideoCapture(nome_video)
    
    if not video.isOpened():
        print("Erro ao abrir o vídeo")
        return

    # Obtém FPS do vídeo para sincronizar a exibição
    fps = video.get(cv2.CAP_PROP_FPS)
    if fps == 0:
        fps = 30  # valor padrão caso falhe
    delay = int(1000 / fps)

    print("Pressione 'S' para sair ou 'C' para capturar frame.")

    while True:
        ret, frame = video.read()
        
        if not ret:
            # Reinicia o vídeo
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue
        
        # Redimensiona para 50%
        frame_resized = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        cv2.imshow("Vídeo", frame_resized)
        
        key = cv2.waitKey(delay) & 0xFF
        if key == ord('s'):
            break
        elif key == ord('c'):
            nome_arquivo = f"frame_capturado_{int(time.time())}.jpg"
            salvar_imagem(nome_arquivo, frame)
            print(f"Frame capturado e salvo como {nome_arquivo}")
    
    video.release()
    cv2.destroyAllWindows()


def ajustar_brilho():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Erro ao carregar a imagem 'img1.jpg'")
        return
    
    valor_brilho = int(input("Digite o valor de brilho (-100 a 100): "))
    valor_brilho = max(-100, min(100, valor_brilho))  # Limita entre -100 e 100
    
    if valor_brilho > 0:
        brilho = imagem + [valor_brilho, valor_brilho, valor_brilho]
    else:
        brilho = imagem - [abs(valor_brilho), abs(valor_brilho), abs(valor_brilho)]
    
    brilho = np.clip(brilho, 0, 255).astype(np.uint8)
    
    cv2.imshow('Imagem Original', imagem)
    cv2.imshow(f'Imagem com Brilho {valor_brilho}', brilho)
    
    salvar_imagem(f'imagem_brilho_{valor_brilho}.jpg', brilho)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def ajustar_contraste():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Erro ao carregar a imagem 'img1.jpg'")
        return
    
    fator = float(input("Digite o fator de contraste (0.0 a 3.0): "))
    fator = max(0.0, min(3.0, fator))  # Limita entre 0.0 e 3.0
    
    contraste = cv2.convertScaleAbs(imagem, alpha=fator, beta=0)
    
    cv2.imshow('Imagem Original', imagem)
    cv2.imshow(f'Imagem com Contraste {fator:.1f}', contraste)
    
    salvar_imagem(f'imagem_contraste_{fator:.1f}.jpg', contraste)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def inverter_cores():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Erro ao carregar a imagem 'img1.jpg'")
        return
    
    negativo = cv2.bitwise_not(imagem)
    
    cv2.imshow('Imagem Original', imagem)
    cv2.imshow('Negativo da Imagem', negativo)
    
    salvar_imagem('imagem_negativo.jpg', negativo)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def operacoes_aritmeticas():
    print("\nOperações Aritméticas disponíveis:")
    print("1 - Adição de imagens")
    print("2 - Subtração de imagens")
    print("3 - Multiplicação de imagens")
    print("4 - Divisão de imagens")
    
    try:
        opcao = int(input("Escolha a operação: "))
        
        imagem1 = cv2.imread('img1.jpg')
        imagem2 = cv2.imread('img2.jpg')  # Você precisa ter uma segunda imagem
        
        if imagem1 is None or imagem2 is None:
            print("Erro ao carregar uma ou ambas as imagens")
            return
            
        # Redimensiona imagem2 para ter o mesmo tamanho que imagem1
        imagem2 = cv2.resize(imagem2, (imagem1.shape[1], imagem1.shape[0]))
        
        if opcao == 1:
            resultado = cv2.add(imagem1, imagem2)
            cv2.imshow('Imagem 1', imagem1)
            cv2.imshow('Imagem 2', imagem2)
            cv2.imshow('Resultado da Adição', resultado)
            salvar_imagem('adicao_imagens.jpg', resultado)
        elif opcao == 2:
            resultado = cv2.subtract(imagem1, imagem2)
            cv2.imshow('Imagem 1', imagem1)
            cv2.imshow('Imagem 2', imagem2)
            cv2.imshow('Resultado da Subtração', resultado)
            salvar_imagem('subtracao_imagens.jpg', resultado)
        elif opcao == 3:
            resultado = cv2.multiply(imagem1, imagem2, scale=1/255)
            cv2.imshow('Imagem 1', imagem1)
            cv2.imshow('Imagem 2', imagem2)
            cv2.imshow('Resultado da Multiplicação', resultado)
            salvar_imagem('multiplicacao_imagens.jpg', resultado)
        elif opcao == 4:
            # Adiciona um pequeno valor para evitar divisão por zero
            imagem2 = imagem2.astype(float) + 0.0001
            resultado = cv2.divide(imagem1.astype(float), imagem2)
            resultado = np.clip(resultado, 0, 255).astype(np.uint8)
            cv2.imshow('Imagem 1', imagem1)
            cv2.imshow('Imagem 2', imagem2.astype(np.uint8))
            cv2.imshow('Resultado da Divisão', resultado)
            salvar_imagem('divisao_imagens.jpg', resultado)
        else:
            print("Opção inválida")
            return
            
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except ValueError:
        print("Entrada inválida")

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

def mostrar_histograma():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Nenhuma imagem carregada.")
        return
    plt.figure()
    if len(imagem.shape) == 2:
        plt.hist(imagem.ravel(), 256, [0, 256], color='gray')
    else:
        cores = ('b', 'g', 'r')
        for i, cor in enumerate(cores):
            plt.hist(imagem[:, :, i].ravel(), 256, [0, 256], label=cor, color=cor)
    plt.title("Histograma")
    plt.xlabel("Intensidade")
    plt.ylabel("Frequência")
    plt.legend()
    plt.show()

def aplicar_morfologia(tipo):
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Nenhuma imagem carregada.")
        return
    img_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((3, 3), np.uint8)
    
    if tipo == 'erosao':
        res = cv2.erode(img_gray, kernel, iterations=1)
    elif tipo == 'dilatacao':
        res = cv2.dilate(img_gray, kernel, iterations=1)
    elif tipo == 'abertura':
        res = cv2.morphologyEx(img_gray, cv2.MORPH_OPEN, kernel)
    elif tipo == 'fechamento':
        res = cv2.morphologyEx(img_gray, cv2.MORPH_CLOSE, kernel)
    elif tipo == 'abertura_fechamento':
        res = cv2.morphologyEx(img_gray, cv2.MORPH_OPEN, kernel)
        res = cv2.morphologyEx(res, cv2.MORPH_CLOSE, kernel)
    elif tipo == 'gradiente':
        res = cv2.morphologyEx(img_gray, cv2.MORPH_GRADIENT, kernel)
    elif tipo == 'top_hat':
        res = cv2.morphologyEx(img_gray, cv2.MORPH_TOPHAT, kernel)
    
    cv2.imshow(f"{tipo}", res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def eliminar_ruido():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Nenhuma imagem carregada.")
        return
    res = cv2.medianBlur(imagem, 3)
    cv2.imshow("Eliminação de Ruído", res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def modificar_histograma():
    imagem = cv2.imread('img1.jpg')
    if imagem is None:
        print("Nenhuma imagem carregada.")
        return
    img_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    print("\nModificações disponíveis:")
    print("1 - Binarização")
    print("2 - Equalização")
    print("3 - Quantização")
    print("4 - Splitting")
    print("5 - Stretching")
    
    escolha = int(input("Escolha a modificação: "))
    
    if escolha == 1:
        _, res = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
        titulo = "Binarização"
    elif escolha == 2:
        res = cv2.equalizeHist(img_gray)
        titulo = "Equalização"
    elif escolha == 3:
        levels = int(input("Digite o número de níveis (ex: 4): "))
        bins = np.linspace(0, 256, levels + 1)
        res = np.digitize(img_gray, bins) * (256 // levels) - 1
        res = np.clip(res, 0, 255).astype(np.uint8)
        titulo = "Quantização"
    elif escolha == 4:
        mid = 128
        low = img_gray[img_gray < mid]
        high = img_gray[img_gray >= mid]
        print(f"Pixels na parte baixa: {len(low)}")
        print(f"Pixels na parte alta: {len(high)}")
        return
    elif escolha == 5:
        min_val = np.min(img_gray)
        max_val = np.max(img_gray)
        res = ((img_gray - min_val) / (max_val - min_val) * 255).astype(np.uint8)
        titulo = "Stretching"
    else:
        print("Opção inválida.")
        return
    
    cv2.imshow(titulo, res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def main():
    tela_boas_vindas()  # Exibe a tela de boas-vindas antes de tudo

    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print('\nMenu de Opcoes:')
        print('1 - Abrir imagem')
        print('2 - Separar canais de cor')
        print('3 - Juntar canais de cor')
        print('4 - Converter para tons de cinza')
        print('5 - Converter RGB para HSV')
        print('6 - Converter HSV para RGB')
        print('7 - Converter para YCrCb')
        print('8 - Converter para LAB')
        print('9 - Carregar vídeo e capturar imagem')
        print('10 - Ajustar brilho')
        print('11 - Ajustar contraste')
        print('12 - Inverter cores (negativo)')
        print('13 - Operações aritméticas')
        print('14 - Aplicar efeito blur')
        print('15 - Detectar bordas (Canny)')
        print('16 - Mostrar propriedades da imagem')
        print('17 - Capturar cor de pixel')
        print('18 - Modificar cor de pixel')
        print('19 - Recortar região da imagem')
        print('20 - Redimensionar imagem')
        print('21 - Aplicar filtro Sobel (detecção de bordas)')
        print('22 - Mostrar Histograma')
        print('23 - Erosão')
        print('24 - Dilatação')
        print('25 - Abertura')
        print('26 - Fechamento')
        print('27 - Abertura e Fechamento em tons de cinza')
        print('28 - Gradiente Morfológico')
        print('29 - Top Hat')
        print('30 - Eliminação de Ruídos')
        print('31 - Modificação do Histograma')
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
                converter_para_cinza()
            elif opcao == 5:
                converter_rgb_para_hsv()
            elif opcao == 6:
                converter_hsv_para_rgb()
            elif opcao == 7:
                converter_para_ycrcb()
            elif opcao == 8:
                converter_para_lab()
            elif opcao == 9:
                carregar_video()
            elif opcao == 10:
                ajustar_brilho()
            elif opcao == 11:
                ajustar_contraste()
            elif opcao == 12:
                inverter_cores()
            elif opcao == 13:
                operacoes_aritmeticas()
            elif opcao == 14:
                aplicar_blur()
            elif opcao == 15:
                detectar_bordas()
            elif opcao == 16:
                mostrar_propriedades()
            elif opcao == 17:
                capturar_cor_de_pixel()
            elif opcao == 18:
                modificar_cor_de_pixel()
            elif opcao == 19:
                recortar_regiao()
            elif opcao == 20:
                redimensionar_imagem()
            elif opcao == 21:
                aplicar_sobel()
            elif opcao == 22:
                mostrar_histograma()
            elif opcao == 23:
                aplicar_morfologia('erosao')
            elif opcao == 24:
                aplicar_morfologia('dilatacao')
            elif opcao == 25:
                aplicar_morfologia('abertura')
            elif opcao == 26:
                aplicar_morfologia('fechamento')
            elif opcao == 27:
                aplicar_morfologia('abertura_fechamento')
            elif opcao == 28:
                aplicar_morfologia('gradiente')
            elif opcao == 29:
                aplicar_morfologia('top_hat')
            elif opcao == 30:
                eliminar_ruido()
            elif opcao == 31:
                modificar_histograma()
            elif opcao == 0:
                print("Saindo do programa...")
                break
            else:
                print('Opcao invalida, tente novamente.')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
        except ValueError:
            print("Entrada invalida. Por favor, digite um numero.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()