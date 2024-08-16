from pjecalc_bibliotecas import *
from pjecalc_funcoes import *
from pjecalc_elementos import *
from pjecalc_variaveis import *

warnings.filterwarnings('ignore', category=UserWarning, module='pandas')

def calculo():

    df_analise_geral, df_analise_decisoes, data = iniciar_planilhas()

# DADOS DO PROCESSO
        
    def var_dados_do_processo():
        global sequencia, digito, ano, tribunal, vara, recte, cpf, adv_recte, recda, cnpj, adv_recda,engenheiro,medico,adv_recda_2,adv_recda_3,adv_recda_4

        sequencia = src(df_analise_geral,txt_sequencia,0,1)[0:7] # OK

        digito = src(df_analise_geral,txt_digito,0,1)[8:10] # OK

        ano = src(df_analise_geral,txt_ano,0,1)[11:15] # OK

        tribunal = src(df_analise_geral,txt_tribunal,0,1)[18:20] # OK

        vara =src(df_analise_geral,txt_vara,0,1)[21:25] # OK

        recte = src(df_analise_geral,txt_recte,0,1) # OK

        cpf = src(df_analise_geral,txt_cpf,0,3) # OK

        adv_recte = src(df_analise_geral,txt_adv_recte,0,1) # OK

        recda = src(df_analise_geral,txt_recda,1,1) # OK

        cnpj = src(df_analise_geral,txt_cnpj,1,3) # OK

        adv_recda = src(df_analise_geral,txt_adv_recda,1,1) # OK

        adv_recda_2 = src(df_analise_geral,txt_adv_recda,0,1)

        adv_recda_3 = src(df_analise_geral,txt_adv_recda,0,1)

        adv_recda_4 = src(df_analise_geral,txt_adv_recda,0,1)

        engenheiro = src(df_analise_geral,txt_engenheiro,0,1) # OK

        medico = src(df_analise_geral,txt_medico,0,1) # OK

# PARÂMETROS DO CÁLCULO

    def var_parametros_do_calculo():
        global estado, municipio, admissao, demissao, ajuizamento, data_inicial, data_final, prescricao, prazo_aviso, oj415, carga_horaria, maior_remuneracao, ultima_remuneracao

        estado = txt_estado # OK

        municipio = src(df_analise_geral,txt_municipio,0,1)[21:25] # OK
        municipio = 'RIBEIRAO PRETO' if municipio in municipio_ribeirao_preto else ('FRANCA' if municipio in municipio_franca else None)

        admissao = converter_data(src(df_analise_geral,txt_admissao,0,1),'dmy') # OK

        demissao = converter_data(src(df_analise_geral,txt_demissao,0,1),'dmy') # OK

        ajuizamento = converter_data(src(df_analise_geral,txt_ajuizamento,0,1),'dmy') # OK

        data_inicial = converter_data(src(df_analise_geral,txt_data_inicial,0,1),'dmy') # OK

        data_final = converter_data(src(df_analise_geral,txt_data_final,0,1),'dmy') # OK

        prescricao = converter_data(src(df_analise_geral,txt_prescricao,0,1)) # OK
        prescricao = 'NÃO' if prescricao in nao_apurar_prescricao else 'SIM'

        prazo_aviso = src(df_analise_geral,txt_prazo_aviso,0,1) # OK
        prazo_aviso = 'NÃO APURAR' if prazo_aviso in valores_nao_apurar_prazo_aviso else prazo_aviso == 'APURAR' 

        oj415 = src(df_analise_decisoes,txt_oj415,0,1) # OK

        carga_horaria = src(df_analise_decisoes,txt_carga_horaria,0,1) # OK

        maior_remuneracao = src(df_analise_decisoes,txt_maior_remuneracao,0,1) # OK

        ultima_remuneracao = src(df_analise_decisoes,txt_ultima_remuneracao,0,1) # OK

# CORREÇÃO, JUROS E MULTA

    def var_correcao_juros_multa():    
        global indice_trabalhista, segundo_indice_trabalhista, data_indice, tabela_juros, segunda_tabela_juros, data_juros, taxa_negativa, pre_juros, base_juros, inss

        indice_trabalhista = src(df_analise_decisoes,txt_indice_trabalhista ,0,1)
        
        segundo_indice_trabalhista = src(df_analise_decisoes, txt_segundo_indice_trabalhista,0,4)
        
        data_indice = converter_data(src(df_analise_decisoes, txt_data_indice,0,3),'dmy')
        
        tabela_juros = src(df_analise_decisoes,txt_tabela_juros ,0,1)
        
        segunda_tabela_juros = src(df_analise_decisoes, txt_segunda_tabela_juros,0,4)
        
        data_juros = converter_data(src(df_analise_decisoes, txt_data_juros,0,3),'dmy')
        
        taxa_negativa = txt_taxa_negativa
        
        pre_juros = src(df_analise_decisoes, txt_pre_juros,1,0)
        
        base_juros = src(df_analise_decisoes, txt_base_juros,1,0) 
        base_juros = '0' if base_juros == 'Verbas' else ('1' if base_juros == 'Verba (-) Contribuição Social' else None)
        
        inss = src(df_analise_decisoes, txt_inss,1,0)
        
# CUSTAS JUDICIAIS

    def var_custas_judiciais():
        global custas, vencimento_custas, valor_custas, index_base_custas

        custas = src(df_analise_decisoes, txt_custas,1,0)

        index_base_custas = txt_index_base_custas

        vencimento_custas = converter_data(src(df_analise_decisoes, txt_vencimento_custas,0,3),'dmy')

        valor_custas = src(df_analise_decisoes, txt_valor_custas,1,0)

