import pandas as pd
import json
import warnings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from pjecalc_funcoes import *
from pjecalc_elementos import *
from pjecalc_variaveis import *

warnings.filterwarnings("ignore", category=UserWarning, module="pandas")

def calculo():

    with open('json/escolha_calculos.json', 'r') as file:
        data = json.load(file)

    processo = data['caminho_arquivo']

    file_path = processo

    if file_path:
        df = pd.read_excel(
            file_path, engine="openpyxl", header=None, sheet_name="ANÁLISE GERAL", dtype=str
        )

        df = df.apply(lambda col: col.map(lambda x: None if pd.isna(x) else x))

# DADOS DO PROCESSO
        
    def var_dados_do_processo():
        sequencia = df.iloc[2, 2]

        digito = df.iloc[2, 4]

        ano = df.iloc[2, 6]

        tribunal = df.iloc[2, 8]

        vara = df.iloc[2, 12]

        recte = df.iloc[3, 2]

        cpf = df.iloc[3, 5]

        adv_recte = df.iloc[3, 8]

        recda = df.iloc[4, 2]

        cnpj = df.iloc[4, 5]

        adv_recda = df.iloc[4, 8]


# PARÂMETROS DO CÁLCULO

    def var_parametros_do_calculo():
        estado = df.iloc[3, 11]

        municipio = df.iloc[4, 11]

        admissao = converter_data_dmy(df.iloc[5, 2])

        demissao = converter_data_dmy(df.iloc[6, 2])

        ajuizamento = converter_data_dmy(df.iloc[7, 2])

        data_inicial = converter_data_dmy(df.iloc[5, 5])

        data_final = converter_data_dmy(df.iloc[6, 5])

        prescricao = df.iloc[7, 5]

        prazo_aviso = df.iloc[8, 2]

        oj415 = df.iloc[8, 5]

        carga_horaria = df.iloc[11, 11]

        maior_remuneracao = df.iloc[12, 11]

        ultima_remuneracao = df.iloc[13, 11]


# CORREÇÃO, JUROS E MULTA

    def var_correcao_juros_multa():    
        indice_trabalhista = df.iloc[9, 2]
        
        segundo_indice_trabalhista = df.iloc[9, 5]
        
        data_indice = converter_data_dmy(df.iloc[9, 8])
        
        tabela_juros = df.iloc[10, 2]
        
        segunda_tabela_juros = df.iloc[10, 5]
        
        data_juros = converter_data_dmy(df.iloc[10, 8])
        
        taxa_negativa = df.iloc[9, 11]
        
        pre_juros = df.iloc[10, 11]
        
        base_juros = df.iloc[11, 5]
        
        inss = df.iloc[11, 2]
        

# CUSTAS JUDICIAIS

    def var_custas_judiciais():
        custas = df.iloc[13,5]

        base_custas=df.iloc[13,2]

        if base_custas == "Bruto Devido ao Reclamante":
            index_base_custas="0"
        elif base_custas =='Bruto Devido ao Reclamante + Outros Débitos do Reclamado':
            index_base_custas="1"

        vencimento_custas = converter_data_dmy(df.iloc[13, 8])

        valor_custas = df.iloc[13, 11]        

# CONTRIBUIÇÃO SOCIAL

    def var_contribuicao_social():
        correcao_trabalhista = df.iloc[34, 2]

        sobre_salarios_pagos = df.iloc[35, 2]

        atividade_economica = df.iloc[34, 5]

        data_inicial_inss = converter_data_dmy(df.iloc[34, 8])

        data_final_inss = converter_data_dmy(df.iloc[34, 11])

        simples_nacional = df.iloc[35, 5]

        inicio_nacional = converter_data_my(df.iloc[35, 8])

        final_nacional = converter_data_my(df.iloc[35, 11])


# FGTS

    def var_fgts():
        fgts = df.iloc[37, 2]

        multa_fgts = df.iloc[37, 5]

        multa_467 = df.iloc[37, 8]

        aliquota_fgts = df.iloc[37, 11]

        incidencia_fgts = df.iloc[38, 2]

        data_saldo_saque_fgts = converter_data_dmy(df.iloc[38, 5])

        valor_saldo_saque_fgts = df.iloc[38, 8]

        deduzir_saldo_saque_fgts = df.iloc[38, 11]


# HONORÁRIOS 1º ADV. RECTE.

    def var_honorarios_1_adv_recte():
        primeiro_adv_recte = df.iloc[15, 2]
        
        vencimento_primeiro_adv_recte = converter_data_dmy(df.iloc[15, 8])
        
        valor_primeiro_adv_recte = df.iloc[15, 11]
        
        tipo_primeiro_adv_recte = df.iloc[16, 5]
        
        vencimento_juros_primeiro_adv_recte = converter_data_dmy(df.iloc[16, 8])
        
        ir_primeiro_adv_recte = df.iloc[16, 11]


# HONORÁRIOS 2º ADV. RECTE.

    def var_honorarios_2_adv_recte():
        segundo_adv_recte = df.iloc[17, 2]
        
        vencimento_segundo_adv_recte = converter_data_dmy(df.iloc[17, 8])
        
        valor_segundo_adv_recte = df.iloc[17, 11]
        
        tipo_segundo_adv_recte = df.iloc[18, 5]
        
        vencimento_juros_segundo_adv_recte = converter_data_dmy(df.iloc[18, 8])
        
        ir_segundo_adv_recte = df.iloc[18, 11]
        

