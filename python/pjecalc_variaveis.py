from pjecalc_bibliotecas import *

# VARIÁVEIS - EXCEL

# GERAIS

vazio = '###'
txt_meses_ir = 0

# DADOS DO PROCESSO

sequencia = None
txt_sequencia=['PROCESSO Nº:']
digito=None
txt_digito=['PROCESSO Nº:']

ano=None
txt_ano=['PROCESSO Nº:']

tribunal=None
txt_tribunal=['PROCESSO Nº:']

vara=None
txt_vara=['PROCESSO Nº:']

recte=None
txt_recte=['Autor(a):']

cpf=None
txt_cpf=['Autor(a):'
]
adv_recte=None
txt_adv_recte=['ADV. 1 RECTE.','ADV. 1RECTE']

recda=None
txt_recda=['Autor(a):']

cnpj=None
txt_cnpj=['Autor(a):']

adv_recda=None
txt_adv_recda=['ADV. 1ª']

adv_recda_2=None
txt_adv_recda=['ADV. 2ª']

adv_recda_3=None
txt_adv_recda=['ADV. 3ª']

adv_recda_4=None
txt_adv_recda=['ADV. 4ª']

engenheiro= None
txt_engenheiro=['ENGENHEIRO']

medico= None
txt_medico=['MÉDICO']


# PARÂMETROS DO CÁLCULO

estado = None
txt_estado =['SP']

municipio = None
txt_municipio =['PROCESSO Nº:']
municipio_ribeirao_preto = ['0066','0067','0113','0004']
municipio_franca=['0015']

admissao=None
txt_admissao=['ADMISSÃO:']

demissao=None
txt_demissao=['DEMISSÃO:']

ajuizamento=None
txt_ajuizamento=['AJUIZAMENTO:']

data_inicial=None
txt_data_inicial=['DATA INICIAL [PJe-Calc]']

data_final=None
txt_data_final=['DATA FINAL [PJe-Calc]']

prescricao=None
txt_prescricao=['PRESCRIÇÃO:','PRESCRIÇÃO']
nao_apurar_prescricao = ['',vazio,'-','NÃO']

prazo_aviso = None
txt_prazo_aviso =['Tipo de Rescisão']
valores_nao_apurar_prazo_aviso = ['COM JUSTA CAUSA', 'CONTRATO VIGENTE', 'vazio']

oj415=None
txt_oj415=['O. J. 415']

carga_horaria=None

txt_carga_horaria=['CARGA HORÁRIA']

maior_remuneracao=None
txt_maior_remuneracao=['MAIOR REMUNERAÇÃO:']

ultima_remuneracao=None
txt_ultima_remuneracao=['ÚLTIMA REMUNERAÇÃO:']


# CORREÇÃO, JUROS E MULTA

indice_trabalhista=None
txt_indice_trabalhista=['CORREÇÃO','CORREÇÃO [PRÉ JUDICIAL]']

taxa_negativa=None
txt_taxa_negativa='SIM'

segundo_indice_trabalhista=None
txt_segundo_indice_trabalhista=['CORREÇÃO','CORREÇÃO [PRÉ JUDICIAL]']

data_indice=None
txt_data_indice=['CORREÇÃO','CORREÇÃO [PRÉ JUDICIAL]']

tabela_juros=None
txt_tabela_juros=['JUROS','JUROS [PRÉ JUDICIAL]','JUROS ']

segunda_tabela_juros=None
txt_segunda_tabela_juros=['JUROS','JUROS [PRÉ JUDICIAL]','JUROS ']

data_juros=None
txt_data_juros=['JUROS','JUROS [PRÉ JUDICIAL]','JUROS ']

pre_juros=None
txt_pre_juros=['JUROS PRÉ-JUDICIAL','JUROS PRÉ-JUDICIAL?']

base_juros=None
txt_base_juros=['BASE DE JUROS PJE-CALC :','BASE DE JUROS\nPJE-CALC :']

inss = None
txt_inss = ['I.N.S.S. [SÚMULA 368] ATENÇÃO: LIMITAR MULTA DEVER SER SEM DATA']
nao_apurar_inss = ['NÃO',vazio,'','Não Aplicar Súmula 368']

# CUSTAS JUDICIAIS
        
custas = None
txt_custas = ['CUSTAS :']
valores_nao_apurar_custas = ['ISENTO','NÃO',vazio,'','PAGO']

index_base_custas= None
txt_index_base_custas=0

vencimento_custas = None
txt_vencimento_custas =['PRESCRIÇÃO:','PRESCRIÇÃO']

valor_custas = None       
txt_valor_custas = ['CUSTAS :']


# CONTRIBUIÇÃO SOCIAL
        
correcao_trabalhista= None
txt_correcao_trabalhista=['Com Correção Trabalhista? [INSS]']

atividade_economica = None
txt_atividade_economica = ['ATIVIDADE PRINCIPAL']

data_inicial_inss = None
txt_data_inicial_inss = ['DATA INICIAL [PJe-Calc]']

data_final_inss = None 
txt_data_final_inss = ['DATA FINAL [PJe-Calc]']

simples_nacional = None
txt_simples_nacional = ['SIMPLES NACIONAL']