# CONTRIBUIÇÃO SOCIAL

    def var_contribuicao_social():
        global correcao_trabalhista, atividade_economica, data_inicial_inss, data_final_inss, simples_nacional, inicio_nacional, final_nacional

        correcao_trabalhista = src(df_analise_decisoes,txt_correcao_trabalhista ,1,0)

        atividade_economica = src(df_analise_geral,txt_atividade_economica ,0,1)

        data_inicial_inss = converter_data(src(df_analise_geral,txt_data_inicial_inss ,0,1),'dmy')

        data_final_inss = converter_data(src(df_analise_geral, txt_data_final_inss,0,1),'dmy')

        simples_nacional = src(df_analise_geral, txt_simples_nacional,0,1)

        inicio_nacional = converter_data(src(df_analise_geral, txt_inicio_nacional,0,1),'my')

        final_nacional = converter_data(src(df_analise_geral, txt_final_nacional,0,1),'my')

# FGTS

    def var_fgts():
        global fgts, multa_fgts, multa_467, incidencia_fgts, excluir_base_sobre_aviso

        fgts = src(df_analise_decisoes,txt_fgts ,1,0)

        multa_fgts = src(df_analise_decisoes,txt_multa_fgts ,1,0)

        multa_467 =src(df_analise_decisoes,txt_multa_467 ,1,0)

        incidencia_fgts = src(df_analise_decisoes,txt_incidencia_fgts ,1,0)

        excluir_base_sobre_aviso = txt_excluir_base_sobre_aviso

# HONORÁRIOS 1º ADV. RECTE.

    def var_honorarios_1_adv_recte():
        global primeiro_adv_recte, vencimento_primeiro_adv_recte, valor_primeiro_adv_recte, tipo_primeiro_adv_recte, vencimento_juros_primeiro_adv_recte

        primeiro_adv_recte = src(df_analise_decisoes,txt_primeiro_adv_recte ,1,0)
        
        vencimento_primeiro_adv_recte = converter_data(src(df_analise_geral, txt_vencimento_primeiro_adv_recte,0,1),'dmy')
        
        valor_primeiro_adv_recte = src(df_analise_decisoes,txt_valor_primeiro_adv_recte ,1,1)
        
        tipo_primeiro_adv_recte = 'INFORMADO' if identificar_tipo(valor_primeiro_adv_recte) == 'INFORMADO' else 'CALCULADO' if identificar_tipo(valor_primeiro_adv_recte) == 'CALCULADO' else tipo_primeiro_adv_recte
        
        vencimento_juros_primeiro_adv_recte = converter_data(src(df_analise_geral,txt_vencimento_juros_primeiro_adv_recte ,0,1),'dmy')
               
               
# HONORÁRIOS 1º ADV. RECDA.
        
    def var_honorarios_1_adv_recda():   
        global primeira_adv_recda, vencimento_primeira_adv_recda, valor_primeira_adv_recda, exigibilidade_primeira_adv_recda, tipo_primeira_adv_recda, vencimento_juros_primeira_adv_recda

        primeira_adv_recda = src(df_analise_decisoes,txt_primeira_adv_recda ,1,0)

        vencimento_primeira_adv_recda = converter_data(src(df_analise_geral, txt_vencimento_primeira_adv_recda,0,1),'dmy')

        valor_primeira_adv_recda = src(df_analise_decisoes,txt_valor_primeira_adv_recda ,1,1)

        exigibilidade_primeira_adv_recda = src(df_analise_decisoes,txt_exigibilidade_primeira_adv_recda ,1,2)

        tipo_primeira_adv_recda = 'INFORMADO' if identificar_tipo(valor_primeira_adv_recda) == 'INFORMADO' else 'CALCULADO' if identificar_tipo(valor_primeira_adv_recda) == 'CALCULADO' else tipo_primeira_adv_recda

        vencimento_juros_primeira_adv_recda = converter_data(src(df_analise_geral, txt_vencimento_juros_primeira_adv_recda,0,1),'dmy')

# HONORÁRIOS 2º ADV. RECDA.
        
    def var_honorarios_2_adv_recda():
        global segunda_adv_recda, vencimento_segunda_adv_recda, valor_segunda_adv_recda, exigibilidade_segunda_adv_recda, tipo_segunda_adv_recda, vencimento_juros_segunda_adv_recda

        segunda_adv_recda = src(df_analise_decisoes,txt_segunda_adv_recda ,2,0)

        vencimento_segunda_adv_recda = converter_data(src(df_analise_geral, txt_vencimento_segunda_adv_recda,0,1),'dmy')

        valor_segunda_adv_recda = src(df_analise_decisoes,txt_valor_segunda_adv_recda ,2,1)

        exigibilidade_segunda_adv_recda = src(df_analise_decisoes,txt_exigibilidade_segunda_adv_recda ,2,2)

        tipo_segunda_adv_recda = 'INFORMADO' if identificar_tipo(valor_segunda_adv_recda) == 'INFORMADO' else 'CALCULADO' if identificar_tipo(valor_segunda_adv_recda) == 'CALCULADO' else tipo_segunda_adv_recda

        vencimento_juros_segunda_adv_recda = converter_data(src(df_analise_geral, txt_vencimento_juros_segunda_adv_recda,0,1),'dmy')