# HONORÁRIOS 1º ADV. RECDA.
        
    def var_honorarios_1_adv_recda():   
        primeira_adv_recda = df.iloc[19, 2]

        vencimento_primeira_adv_recda = converter_data_dmy(df.iloc[19, 8])

        valor_primeira_adv_recda = df.iloc[19, 11]

        exigibilidade_primeira_adv_recda = df.iloc[20, 2]

        tipo_primeira_adv_recda = df.iloc[20, 5]

        vencimento_juros_primeira_adv_recda = converter_data_dmy(df.iloc[20, 8])

        ir_primeira_adv_recda = df.iloc[20, 11]


# HONORÁRIOS 2º ADV. RECDA.
        
    def var_honorarios_2_adv_recda():
        segunda_adv_recda = df.iloc[21, 2]

        vencimento_segunda_adv_recda = converter_data_dmy(df.iloc[21, 8])

        valor_segunda_adv_recda = df.iloc[21, 11]

        exigibilidade_segunda_adv_recda = df.iloc[22, 2]

        tipo_segunda_adv_recda = df.iloc[22, 5]

        vencimento_juros_segunda_adv_recda = converter_data_dmy(df.iloc[22, 8])

        ir_segunda_adv_recda = df.iloc[22, 11]


# HONORÁRIOS 3º ADV. RECDA.
        
    def var_honorarios_3_adv_recda():
        terceira_adv_recda = df.iloc[23, 2]

        vencimento_terceira_adv_recda = converter_data_dmy(df.iloc[23, 8])

        valor_terceira_adv_recda = df.iloc[23, 11]

        exigibilidade_terceira_adv_recda = df.iloc[24, 2]

        tipo_terceira_adv_recda = df.iloc[24, 5]

        vencimento_juros_terceira_adv_recda = converter_data_dmy(df.iloc[24, 8])

        ir_terceira_adv_recda = df.iloc[24, 11]


# HONORÁRIOS 4º ADV. RECDA.
        
    def var_honorarios_4_adv_recda():
        quarta_adv_recda = df.iloc[25, 2]

        vencimento_quarta_adv_recda = converter_data_dmy(df.iloc[25, 8])

        valor_quarta_adv_recda = df.iloc[25, 11]

        exigibilidade_quarta_adv_recda = df.iloc[26, 2]

        tipo_quarta_adv_recda = df.iloc[26, 5]

        vencimento_juros_quarta_adv_recda = converter_data_dmy(df.iloc[26, 8])

        ir_quarta_adv_recda = df.iloc[26, 11]              


# HONORÁRIOS PERITO CONTÁBIL
         
    def var_honorarios_perito_contabil():
        perito_contabil = df.iloc[27, 2]

        vencimento_perito_contabil = converter_data_dmy(df.iloc[27, 8])

        valor_perito_contabil = df.iloc[27, 11]

        tipo_perito_contabil = df.iloc[28, 5]

        vencimento_juros_perito_contabil = converter_data_dmy(df.iloc[28, 8])

        ir_perito_contabil = df.iloc[28, 11]


# HONORÁRIOS ENGENHEIRO
        
    def var_honorarios_engenheiro():
        engenheiro = df.iloc[29, 2]

        vencimento_engenheiro = converter_data_dmy(df.iloc[29, 8])

        valor_engenheiro = df.iloc[29, 11]

        tipo_engenheiro = df.iloc[30, 5]

        vencimento_juros_engenheiro = converter_data_dmy(df.iloc[30, 8])

        ir_engenheiro = df.iloc[30, 11]


# HONORÁRIOS MÉDICO
        
    def var_honorarios_medico():
        medico = df.iloc[31, 2]

        vencimento_medico = converter_data_dmy(df.iloc[31, 8])

        valor_medico = df.iloc[31, 11]

        tipo_medico = df.iloc[32, 5]

        vencimento_juros_medico = converter_data_dmy(df.iloc[32, 8])

        ir_medico = df.iloc[32, 11] 


# INICIAR NAVEGADOR

        servico = Service(ChromeDriverManager().install())

        navegador = webdriver.Chrome(
            
            service=servico)

        navegador.get(link)

        navegador.maximize_window()

        tempo_espera("alteração")

        navegador.find_element(*xpath_botao_calculo).click()

        tempo_espera("alteração")

        limpar()

# DADOS DO PROCESSO
        
        var_dados_do_processo()

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

        var_parametros_do_calculo()

        navegador.find_element(*xpath_estado).send_keys(estado)
        
        tempo_espera("alteração") 
        
        navegador.find_element(*xpath_municipio).send_keys(municipio)
        
        tempo_espera("alteração")
        
        navegador.find_element(*xpath_admissao).click()
        
        navegador.find_element(*xpath_admissao).send_keys(admissao)
        
        if demissao != vazio:
        
            navegador.find_element(*xpath_demissao).click()
        
            navegador.find_element(*xpath_demissao).send_keys(demissao)

        elif demissao == vazio:
        
            navegador.find_element(*xpath_data_final).click()
        
            navegador.find_element(*xpath_data_final).send_keys(data_final)
        
        navegador.find_element(*xpath_ajuizamento).click()
        
        navegador.find_element(*xpath_ajuizamento).send_keys(ajuizamento)
        
        if data_inicial != vazio:
        
            navegador.find_element(*xpath_data_inicial).click()
        
            navegador.find_element(*xpath_data_inicial).send_keys(data_inicial)
        
        if data_final != vazio:
        
            navegador.find_element(*xpath_data_final).click()
        
            navegador.find_element(*xpath_data_final).send_keys(data_final)
        
        if prescricao == "SIM":
        
            navegador.find_element(*xpath_prescricao).click()
        
        navegador.find_element(*xpath_aviso_previo).send_keys(prazo_aviso)
        
        if prazo_aviso == "NÃO APURAR":
        
            navegador.find_element(*xpath_projetar_aviso).click()
        
        if oj415 == "SIM":
        
            navegador.find_element(*xpath_oj415).click()
        
        if ultima_remuneracao != vazio:

            navegador.find_element(*xpath_ultima_remuneracao).click()

            navegador.find_element(*xpath_ultima_remuneracao).send_keys(*xpath_ultima_remuneracao)

        if maior_remuneracao != vazio:

            navegador.find_element(*xpath_maior_remuneracao).click()

            navegador.find_element(*xpath_maior_remuneracao).send_keys(*xpath_maior_remuneracao)        

        if carga_horaria!= vazio:

            navegador.find_element(*xpath_carga_horaria).click()
            
            navegador.find_element(*xpath_carga_horaria).send_keys(carga_horaria)
        
        navegador.find_element(*xpath_ponto_facultativo).click()
        
        navegador.find_element(*xpath_salvar).click()
        
        tempo_espera("alteração")

