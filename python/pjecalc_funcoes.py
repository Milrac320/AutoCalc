from pjecalc_bibliotecas import *
from pjecalc_variaveis import *

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl.worksheet._reader')

# TEMPO ENTRE AÇÕES

def tempo_espera(modo):
    if modo == 'alteração':
        time.sleep(1.5)
    elif modo == 'salvar':
        time.sleep(2)
    elif modo == 'exportar':
        time.sleep(3)
    elif modo == 'extra':
        time.sleep(5)

# LIMPAR PROMPT      

def limpar():
    os.system('cls')      
    
# TRANSFORMAR DATAS - DIA - MÊS - ANO      

def converter_data(valor, formato='dmy'):
    if pd.isna(valor) or valor == '':
        return None
    
    # Definir os formatos de data
    formatos = {
        'dmy': '%d-%m-%Y',
        'my': '%m-%Y'
    }

    # Verificar se o formato é válido
    if formato not in formatos:
        raise ValueError('Formato inválido. Use "dmy" para dia-mês-ano ou "my" para mês-ano.')

    try:
        # Tente primeiro converter a string para uma data
        data = pd.to_datetime(valor)
        data_formatada = data.strftime(formatos[formato])
        return data_formatada
    except (ValueError, TypeError):
        # Se ocorrer um erro na conversão da string, continue com o fluxo original
        pass

    try:
        valor_int = int(valor)
    except ValueError:
        return None

    if valor_int > 59:
        valor_int -= 1

    data_base_excel = datetime.date(1899, 12, 31)
    data = data_base_excel + datetime.timedelta(days=valor_int)
    data_formatada = data.strftime(formatos[formato])

    return data_formatada

# TIPO DE HONORÁRIO | CALCULADO / INFORMADO

def identificar_tipo(valor):
    # Converte o valor para string, se não for uma string
    if not isinstance(valor, str):
        valor = str(valor)

    # Remove símbolos monetários e espaços
    valor_limpo = valor.strip().replace(',', '').replace('$', '').replace('€', '').replace('£', '').replace(' ', '')
    
    # Verifica se é uma porcentagem explícita
    if re.match(r'^\d+(\.\d+)?%$', valor_limpo):
        return 'CALCULADO'
    
    # Verifica se é um número decimal menor que 1 (tratado como porcentagem implícita)
    try:
        numero = float(valor_limpo)
        if 0 < numero < 1:
            return 'CALCULADO'
    except ValueError:
        pass
    
    # Verifica se é um número monetário
    if re.match(r'^\d+(\.\d{2})?$', valor_limpo):
        return 'INFORMADO'
    
    return None

# PRIMEIRO DIA DO MÊS

def primeiro_dia_mes():
    agora = datetime.datetime.now()

    # Cria uma nova data com o dia fixado em 1
    primeiro_dia_mes = datetime.datetime(agora.year, agora.month, 1)

    return primeiro_dia_mes
  
# CASAS DECIMAIS

def criarDecimal(valor):
    partes = valor.split(',')
    if len(partes) >= 2 and len(partes[1]) >= 2:
        return valor
    return valor + ',00'    

# BUSCA DE VALORES NAS PLANILHAS

def src(df, valores_busca, deslocamento_linhas, deslocamento_colunas):

    for i, row in df.iterrows():
        for valor_busca in valores_busca:
            if valor_busca in row.values:
                col_index = row.tolist().index(valor_busca)
                nova_linha_index = i + deslocamento_linhas
                nova_coluna_index = col_index + deslocamento_colunas

                # Verificar se o novo índice está dentro dos limites do DataFrame
                if 0 <= nova_linha_index < len(df) and 0 <= nova_coluna_index < len(df.columns):
                    return df.iat[nova_linha_index, nova_coluna_index]
                return None

    return None

# INICIA PLANILHAS DO ARQUIVO EXCEL

def iniciar_planilhas():
    try:
        with open('json/escolha_calculos.json', 'r') as file:
            data = json.load(file)

        processo = data['caminho_arquivo']
        file_path = processo

        if file_path and os.path.exists(file_path):
            df_analise_geral = pd.read_excel(file_path, engine='openpyxl', header=None, sheet_name='ANÁLISE GERAL', dtype=str)
            df_analise_geral = df_analise_geral.apply(lambda col: col.map(lambda x: None if pd.isna(x) else x))

            df_analise_decisoes = pd.read_excel(file_path, engine='openpyxl', header=None, sheet_name='ANÁLISE DECISÕES 2024', dtype=str)
            df_analise_decisoes = df_analise_decisoes.apply(lambda col: col.map(lambda x: None if pd.isna(x) else x))

            return df_analise_geral, df_analise_decisoes, data
        else:
            print('O arquivo especificado não foi encontrado.')
            return None, None, None
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
        return None, None, None
    