# HONORÁRIOS 3º ADV. RECDA.
        
    def var_honorarios_3_adv_recda():
        global terceira_adv_recda, vencimento_terceira_adv_recda, valor_terceira_adv_recda, exigibilidade_terceira_adv_recda, tipo_terceira_adv_recda, vencimento_juros_terceira_adv_recda

        terceira_adv_recda = src(df_analise_decisoes,txt_terceira_adv_recda ,3,0)

        vencimento_terceira_adv_recda = converter_data(src(df_analise_geral, txt_vencimento_terceira_adv_recda,0,1),'dmy')

        valor_terceira_adv_recda = src(df_analise_decisoes,txt_valor_terceira_adv_recda ,3,1)

        exigibilidade_terceira_adv_recda = src(df_analise_decisoes,txt_exigibilidade_terceira_adv_recda ,3,2)

        tipo_terceira_adv_recda = 'INFORMADO' if identificar_tipo(valor_terceira_adv_recda) == 'INFORMADO' else 'CALCULADO' if identificar_tipo(valor_terceira_adv_recda) == 'CALCULADO' else tipo_terceira_adv_recda

        vencimento_juros_terceira_adv_recda = converter_data(src(df_analise_geral, txt_vencimento_juros_terceira_adv_recda,0,1),'dmy')

# HONORÁRIOS 4º ADV. RECDA.
        
    def var_honorarios_4_adv_recda():
        global quarta_adv_recda, vencimento_quarta_adv_recda, valor_quarta_adv_recda, exigibilidade_quarta_adv_recda, tipo_quarta_adv_recda, vencimento_juros_quarta_adv_recda

        quarta_adv_recda = src(df_analise_decisoes,txt_quarta_adv_recda ,4,0)

        vencimento_quarta_adv_recda =converter_data(src(df_analise_geral, txt_vencimento_quarta_adv_recda,0,1),'dmy')

        valor_quarta_adv_recda = src(df_analise_decisoes,txt_valor_quarta_adv_recda ,4,1)

        exigibilidade_quarta_adv_recda = src(df_analise_decisoes,txt_exigibilidade_quarta_adv_recda ,4,2)

        tipo_quarta_adv_recda = 'INFORMADO' if identificar_tipo(vencimento_quarta_adv_recda) == 'INFORMADO' else 'CALCULADO' if identificar_tipo(vencimento_quarta_adv_recda) == 'CALCULADO' else tipo_quarta_adv_recda

        vencimento_juros_quarta_adv_recda =converter_data(src(df_analise_geral, txt_vencimento_juros_quarta_adv_recda,0,1),'dmy')

# HONORÁRIOS PERITO CONTÁBIL
         
    def var_honorarios_perito_contabil():
        global perito_contabil, vencimento_perito_contabil, valor_perito_contabil, tipo_perito_contabil, apurar_honorario_perito

        apurar_honorario_perito = src(df_analise_decisoes,txt_apurar_honorario_perito ,1,0)

        perito_contabil = txt_perito_contabil

        vencimento_perito_contabil = converter_data(primeiro_dia_mes(),'dmy')

        valor_perito_contabil = txt_valor_perito_contabil

        tipo_perito_contabil = 'INFORMADO' if identificar_tipo(valor_perito_contabil) == 'INFORMADO' else 'CALCULADO' if identificar_tipo(valor_perito_contabil) == 'CALCULADO' else tipo_perito_contabil

# HONORÁRIOS ENGENHEIRO
        
    def var_honorarios_engenheiro():
        global vencimento_engenheiro, valor_engenheiro, tipo_engenheiro

        vencimento_engenheiro = converter_data(src(df_analise_decisoes,txt_vencimento_engenheiro ,0,3),'dmy')

        valor_engenheiro = src(df_analise_decisoes,txt_valor_engenheiro ,0,1)

        tipo_engenheiro = 'INFORMADO' if identificar_tipo(valor_engenheiro) == 'INFORMADO' else 'CALCULADO' if identificar_tipo(valor_engenheiro) == 'CALCULADO' else tipo_engenheiro

# HONORÁRIOS MÉDICO
        
    def var_honorarios_medico():
        global vencimento_medico, valor_medico, tipo_medico

        vencimento_medico = converter_data(src(df_analise_decisoes,txt_vencimento_medico ,0,3),'dmy')

        valor_medico = src(df_analise_decisoes,txt_valor_medico ,0,1)

        tipo_medico = 'INFORMADO' if identificar_tipo(valor_medico) == 'INFORMADO' else 'CALCULADO' if identificar_tipo(valor_medico) == 'CALCULADO' else tipo_medico

# INICIAR NAVEGADOR
    
    servico = Service(ChromeDriverManager().install())
    
    navegador = webdriver.Chrome(service=servico)
    
    navegador.get(link)
    
    navegador.maximize_window()
    
    tempo_espera('alteração')
    
    navegador.find_element(*xpath_botao_calculo).click()
    
    tempo_espera('alteração')
    
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
  
    (lambda:(
        navegador.find_element(*xpath_adv_recte).send_keys(adv_recte),
        navegador.find_element(*xpath_enviar_adv_recte).click()
    )if adv_recte != None else None)()

    navegador.find_element(*xpath_reclamada).send_keys(recda)
    
    navegador.find_element(*xpath_selecionar_cnpj).click()
    
    navegador.find_element(*xpath_cnpj).click()
    
    navegador.find_element(*xpath_cnpj).send_keys(cnpj)

    (lambda:(
        navegador.find_element(*xpath_adv_recda).send_keys(adv_recda),
        navegador.find_element(*xpath_enviar_adv_recda).click()
    )if adv_recda != None else None)()
    
    navegador.find_element(*xpath_aba_parametros).click()
    
    tempo_espera('alteração')