# CORREÇÃO, JUROS E MULTA

        if data['Correção, Juros e Multa'].value == True:
            
            var_correcao_juros_multa()

            navegador.find_element(*xpath_aba_inss).click()
            
            tempo_espera("alteração")
            
            navegador.find_element(*xpath_indice_trabalhista).send_keys(indice_trabalhista)
            
            tempo_espera("alteração")
            
            if segundo_indice_trabalhista != vazio:
            
                navegador.find_element(*xpath_ativar_segundo_indice).click()
            
                tempo_espera("alteração")
            
                navegador.find_element(*xpath_segundo_indice).send_keys(segundo_indice_trabalhista)
            
                navegador.find_element(*xpath_data_segundo_indice).click()
            
                navegador.find_element(*xpath_data_segundo_indice).send_keys(data_indice)
            
                navegador.find_element(*xpath_add_data_segundo_indice).click()
            
                tempo_espera("alteração")
            
            if taxa_negativa == "SIM":
                navegador.find_element(*xpath_taxa_negativa).click()
            
            if pre_juros == "SIM":
            
                navegador.find_element(*xpath_remover_juros).click()
            
                tempo_espera("alteração")
            
                navegador.find_element(*xpath_tabela_juros).send_keys(tabela_juros)
            
                navegador.find_element(*xpath_ativar_segundo_juros).click()
            
                tempo_espera("alteração")
            
                navegador.find_element(*xpath_segundo_juros).send_keys(segunda_tabela_juros)
            
                navegador.find_element(*xpath_data_segundo_juros).click()
            
                navegador.find_element(*xpath_data_segundo_juros).send_keys(data_juros)
            
                navegador.find_element(*xpath_add_data_segundo_juros).click()
            
                tempo_espera("alteração")
            
            elif pre_juros == "NÃO" or vazio:
            
                navegador.find_element(*xpath_juros_pre).click()
            
                tempo_espera("alteração")
            
                navegador.find_element(*xpath_tabela_juros).send_keys(tabela_juros)

# DADOS ESPECÍFICOS

            navegador.find_element(*xpath_aba_dados_especificos).click()
            
            tempo_espera("salvar")
            
            lista_suspensa = Select(navegador.find_element(*xpath_base_juros))
            
            lista_suspensa.select_by_index(base_juros)
            
            tempo_espera("alteração")
            
            if inss == "NÃO" or inss == vazio:
            
                navegador.find_element(*xpath_inss).click()
            
            navegador.find_element(*xpath_salvar).click()
            
            tempo_espera("alteração")
        
# CUSTAS JUDICIAIS

        if data['Custas Judiciais'].value == True:

            var_custas_judiciais()

            navegador.find_element(*xpath_aba_custas).click()
            
            tempo_espera("salvar")
            
            lista_suspensa = Select(navegador.find_element(*xpath_base_custas))
            
            lista_suspensa.select_by_index(index_base_custas)
            
            tempo_espera("alteração")
            
            if custas == 'ISENTO' or custas == 'PAGO' or custas == vazio:
            
                navegador.find_element(*xpath_custas_devido).click()
            
            else:
            
                navegador.find_element(*xpath_ativar_custas).click()
            
                tempo_espera("alteração")
            
                navegador.find_element(*xpath_data_custas).click()
            
                tempo_espera("alteração")
            
                navegador.find_element(*xpath_data_custas).send_keys(vencimento_custas)
            
                navegador.find_element(*xpath_valor_custas).send_keys(valor_custas)
            
            navegador.find_element(*xpath_salvar).click()
            
            tempo_espera("alteração")

# HONORÁRIOS

        if data['Honorários'].value == True:
        
            navegador.find_element(*xpath_aba_honorarios).click()

            tempo_espera("salvar")