# TESTE DE VARIAVEIS NAS PLANILHAS
    
def testeDeVariaveis():
    df_analise_geral, df_analise_decisoes, _ = iniciar_planilhas()

    variaveis = [
        ('','''------------------------------------
        DADOS DO PROCESSO
        ------------------------------------'''),
        ('SEQUENCIA | ', src(df_analise_geral,txt_sequencia,0,1)[0:7]),
        ('DIGITO | ', src(df_analise_geral,txt_digito,0,1)[8:10]),
        ('ANO | ', src(df_analise_geral,txt_ano,0,1)[11:15]),
        ('TRIBUNAL | ', src(df_analise_geral,txt_tribunal,0,1)[18:20]),
        ('VARA | ', src(df_analise_geral,txt_vara,0,1)[21:25]),
        ('RECTE | ', src(df_analise_geral,txt_recte,0,1)),
        ('CPF | ', src(df_analise_geral,txt_cpf,0,3)),
        ('ADV_RECTE | ', src(df_analise_geral,txt_adv_recte,0,1)),
        ('RECDA | ', src(df_analise_geral,txt_recda,1,1)),
        ('CNPJ | ', src(df_analise_geral,txt_cnpj,1,3)),
        ('ADV_RECDA | ', src(df_analise_geral,txt_adv_recda,1,1)),
        ('', '''------------------------------------
        PARÂMETROS DO CÁLCULO
        ------------------------------------'''),
        ('ESTADO | ', 'SP'),
        ('MUNICIPIO | ', src(df_analise_geral,txt_municipio,0,1)[21:25]),
        ('ADMISSAO | ', converter_data(src(df_analise_geral,txt_admissao,0,1),'dmy')),
        ('DEMISSAO | ', converter_data(src(df_analise_geral,txt_demissao,0,1),'dmy')),
        ('AJUIZAMENTO | ', converter_data(src(df_analise_geral,txt_ajuizamento,0,1),'dmy')),
        ('DATA_INICIAL | ', converter_data(src(df_analise_geral,txt_data_inicial,0,1),'dmy')),
        ('DATA_FINAL | ', converter_data(src(df_analise_geral,txt_data_final,0,1),'dmy')),
        ('PRESCRICAO | ', src(df_analise_geral,txt_prescricao,0,1)),
        ('PRAZO_AVISO | ', src(df_analise_geral,txt_prazo_aviso,0,1)),
        ('OJ415 | ', src(df_analise_decisoes,txt_oj415,0,1)),
        ('CARGA_HORARIA | ', src(df_analise_decisoes,txt_carga_horaria,0,1)),
        ('MAIOR_REMUNERACAO | ', src(df_analise_decisoes,txt_maior_remuneracao,0,1)),
        ('ULTIMA_REMUNERACAO | ', src(df_analise_decisoes,txt_ultima_remuneracao,0,1)),
        ('', '''------------------------------------
        CORREÇÃO, JUROS E MULTA
        ------------------------------------'''),
        ('INDICE_TRABALHISTA | ', src(df_analise_decisoes,txt_indice_trabalhista ,0,1)),
        ('SEGUNDO_INDICE_TRABALHISTA | ', src(df_analise_decisoes, txt_segundo_indice_trabalhista,0,4)),
        ('DATA_INDICE | ', converter_data(src(df_analise_decisoes, txt_data_indice,0,3),'dmy')),
        ('TABELA_JUROS | ', src(df_analise_decisoes,txt_tabela_juros ,0,1)),
        ('SEGUNDA_TABELA_JUROS | ', src(df_analise_decisoes, txt_segunda_tabela_juros,0,4)),
        ('DATA_JUROS | ', converter_data(src(df_analise_decisoes, txt_data_juros,0,3),'dmy')),
        ('TAXA_NEGATIVA | ', txt_taxa_negativa),
        ('PRE_JUROS | ', src(df_analise_decisoes, txt_pre_juros,1,0)),
        ('BASE_JUROS | ', src(df_analise_decisoes, txt_base_juros,1,0) ),
        ('INSS | ', src(df_analise_decisoes, txt_inss,1,0)),
        ('', '''------------------------------------
        CUSTAS JUDICIAIS
        ------------------------------------'''),
        ('CUSTAS | ', src(df_analise_decisoes, txt_custas,1,0)),
        ('VENCIMENTO_CUSTAS | ', converter_data(src(df_analise_decisoes, txt_vencimento_custas,0,3),'dmy')),
        ('VALOR_CUSTAS | ', src(df_analise_decisoes, txt_valor_custas,1,0)),
        ('', '''------------------------------------
        CONTRIBUIÇÃO SOCIAL
        ------------------------------------'''),
        ('CORRECAO_TRABALHISTA | ', src(df_analise_decisoes,txt_correcao_trabalhista ,1,0)),
        ('ATIVIDADE_ECONOMICA | ', src(df_analise_geral,txt_atividade_economica ,0,1)),
        ('DATA_INICIAL_INSS | ', converter_data(src(df_analise_geral,txt_data_inicial_inss ,0,1),'dmy')),
        ('DATA_FINAL_INSS | ', converter_data(src(df_analise_geral, txt_data_final_inss,0,1),'dmy')),
        ('SIMPLES_NACIONAL | ', src(df_analise_geral, txt_simples_nacional,0,1)),
        ('INICIO_NACIONAL | ', converter_data(src(df_analise_geral, txt_inicio_nacional,0,1),'my')),
        ('FINAL_NACIONAL | ', converter_data(src(df_analise_geral, txt_final_nacional,0,1),'my')),
        ('', '''------------------------------------
        FGTS
        ------------------------------------'''),
        ('FGTS | ', src(df_analise_decisoes,txt_fgts ,1,0)),
        ('MULTA_FGTS | ', src(df_analise_decisoes,txt_multa_fgts ,1,0)),
        ('MULTA_467 | ', src(df_analise_decisoes,txt_multa_467 ,1,0)),
        ('INCIDENCIA_FGTS | ', src(df_analise_decisoes,txt_incidencia_fgts ,1,0)),
        ('EXCLUIR_BASE_SOBRE_AVISO | ',  txt_excluir_base_sobre_aviso),
        ('', '''------------------------------------
        HONORÁRIOS 1º ADV. RECTE.
        ------------------------------------'''),
        ('PRIMEIRO_ADV_RECTE | ', f'{src(df_analise_decisoes,txt_primeiro_adv_recte ,1,0)} [ADV.RECTE.]'),
        ('VENCIMENTO_PRIMEIRO_ADV_RECTE | ', converter_data(src(df_analise_geral, txt_vencimento_primeiro_adv_recte,0,1),'dmy')),
        ('VALOR_PRIMEIRO_ADV_RECTE | ', src(df_analise_decisoes,txt_valor_primeiro_adv_recte ,1,1)),
        ('VENCIMENTO_JUROS_PRIMEIRO_ADV_RECTE | ', converter_data(src(df_analise_geral,txt_vencimento_juros_primeiro_adv_recte ,0,1),'dmy')),
        ('', '''------------------------------------
        HONORÁRIOS 1º ADV. RECDA.
        ------------------------------------'''),
        ('PRIMEIRA_ADV_RECDA | ', f'{src(df_analise_decisoes,txt_primeira_adv_recda ,1,0)} [ADV.RECDA.]'),
        ('VENCIMENTO_PRIMEIRA_ADV_RECDA | ', converter_data(src(df_analise_geral, txt_vencimento_primeira_adv_recda,0,1),'dmy')),
        ('VALOR_PRIMEIRA_ADV_RECDA | ', src(df_analise_decisoes,txt_valor_primeira_adv_recda ,1,1)),
        ('EXIGIBILIDADE_PRIMEIRA_ADV_RECDA | ', src(df_analise_decisoes,txt_exigibilidade_primeira_adv_recda ,1,2)),
        ('VENCIMENTO_JUROS_PRIMEIRA_ADV_RECDA | ', converter_data(src(df_analise_geral, txt_vencimento_juros_primeira_adv_recda,0,1),'dmy')),
        ('', '''------------------------------------
        HONORÁRIOS 2º ADV. RECDA.
        ------------------------------------'''),
        ('SEGUNDA_ADV_RECDA | ', f'{src(df_analise_decisoes,txt_segunda_adv_recda ,2,0)} [ADV. 2ª RECDA.]'),
        ('VENCIMENTO_SEGUNDA_ADV_RECDA | ', converter_data(src(df_analise_geral, txt_vencimento_segunda_adv_recda,0,1),'dmy')),
        ('VALOR_SEGUNDA_ADV_RECDA | ', src(df_analise_decisoes,txt_valor_segunda_adv_recda ,2,1)),
        ('EXIGIBILIDADE_SEGUNDA_ADV_RECDA | ', src(df_analise_decisoes,txt_exigibilidade_segunda_adv_recda ,2,2)),
        ('VENCIMENTO_JUROS_SEGUNDA_ADV_RECDA | ', converter_data(src(df_analise_geral, txt_vencimento_juros_segunda_adv_recda,0,1),'dmy')),
        ('', '''------------------------------------
        HONORÁRIOS 3º ADV. RECDA.
        ------------------------------------'''),
        ('TERCEIRA_ADV_RECDA | ', f'{src(df_analise_decisoes,txt_terceira_adv_recda ,3,0)} [ADV. 3ª RECDA.]'),
        ('VENCIMENTO_TERCEIRA_ADV_RECDA | ', converter_data(src(df_analise_geral, txt_vencimento_terceira_adv_recda,0,1),'dmy')),
        ('VALOR_TERCEIRA_ADV_RECDA | ', src(df_analise_decisoes,txt_valor_terceira_adv_recda ,3,1)),
        ('EXIGIBILIDADE_TERCEIRA_ADV_RECDA | ', src(df_analise_decisoes,txt_exigibilidade_terceira_adv_recda ,3,2)),
        ('VENCIMENTO_JUROS_TERCEIRA_ADV_RECDA | ', converter_data(src(df_analise_geral, txt_vencimento_juros_terceira_adv_recda,0,1),'dmy')),
        ('', '''------------------------------------
        HONORÁRIOS 4º ADV. RECDA.
        ------------------------------------'''),
        ('QUARTA_ADV_RECDA | ', f'{src(df_analise_decisoes,txt_quarta_adv_recda ,4,0)} [ADV. 4ª RECDA.]'),
        ('VENCIMENTO_QUARTA_ADV_RECDA | ', converter_data(src(df_analise_geral, txt_vencimento_quarta_adv_recda,0,1),'dmy')),
        ('VALOR_QUARTA_ADV_RECDA | ', src(df_analise_decisoes,txt_valor_quarta_adv_recda ,4,1)),
        ('EXIGIBILIDADE_QUARTA_ADV_RECDA | ', src(df_analise_decisoes,txt_exigibilidade_quarta_adv_recda ,4,2)),
        ('VENCIMENTO_JUROS_QUARTA_ADV_RECDA | ', converter_data(src(df_analise_geral, txt_vencimento_juros_quarta_adv_recda,0,1),'dmy')),
        ('', '''------------------------------------
        HONORÁRIOS PERITO CONTÁBIL
        ------------------------------------'''),
        ('PERITO_CONTABIL | ', txt_perito_contabil),
        ('VENCIMENTO_PERITO_CONTABIL | ', converter_data(primeiro_dia_mes(),'dmy')),
        ('VALOR_PERITO_CONTABIL | ', txt_valor_perito_contabil),
        ('', '''------------------------------------
        HONORÁRIOS ENGENHEIRO
        ------------------------------------'''),
        ('ENGENHEIRO | ', src(df_analise_geral,txt_engenheiro,0,1)),
        ('VENCIMENTO_ENGENHEIRO | ', converter_data(src(df_analise_decisoes,txt_vencimento_engenheiro ,0,3),'dmy')),
        ('VALOR_ENGENHEIRO | ', src(df_analise_decisoes,txt_valor_engenheiro ,0,1)),
        ('', '''------------------------------------
        HONORÁRIOS MÉDICO
        ------------------------------------'''),
        ('MEDICO | ',  src(df_analise_geral,txt_medico,0,1)),
        ('VENCIMENTO_MEDICO | ', converter_data(src(df_analise_decisoes,txt_vencimento_medico ,0,3),'dmy')),
        ('VALOR_MEDICO | ', src(df_analise_decisoes,txt_valor_medico ,0,1)),
        ]

    for i, (nome_variavel, valor) in enumerate(variaveis):
        try:
        # Tente acessar o valor, se necessário
            if valor is None or valor == '':
                variaveis[i] = (nome_variavel, '###')
        except Exception as e:
        # Se ocorrer qualquer exceção, trate-a e substitua o valor
            variaveis[i] = (nome_variavel, '###')

    # Escrever a saída para um arquivo de texto
    with open('txt/variaveis.txt', 'w') as f:
        for nome_variavel, valor in variaveis:
            f.write(f'{nome_variavel}{valor}\n')

    # Abrir o arquivo de texto em um terminal separado
    subprocess.run(['cmd', '/c', 'start', 'txt/variaveis.txt'], shell=True)

# VERIFICAR CUSTAS

def valor_monetario(value):

    padrao_monetario = r'^\s*(R\$|\$)?\s*\d{1,3}(\.\d{3})*(\d{1,3})?(,\d{2})?\s*$'
    return bool(re.match(padrao_monetario, str(value)))