# PARÂMETROS DO CÁLCULO

    var_parametros_do_calculo()
    navegador.find_element(*xpath_estado).send_keys(estado)
    
    tempo_espera('alteração') 
    
    navegador.find_element(*xpath_municipio).send_keys(municipio)
    
    tempo_espera('alteração')
    
    navegador.find_element(*xpath_admissao).click()
    
    navegador.find_element(*xpath_admissao).send_keys(admissao) if admissao is not None else None

    (lambda: (
        navegador.find_element(*xpath_data_final).click(),
        navegador.find_element(*xpath_data_final).send_keys(data_final)
    ) if demissao == None else (
        navegador.find_element(*xpath_demissao).click(),
        navegador.find_element(*xpath_demissao).send_keys(demissao)))()

    navegador.find_element(*xpath_ajuizamento).click()
    
    navegador.find_element(*xpath_ajuizamento).send_keys(ajuizamento)
    
    (lambda: (
        navegador.find_element(*xpath_data_inicial).click(),
        navegador.find_element(*xpath_data_inicial).send_keys(data_inicial) if data_inicial is not None else None
    ) if data_inicial != None else None)()

    (lambda: (
        navegador.find_element(*xpath_data_final).click(),
        navegador.find_element(*xpath_data_final).send_keys(data_final) if data_final is not None else None
    ) if data_final != None else None)()
 
    navegador.find_element(*xpath_prescricao).click() if prescricao == 'SIM' else None
    
    navegador.find_element(*xpath_aviso_previo).send_keys(prazo_aviso)
    
    navegador.find_element(*xpath_projetar_aviso).click() if prazo_aviso == 'NÃO APURAR' else None
    
    navegador.find_element(*xpath_oj415).click() if oj415 == 'SIM' else None   
        
    (lambda: (
        navegador.find_element(*xpath_ultima_remuneracao).click(),
        navegador.find_element(*xpath_ultima_remuneracao).send_keys(criarDecimal(ultima_remuneracao))
    ) if ultima_remuneracao != None else None)()

    (lambda: (
        navegador.find_element(*xpath_maior_remuneracao).click(),
        navegador.find_element(*xpath_maior_remuneracao).send_keys(criarDecimal(maior_remuneracao))
    ) if maior_remuneracao != None else None)()

    (lambda: (
        navegador.find_element(*xpath_carga_horaria).click(),
        navegador.find_element(*xpath_carga_horaria).send_keys(criarDecimal(carga_horaria))
    ) if carga_horaria != None else None)()
    
    navegador.find_element(*xpath_ponto_facultativo).click()
    
    navegador.find_element(*xpath_salvar).click()
    
    tempo_espera('alteração')

# CORREÇÃO, JUROS E MULTA

    if data['Correção, Juros e Multa']:
        
        var_correcao_juros_multa()
        navegador.find_element(*xpath_aba_inss).click()
        
        tempo_espera('alteração')
        
        navegador.find_element(*xpath_indice_trabalhista).send_keys(indice_trabalhista)
        
        tempo_espera('alteração')
        
        (lambda:(
            navegador.find_element(*xpath_ativar_segundo_indice).click(),
            tempo_espera('alteração'),
            navegador.find_element(*xpath_segundo_indice).send_keys(segundo_indice_trabalhista),
            navegador.find_element(*xpath_data_segundo_indice).click(),
            navegador.find_element(*xpath_data_segundo_indice).send_keys(data_indice),
            navegador.find_element(*xpath_add_data_segundo_indice).click(),
            tempo_espera('alteração')
        )if segundo_indice_trabalhista != None else None)()
                
        navegador.find_element(*xpath_taxa_negativa).click() if taxa_negativa == 'SIM' else None
        
        (lambda:(
            navegador.find_element(*xpath_remover_juros).click(),
            tempo_espera('alteração'),
            navegador.find_element(*xpath_tabela_juros).send_keys(tabela_juros),
            navegador.find_element(*xpath_ativar_segundo_juros).click(),
            tempo_espera('alteração'),
            navegador.find_element(*xpath_segundo_juros).send_keys(segunda_tabela_juros),
            navegador.find_element(*xpath_data_segundo_juros).click(),
            navegador.find_element(*xpath_data_segundo_juros).send_keys(data_juros),
            navegador.find_element(*xpath_add_data_segundo_juros).click(),
            tempo_espera('alteração')
        )if pre_juros == 'SIM' else(
            navegador.find_element(*xpath_juros_pre).click(),
            tempo_espera('alteração'),
            navegador.find_element(*xpath_tabela_juros).send_keys(tabela_juros)
        ))()  

# DADOS ESPECÍFICOS

        navegador.find_element(*xpath_aba_dados_especificos).click()
        
        tempo_espera('salvar')
        
        lista_suspensa = Select(navegador.find_element(*xpath_base_juros))
        
        lista_suspensa.select_by_index(base_juros)
        
        tempo_espera('alteração')
        
        navegador.find_element(*xpath_inss).click() if inss in nao_apurar_inss else None
        
        navegador.find_element(*xpath_salvar).click()
        
        tempo_espera('alteração')
        
    else: 
        pass              

# CUSTAS JUDICIAIS

    if data['Custas Judiciais']:
        var_custas_judiciais()
        navegador.find_element(*xpath_aba_custas).click()
        
        tempo_espera('salvar')
        
        lista_suspensa = Select(navegador.find_element(*xpath_base_custas))
        
        lista_suspensa.select_by_index(index_base_custas)
        
        tempo_espera('alteração')
        
        (lambda:(
            navegador.find_element(*xpath_ativar_custas).click(),
            tempo_espera('alteração'),
            navegador.find_element(*xpath_data_custas).click(),
            tempo_espera('alteração'),
            navegador.find_element(*xpath_data_custas).send_keys(vencimento_custas),
            navegador.find_element(*xpath_valor_custas).send_keys(criarDecimal(valor_custas))
        )if valor_monetario(custas) else (
            navegador.find_element(*xpath_custas_devido).click()))()
        
        navegador.find_element(*xpath_salvar).click()
        
        tempo_espera('alteração')
    
    else: 
        pass     