# HONORÁRIOS 1º ADV. RECTE.

            if primeiro_adv_recte != vazio:
            
                var_honorarios_1_adv_recte()

                navegador.find_element(*xpath_novo_honorario).click()
            
                tempo_espera("alteração")
            
                lista_suspensa = Select(navegador.find_element(*xpath_tipo_honorario))
            
                lista_suspensa.select_by_index(9)
            
                tempo_espera("alteração")
            
                navegador.find_element(*xpath_tipo_devedor_reclamado).click()
            
                tempo_espera("alteração")
            
                if tipo_primeiro_adv_recte == "INFORMADO":
            
                    navegador.find_element(*xpath_valor_informado).click()
            
                    navegador.find_element(*xpath_data_honorario).send_keys(vencimento_primeiro_adv_recte)
            
                    navegador.find_element(*xpath_valor_honorario).send_keys(valor_primeiro_adv_recte)

                    if vencimento_juros_primeiro_adv_recte != vazio:

                        navegador.find_element(*xpath_juros_honorario).click()

                        navegador.find_element(*xpath_data_juros_honorario).send_keys(vencimento_juros_primeiro_adv_recte)
            
                    tempo_espera("alteração")
            
                elif tipo_primeiro_adv_recte == "CALCULADO":
            
                    navegador.find_element(*xpath_aliquota_honorario).send_keys(valor_primeiro_adv_recte)
            
                    lista_suspensa = Select(navegador.find_element(*xpath_base_honorario))
            
                    lista_suspensa.select_by_index(1)
            
                    tempo_espera("alteração")
            
                navegador.find_element(*xpath_nome_honorario).send_keys(primeiro_adv_recte)
            
                if ir_primeiro_adv_recte == "IRPF":

                    navegador.find_element(*xpath_apurar_ir_honorarios).click()
                    
                    navegador.find_element(*xpath_irpf_honorarios).click()

                    tempo_espera("alteração")

                elif ir_primeiro_adv_recte == "IRPJ":

                    navegador.find_element(*xpath_apurar_ir_honorarios).click()
                   
                    navegador.find_element(*xpath_irpj_honorarios).click()             

                    tempo_espera("alteração")       
            
                navegador.find_element(*xpath_salvar).click()
            
                tempo_espera("alteração")

# HONORÁRIOS 2º ADV. RECTE.

            if segundo_adv_recte != vazio:
            
                var_honorarios_2_adv_recte()

                navegador.find_element(*xpath_novo_honorario).click()
            
                tempo_espera("alteração")
            
                lista_suspensa = Select(navegador.find_element(*xpath_tipo_honorario))
            
                lista_suspensa.select_by_index(9)
            
                tempo_espera("alteração")
            
                navegador.find_element(*xpath_tipo_devedor_reclamado).click()
            
                tempo_espera("alteração")
            
                if tipo_segundo_adv_recte == "INFORMADO":
            
                    navegador.find_element(*xpath_valor_informado).click()
            
                    navegador.find_element(*xpath_data_honorario).send_keys(vencimento_segundo_adv_recte)
            
                    navegador.find_element(*xpath_valor_honorario).send_keys(valor_segundo_adv_recte)

                    if vencimento_juros_segundo_adv_recte != vazio:

                        navegador.find_element(*xpath_juros_honorario).click()

                        navegador.find_element(*xpath_data_juros_honorario).send_keys(vencimento_juros_segundo_adv_recte)
            
                    tempo_espera("alteração")
            
                elif tipo_segundo_adv_recte == "CALCULADO":
            
                    navegador.find_element(*xpath_aliquota_honorario).send_keys(vencimento_segundo_adv_recte)
            
                    lista_suspensa = Select(navegador.find_element(*xpath_base_honorario))
            
                    lista_suspensa.select_by_index(1)
            
                    tempo_espera("alteração")
            
                navegador.find_element(*xpath_nome_honorario).send_keys(segundo_adv_recte)
            
                if ir_segundo_adv_recte == "IRPF":

                    navegador.find_element(*xpath_apurar_ir_honorarios).click()
                    
                    navegador.find_element(*xpath_irpf_honorarios).click()

                    tempo_espera("alteração")  

                elif ir_segundo_adv_recte == "IRPJ":

                    navegador.find_element(*xpath_apurar_ir_honorarios).click()
                   
                    navegador.find_element(*xpath_irpj_honorarios).click()  

                    tempo_espera("alteração")                    
            
                navegador.find_element(*xpath_salvar).click()
            
                tempo_espera("alteração")             

# HONORÁRIOS 1º ADV. RECDA.
            
            if primeira_adv_recda != vazio:
            
                var_honorarios_1_adv_recda()

                tempo_espera("alteração")
            
                navegador.find_element(*xpath_novo_honorario).click()
            
                tempo_espera("alteração")
            
                lista_suspensa = Select(navegador.find_element(*xpath_tipo_honorario))
            
                lista_suspensa.select_by_index(9)
            
                navegador.find_element(*xpath_tipo_devedor_reclamante).click()
            
                tempo_espera("alteração")
            
                if exigibilidade_primeira_adv_recda == "SIM":
            
                    navegador.find_element(*xpath_cobrar_honorario).click()
            
                if tipo_primeira_adv_recda == "INFORMADO":
            
                    navegador.find_element(*xpath_valor_informado).click()
            
                    tempo_espera("alteração")
            
                    navegador.find_element(*xpath_data_honorario).click()
            
                    navegador.find_element(*xpath_data_honorario).send_keys(vencimento_primeira_adv_recda)
            
                    tempo_espera("alteração")
            
                    navegador.find_element(*xpath_valor_honorario).send_keys(valor_primeira_adv_recda)
            
                    navegador.find_element(*xpath_juros_honorario).click()
                        
                    if vencimento_juros_primeira_adv_recda != vazio:

                        navegador.find_element(*xpath_juros_honorario).click()

                        navegador.find_element(*xpath_data_juros_honorario).send_keys(vencimento_juros_primeira_adv_recda)

                    tempo_espera("alteração")
            
                elif tipo_primeira_adv_recda == "CALCULADO":
            
                    navegador.find_element(*xpath_aliquota_honorario).send_keys(valor_primeira_adv_recda)
            
                    lista_suspensa = Select(navegador.find_element(*xpath_base_honorario))
            
                    lista_suspensa.select_by_index(1)
            
                navegador.find_element(*xpath_nome_honorario).send_keys(primeira_adv_recda)

                if ir_primeira_adv_recda == "IRPF":

                    navegador.find_element(*xpath_apurar_ir_honorarios).click()
                    
                    navegador.find_element(*xpath_irpf_honorarios).click()

                    tempo_espera("alteração")

                elif ir_primeira_adv_recda == "IRPJ":

                    navegador.find_element(*xpath_apurar_ir_honorarios).click()
                   
                    navegador.find_element(*xpath_irpj_honorarios).click()    

                    tempo_espera("alteração")                
            
                navegador.find_element(*xpath_salvar).click()                
                        
                tempo_espera("alteração")
    
