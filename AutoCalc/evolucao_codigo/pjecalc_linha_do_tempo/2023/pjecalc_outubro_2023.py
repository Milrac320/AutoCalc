
def automacao():

    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.support.ui import Select
    from selenium.common.exceptions import NoSuchElementException
    import tkinter as tk
    from tkinter import filedialog
    import pandas as pd
    import time
    import datetime
    import math
    import warnings
    from colorama import init, Fore
    import psutil
    import subprocess

    warnings.simplefilter(action='ignore', category=FutureWarning)

    def centralizar_texto(texto, largura):
        espacos_esquerda = (largura - len(texto)) // 2
        return " " * espacos_esquerda + texto
    
    init(autoreset=True)
    largura_menu = 125

    def verifica_processo_ativo(nome_processo):
        for processo in psutil.process_iter(attrs=['pid', 'name']):
            if nome_processo.lower() in processo.info['name'].lower():
                return True
        return False

    def encerrar_processo(nome_processo):
        for processo in psutil.process_iter(attrs=['pid', 'name']):
            if nome_processo.lower() in processo.info['name'].lower():
                try:
                    processo_pje = psutil.Process(processo.info['pid'])
                    processo_pje.terminate()
                    processo_pje.wait()
                except Exception as e:
                    print(f"Erro ao encerrar o processo {nome_processo}: {e}")

    caminho_arquivo_bat = "C:/Users/user/Downloads/arquivosPASTAS/pjecalc-windows64-2.12.0/iniciarPjeCalc.bat"
    nome_processo_javaw = "javaw.exe"
    nome_processo_firefox = "firefox.exe"

    if verifica_processo_ativo(nome_processo_javaw):
        print(f"O processo {nome_processo_javaw} está ativo.")
    else:
        print(f"O processo {nome_processo_javaw} não está ativo, aguarde.")
        try:
            # Inicie o subprocesso
            processo = subprocess.Popen(caminho_arquivo_bat, shell=True)
            
            # Aguarde até que o processo "javaw.exe" seja iniciado
            while not verifica_processo_ativo(nome_processo_javaw):
                time.sleep(1)

            # Aguarde até que o processo "firefox.exe" esteja ativo
            while not verifica_processo_ativo(nome_processo_firefox):
                time.sleep(1)

            # Se o processo "firefox.exe" estiver ativo, encerre-o
            encerrar_processo(nome_processo_firefox)

        except Exception as e:
            print(f"Erro ao executar o arquivo .bat ou encerrar o processo: {e}")

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[("Arquivos Excel", "*.xlsm")])

    if file_path:
        df = pd.read_excel(file_path, engine='openpyxl', header=None, sheet_name='PJE CALC', dtype=str)
        df = df.applymap(lambda x: None if pd.isna(x) else x)
        
        # TRANSFORMAR DATAS

        def converter_data(valor):
            if pd.isna(valor):
                return None
            valor_int = int(valor)
            if valor_int > 59:
                valor_int -= 1
                data_base_excel = datetime.date(1899, 12, 31)
                data = data_base_excel + datetime.timedelta(days=valor_int)
                data_formatada = data.strftime('%d-%m-%Y')
                return data_formatada
            
        # VARIÁVEIS

        link= "http://localhost:9257/pjecalc/pages/principal.jsf?conversationId=1"

        sequencia = df.iloc[3, 5]
        digito = df.iloc[3, 7]
        ano = df.iloc[3, 9]
        tribunal = df.iloc[3, 13]
        vara = df.iloc[3, 15]

        estado= df.iloc[6,5]
        municipio= df.iloc[6,10]

        demissao = converter_data(df.iloc[7,10])
        ajuizamento = converter_data(df.iloc[7,14])
        data_inicial = converter_data(df.iloc[8,5])
        data_final = converter_data(df.iloc[8,10])
        data_inicial_inss = converter_data(df.iloc[15,10])
        data_final_inss = converter_data(df.iloc[15,14])
        admissao = converter_data(df.iloc[7,5])
        ultima_atualizacao = converter_data(df.iloc[6, 14])

        prescricao=df.iloc[8,14]

        prazo_aviso=df.iloc[9,5]
        oj415=df.iloc[9,10]
        carga_horaria=df.iloc[9,14]

        recte = df.iloc[4, 5]
        cpf = df.iloc[4, 10]
        adv_recte = df.iloc[4, 14]
        recda = df.iloc[5, 5]
        cnpj = df.iloc[5, 10]
        adv_recda = df.iloc[5, 14]

        indice_trabalhista = df.iloc[10, 5]
        segundo_indice_trabalhista= df.iloc[10, 10]
        data_indice=converter_data(df.iloc[10,14])

        tabela_juros = df.iloc[11, 5]
        segunda_tabela_juros = df.iloc[11, 10]
        data_juros=converter_data(df.iloc[11,14])
        pre_juros=df.iloc[12,14]

        base_juros = df.iloc[12, 5]
        fgts = df.iloc[18, 5]
        multa_fgts=df.iloc[18, 10]
        aliquota_fgts=df.iloc[18, 14]
        inss = df.iloc[12, 10]

        custas= df.iloc[13, 5]
        vencimento_custas= converter_data(df.iloc[13, 10])
        valor_custas= df.iloc[13, 14]

        atividade_economica=df.iloc[15,5]
        simples_nacional=df.iloc[16,5]
        inicio_nacional=converter_data(df.iloc[16, 10])
        final_nacional=converter_data(df.iloc[16, 14])

        sucumbencia_recte=df.iloc[20,5]
        vencimento_recte=converter_data(df.iloc[20,10])
        valor_recte=df.iloc[20,14]
        devedor_recte=df.iloc[21,10]
        tipo_recte=df.iloc[21,14]

        sucumbencia_recda=df.iloc[23,5]
        vencimento_recda=converter_data(df.iloc[23,10])
        valor_recda=df.iloc[23,14]
        exigibilidade_recda=df.iloc[24,5]
        devedor_recda=df.iloc[24,10]
        tipo_recda=df.iloc[24,14]

        sucumbencia_recda_2=df.iloc[26,5]
        vencimento_recda_2=converter_data(df.iloc[26,10])
        valor_recda_2=df.iloc[26,14]
        exigibilidade_recda_2=df.iloc[27,5]
        devedor_recda_2=df.iloc[27,10]
        tipo_recda_2=df.iloc[27,14]

        sucumbencia_contador=df.iloc[29,5]
        vencimento_contador=converter_data(df.iloc[29,10])
        valor_contador=df.iloc[29,14]
        devedor_contador=df.iloc[30,10]
        tipo_contador=df.iloc[30,14]

        sucumbencia_engenheiro=df.iloc[32,5]
        vencimento_engenheiro=converter_data(df.iloc[32,10])
        valor_engenheiro=df.iloc[32,14]
        devedor_engenheiro=df.iloc[33,10]
        tipo_engenheiro=df.iloc[33,14]

        sucumbencia_medico=df.iloc[35,5]
        vencimento_medico=converter_data(df.iloc[35,10])
        valor_medico=df.iloc[35,14]
        devedor_medico=df.iloc[36,10]
        tipo_medico=df.iloc[36,14]
        
        print("")
        print(centralizar_texto("Cálculo de Atualização (0) | Laudo (1)", largura_menu))
        print("")
        escolha = input(centralizar_texto("Digite o Nº da opção desejada: ", largura_menu))

        # INICIAR NAVEGADOR

        servico = Service(ChromeDriverManager().install())

        navegador = webdriver.Chrome(service=servico)

        navegador.get(link)

        time.sleep(1)

        # EXECUÇÃO PRIMEIRA ESCOLHA [ ATUALIZAÇÃO ]

        if escolha == '0':
            try:
                # ABERTURA CÁLCULO ATUALIZAÇÃO

                navegador.find_element('xpath','//*[@id="menupainel"]/li[1]').click()

                time.sleep(1)

                navegador.find_element('xpath','//*[@id="formulario:j_id38:0:j_id41:2:j_id46"]').click()

                time.sleep(1)

                # DADOS DO PROCESSO

                navegador.find_element('xpath','//*[@id="formulario:numero"]').send_keys(sequencia)

                navegador.find_element('xpath','//*[@id="formulario:digito"]').send_keys(digito)

                navegador.find_element('xpath','//*[@id="formulario:ano"]').send_keys(ano)

                navegador.find_element('xpath','//*[@id="formulario:regiao"]').send_keys(tribunal)

                navegador.find_element('xpath','//*[@id="formulario:vara"]').send_keys(vara)

                navegador.find_element('xpath','//*[@id="formulario:reclamanteNome"]').send_keys(recte)

                navegador.find_element('xpath','//*[@id="formulario:documentoFiscalReclamante:0"]').click()

                navegador.find_element('xpath','//*[@id="formulario:reclamanteNumeroDocumentoFiscal"]').click()

                navegador.find_element('xpath','//*[@id="formulario:reclamanteNumeroDocumentoFiscal"]').send_keys(cpf)

                if adv_recte != None:
                    navegador.find_element('xpath','//*[@id="formulario:nomeAdvogadoReclamante"]').send_keys(adv_recte)
                    navegador.find_element('xpath','//*[@id="formulario:incluirAdvogadoReclamante"]').click()

                navegador.find_element('xpath','//*[@id="formulario:reclamadoNome"]').send_keys(recda)

                navegador.find_element('xpath','//*[@id="formulario:tipoDocumentoFiscalReclamado:1"]').click()

                navegador.find_element('xpath','//*[@id="formulario:reclamadoNumeroDocumentoFiscal"]').click()

                navegador.find_element('xpath','//*[@id="formulario:reclamadoNumeroDocumentoFiscal"]').send_keys(cnpj)

                if adv_recda!=None:
                    navegador.find_element('xpath','//*[@id="formulario:nomeAdvogadoReclamado"]').send_keys(adv_recda)
                    navegador.find_element('xpath','//*[@id="formulario:incluirAdvogadoReclamado"]').click()
                
                navegador.find_element('xpath','//*[@id="formulario:tabParametrosCalculo_lbl"]').click()

                time.sleep(1)

                # PARÂMETROS DO CÁLCULO

                navegador.find_element('xpath','//*[@id="formulario:dataUltimaAtualizacaoInputDate"]').click()
                navegador.find_element('xpath','//*[@id="formulario:dataUltimaAtualizacaoInputDate"]').send_keys(ultima_atualizacao)

                if segundo_indice_trabalhista == None:
                    navegador.find_element('xpath','//*[@id="formulario:indiceTrabalhista"]').send_keys(indice_trabalhista)
                else:
                    navegador.find_element('xpath','//*[@id="formulario:indiceTrabalhista"]').send_keys(segundo_indice_trabalhista)

                navegador.find_element('xpath','//*[@id="formulario:ignorarTaxaNegativa"]').click()


                lista_suspensa = Select(navegador.find_element('xpath','//*[@id="formulario:baseDeJurosDasVerbas"]'))
                lista_suspensa.select_by_index(base_juros)

                if fgts == "SIM":
                    navegador.find_element('xpath','//*[@id="formulario:tipoDeVerba:0"]').click()
                elif fgts == "NÃO":
                    navegador.find_element('xpath','//*[@id="formulario:tipoDeVerba:1"]').click()

                if segunda_tabela_juros == None:
                    navegador.find_element('xpath','//*[@id="formulario:juros"]').send_keys(tabela_juros)
                else:
                    navegador.find_element('xpath','//*[@id="formulario:juros"]').send_keys(segunda_tabela_juros)
                                                
                if inss == "NÃO":
                    navegador.find_element('xpath','//*[@id="formulario:correcaoLei11941"]').click()

                navegador.find_element('xpath','//*[@id="formulario:qtdMesesRendimento"]').send_keys("0")

                lista_suspensa = Select(navegador.find_element('xpath','//*[@id="formulario:baseParaCustasCalculadas"]'))
                lista_suspensa.select_by_index(0)

                navegador.find_element('xpath','//*[@id="formulario:salvar"]').click()

            except Exception as e:
                print(f"Ocorreu um erro: {str(e)}")
                input()

            input()

        # EXECUÇÃO SEGUNDA ESCOLHA [ LAUDO ]
        
        elif escolha == '1':
            try:

                navegador.find_element('xpath','//*[@id="botoesInicio"]/div[1]/a').click()

                time.sleep(1)

                # DADOS DO PROCESSO --- OK

                navegador.find_element('xpath','//*[@id="formulario:numero"]').send_keys(sequencia)
                
                navegador.find_element('xpath','//*[@id="formulario:digito"]').send_keys(digito)
                
                navegador.find_element('xpath','//*[@id="formulario:ano"]').send_keys(ano)
            
                navegador.find_element('xpath','//*[@id="formulario:regiao"]').send_keys(tribunal)
            
                navegador.find_element('xpath','//*[@id="formulario:vara"]').send_keys(vara)
                
                navegador.find_element('xpath','//*[@id="formulario:reclamanteNome"]').send_keys(recte)
                
                navegador.find_element('xpath','//*[@id="formulario:documentoFiscalReclamante:0"]').click()
                
                navegador.find_element('xpath','//*[@id="formulario:reclamanteNumeroDocumentoFiscal"]').click()
                
                navegador.find_element('xpath','//*[@id="formulario:reclamanteNumeroDocumentoFiscal"]').send_keys(cpf)
                
                if adv_recte != None:
                    navegador.find_element('xpath','//*[@id="formulario:nomeAdvogadoReclamante"]').send_keys(adv_recte)
                    navegador.find_element('xpath','//*[@id="formulario:incluirAdvogadoReclamante"]').click()
                
                navegador.find_element('xpath','//*[@id="formulario:reclamadoNome"]').send_keys(recda)
                
                navegador.find_element('xpath','//*[@id="formulario:tipoDocumentoFiscalReclamado:1"]').click()
                
                navegador.find_element('xpath','//*[@id="formulario:reclamadoNumeroDocumentoFiscal"]').click()
                
                navegador.find_element('xpath','//*[@id="formulario:reclamadoNumeroDocumentoFiscal"]').send_keys(cnpj)
                
                if adv_recda != None:
                    navegador.find_element('xpath','//*[@id="formulario:nomeAdvogadoReclamado"]').send_keys(adv_recda)
                    navegador.find_element('xpath','//*[@id="formulario:incluirAdvogadoReclamado"]').click()
                
                navegador.find_element('xpath','//*[@id="formulario:tabParametrosCalculo_lbl"]').click()

                time.sleep(1)


                # PARÂMETROS DO CÁLCULO --- OK

                navegador.find_element('xpath','//*[@id="formulario:estado"]').send_keys(estado)
                time.sleep(1)
                navegador.find_element('xpath','//*[@id="formulario:municipio"]').send_keys(municipio)
                time.sleep(1)       
                navegador.find_element('xpath','//*[@id="formulario:dataAdmissaoInputDate"]').click()
                navegador.find_element('xpath','//*[@id="formulario:dataAdmissaoInputDate"]').send_keys(admissao)
                
                if demissao != None:
                    navegador.find_element('xpath','//*[@id="formulario:dataDemissaoInputDate"]').click()
                    navegador.find_element('xpath','//*[@id="formulario:dataDemissaoInputDate"]').send_keys(demissao)
                elif demissao == None:
                    navegador.find_element('xpath','//*[@id="formulario:dataTerminoCalculoInputDate"]').click()
                    navegador.find_element('xpath','//*[@id="formulario:dataTerminoCalculoInputDate"]').send_keys(data_final)          
                
                navegador.find_element('xpath','//*[@id="formulario:dataAjuizamentoInputDate"]').click()
                navegador.find_element('xpath','//*[@id="formulario:dataAjuizamentoInputDate"]').send_keys(ajuizamento)
                
                if data_inicial != None:
                    navegador.find_element('xpath','//*[@id="formulario:dataInicioCalculoInputDate"]').click()
                    navegador.find_element('xpath','//*[@id="formulario:dataInicioCalculoInputDate"]').send_keys(data_inicial)
                
                if data_final != None:
                    navegador.find_element('xpath','//*[@id="formulario:dataTerminoCalculoInputDate"]').click()
                    navegador.find_element('xpath','//*[@id="formulario:dataTerminoCalculoInputDate"]').send_keys(data_final)
                
                if prescricao == 'SIM':
                    navegador.find_element('xpath','//*[@id="formulario:prescricaoQuinquenal"]').click()
                
                navegador.find_element('xpath','//*[@id="formulario:apuracaoPrazoDoAvisoPrevio"]').send_keys(prazo_aviso)
                
                if prazo_aviso == 'Não apurar':
                    navegador.find_element('xpath','//*[@id="formulario:projetaAvisoIndenizado"]').click()
                
                if oj415 == 'SIM':
                    navegador.find_element('xpath','//*[@id="formulario:zeraValorNegativo"]').click()
                
                navegador.find_element('xpath','//*[@id="formulario:valorCargaHorariaPadrao"]').click()
                navegador.find_element('xpath','//*[@id="formulario:valorCargaHorariaPadrao"]').send_keys(carga_horaria)
                
                navegador.find_element('xpath','//*[@id="formulario:listagemPontosFacultativos:0:excluirPontoFacultativo"]').click()
                
                navegador.find_element('xpath','//*[@id="formulario:salvar"]').click()

                time.sleep(1)

                navegador.find_element('xpath','//*[@id="formulario:j_id38:0:j_id41:22:j_id46"]').click()

                time.sleep(1)

                # CORREÇÃO, JUROS E MULTA

                navegador.find_element('xpath','//*[@id="formulario:indiceTrabalhista"]').send_keys(indice_trabalhista)
                time.sleep(1)

                if segundo_indice_trabalhista != None:
                    navegador.find_element('xpath','//*[@id="formulario:combinarOutroIndice"]').click()
                    time.sleep(1)     
                    navegador.find_element('xpath','//*[@id="formulario:outroIndiceTrabalhista"]').send_keys(segundo_indice_trabalhista)            
                    navegador.find_element('xpath','//*[@id="formulario:apartirDeOutroIndiceInputDate"]').click()
                    navegador.find_element('xpath','//*[@id="formulario:apartirDeOutroIndiceInputDate"]').send_keys(data_indice)
                    navegador.find_element('xpath','//*[@id="formulario:addOutroIndice"]').click()
                    time.sleep(1)

                navegador.find_element('xpath','//*[@id="formulario:ignorarTaxaNegativa"]').click()

                print(centralizar_texto("Faça as alterações dos Juros. Depois de pronto, pressione [1]", largura_menu))
                alterar_juros = input(centralizar_texto("Digite aqui: ", largura_menu))

                if alterar_juros == '1':

                    # if pre_juros == "SIM":
                    #     navegador.find_element('xpath','//*[@id="formulario:j_id150:0:excluirDep"]').click()
                    #     time.sleep(1)
                    #     navegador.find_element('xpath','//*[@id="formulario:juros"]').send_keys(tabela_juros)
                    #     navegador.find_element('xpath','//*[@id="formulario:combinarOutroJuros"]').click()
                    #     time.sleep(1)
                    #     navegador.find_element('xpath','//*[@id="formulario:outroJuros"]').send_keys(segunda_tabela_juros)
                    #     navegador.find_element('xpath','//*[@id="formulario:apartirDeOutroJurosInputDate"]').click()
                    #     navegador.find_element('xpath','//*[@id="formulario:apartirDeOutroJurosInputDate"]').send_keys(data_juros)
                    #     navegador.find_element('xpath','//*[@id="formulario:addOutroJuros"]').click()
                    #     time.sleep(1)

                    # elif pre_juros == "NÃO" or None:
                    #     navegador.find_element('xpath','//*[@id="formulario:aplicarJurosFasePreJudicial"]').click()
                    #     navegador.find_element('xpath','//*[@id="formulario:juros"]').send_keys(tabela_juros)

                    # DADOS ESPECÍFICOS --- OK

                    navegador.find_element('xpath','//*[@id="formulario:tabDadosEspecificos_lbl"]').click()

                    time.sleep(2)

                    lista_suspensa = Select(navegador.find_element('xpath','//*[@id="formulario:baseDeJurosDasVerbas"]'))
                    lista_suspensa.select_by_index(base_juros)
                    
                    time.sleep(1)

                    if inss == "NÃO":
                        navegador.find_element('xpath','//*[@id="formulario:correcaoLei11941"]').click()

                    navegador.find_element('xpath','//*[@id="formulario:salvar"]').click()

                    time.sleep(1)

                    navegador.find_element('xpath','//*[@id="formulario:j_id38:0:j_id41:21:j_id46"]').click()

                    # CUSTAS JUDICIAIS --- OK

                    time.sleep(2)

                    lista_suspensa = Select(navegador.find_element('xpath','//*[@id="formulario:baseParaCustasCalculadas"]'))
                    lista_suspensa.select_by_index(0)

                    time.sleep(1)

                    if custas == 'ISENTO' or custas == None or custas == "PAGOU":
                        navegador.find_element('xpath','//*[@id="formulario:tipoDeCustasDeConhecimentoDoReclamado:0"]').click()
                    else:
                        navegador.find_element('xpath','//*[@id="formulario:tipoDeCustasDeConhecimentoDoReclamado:2"]').click()
                        time.sleep(1)
                        navegador.find_element('xpath','//*[@id="formulario:dataVencimentoConhecimentoDoReclamadoInputDate"]').click()
                        time.sleep(1)
                        navegador.find_element('xpath','//*[@id="formulario:dataVencimentoConhecimentoDoReclamadoInputDate"]').send_keys(vencimento_custas)
                        navegador.find_element('xpath','//*[@id="formulario:valorConhecimentoDoReclamado"]').send_keys(valor_custas)

                    navegador.find_element('xpath','//*[@id="formulario:salvar"]').click()

                    time.sleep(1)

                    navegador.find_element('xpath','//*[@id="formulario:j_id38:0:j_id41:20:j_id46"]').click()

                    time.sleep(2)

                    # HONORÁRIOS --- OK

                    # HONORÁRIO RECLAMANTE --- OK

                    if sucumbencia_recte != any:
                        navegador.find_element('xpath','//*[@id="formulario:incluir"]').click()
                        time.sleep(1)
                        lista_suspensa = Select(navegador.find_element('xpath','//*[@id="formulario:tpHonorario"]'))
                        lista_suspensa.select_by_index(9)
                        time.sleep(1)
                        navegador.find_element('xpath','//*[@id="formulario:tipoDeDevedor:1"]').click()
                        time.sleep(1)
                        if tipo_recte == 'Informado':
                            navegador.find_element('xpath','//*[@id="formulario:tipoValor:0"]').click()
                            navegador.find_element('xpath','//*[@id="formulario:dataVencimentoInputDate"]').send_keys(vencimento_recte)
                            navegador.find_element('xpath','//*[@id="formulario:valor"]').send_keys(valor_recte)
                            time.sleep(1)
                        elif tipo_recte == 'Calculado':
                            navegador.find_element('xpath','//*[@id="formulario:aliquota"]').send_keys(valor_recte)
                            lista_suspensa = Select(navegador.find_element('xpath','//*[@id="formulario:baseParaApuracao"]'))
                            lista_suspensa.select_by_index(1)
                            time.sleep(1)
                        navegador.find_element('xpath','//*[@id="formulario:nomeCredor"]').send_keys(sucumbencia_recte)
                        time.sleep(1)
                        navegador.find_element('xpath','//*[@id="formulario:salvar"]').click()
                        time.sleep(1)
                    
                    # HONORÁRIO RECLAMADA --- OK

                    if sucumbencia_recda != None:
                        time.sleep(1)
                        navegador.find_element('xpath','//*[@id="formulario:incluir"]').click()
                        time.sleep(1)
                        lista_suspensa = Select(navegador.find_element('xpath','//*[@id="formulario:tpHonorario"]'))
                        lista_suspensa.select_by_index(9)
                        navegador.find_element('xpath','//*[@id="formulario:tipoDeDevedor:0"]').click()
                        time.sleep(1)
                        if exigibilidade_recda == 'SIM':
                            navegador.find_element('xpath','//*[@id="formulario:tipoCobrancaReclamante:1"]').click()
                        if tipo_recda == 'Informado':
                            navegador.find_element('xpath','//*[@id="formulario:tipoValor:0"]').click()
                            time.sleep(1)
                            navegador.find_element('xpath','//*[@id="formulario:dataVencimentoInputDate"]').click()
                            navegador.find_element('xpath','//*[@id="formulario:dataVencimentoInputDate"]').send_keys(vencimento_recda)
                            time.sleep(1)
                            navegador.find_element('xpath','//*[@id="formulario:valor"]').send_keys(valor_recda)
                            navegador.find_element('xpath','//*[@id="formulario:aplicarJuros"]').click()
                            time.sleep(1)
                            navegador.find_element('xpath','//*[@id="formulario:dataJurosAPartirDeInputDate"]').click()                
                            navegador.find_element('xpath','//*[@id="formulario:dataJurosAPartirDeInputDate"]').send_keys(vencimento_recda)
                            time.sleep(1)
                        elif tipo_recte == 'Calculado':
                            navegador.find_element('xpath','//*[@id="formulario:aliquota"]').send_keys(valor_recda)
                            lista_suspensa = Select(navegador.find_element('xpath','//*[@id="formulario:baseParaApuracao"]'))
                            lista_suspensa.select_by_index(1)
                        navegador.find_element('xpath','//*[@id="formulario:nomeCredor"]').send_keys(sucumbencia_recda)
                        navegador.find_element('xpath','//*[@id="formulario:salvar"]').click()
                        time.sleep(1)

                    # HONORÁRIO RECLAMADA 2 --- OK
                        
                    if sucumbencia_recda_2 != None:
                        time.sleep(1)
                        navegador.find_element('xpath','//*[@id="formulario:incluir"]').click()
                        time.sleep(1)
                        lista_suspensa = Select(navegador.find_element('xpath','//*[@id="formulario:tpHonorario"]'))
                        lista_suspensa.select_by_index(9)
                        navegador.find_element('xpath','//*[@id="formulario:tipoDeDevedor:0"]').click()
                        time.sleep(1)
                        if exigibilidade_recda_2 == 'SIM':
                            navegador.find_element('xpath','//*[@id="formulario:tipoCobrancaReclamante:1"]').click()
                        if tipo_recda_2 == 'Informado':
                            navegador.find_element('xpath','//*[@id="formulario:tipoValor:0"]').click()
                            time.sleep(1)
                            navegador.find_element('xpath','//*[@id="formulario:dataVencimentoInputDate"]').click()
                            navegador.find_element('xpath','//*[@id="formulario:dataVencimentoInputDate"]').send_keys(vencimento_recda_2)
                            time.sleep(1)
                            navegador.find_element('xpath','//*[@id="formulario:valor"]').send_keys(valor_recda_2)
                            navegador.find_element('xpath','//*[@id="formulario:aplicarJuros"]').click()
                            time.sleep(1)
                            navegador.find_element('xpath','//*[@id="formulario:dataJurosAPartirDeInputDate"]').click()                
                            navegador.find_element('xpath','//*[@id="formulario:dataJurosAPartirDeInputDate"]').send_keys(vencimento_recda_2)
                            time.sleep(1)
                        elif tipo_recda_2 == 'Calculado':
                            navegador.find_element('xpath','//*[@id="formulario:aliquota"]').send_keys(valor_recda_2)
                            lista_suspensa = Select(navegador.find_element('xpath','//*[@id="formulario:baseParaApuracao"]'))
                            lista_suspensa.select_by_index(1)
                        navegador.find_element('xpath','//*[@id="formulario:nomeCredor"]').send_keys(sucumbencia_recda_2)
                        navegador.find_element('xpath','//*[@id="formulario:salvar"]').click()
                        time.sleep(1)

                    # HONORÁRIO CONTADOR --- OK

                    if sucumbencia_contador != None:
                        navegador.find_element('xpath','//*[@id="formulario:incluir"]').click()
                        time.sleep(1)
                        lista_suspensa = Select(navegador.find_element('xpath','//*[@id="formulario:tpHonorario"]'))
                        lista_suspensa.select_by_index(3)
                        navegador.find_element('xpath','//*[@id="formulario:tipoDeDevedor:1"]').click()
                        if tipo_contador == 'Informado':
                            navegador.find_element('xpath','//*[@id="formulario:tipoValor:0"]').click()
                            time.sleep(1)
                            navegador.find_element('xpath','//*[@id="formulario:dataVencimentoInputDate"]').click()
                            navegador.find_element('xpath','//*[@id="formulario:dataVencimentoInputDate"]').send_keys(vencimento_contador)
                            time.sleep(1)
                            navegador.find_element('xpath','//*[@id="formulario:valor"]').send_keys(valor_contador)
                        elif tipo_contador == 'Calculado':
                            navegador.find_element('xpath','//*[@id="formulario:aliquota"]').send_keys(valor_contador)
                            lista_suspensa = Select(navegador.find_element('xpath','//*[@id="formulario:baseParaApuracao"]'))
                            lista_suspensa.select_by_index(1)
                        navegador.find_element('xpath','//*[@id="formulario:nomeCredor"]').send_keys(sucumbencia_contador)
                        navegador.find_element('xpath','//*[@id="formulario:salvar"]').click()
                        time.sleep(1)

                    # HONORÁRIO ENGENHEIRO --- OK

                    if sucumbencia_engenheiro != None:
                        navegador.find_element('xpath','//*[@id="formulario:incluir"]').click()
                        time.sleep(1)
                        lista_suspensa = Select(navegador.find_element('xpath','//*[@id="formulario:tpHonorario"]'))
                        lista_suspensa.select_by_index(5)
                        navegador.find_element('xpath','//*[@id="formulario:tipoDeDevedor:1"]').click()
                        if tipo_engenheiro == 'Informado':
                            navegador.find_element('xpath','//*[@id="formulario:tipoValor:0"]').click()
                            time.sleep(1)
                            navegador.find_element('xpath','//*[@id="formulario:dataVencimentoInputDate"]').click()
                            navegador.find_element('xpath','//*[@id="formulario:dataVencimentoInputDate"]').send_keys(vencimento_engenheiro)
                            time.sleep(1)
                            navegador.find_element('xpath','//*[@id="formulario:valor"]').send_keys(valor_engenheiro)
                        elif tipo_engenheiro == 'Calculado':
                            navegador.find_element('xpath','//*[@id="formulario:aliquota"]').send_keys(valor_engenheiro)
                            lista_suspensa = Select(navegador.find_element('xpath','//*[@id="formulario:baseParaApuracao"]'))
                            lista_suspensa.select_by_index(1)
                        navegador.find_element('xpath','//*[@id="formulario:nomeCredor"]').send_keys(sucumbencia_engenheiro)
                        navegador.find_element('xpath','//*[@id="formulario:salvar"]').click()
                        time.sleep(1)

                    # HONORÁRIO MÉDICO --- OK

                    if sucumbencia_medico != None:
                        navegador.find_element('xpath','//*[@id="formulario:incluir"]').click()
                        time.sleep(1)
                        lista_suspensa = Select(navegador.find_element('xpath','//*[@id="formulario:tpHonorario"]'))
                        lista_suspensa.select_by_index(7)
                        navegador.find_element('xpath','//*[@id="formulario:tipoDeDevedor:1"]').click()
                        if tipo_medico == 'Informado':
                            navegador.find_element('xpath','//*[@id="formulario:tipoValor:0"]').click()
                            time.sleep(1)
                            navegador.find_element('xpath','//*[@id="formulario:dataVencimentoInputDate"]').click()
                            navegador.find_element('xpath','//*[@id="formulario:dataVencimentoInputDate"]').send_keys(vencimento_medico)
                            time.sleep(1)
                            navegador.find_element('xpath','//*[@id="formulario:valor"]').send_keys(valor_medico)
                        elif tipo_medico == 'Calculado':
                            navegador.find_element('xpath','//*[@id="formulario:aliquota"]').send_keys(valor_medico)
                            lista_suspensa = Select(navegador.find_element('xpath','//*[@id="formulario:baseParaApuracao"]'))
                            lista_suspensa.select_by_index(1)
                        navegador.find_element('xpath','//*[@id="formulario:nomeCredor"]').send_keys(sucumbencia_medico)
                        navegador.find_element('xpath','//*[@id="formulario:salvar"]').click()
                        time.sleep(1)

                    time.sleep(1)

                    navegador.find_element('xpath','//*[@id="formulario:j_id38:0:j_id41:15:j_id46"]').click()

                    # CONTRIBUIÇÃO SOCIAL

                    time.sleep(2)

                    navegador.find_element('xpath','//*[@id="formulario:corrigirDescontoReclamante"]').click()

                    navegador.find_element('xpath','//*[@id="formulario:salvar"]').click()

                    time.sleep(1)

                    navegador.find_element('xpath','//*[@id="formulario:ocorrencias"]').click()

                    time.sleep(1)

                    navegador.find_element('xpath','//*[@id="formulario:tabOcorrenciasSalariosPagos_lbl"]').click()

                    time.sleep(1)

                    navegador.find_element('xpath','//*[@id="formulario:regerar"]').click()

                    time.sleep(1)

                    navegador.find_element('xpath','//*[@id="formulario:aliquotaEmpregador:0"]').click()

                    time.sleep(1)
                    
                    navegador.find_element('xpath','//*[@id="formulario:atividadesEconomicas"]').send_keys(atividade_economica)

                    time.sleep(1)

                    navegador.find_element('xpath','//*[@id="formulario:suggestionautoCompleteAtividades:suggest"]/tbody/tr[1]/td').click()

                    time.sleep(1)

                    if data_inicial_inss != None:
                        navegador.find_element('xpath','//*[@id="formulario:periodoInicialPAGOSInputDate"]').clear()
                        navegador.find_element('xpath','//*[@id="formulario:periodoInicialPAGOSInputDate"]').click()
                        time.sleep(1)
                        navegador.find_element('xpath','//*[@id="formulario:periodoInicialPAGOSInputDate"]').send_keys(data_inicial_inss)
                        time.sleep(1)
                    
                    if data_final_inss != None:
                        navegador.find_element('xpath','//*[@id="formulario:periodoFinalPAGOSInputDate"]').clear()
                        navegador.find_element('xpath','//*[@id="formulario:periodoFinalPAGOSInputDate"]').click()
                        time.sleep(1)
                        navegador.find_element('xpath','//*[@id="formulario:periodoFinalPAGOSInputDate"]').send_keys(data_final_inss)
                        time.sleep(1)
                    
                    if simples_nacional == 'OPTANTE':
                        navegador.find_element('xpath','//*[@id="formulario:dataInicioSimplesInputDate"]').click()
                        navegador.find_element('xpath','//*[@id="formulario:dataInicioSimplesInputDate"]').send_keys(inicio_nacional)
                        navegador.find_element('xpath','//*[@id="formulario:dataTerminoSimplesInputDate"]').click()
                        navegador.find_element('xpath','//*[@id="formulario:dataTerminoSimplesInputDate"]').send_keys(final_nacional)
                        time.sleep(1)
                        navegador.find_element('xpath','//*[@id="formulario:cmdIncluirPeriodoSimples"]').click()

                    navegador.find_element('xpath','//*[@id="formulario:confirmarGeracao"]').click()

                    time.sleep(1)
                    
                    navegador.find_element('xpath','//*[@id="formulario:salvar"]').click()

                    time.sleep(2)

                    navegador.find_element('xpath','//*[@id="formulario:j_id38:0:j_id41:14:j_id46"]').click()
                    
                    # FGTS --- OK

                    time.sleep(1)
                    
                    if fgts == "SIM":
                        navegador.find_element('xpath','//*[@id="formulario:tipoDeVerba:0"]').click()
                    elif fgts == "NÃO":
                        navegador.find_element('xpath','//*[@id="formulario:tipoDeVerba:1"]').click()
                    
                    if multa_fgts == "SIM":
                        navegador.find_element('xpath','//*[@id="formulario:multa"]').click()
                        navegador.find_element('xpath','//*[@id="formulario:multaDoArtigo467"]').click()
                        if aliquota_fgts =="20%":
                            navegador.find_element('xpath','//*[@id="formulario:multaDoFgts:0"]').click()
                        elif aliquota_fgts=="40%":
                            navegador.find_element('xpath','//*[@id="formulario:multaDoFgts:1"]').click()
                        
                    navegador.find_element('xpath','//*[@id="formulario:salvar"]').click()

                    time.sleep(2)

                    navegador.find_element('xpath','//*[@id="formulario:j_id38:0:j_id41:8:j_id46"]').click()

                    # FÉRIAS --- OK
                    
                    time.sleep(1)
                    
                    navegador.find_element('xpath','//*[@id="formulario:arquivo:add1"]').click()

                    time.sleep(15)

                    navegador.find_element('xpath','//*[@id="formulario:j_id96"]').click()

                    navegador.find_element('xpath','//*[@id="formulario:panelBotoes"]/input[2]').click()

                    time.sleep(2)

                    input()
                
                else:
                    print("Código não continuará devido à entrada incorreta.")

            except Exception as e:
                print(f"Ocorreu um erro: {str(e)}")
                input()

automacao().exe