# HONORÁRIOS

    if data['Honorários']:
    
        navegador.find_element(*xpath_aba_honorarios).click()
        tempo_espera('salvar')
        var_honorarios_1_adv_recte()
        var_honorarios_1_adv_recda()
        var_honorarios_2_adv_recda()
        var_honorarios_3_adv_recda()
        var_honorarios_4_adv_recda()
    
# HONORÁRIOS 1º ADV. RECTE.

        if primeiro_adv_recte is not None and adv_recte is not None and valor_primeiro_adv_recte != "INDEVIDO":

            navegador.find_element(*xpath_novo_honorario).click()
        
            tempo_espera('alteração')
        
            lista_suspensa = Select(navegador.find_element(*xpath_tipo_honorario))
        
            lista_suspensa.select_by_index(9)
        
            tempo_espera('alteração')
        
            navegador.find_element(*xpath_tipo_devedor_reclamado).click()
        
            tempo_espera('alteração')
        
            if tipo_primeiro_adv_recte == 'INFORMADO':
        
                navegador.find_element(*xpath_valor_informado).click()
        
                navegador.find_element(*xpath_data_honorario).send_keys(vencimento_primeiro_adv_recte)
        
                navegador.find_element(*xpath_valor_honorario).send_keys(criarDecimal(valor_primeiro_adv_recte))

                navegador.find_element(*xpath_juros_honorario).click()
                    
                navegador.find_element(*xpath_data_juros_honorario).send_keys(vencimento_juros_primeiro_adv_recte)
                    
                tempo_espera('alteração')
        
            elif tipo_primeiro_adv_recte == 'CALCULADO':
        
                navegador.find_element(*xpath_aliquota_honorario).send_keys(str(Decimal(valor_primeiro_adv_recte) * Decimal('100')))
        
                lista_suspensa = Select(navegador.find_element(*xpath_base_honorario))

                lista_suspensa.select_by_index(1)
        
                tempo_espera('alteração')
        
            navegador.find_element(*xpath_nome_honorario).send_keys(f'{primeiro_adv_recte} [ADV.RECTE.]')
               
            navegador.find_element(*xpath_salvar).click()
        
            tempo_espera('alteração')       

# HONORÁRIOS 1º ADV. RECDA.
            
        if (primeira_adv_recda is not None or adv_recda is not None) and not (exigibilidade_primeira_adv_recda == 'SUSPENSA' and municipio == 'RIBEIRAO PRETO') and valor_primeira_adv_recda != "INDEVIDO":

            tempo_espera('alteração')
        
            navegador.find_element(*xpath_novo_honorario).click()
        
            tempo_espera('alteração')
        
            lista_suspensa = Select(navegador.find_element(*xpath_tipo_honorario))
        
            lista_suspensa.select_by_index(9)
        
            navegador.find_element(*xpath_tipo_devedor_reclamante).click()
        
            tempo_espera('alteração')
        
            if exigibilidade_primeira_adv_recda == 'SUSPENSA':
        
                navegador.find_element(*xpath_cobrar_honorario).click()
        
            if tipo_primeira_adv_recda == 'INFORMADO':
        
                navegador.find_element(*xpath_valor_informado).click()
        
                tempo_espera('alteração')
        
                navegador.find_element(*xpath_data_honorario).click()
        
                navegador.find_element(*xpath_data_honorario).send_keys(vencimento_primeira_adv_recda)
        
                tempo_espera('alteração')
        
                navegador.find_element(*xpath_valor_honorario).send_keys(criarDecimal(valor_primeira_adv_recda))
        
                navegador.find_element(*xpath_juros_honorario).click()
                    
                navegador.find_element(*xpath_juros_honorario).click()

                navegador.find_element(*xpath_data_juros_honorario).send_keys(vencimento_juros_primeira_adv_recda)

                tempo_espera('alteração')
        
            elif tipo_primeira_adv_recda == 'CALCULADO':
        
                navegador.find_element(*xpath_aliquota_honorario).send_keys(str(Decimal(valor_primeira_adv_recda) * Decimal('100')))
        
                lista_suspensa = Select(navegador.find_element(*xpath_base_honorario))
        
                lista_suspensa.select_by_index(1)
        
            navegador.find_element(*xpath_nome_honorario).send_keys(f'{primeira_adv_recda} [ADV.RECDA.]')      
        
            navegador.find_element(*xpath_salvar).click()                
                    
            tempo_espera('alteração')
    