# HONORÁRIOS 2º ADV. RECDA.
            
            if segunda_adv_recda != vazio:

                var_honorarios_2_adv_recda()
            
                tempo_espera("alteração")
            
                navegador.find_element(*xpath_novo_honorario).click()
            
                tempo_espera("alteração")
            
                lista_suspensa = Select(navegador.find_element(*xpath_tipo_honorario))
            
                lista_suspensa.select_by_index(9)
            
                navegador.find_element(*xpath_tipo_devedor_reclamante).click()
            
                tempo_espera("alteração")
            
                if exigibilidade_segunda_adv_recda == "SIM":
            
                    navegador.find_element(*xpath_cobrar_honorario).click()
            
                if tipo_segunda_adv_recda == "INFORMADO":
            
                    navegador.find_element(*xpath_valor_informado).click()
            
                    tempo_espera("alteração")
            
                    navegador.find_element(*xpath_data_honorario).click()
            
                    navegador.find_element(*xpath_data_honorario).send_keys(vencimento_segunda_adv_recda)
            
                    tempo_espera("alteração")
            
                    navegador.find_element(*xpath_valor_honorario).send_keys(valor_segunda_adv_recda)
            
                    navegador.find_element(*xpath_juros_honorario).click()
                        
                    if vencimento_juros_segunda_adv_recda != vazio:

                        navegador.find_element(*xpath_juros_honorario).click()

                        navegador.find_element(*xpath_data_juros_honorario).send_keys(vencimento_juros_segunda_adv_recda)

                    tempo_espera("alteração")
            
                elif tipo_segunda_adv_recda == "CALCULADO":
            
                    navegador.find_element(*xpath_aliquota_honorario).send_keys(valor_segunda_adv_recda)
            
                    lista_suspensa = Select(navegador.find_element(*xpath_base_honorario))
            
                    lista_suspensa.select_by_index(1)
            
                navegador.find_element(*xpath_nome_honorario).send_keys(segunda_adv_recda)

                if ir_segunda_adv_recda == "IRPF":

                    navegador.find_element(*xpath_apurar_ir_honorarios).click()
                    
                    navegador.find_element(*xpath_irpf_honorarios).click()

                    tempo_espera("alteração")

                elif ir_segunda_adv_recda == "IRPJ":

                    navegador.find_element(*xpath_apurar_ir_honorarios).click()
                   
                    navegador.find_element(*xpath_irpj_honorarios).click()

                    tempo_espera("alteração")                    
            
                navegador.find_element(*xpath_salvar).click()                
                        
                tempo_espera("alteração")
            
# HONORÁRIOS 3º ADV. RECDA.
            
            if terceira_adv_recda != vazio:
            
                var_honorarios_3_adv_recda()

                tempo_espera("alteração")
            
                navegador.find_element(*xpath_novo_honorario).click()
            
                tempo_espera("alteração")
            
                lista_suspensa = Select(navegador.find_element(*xpath_tipo_honorario))
            
                lista_suspensa.select_by_index(9)
            
                navegador.find_element(*xpath_tipo_devedor_reclamante).click()
            
                tempo_espera("alteração")
            
                if exigibilidade_terceira_adv_recda == "SIM":
            
                    navegador.find_element(*xpath_cobrar_honorario).click()
            
                if tipo_terceira_adv_recda == "INFORMADO":
            
                    navegador.find_element(*xpath_valor_informado).click()
            
                    tempo_espera("alteração")
            
                    navegador.find_element(*xpath_data_honorario).click()
            
                    navegador.find_element(*xpath_data_honorario).send_keys(vencimento_terceira_adv_recda)
            
                    tempo_espera("alteração")
            
                    navegador.find_element(*xpath_valor_honorario).send_keys(valor_terceira_adv_recda)
            
                    navegador.find_element(*xpath_juros_honorario).click()
            
                    if vencimento_juros_terceira_adv_recda != vazio:

                        navegador.find_element(*xpath_juros_honorario).click()

                        navegador.find_element(*xpath_data_juros_honorario).send_keys(vencimento_juros_terceira_adv_recda)

                    tempo_espera("alteração")
            
                elif tipo_terceira_adv_recda == "CALCULADO":
            
                    navegador.find_element(*xpath_aliquota_honorario).send_keys(valor_terceira_adv_recda)
            
                    lista_suspensa = Select(navegador.find_element(*xpath_base_honorario))
            
                    lista_suspensa.select_by_index(1)
            
                navegador.find_element(*xpath_nome_honorario).send_keys(terceira_adv_recda)

                if ir_terceira_adv_recda == "IRPF":

                    navegador.find_element(*xpath_apurar_ir_honorarios).click()
                    
                    navegador.find_element(*xpath_irpf_honorarios).click()

                    tempo_espera("alteração")

                elif ir_terceira_adv_recda == "IRPJ":

                    navegador.find_element(*xpath_apurar_ir_honorarios).click()
                   
                    navegador.find_element(*xpath_irpj_honorarios).click()       

                    tempo_espera("alteração")             
            
                navegador.find_element(*xpath_salvar).click()                
                        
                tempo_espera("alteração")