inicio_nacional = None
txt_inicio_nacional = ['INICIO']

final_nacional = None
txt_final_nacional =['FIM']


# FGTS

fgts = None
txt_fgts =['DESTINO F G T S :']

multa_fgts = None
txt_multa_fgts =['MULTA DE 40% ?']

multa_467 = None
txt_multa_467 =['APLICAR MULTA ART. 467 S/ MULTA FGTS?']

incidencia_fgts= None
txt_incidencia_fgts=['BASE DE CÁLCULO DA MULTA :']

excluir_base_sobre_aviso=None
txt_excluir_base_sobre_aviso = ['SIM']

# HONORÁRIOS 1º ADV. RECTE.

primeiro_adv_recte = None
txt_primeiro_adv_recte =['HONORÁRIO ADV.']

vencimento_primeiro_adv_recte= None
txt_vencimento_primeiro_adv_recte=['AJUIZAMENTO:']

valor_primeiro_adv_recte= None
txt_valor_primeiro_adv_recte=['HONORÁRIO ADV.']

tipo_primeiro_adv_recte= None

vencimento_juros_primeiro_adv_recte= None
txt_vencimento_juros_primeiro_adv_recte=['AJUIZAMENTO:']

# HONORÁRIOS 1º ADV. RECDA.

primeira_adv_recda= None
txt_primeira_adv_recda=['HONORÁRIO ADVs.']

vencimento_primeira_adv_recda= None
txt_vencimento_primeira_adv_recda=['AJUIZAMENTO:']

valor_primeira_adv_recda= None
txt_valor_primeira_adv_recda=['HONORÁRIO ADVs.']

exigibilidade_primeira_adv_recda= None
txt_exigibilidade_primeira_adv_recda=['HONORÁRIO ADVs.']

tipo_primeira_adv_recda= None

vencimento_juros_primeira_adv_recda= None
txt_vencimento_juros_primeira_adv_recda=['AJUIZAMENTO:']


# HONORÁRIOS 2º ADV. RECDA.

segunda_adv_recda= None
txt_segunda_adv_recda=['HONORÁRIO ADVs.']

vencimento_segunda_adv_recda= None
txt_vencimento_segunda_adv_recda=['AJUIZAMENTO:']

valor_segunda_adv_recda= None
txt_valor_segunda_adv_recda=['HONORÁRIO ADVs.']

exigibilidade_segunda_adv_recda= None
txt_exigibilidade_segunda_adv_recda=['HONORÁRIO ADVs.']

tipo_segunda_adv_recda= None

vencimento_juros_segunda_adv_recda= None
txt_vencimento_juros_segunda_adv_recda=['AJUIZAMENTO:']

# HONORÁRIOS 3º ADV. RECDA.

terceira_adv_recda= None
txt_terceira_adv_recda=['HONORÁRIO ADVs.']

vencimento_terceira_adv_recda= None
txt_vencimento_terceira_adv_recda=['AJUIZAMENTO:']

valor_terceira_adv_recda= None
txt_valor_terceira_adv_recda=['HONORÁRIO ADVs.']

exigibilidade_terceira_adv_recda= None
txt_exigibilidade_terceira_adv_recda=['HONORÁRIO ADVs.']

tipo_terceira_adv_recda= None

vencimento_juros_terceira_adv_recda= None
txt_vencimento_juros_terceira_adv_recda=['AJUIZAMENTO:']


# HONORÁRIOS 4º ADV. RECDA.

quarta_adv_recda= None
txt_quarta_adv_recda=['HONORÁRIO ADVs.']

vencimento_quarta_adv_recda= None
txt_vencimento_quarta_adv_recda=['AJUIZAMENTO:']

valor_quarta_adv_recda= None
txt_valor_quarta_adv_recda=['HONORÁRIO ADVs.']

exigibilidade_quarta_adv_recda= None
txt_exigibilidade_quarta_adv_recda=['HONORÁRIO ADVs.']

tipo_quarta_adv_recda= None

vencimento_juros_quarta_adv_recda= None
txt_vencimento_juros_quarta_adv_recda=txt_ajuizamento


# HONORÁRIOS PERITO CONTÁBIL

apurar_honorario_perito = None
txt_apurar_honorario_perito =['HONORÁRIOS C O N T A D O R ?','HONORÁRIOS                         C O N T A D O R ?']

perito_contabil= None
txt_perito_contabil=['IGOR DE MARCHI SOARES']

vencimento_perito_contabil= None

valor_perito_contabil= None
txt_valor_perito_contabil=['500,00']

tipo_perito_contabil= None

# HONORÁRIOS ENGENHEIRO

vencimento_engenheiro= None
txt_vencimento_engenheiro=['PRESCRIÇÃO:','PRESCRIÇÃO']

valor_engenheiro= None
txt_valor_engenheiro=['ENGENHEIRO']

tipo_engenheiro= None

# HONORÁRIOS MÉDICO

vencimento_medico= None
txt_vencimento_medico=['PRESCRIÇÃO:','PRESCRIÇÃO']

valor_medico= None
txt_valor_medico=['MÉDICO']

tipo_medico= None