from pjecalc_bibliotecas import *
from pjecalc_funcoes import *
from pjecalc_elementos import *
from pjecalc_variaveis import *

warnings.filterwarnings('ignore', category=UserWarning, module='pandas')

def calculoExterno():

    df_analise_geral, df_analise_decisoes, _ = iniciar_planilhas()
        
# DADOS DO PROCESSO

    def varDadosProcessoCalcExt():
        global sequencia, digito, ano, tribunal, vara, recte, cpf, adv_recte, recda, cnpj, adv_recda,engenheiro,medico

        sequencia = src(df_analise_geral,txt_sequencia,0,1)[0:7]

        digito = src(df_analise_geral,txt_digito,0,1)[8:10]

        ano = src(df_analise_geral,txt_ano,0,1)[11:15]

        tribunal = src(df_analise_geral,txt_tribunal,0,1)[18:20]

        vara =src(df_analise_geral,txt_vara,0,1)[21:25]

        recte = src(df_analise_geral,txt_recte,0,1)

        cpf = src(df_analise_geral,txt_cpf,0,3)

        adv_recte = src(df_analise_geral,txt_adv_recte,0,1)

        recda = src(df_analise_geral,txt_recda,1,1)

        cnpj = src(df_analise_geral,txt_cnpj,1,3)

        adv_recda = src(df_analise_geral,txt_adv_recda,1,1)

# PARÂMETROS DO CÁLCULO
        
    def varParamentrosCalcExt():
        global ultima_remuneracao,indice_trabalhista,segundo_indice_trabalhista,tabela_juros,segunda_tabela_juros,base_juros,fgts,inss,taxa_negativa,custas,index_base_custas,meses_ir,ultima_atualizacao

        ultima_atualizacao = converter_data(primeiro_dia_mes(),'dmy')
        
        ultima_remuneracao = src(df_analise_decisoes,txt_ultima_remuneracao,0,1)

        indice_trabalhista = src(df_analise_decisoes,txt_indice_trabalhista ,0,1)
        
        segundo_indice_trabalhista = src(df_analise_decisoes, txt_segundo_indice_trabalhista,0,4)

        tabela_juros = src(df_analise_decisoes,txt_tabela_juros ,0,1)
        
        segunda_tabela_juros = src(df_analise_decisoes, txt_segunda_tabela_juros,0,4)

        base_juros = src(df_analise_decisoes, txt_base_juros,1,0) 
        base_juros = '0' if base_juros == 'Verbas' else ('1' if base_juros == 'Verba (-) Contribuição Social' else None)

        fgts = src(df_analise_decisoes,txt_fgts ,1,0)

        inss = src(df_analise_decisoes, txt_inss,1,0)
        
        taxa_negativa = txt_taxa_negativa

        custas = src(df_analise_decisoes, txt_custas,1,0)

        index_base_custas = txt_index_base_custas

        meses_ir=txt_meses_ir

# INICIAR NAVEGADOR

    servico = Service(ChromeDriverManager().install())

    navegador = webdriver.Chrome(service=servico)

    navegador.get(link)

    navegador.maximize_window()

    tempo_espera('alteração')
    
# ABERTURA CÁLCULO ATUALIZAÇÃO

    navegador.find_element(*xpath_menu_painel).click()

    tempo_espera('alteração')

    limpar()

    navegador.find_element(*xpath_aba_calculo_externo).click()

    tempo_espera('alteração')

# DADOS DO PROCESSO

    varDadosProcessoCalcExt()

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

    varParamentrosCalcExt()

    navegador.find_element(*xpath_ativar_ultima_atualizacao).click()
    navegador.find_element(*xpath_ultima_atualizacao).send_keys(ultima_atualizacao)

    navegador.find_element(*xpath_indice_trabalhista).send_keys(indice_trabalhista) if segundo_indice_trabalhista == vazio else navegador.find_element(*xpath_indice_trabalhista).send_keys(segundo_indice_trabalhista)

    navegador.find_element(*xpath_taxa_negativa).click() if taxa_negativa == 'SIM' else None

    lista_suspensa = Select(navegador.find_element(*xpath_base_juros))

    lista_suspensa.select_by_index(base_juros)

    navegador.find_element(*xpath_fgts_sim).click() if fgts == 'PAGAR' else (navegador.find_element(*xpath_fgts_nao).click() if fgts == 'RECOLHER' else None)

    navegador.find_element(*xpath_tabela_juros).send_keys(tabela_juros) if segunda_tabela_juros == vazio else navegador.find_element(*xpath_tabela_juros).send_keys(segunda_tabela_juros)

    navegador.find_element(*xpath_inss).click() if inss == 'NÃO' else None

    navegador.find_element(*xpath_meses_ir).send_keys(meses_ir)

    lista_suspensa = Select(navegador.find_element(*xpath_base_custas))

    lista_suspensa.select_by_index(index_base_custas)

    navegador.find_element(*xpath_salvar).click()

# SALVAMENTO        

    tempo_espera('salvar')
    navegador.find_element(*xpath_menu_exportar).click()
    tempo_espera('salvar')
    navegador.find_element(*xpath_aba_exportar).click()
    tempo_espera('salvar')        
    navegador.execute_script(js_exportar)
    tempo_espera('exportar')