# HONORÁRIOS 4º ADV. RECDA.
            
            if quarta_adv_recda != vazio:

                var_honorarios_4_adv_recda()
            
                tempo_espera("alteração")
            
                navegador.find_element(*xpath_novo_honorario).click()
            
                tempo_espera("alteração")
            
                lista_suspensa = Select(navegador.find_element(*xpath_tipo_honorario))
            
                lista_suspensa.select_by_index(9)
            
                navegador.find_element(*xpath_tipo_devedor_reclamante).click()
            
                tempo_espera("alteração")
            
                if exigibilidade_quarta_adv_recda == "SIM":
            
                    navegador.find_element(*xpath_cobrar_honorario).click()
            
                if tipo_quarta_adv_recda == "INFORMADO":
            
                    navegador.find_element(*xpath_valor_informado).click()
            
                    tempo_espera("alteração")
            
                    navegador.find_element(*xpath_data_honorario).click()
            
                    navegador.find_element(*xpath_data_honorario).send_keys(vencimento_quarta_adv_recda)
            
                    tempo_espera("alteração")
            
                    navegador.find_element(*xpath_valor_honorario).send_keys(valor_quarta_adv_recda)
            
                    navegador.find_element(*xpath_juros_honorario).click()
            
                    tempo_espera("alteração")
            
                    if vencimento_juros_quarta_adv_recda != vazio:

                        navegador.find_element(*xpath_juros_honorario).click()

                        navegador.find_element(*xpath_data_juros_honorario).send_keys(vencimento_juros_quarta_adv_recda)

                        tempo_espera("alteração")
            
                elif tipo_quarta_adv_recda == "CALCULADO":
            
                    navegador.find_element(*xpath_aliquota_honorario).send_keys(valor_quarta_adv_recda)
            
                    lista_suspensa = Select(navegador.find_element(*xpath_base_honorario))
            
                    lista_suspensa.select_by_index(1)
            
                navegador.find_element(*xpath_nome_honorario).send_keys(quarta_adv_recda)

                if ir_quarta_adv_recda == "IRPF":

                    navegador.find_element(*xpath_apurar_ir_honorarios).click()
                    
                    navegador.find_element(*xpath_irpf_honorarios).click()

                    tempo_espera("alteração")

                elif ir_quarta_adv_recda == "IRPJ":

                    navegador.find_element(*xpath_apurar_ir_honorarios).click()
                   
                    navegador.find_element(*xpath_irpj_honorarios).click()   

                    tempo_espera("alteração")                 
            
                navegador.find_element(*xpath_salvar).click()                
                        
                tempo_espera("alteração")

# HONORÁRIOS PERITO CONTÁBIL
            
            if perito_contabil != vazio:

                var_honorarios_perito_contabil()
            
                navegador.find_element(*xpath_novo_honorario).click()
            
                tempo_espera("alteração")
            
                lista_suspensa = Select(navegador.find_element(*xpath_tipo_honorario))
            
                lista_suspensa.select_by_index(3)
            
                navegador.find_element(*xpath_tipo_devedor_reclamado).click()
            
                if tipo_perito_contabil == "INFORMADO":
            
                    navegador.find_element(*xpath_valor_informado).click()
            
                    tempo_espera("alteração")
            
                    navegador.find_element(*xpath_data_honorario).click()
            
                    navegador.find_element(*xpath_data_honorario).send_keys(vencimento_perito_contabil)
            
                    tempo_espera("alteração")
            
                    navegador.find_element(*xpath_valor_honorario).send_keys(valor_perito_contabil)
            
                    if vencimento_juros_perito_contabil != vazio:

                        navegador.find_element(*xpath_juros_honorario).click()

                        navegador.find_element(*xpath_data_juros_honorario).send_keys(vencimento_juros_perito_contabil)

                        tempo_espera("alteração")

                elif tipo_perito_contabil == "CALCULADO":
            
                    navegador.find_element(*xpath_aliquota_honorario).send_keys(valor_perito_contabil)
            
                    lista_suspensa = Select(navegador.find_element(*xpath_base_honorario))
            
                    lista_suspensa.select_by_index(1)
            
                navegador.find_element(*xpath_nome_honorario).send_keys(perito_contabil)

                if ir_perito_contabil == "IRPF":

                    navegador.find_element(*xpath_apurar_ir_honorarios).click()
                    
                    navegador.find_element(*xpath_irpf_honorarios).click()

                    tempo_espera("alteração")

                elif ir_perito_contabil == "IRPJ":

                    navegador.find_element(*xpath_apurar_ir_honorarios).click()
                   
                    navegador.find_element(*xpath_irpj_honorarios).click()   

                    tempo_espera("alteração")                    
            
                navegador.find_element(*xpath_salvar).click()
            
                tempo_espera("alteração")