# HONORÁRIOS 2º ADV. RECDA.
            
        if (segunda_adv_recda is not None or adv_recda_2 is not None) and not (exigibilidade_segunda_adv_recda == 'SUSPENSA' and municipio == 'RIBEIRAO PRETO') and valor_segunda_adv_recda != "INDEVIDO":
        
            tempo_espera('alteração')
        
            navegador.find_element(*xpath_novo_honorario).click()
        
            tempo_espera('alteração')
        
            lista_suspensa = Select(navegador.find_element(*xpath_tipo_honorario))
        
            lista_suspensa.select_by_index(9)
        
            navegador.find_element(*xpath_tipo_devedor_reclamante).click()
        
            tempo_espera('alteração')
        
            if exigibilidade_segunda_adv_recda == 'SUSPENSA':
        
                navegador.find_element(*xpath_cobrar_honorario).click()
        
            if tipo_segunda_adv_recda == 'INFORMADO':
        
                navegador.find_element(*xpath_valor_informado).click()
        
                tempo_espera('alteração')
        
                navegador.find_element(*xpath_data_honorario).click()
        
                navegador.find_element(*xpath_data_honorario).send_keys(vencimento_segunda_adv_recda)
        
                tempo_espera('alteração')
        
                navegador.find_element(*xpath_valor_honorario).send_keys(criarDecimal(valor_segunda_adv_recda))
        
                navegador.find_element(*xpath_juros_honorario).click()
                    
                navegador.find_element(*xpath_juros_honorario).click()

                navegador.find_element(*xpath_data_juros_honorario).send_keys(vencimento_juros_segunda_adv_recda)

                tempo_espera('alteração')
        
            elif tipo_segunda_adv_recda == 'CALCULADO':
        
                navegador.find_element(*xpath_aliquota_honorario).send_keys(str(Decimal(valor_segunda_adv_recda) * Decimal('100')))
        
                lista_suspensa = Select(navegador.find_element(*xpath_base_honorario))
        
                lista_suspensa.select_by_index(1)
        
            navegador.find_element(*xpath_nome_honorario).send_keys(f'{segunda_adv_recda} [ADV. 2ª RECDA.]')
        
            navegador.find_element(*xpath_salvar).click()                
                    
            tempo_espera('alteração')
            
# HONORÁRIOS 3º ADV. RECDA.
            
        if (terceira_adv_recda is not None or adv_recda_3 is not None) and not (exigibilidade_terceira_adv_recda == 'SUSPENSA' and municipio == 'RIBEIRAO PRETO') and valor_terceira_adv_recda != "INDEVIDO":
        
            tempo_espera('alteração')
        
            navegador.find_element(*xpath_novo_honorario).click()
        
            tempo_espera('alteração')
        
            lista_suspensa = Select(navegador.find_element(*xpath_tipo_honorario))
        
            lista_suspensa.select_by_index(9)
        
            navegador.find_element(*xpath_tipo_devedor_reclamante).click()
        
            tempo_espera('alteração')
        
            if exigibilidade_terceira_adv_recda == 'SUSPENSA':
        
                navegador.find_element(*xpath_cobrar_honorario).click()
        
            if tipo_terceira_adv_recda == 'INFORMADO':
        
                navegador.find_element(*xpath_valor_informado).click()
        
                tempo_espera('alteração')
        
                navegador.find_element(*xpath_data_honorario).click()
        
                navegador.find_element(*xpath_data_honorario).send_keys(vencimento_terceira_adv_recda)
        
                tempo_espera('alteração')
        
                navegador.find_element(*xpath_valor_honorario).send_keys(criarDecimal(valor_terceira_adv_recda))
        
                navegador.find_element(*xpath_juros_honorario).click()

                navegador.find_element(*xpath_juros_honorario).click()

                navegador.find_element(*xpath_data_juros_honorario).send_keys(vencimento_juros_terceira_adv_recda)

                tempo_espera('alteração')
        
            elif tipo_terceira_adv_recda == 'CALCULADO':
        
                navegador.find_element(*xpath_aliquota_honorario).send_keys(valor_terceira_adv_recda)
        
                lista_suspensa = Select(navegador.find_element(*xpath_base_honorario))
        
                lista_suspensa.select_by_index(1)
        
            navegador.find_element(*xpath_nome_honorario).send_keys(f'{terceira_adv_recda} [ADV. 3ª RECDA.]')
        
            navegador.find_element(*xpath_salvar).click()                
                    
            tempo_espera('alteração')

# HONORÁRIOS 4º ADV. RECDA.
            
        if (quarta_adv_recda is not None or adv_recda_4 is not None) and not (exigibilidade_quarta_adv_recda == 'SUSPENSA' and municipio == 'RIBEIRAO PRETO') and valor_quarta_adv_recda != "INDEVIDO":
            
            tempo_espera('alteração')
        
            navegador.find_element(*xpath_novo_honorario).click()
        
            tempo_espera('alteração')
        
            lista_suspensa = Select(navegador.find_element(*xpath_tipo_honorario))
        
            lista_suspensa.select_by_index(9)
        
            navegador.find_element(*xpath_tipo_devedor_reclamante).click()
        
            tempo_espera('alteração')
        
            if exigibilidade_quarta_adv_recda == 'SUSPENSA':
        
                navegador.find_element(*xpath_cobrar_honorario).click()
        
            if tipo_quarta_adv_recda == 'INFORMADO':
        
                navegador.find_element(*xpath_valor_informado).click()
        
                tempo_espera('alteração')
        
                navegador.find_element(*xpath_data_honorario).click()
        
                navegador.find_element(*xpath_data_honorario).send_keys(vencimento_quarta_adv_recda)
        
                tempo_espera('alteração')
        
                navegador.find_element(*xpath_valor_honorario).send_keys(criarDecimal(valor_quarta_adv_recda))
        
                navegador.find_element(*xpath_juros_honorario).click()
        
                tempo_espera('alteração')
        
                navegador.find_element(*xpath_juros_honorario).click()

                navegador.find_element(*xpath_data_juros_honorario).send_keys(vencimento_juros_quarta_adv_recda)

                tempo_espera('alteração')
        
            elif tipo_quarta_adv_recda == 'CALCULADO':
        
                navegador.find_element(*xpath_aliquota_honorario).send_keys(str(Decimal(valor_quarta_adv_recda) * Decimal('100')))
        
                lista_suspensa = Select(navegador.find_element(*xpath_base_honorario))
        
                lista_suspensa.select_by_index(1)
        
            navegador.find_element(*xpath_nome_honorario).send_keys(f'{quarta_adv_recda} [ADV. 4ª RECDA.]')         
        
            navegador.find_element(*xpath_salvar).click()                
                    
            tempo_espera('alteração')

