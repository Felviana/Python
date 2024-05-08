"""
# Pegar os dados da planilha 
Tipo nome do curso, nome participante, tipo de participação, data do inicio, data do final, carga horária, data da emissão do certificado

# Transferir os dados da planilha para a imagem do certificado
"""
# Pegar os dados da planilha 
import openpyxl
from PIL import Image, ImageDraw, ImageFont
import datetime

workbook_alunos = openpyxl.load_workbook('planilha_alunos.xlsx')
sheet_alunos = workbook_alunos['Sheet1']  # Selecionar a aba da planilha Carregar a planilha

# Iterar sobre as linhas da planilha
for indice, linha in enumerate(sheet_alunos.iter_rows(min_row=2,max_row=2)):#Aqui está dizendo para iniciar a buscar apartir da linha 2, porque no caso não queremos o cabeçario,quando fazer com eles não esqueça de usar o (min_row=2,max_row=2)
    # Extrair os dados de cada célula
    nome_curso = linha[0].value #Extraindo o nome do curso 
    nome_participante = linha[1].value #Extraindo o nome do participante
    tipo_participacao = linha[2].value #Extraindo o tipo da participação
    data_inicio = linha[3].value #Extraindo a data inicial do curso
    data_final = linha[4].value #Extraindo a data final do curso
    carga_horaria = linha[5].value#Extraindo a carga horaria do curso
    data_emissao = linha[6].value #Extraindo a data de emissão do curso

    # Verificar se as datas são do tipo datetime e formatá-las
    if isinstance(data_inicio, datetime.datetime):
        data_inicio = data_inicio.strftime('%d/%m/%Y')
    if isinstance(data_final, datetime.datetime):
        data_final = data_final.strftime('%d/%m/%Y')
    if isinstance(data_emissao, datetime.datetime):
        data_emissao = data_emissao.strftime('%d/%m/%Y')

    # Definir as fontes a serem usadas
    fonte_nome = ImageFont.truetype('./tahomabd.ttf', 80)
    fonte_geral = ImageFont.truetype('./tahoma.ttf', 60)
    fonte_data = ImageFont.truetype('./tahoma.ttf', 30)

    # Abrir a imagem do certificado
    image = Image.open('./certificado_padrao.jpg') #Abrindo a imagem para sobreescrever
    desenhar = ImageDraw.Draw(image) #Sobreescrevendo minha imagem

    # Adicionar os dados do participante ao certificado
    desenhar.text((510, 460), nome_participante, fill='black', font=fonte_nome)#Aqui esta as coordenadas do nosso código salvando em nossa variavel.
    desenhar.text((490, 570), nome_curso, fill='black', font=fonte_geral)
    desenhar.text((680, 670), tipo_participacao, fill='black', font=fonte_geral)
    desenhar.text((725, 760), str(carga_horaria), fill='black', font=fonte_geral)
    desenhar.text((440, 940), str(data_inicio), fill='black', font=fonte_data)
    desenhar.text((500, 1020), str(data_final), fill='black', font=fonte_data)
    desenhar.text((1690, 940), str(data_emissao), fill='black', font=fonte_data)

    # Salvar o certificado com um nome único
    image.save(f'./{indice}_{nome_participante}_certificado.png')