# HONORÁRIOS ENGENHEIRO
        
            if engenheiro != vazio:

                var_honorarios_engenheiro()
            
                navegador.find_element(*xpath_novo_honorario).click()
            
                tempo_espera("alteração")
            
                lista_suspensa = Select(navegador.find_element(*xpath_tipo_honorario))
            
                lista_suspensa.select_by_index(3)
            
                navegador.find_element(*xpath_tipo_devedor_reclamado).click()
            
                if tipo_engenheiro == "INFORMADO":
            
                    navegador.find_element(*xpath_valor_informado).click()
            
                    tempo_espera("alteração")
            
                    navegador.find_element(*xpath_data_honorario).click()
            
                    navegador.find_element(*xpath_data_honorario).send_keys(vencimento_engenheiro)
            
                    tempo_espera("alteração")
            
                    navegador.find_element(*xpath_valor_honorario).send_keys(valor_engenheiro)
            
                    if vencimento_juros_engenheiro != vazio:

                        navegador.find_element(*xpath_juros_honorario).click()

                        navegador.find_element(*xpath_data_juros_honorario).send_keys(vencimento_juros_engenheiro)

                        tempo_espera("alteração")

                elif tipo_engenheiro == "CALCULADO":
            
                    navegador.find_element(*xpath_aliquota_honorario).send_keys(valor_engenheiro)
            
                    lista_suspensa = Select(navegador.find_element(*xpath_base_honorario))
            
                    lista_suspensa.select_by_index(1)
            
                navegador.find_element(*xpath_nome_honorario).send_keys(engenheiro)

                if ir_engenheiro == "IRPF":

                    navegador.find_element(*xpath_apurar_ir_honorarios).click()
                    
                    navegador.find_element(*xpath_irpf_honorarios).click()

                    tempo_espera("alteração")

                elif ir_engenheiro == "IRPJ":

                    navegador.find_element(*xpath_apurar_ir_honorarios).click()
                   
                    navegador.find_element(*xpath_irpj_honorarios).click()   

                    tempo_espera("alteração")                    
            
                navegador.find_element(*xpath_salvar).click()
            
                tempo_espera("alteração")

# HONORÁRIOS MÉDICO
            
            if medico != vazio:

                var_honorarios_medico()
            
                navegador.find_element(*xpath_novo_honorario).click()
            
                tempo_espera("alteração")
            
                lista_suspensa = Select(navegador.find_element(*xpath_tipo_honorario))
            
                lista_suspensa.select_by_index(3)
            
                navegador.find_element(*xpath_tipo_devedor_reclamado).click()
            
                if tipo_medico == "INFORMADO":
            
                    navegador.find_element(*xpath_valor_informado).click()
            
                    tempo_espera("alteração")
            
                    navegador.find_element(*xpath_data_honorario).click()
            
                    navegador.find_element(*xpath_data_honorario).send_keys(vencimento_medico)
            
                    tempo_espera("alteração")
            
                    navegador.find_element(*xpath_valor_honorario).send_keys(valor_medico)
            
                    if vencimento_juros_medico != vazio:

                        navegador.find_element(*xpath_juros_honorario).click()

                        navegador.find_element(*xpath_data_juros_honorario).send_keys(vencimento_juros_medico)

                        tempo_espera("alteração")

                elif tipo_medico == "CALCULADO":
            
                    navegador.find_element(*xpath_aliquota_honorario).send_keys(valor_medico)
            
                    lista_suspensa = Select(navegador.find_element(*xpath_base_honorario))
            
                    lista_suspensa.select_by_index(1)
            
                navegador.find_element(*xpath_nome_honorario).send_keys(medico)

                if ir_medico == "IRPF":

                    navegador.find_element(*xpath_apurar_ir_honorarios).click()
                    
                    navegador.find_element(*xpath_irpf_honorarios).click()

                    tempo_espera("alteração")

                elif ir_medico == "IRPJ":

                    navegador.find_element(*xpath_apurar_ir_honorarios).click()
                   
                    navegador.find_element(*xpath_irpj_honorarios).click()   

                    tempo_espera("alteração")                    
            
                navegador.find_element(*xpath_salvar).click()
            
                tempo_espera("alteração")
        
# MULTAS E INDENIZAÇÕES

        if data['Multas e Indenizações'].value == True:

            navegador.find_element(*xpath_aba_multas).click()

            tempo_espera("alteração")

# IMPOSTO DE RENDA

        if data['Imposto de Renda'].value == True:

            navegador.find_element(*xpath_aba_ir).click()

            tempo_espera("alteração")            

# PENSÃO ALIMENTÍCIA

        if data['Pensão Alimentícia'].value == True:

            navegador.find_element(*xpath_pensao_alimenticia).click()

            tempo_espera("alteração")               

# PREVIDÊNCIA PRIVADA

        if data['Previdência Privada'].value == True:

            navegador.find_element(*xpath_previdencia_privada).click()

            tempo_espera("alteração")              