# HONORÁRIOS PERITO CONTÁBIL
            
        if apurar_honorario_perito == 'SIM':

            var_honorarios_perito_contabil()
        
            navegador.find_element(*xpath_novo_honorario).click()
        
            tempo_espera('alteração')
        
            lista_suspensa = Select(navegador.find_element(*xpath_tipo_honorario))
        
            lista_suspensa.select_by_index(3)
        
            navegador.find_element(*xpath_tipo_devedor_reclamado).click()
        
            if tipo_perito_contabil == 'INFORMADO':
        
                navegador.find_element(*xpath_valor_informado).click()
        
                tempo_espera('alteração')
        
                navegador.find_element(*xpath_data_honorario).click()
        
                navegador.find_element(*xpath_data_honorario).send_keys(vencimento_perito_contabil)
        
                tempo_espera('alteração')
        
                navegador.find_element(*xpath_valor_honorario).send_keys(criarDecimal(valor_perito_contabil))
        
            elif tipo_perito_contabil == 'CALCULADO':
        
                navegador.find_element(*xpath_aliquota_honorario).send_keys(str(Decimal(valor_perito_contabil) * Decimal('100')))
        
                lista_suspensa = Select(navegador.find_element(*xpath_base_honorario))
        
                lista_suspensa.select_by_index(1)
        
            navegador.find_element(*xpath_nome_honorario).send_keys(perito_contabil)              
        
            navegador.find_element(*xpath_salvar).click()
        
            tempo_espera('alteração')

# HONORÁRIOS ENGENHEIRO
        
        if engenheiro is not None and (valor_engenheiro != "INDEVIDO" and valor_engenheiro != "JUSTIÇA GRATUITA"):

            var_honorarios_engenheiro()
        
            navegador.find_element(*xpath_novo_honorario).click()
        
            tempo_espera('alteração')
        
            lista_suspensa = Select(navegador.find_element(*xpath_tipo_honorario))
        
            lista_suspensa.select_by_index(3)
        
            navegador.find_element(*xpath_tipo_devedor_reclamado).click()
        
            if tipo_engenheiro == 'INFORMADO':
        
                navegador.find_element(*xpath_valor_informado).click()
        
                tempo_espera('alteração')
        
                navegador.find_element(*xpath_data_honorario).click()
        
                navegador.find_element(*xpath_data_honorario).send_keys(vencimento_engenheiro)
        
                tempo_espera('alteração')
        
                navegador.find_element(*xpath_valor_honorario).send_keys(criarDecimal(valor_engenheiro))
        
            elif tipo_engenheiro == 'CALCULADO':
        
                navegador.find_element(*xpath_aliquota_honorario).send_keys(str(Decimal(valor_engenheiro) * Decimal('100')))
        
                lista_suspensa = Select(navegador.find_element(*xpath_base_honorario))
        
                lista_suspensa.select_by_index(1)
        
            navegador.find_element(*xpath_nome_honorario).send_keys(engenheiro)                
        
            navegador.find_element(*xpath_salvar).click()
        
            tempo_espera('alteração')

# HONORÁRIOS MÉDICO
            
        if medico is not None and (valor_medico != "INDEVIDO" and valor_medico != "JUSTIÇA GRATUITA"):
                   
            var_honorarios_medico()

            navegador.find_element(*xpath_novo_honorario).click()
        
            tempo_espera('alteração')
        
            lista_suspensa = Select(navegador.find_element(*xpath_tipo_honorario))
        
            lista_suspensa.select_by_index(3)
        
            navegador.find_element(*xpath_tipo_devedor_reclamado).click()
        
            if tipo_medico == 'INFORMADO':
        
                navegador.find_element(*xpath_valor_informado).click()
        
                tempo_espera('alteração')
        
                navegador.find_element(*xpath_data_honorario).click()
        
                navegador.find_element(*xpath_data_honorario).send_keys(vencimento_medico)
        
                tempo_espera('alteração')
        
                navegador.find_element(*xpath_valor_honorario).send_keys(criarDecimal(valor_medico))
        
            elif tipo_medico == 'CALCULADO':
        
                navegador.find_element(*xpath_aliquota_honorario).send_keys(str(Decimal(valor_medico) * Decimal('100')))
        
                lista_suspensa = Select(navegador.find_element(*xpath_base_honorario))
        
                lista_suspensa.select_by_index(1)
        
            navegador.find_element(*xpath_nome_honorario).send_keys(medico)

            navegador.find_element(*xpath_salvar).click()
        
            tempo_espera('alteração')

    else: 
        pass               
        
# MULTAS E INDENIZAÇÕES

    if data['Multas e Indenizações']:
        navegador.find_element(*xpath_aba_multas).click()
        tempo_espera('alteração')
    else: 
        pass           

# IMPOSTO DE RENDA

    if data['Imposto de Renda']:
        navegador.find_element(*xpath_aba_ir).click()
        tempo_espera('alteração')            
    else: 
        pass    

# PENSÃO ALIMENTÍCIA

    if data['Pensão Alimentícia']:
        navegador.find_element(*xpath_pensao_alimenticia).click()
        tempo_espera('alteração')    
    else: 
        pass            

# PREVIDÊNCIA PRIVADA

    if data['Previdência Privada']:
        navegador.find_element(*xpath_previdencia_privada).click()
        tempo_espera('alteração')   
    else: 
        pass             

