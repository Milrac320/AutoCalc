import pandas as pd
import json
import warnings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pjecalc_funcoes import *
from pjecalc_elementos import *
from pjecalc_variaveis import *

warnings.filterwarnings("ignore", category=UserWarning, module="pandas")

def calculoExterno():

    with open('json/escolha_calculos.json', 'r') as file:
        data = json.load(file)

    processo = data['caminho_arquivo']

    file_path = processo

    if file_path:

        df = pd.read_excel(

            file_path, engine="openpyxl", header=None, sheet_name="PJE CALC", dtype=str

        )

        df = df.apply(lambda col: col.map(lambda x: None if pd.isna(x) else x))

    # VARIÁVEIS

        sequencia = df.iloc[2,2]

        digito = df.iloc[2,4]

        ano = df.iloc[2,6]

        tribunal = df.iloc[2,10]

        vara = df.iloc[2,12]

        ultima_atualizacao = converter_data_dmy(df.iloc[40,2])

        recte = df.iloc[3,2]

        cpf = df.iloc[3,5]

        adv_recte = df.iloc[3,8]

        recda = df.iloc[4,2]

        cnpj = df.iloc[4,5]

        adv_recda = df.iloc[4,8]

        indice_trabalhista = df.iloc[9,2]

        segundo_indice_trabalhista = df.iloc[9,5]

        tabela_juros = df.iloc[10,2]

        segunda_tabela_juros = df.iloc[10,5]

        base_juros = df.iloc[11,5]

        fgts = df.iloc[37,2]

        inss = df.iloc[34,2]

        taxa_negativa=df.iloc[9,11]

        base_custas=df.iloc[13,2]

        if base_custas == "Bruto Devido ao Reclamante":
            index_base_custas="0"
        elif base_custas =='Bruto Devido ao Reclamante + Outros Débitos do Reclamado':
            index_base_custas="1"

        meses_ir=df.iloc[40,5]

        # INICIAR NAVEGADOR

    servico = Service(ChromeDriverManager().install())

    navegador = webdriver.Chrome(service=servico)

    navegador.get(link)

    navegador.maximize_window()

    tempo_espera("alteração")
    
    # ABERTURA CÁLCULO ATUALIZAÇÃO

    navegador.find_element(*xpath_menu_painel).click()

    tempo_espera("alteração")

    limpar()

    navegador.find_element(*xpath_aba_calculo_externo).click()

    tempo_espera("alteração")

    # DADOS DO PROCESSO

    navegador.find_element(*xpath_numero_processo).send_keys(sequencia)

    navegador.find_element(*xpath_digito_processo).send_keys(digito)

    navegador.find_element(*xpath_ano_processo).send_keys(ano)

    navegador.find_element(*xpath_regiao_processo).send_keys(tribunal)

    navegador.find_element(*xpath_vara_processo).send_keys(vara)

    navegador.find_element(*xpath_reclamante).send_keys(recte)

    navegador.find_element(*xpath_selecionar_cpf).click()

    navegador.find_element(*xpath_ativar_cpf).click()

    navegador.find_element(*xpath_cpf).send_keys(cpf)

    if adv_recte != vazio:

        navegador.find_element(*xpath_adv_recte).send_keys(adv_recte)

        navegador.find_element(*xpath_enviar_adv_recte).click()

    navegador.find_element(*xpath_reclamada).send_keys(recda)

    navegador.find_element(*xpath_selecionar_cnpj).click()

    navegador.find_element(*xpath_cnpj).click()

    navegador.find_element(*xpath_cnpj).send_keys(cnpj)

    if adv_recda != vazio:

        navegador.find_element(*xpath_adv_recda).send_keys(adv_recda)

        navegador.find_element(*xpath_enviar_adv_recda).click()

    navegador.find_element(*xpath_aba_parametros).click()

    tempo_espera("alteração")

    # PARÂMETROS DO CÁLCULO

    navegador.find_element(*xpath_ativar_ultima_atualizacao).click()

    navegador.find_element(*xpath_ultima_atualizacao).send_keys(ultima_atualizacao)

    if segundo_indice_trabalhista == vazio:

        navegador.find_element(*xpath_indice_trabalhista).send_keys(indice_trabalhista)

    else:

        navegador.find_element(*xpath_indice_trabalhista).send_keys(segundo_indice_trabalhista)

    if taxa_negativa == "SIM":
        
        navegador.find_element(*xpath_taxa_negativa).click()

    lista_suspensa = Select(navegador.find_element(*xpath_base_juros))

    lista_suspensa.select_by_index(base_juros)

    if fgts == "PAGAR":

        navegador.find_element(*xpath_fgts_sim).click()

    elif fgts == "RECOLHER":

        navegador.find_element(*xpath_fgts_nao).click()

    if segunda_tabela_juros == vazio:

        navegador.find_element(*xpath_tabela_juros).send_keys(tabela_juros)

    else:

        navegador.find_element(*xpath_tabela_juros).send_keys(segunda_tabela_juros)

    if inss == "NÃO":

        navegador.find_element(*xpath_inss).click()

    navegador.find_element(*xpath_meses_ir).send_keys(meses_ir)

    lista_suspensa = Select(navegador.find_element(*xpath_base_custas))

    lista_suspensa.select_by_index(index_base_custas)

    navegador.find_element(*xpath_salvar).click()

    # SALVAMENTO        

    tempo_espera("extra")

    WebDriverWait(navegador, 20).until(EC.element_to_be_clickable(*xpath_menu_exportar)).click()

    tempo_espera("exportar")

    navegador.find_element("xpath",xpath_aba_exportar).click()

    tempo_espera("salvar")

    navegador.execute_script(js_exportar)

    tempo_espera("exportar")