# CONTRIBUIÇÃO SOCIAL

        if data['Contribuição Social'].value == True:

            var_contribuicao_social()
        
            navegador.find_element(*xpath_contribuicao_social).click()

            tempo_espera("salvar")
            
            if correcao_trabalhista =="SIM":
                navegador.find_element(*xpath_correcao_trabalhista).click()

            if sobre_salarios_pagos=="SIM":
                navegador.find_element(*xpath_sobre_salarios_pagos).click()
            
            navegador.find_element(*xpath_salvar).click()
            
            tempo_espera("alteração")
            
            navegador.find_element(*xpath_ocorrencias_inss).click()
            
            tempo_espera("alteração")
            
            navegador.find_element(*xpath_aba_salarios_pagos).click()
            
            tempo_espera("alteração")
            
            navegador.find_element(*xpath_regerar_inss).click()
            
            tempo_espera("alteração")
            
            navegador.find_element(*xpath_ativar_atividade_economica).click()
            
            tempo_espera("alteração")
            
            navegador.find_element(*xpath_atividade_economica).send_keys(atividade_economica)
            
            tempo_espera("alteração")
            
            if navegador.find_elements(*xpath_erro_atividade_economica):
            
                navegador.find_element(*xpath_aliquota_fixa).click()
            
                print("")
            
                print("ATENÇÃO! - A Atividade Econômica não foi encontrada!")
            
                tempo_espera("alteração")
            
            else:
            
                navegador.find_element(*xpath_selecionar_atividade_economica).click()
            
            if data_inicial_inss != vazio:
            
                navegador.find_element(*xpath_inicio_inss).clear()
            
                navegador.find_element(*xpath_inicio_inss).click()
            
                tempo_espera("alteração")
            
                navegador.find_element(*xpath_inicio_inss).send_keys(data_inicial_inss)
            
                tempo_espera("alteração")

            if data_final_inss != vazio:
            
                navegador.find_element(*xpath_final_inss).clear()
            
                navegador.find_element(*xpath_final_inss).click()
            
                tempo_espera("alteração")
            
                navegador.find_element(*xpath_final_inss).send_keys(data_final_inss)
            
                tempo_espera("alteração")
            
            if simples_nacional == "OPTANTE":
            
                navegador.find_element(*xpath_inicio_simples).click()
            
                navegador.find_element(*xpath_inicio_simples).send_keys(inicio_nacional)
            
                navegador.find_element(xpath_final_simples).click()
            
                navegador.find_element(xpath_final_simples).send_keys(final_nacional)
            
                tempo_espera("alteração")
            
                navegador.find_element(*xpath_adicionar_simples).click()
            
            navegador.find_element(*xpath_confirmar_inss).click()
            
            tempo_espera("alteração")
    
            navegador.find_element(*xpath_salvar).click()
            
            tempo_espera("salvar")
        
# FGTS

        if data['FGTS'].value == True:

            var_fgts()

            navegador.find_element(*xpath_aba_fgts).click()

            tempo_espera("salvar")

            if fgts == "SIM":
            
                navegador.find_element(*xpath_fgts_sim).click()
            
            elif fgts == "NÃO":
            
                navegador.find_element(*xpath_fgts_nao).click()

            if multa_fgts == "SIM":

                navegador.find_element(*xpath_fgts_multa).click()

                tempo_espera("alteração")

                if aliquota_fgts == "20%":
            
                    navegador.find_element(*xpath_fgts_multa_20).click()           
                
                    tempo_espera("alteração")
            
                elif aliquota_fgts == "40%":
            
                    navegador.find_element(*xpath_fgts_multa_40).click()

                    tempo_espera("alteração")

                if multa_467 == "SIM":

                    navegador.find_element(*xpath_fgts_multa_467).click()
                
                    lista_suspensa = Select(navegador.find_element(*xpath_incidencia_fgts))
                
                    lista_suspensa.select_by_value(incidencia_fgts)

                    navegador.find_element(*xpath_data_saldo_saque_fgts).send_keys(data_saldo_saque_fgts)

                    navegador.find_element(*xpath_valor_saldo_saque_fgts).send_keys(valor_saldo_saque_fgts)

                    if deduzir_saldo_saque_fgts != vazio:
                        navegador.find_element(*xpath_deduzir_saldo_saque_fgts).click()  
                
            tempo_espera("salvar")

            navegador.find_element(*xpath_salvar).click()
            
            tempo_espera("salvar")

# SEGURO-DESEMPREGO

        if data['Seguro-desemprego'].value == True:

            navegador.find_element(*xpath_aba_seguro_desemprego).click()

            tempo_espera("alteração")              

# SALÁRIO-FAMÍLIA

        if data['Salário-família'].value == True:

            navegador.find_element(*xpath_aba_salario_familia).click()

            tempo_espera("alteração")

# CARTÃO DE PONTO

        if data['Cartão de Ponto'].value == True:

            navegador.find_element(*xpath_aba_cartao_ponto).click()

            tempo_espera("alteração")            

# VERBAS

        if data['Verbas'].value == True:

            navegador.find_element(*xpath_aba_verbas).click()

            tempo_espera("alteração")               

# HISTÓRICO SALARIAL

        if data['Histórico Salarial'].value == True:

            navegador.find_element(*xpath_historico_salarial).click()

            tempo_espera("alteração")            

# FÉRIAS

        if data['Férias'].value == True:

            navegador.find_element(*xpath_aba_ferias).click()

            tempo_espera("alteração")

            navegador.find_element(*xpath_adicionar_ferias).click()
            
            WebDriverWait(navegador,20).until(EC.visibility_of_element_located(*xpath_erro_ferias))
                                                    
            navegador.find_element(*xpath_confirmar_ferias).click()
            
            tempo_espera("alteração")

            navegador.find_element(*xpath_salvar).click()

# FALTAS

        if data['Faltas'].value == True:

            navegador.find_element(*xpath_aba_faltas).click()

            tempo_espera("alteração")             

# SALVAMENTO

        tempo_espera("salvar")

        navegador.find_element(*xpath_menu_exportar).click()

        tempo_espera("salvar")

        navegador.find_element(*xpath_aba_exportar).click()

        tempo_espera("salvar")        

        navegador.execute_script(js_exportar)

        tempo_espera("exportar")