# CONTRIBUIÇÃO SOCIAL

    if data['Contribuição Social']:
        var_contribuicao_social()
    
        navegador.find_element(*xpath_contribuicao_social).click()
        tempo_espera('salvar')
        
        navegador.find_element(*xpath_correcao_trabalhista).click() if correcao_trabalhista =='SIM' else None
            
        navegador.find_element(*xpath_salvar).click()
        
        tempo_espera('alteração')
        
        navegador.find_element(*xpath_ocorrencias_inss).click()
        
        tempo_espera('alteração')
        
        navegador.find_element(*xpath_aba_salarios_pagos).click()
        
        tempo_espera('alteração')
        
        navegador.find_element(*xpath_regerar_inss).click()
        
        tempo_espera('alteração')
        
        navegador.find_element(*xpath_ativar_atividade_economica).click()
        
        tempo_espera('alteração')
        
        navegador.find_element(*xpath_atividade_economica).send_keys(atividade_economica)
        
        tempo_espera('alteração')
        
        (lambda:(
            navegador.find_element(*xpath_aliquota_fixa).click(),
            print(''),
            print('ATENÇÃO! - A Atividade Econômica não foi encontrada!'),
            tempo_espera('alteração')
        )if navegador.find_elements(*xpath_erro_atividade_economica) else (
            navegador.find_element(*xpath_selecionar_atividade_economica).click()))()

        (lambda:(
            navegador.find_element(*xpath_inicio_inss).clear(),
            navegador.find_element(*xpath_inicio_inss).click(),
            tempo_espera('alteração'),
            navegador.find_element(*xpath_inicio_inss).send_keys(data_inicial_inss),
            tempo_espera('alteração')
        )if data_inicial_inss != None else None)()

        (lambda:(
            navegador.find_element(*xpath_final_inss).clear(),
            navegador.find_element(*xpath_final_inss).click(),
            tempo_espera('alteração'),
            navegador.find_element(*xpath_final_inss).send_keys(data_final_inss),
            tempo_espera('alteração')
        )if data_final_inss != None and demissao == None else None)()
        
        (lambda:(
            navegador.find_element(*xpath_inicio_simples).click(),
            navegador.find_element(*xpath_inicio_simples).send_keys(inicio_nacional),
            navegador.find_element(xpath_final_simples).click(),
            navegador.find_element(xpath_final_simples).send_keys(final_nacional),
            tempo_espera('alteração'),
            navegador.find_element(*xpath_adicionar_simples).click()
        )if simples_nacional == 'OPTANTE' else None)()

        navegador.find_element(*xpath_confirmar_inss).click()
        
        tempo_espera('alteração')

        navegador.find_element(*xpath_salvar).click()
        
        tempo_espera('salvar')
    else: 
        pass   
        
# FGTS

    if data['FGTS']:
        var_fgts()
        navegador.find_element(*xpath_aba_fgts).click()
        tempo_espera('salvar')

        navegador.find_element(*xpath_fgts_sim).click() if fgts == 'PAGAR' else navegador.find_element(*xpath_fgts_nao).click()

        if multa_fgts == 'SIM':
            navegador.find_element(*xpath_fgts_multa).click()
            tempo_espera('alteração')

            navegador.find_element(*xpath_fgts_multa_40).click()
            tempo_espera('alteração')

            navegador.find_element(*xpath_excluir_base_sobre_aviso).click()
            tempo_espera('alteração')

            (lambda:(
                navegador.find_element(*xpath_fgts_multa_467).click(),
                Select(navegador.find_element(*xpath_incidencia_fgts)).select_by_value(incidencia_fgts),
            )if multa_467 == 'SIM' else None)()
                      
        tempo_espera('salvar')
        navegador.find_element(*xpath_salvar).click()
        
        tempo_espera('salvar')
    else: 
        pass   

# SEGURO-DESEMPREGO

    if data['Seguro-desemprego']:
        navegador.find_element(*xpath_aba_seguro_desemprego).click()
        tempo_espera('alteração')   
    else: 
        pass              

# SALÁRIO-FAMÍLIA

    if data['Salário-família']:
        navegador.find_element(*xpath_aba_salario_familia).click()
        tempo_espera('alteração')
    else: 
        pass   

# CARTÃO DE PONTO

    if data['Cartão de Ponto']:
        navegador.find_element(*xpath_aba_cartao_ponto).click()
        tempo_espera('alteração') 
    else: 
        pass             

# VERBAS

    if data['Verbas']:
        navegador.find_element(*xpath_aba_verbas).click()
        tempo_espera('alteração')   
    else: 
        pass            

# HISTÓRICO SALARIAL

    if data['Histórico Salarial']:
        navegador.find_element(*xpath_historico_salarial).click()
        tempo_espera('alteração')    
    else: 
        pass         

# FÉRIAS

    if data['Férias']:

        navegador.find_element(*xpath_aba_ferias).click()

        tempo_espera('alteração')

        navegador.find_element(*xpath_adicionar_ferias).click()

        WebDriverWait(navegador,20).until(EC.visibility_of_element_located(*xpath_erro_ferias))

        navegador.find_element(*xpath_confirmar_ferias).click()

        tempo_espera('alteração')

        navegador.find_element(*xpath_salvar).click()
    else: 
        pass   

# FALTAS

    if data['Faltas']:
        navegador.find_element(*xpath_aba_faltas).click()
        tempo_espera('alteração')      
    else: 
        pass            

# SALVAMENTO

    tempo_espera('salvar')
    try:
        navegador.find_element(*xpath_menu_exportar).click()
    except NoSuchElementException:
        tempo_espera('salvar')
        navegador.find_element(*xpath_menu_exportar).click()
    tempo_espera('salvar')
    navegador.find_element(*xpath_aba_exportar).click()
    tempo_espera('salvar')        
    navegador.execute_script(js_exportar)
    tempo_espera('exportar')