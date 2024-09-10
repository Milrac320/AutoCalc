from pjecalc_bibliotecas import *

# CÁLCULO EXTERNO [ ATUALIZAÇÃO ]

link ='http://localhost:9257/pjecalc/pages/principal.jsf'

xpath_menu_painel=(By.XPATH,'//*[@id="menupainel"]/li[1]')

xpath_aba_calculo_externo=(By.XPATH,'//*[@id="formulario:j_id38:0:j_id41:2:j_id46"]')

xpath_numero_processo=(By.XPATH,'//*[@id="formulario:numero"]')

xpath_digito_processo=(By.XPATH,'//*[@id="formulario:digito"]')

xpath_ano_processo=(By.XPATH,'//*[@id="formulario:ano"]')

xpath_regiao_processo=(By.XPATH,'//*[@id="formulario:regiao"]')

xpath_vara_processo=(By.XPATH,'//*[@id="formulario:vara"]')

xpath_reclamante=(By.XPATH,'//*[@id="formulario:reclamanteNome"]')

xpath_selecionar_cpf=(By.XPATH,'//*[@id="formulario:documentoFiscalReclamante:0"]')

xpath_ativar_cpf=(By.XPATH,'//*[@id="formulario:reclamanteNumeroDocumentoFiscal"]')

xpath_cpf=(By.XPATH,'//*[@id="formulario:reclamanteNumeroDocumentoFiscal"]')

xpath_adv_recte=(By.XPATH,'//*[@id="formulario:nomeAdvogadoReclamante"]')

xpath_enviar_adv_recte=(By.XPATH,'//*[@id="formulario:incluirAdvogadoReclamante"]')

xpath_reclamada=(By.XPATH,'//*[@id="formulario:reclamadoNome"]')

xpath_selecionar_cnpj=(By.XPATH,'//*[@id="formulario:tipoDocumentoFiscalReclamado:1"]')

xpath_cnpj=(By.XPATH,'//*[@id="formulario:reclamadoNumeroDocumentoFiscal"]')

xpath_adv_recda=(By.XPATH,'//*[@id="formulario:nomeAdvogadoReclamado"]')

xpath_enviar_adv_recda=(By.XPATH,'//*[@id="formulario:incluirAdvogadoReclamado"]')

xpath_aba_parametros=(By.XPATH,'//*[@id="formulario:tabParametrosCalculo_lbl"]')

xpath_ativar_ultima_atualizacao=(By.XPATH,'//*[@id="formulario:dataUltimaAtualizacaoInputDate"]')

xpath_ultima_atualizacao=(By.XPATH,'//*[@id="formulario:dataUltimaAtualizacaoInputDate"]')

xpath_indice_trabalhista=(By.XPATH,'//*[@id="formulario:indiceTrabalhista"]')

xpath_taxa_negativa=(By.XPATH,'//*[@id="formulario:ignorarTaxaNegativa"]')

xpath_base_juros=(By.XPATH,'//*[@id="formulario:baseDeJurosDasVerbas"]')

xpath_fgts_sim=(By.XPATH,'//*[@id="formulario:tipoDeVerba:0"]')

xpath_fgts_nao=(By.XPATH,'//*[@id="formulario:tipoDeVerba:1"]')

xpath_tabela_juros=(By.XPATH,'//*[@id="formulario:juros"]')

xpath_inss=(By.XPATH, '//*[@id="formulario:correcaoLei11941"]')

xpath_meses_ir=(By.XPATH,'//*[@id="formulario:qtdMesesRendimento"]')

xpath_base_custas=(By.XPATH,'//*[@id="formulario:baseParaCustasCalculadas"]')

xpath_salvar=(By.XPATH,'//*[@id="formulario:salvar"]')

xpath_menu_exportar=(By.XPATH,'//*[@id="menupainel"]/li[3]')

xpath_aba_exportar=(By.XPATH,'//*[@id="formulario:j_id38:2:j_id41:4:j_id46"]')

js_exportar ="A4J.AJAX.Submit('formulario',event,{'similarityGroupingId':'formulario:exportar','parameters':{'formulario:exportar':'formulario:exportar'} } );return false;"

# CÁLCULO [ LAUDO ]

xpath_botao_calculo=(By.XPATH,'//*[@id="botoesInicio"]/div[1]/a')

xpath_estado=(By.XPATH,'//*[@id="formulario:estado"]')

xpath_municipio=(By.XPATH,'//*[@id="formulario:municipio"]')

xpath_admissao=(By.XPATH,'//*[@id="formulario:dataAdmissaoInputDate"]')

xpath_demissao=(By.XPATH,'//*[@id="formulario:dataDemissaoInputDate"]')

xpath_data_final=(By.XPATH,'//*[@id="formulario:dataTerminoCalculoInputDate"]')

xpath_ajuizamento=(By.XPATH,'//*[@id="formulario:dataAjuizamentoInputDate"]')

xpath_data_inicial=(By.XPATH,'//*[@id="formulario:dataInicioCalculoInputDate"]')

xpath_prescricao=(By.XPATH,'//*[@id="formulario:prescricaoQuinquenal"]')

xpath_aviso_previo=(By.XPATH,'//*[@id="formulario:apuracaoPrazoDoAvisoPrevio"]')

xpath_projetar_aviso=(By.XPATH,'//*[@id="formulario:projetaAvisoIndenizado"]')

xpath_oj415=(By.XPATH,'//*[@id="formulario:zeraValorNegativo"]')

xpath_carga_horaria=(By.XPATH,'//*[@id="formulario:valorCargaHorariaPadrao"]')

xpath_ponto_facultativo=(By.XPATH,'//*[@id="formulario:listagemPontosFacultativos:0:excluirPontoFacultativo"]')

xpath_maior_remuneracao=(By.XPATH,'//*[@id="formulario:valorMaiorRemuneracao"]')

xpath_ultima_remuneracao=(By.XPATH,'//*[@id="formulario:valorUltimaRemuneracao"]')

xpath_aba_inss=(By.XPATH,'//*[@id="formulario:j_id38:0:j_id41:22:j_id46"]')

xpath_ativar_segundo_indice=(By.XPATH, '//*[@id="formulario:combinarOutroIndice"]')

xpath_segundo_indice=(By.XPATH,'//*[@id="formulario:outroIndiceTrabalhista"]')

xpath_data_segundo_indice=(By.XPATH,'//*[@id="formulario:apartirDeOutroIndiceInputDate"]')

xpath_add_data_segundo_indice=(By.XPATH,'//*[@id="formulario:addOutroIndice"]')

xpath_remover_juros=(By.XPATH,'//*[@id="formulario:j_id150:0:excluirDep"]')

xpath_ativar_segundo_juros=(By.XPATH,'//*[@id="formulario:combinarOutroJuros"]')

xpath_segundo_juros=(By.XPATH,'//*[@id="formulario:outroJuros"]')

xpath_data_segundo_juros=(By.XPATH,'//*[@id="formulario:apartirDeOutroJurosInputDate"]')

xpath_add_data_segundo_juros=(By.XPATH,'//*[@id="formulario:addOutroJuros"]')

xpath_juros_pre=(By.XPATH,'//*[@id="formulario:aplicarJurosFasePreJudicial"]')

xpath_aba_dados_especificos=(By.XPATH,'//*[@id="formulario:tabDadosEspecificos_lbl"]')

xpath_aba_custas=(By.XPATH,'//*[@id="formulario:j_id38:0:j_id41:21:j_id46"]')

xpath_custas_devido=(By.XPATH,'//*[@id="formulario:tipoDeCustasDeConhecimentoDoReclamado:0"]')

xpath_ativar_custas=(By.XPATH,'//*[@id="formulario:tipoDeCustasDeConhecimentoDoReclamado:2"]')

xpath_data_custas=(By.XPATH,'//*[@id="formulario:dataVencimentoConhecimentoDoReclamadoInputDate"]')

xpath_valor_custas=(By.XPATH,'//*[@id="formulario:valorConhecimentoDoReclamado"]')

xpath_aba_honorarios=(By.XPATH,'//*[@id="formulario:j_id38:0:j_id41:20:j_id46"]')

xpath_novo_honorario=(By.XPATH,'//*[@id="formulario:incluir"]')

xpath_tipo_honorario=(By.XPATH,'//*[@id="formulario:tpHonorario"]')

xpath_tipo_devedor_reclamado=(By.XPATH,'//*[@id="formulario:tipoDeDevedor:1"]')

xpath_valor_informado=(By.XPATH,'//*[@id="formulario:tipoValor:0"]')

xpath_data_honorario=(By.XPATH,'//*[@id="formulario:dataVencimentoInputDate"]')

xpath_valor_honorario=(By.XPATH,'//*[@id="formulario:valor"]')

xpath_aliquota_honorario=(By.XPATH,'//*[@id="formulario:aliquota"]')

xpath_base_honorario=(By.XPATH,'//*[@id="formulario:baseParaApuracao"]')

xpath_nome_honorario=(By.XPATH,'//*[@id="formulario:nomeCredor"]')

xpath_tipo_devedor_reclamante=(By.XPATH,'//*[@id="formulario:tipoDeDevedor:0"]')

xpath_cobrar_honorario=(By.XPATH,'//*[@id="formulario:tipoCobrancaReclamante:1"]')

xpath_juros_honorario=(By.XPATH,'//*[@id="formulario:aplicarJuros"]')

xpath_data_juros_honorario=(By.XPATH,'//*[@id="formulario:dataJurosAPartirDeInputDate"]')

# MULTAS E INDENIZAÇÕES

xpath_aba_multas=(By.XPATH,'//*[@id="formulario:j_id38:0:j_id41:19:j_id46"]')

xpath_button_nova_multa= (By.XPATH,'//*[@id="formulario:incluir"]')

xpath_input_descricao_multa = (By.XPATH,'//*[@id="formulario:descricao"]')

xpath_checkbox_valor_informado = (By.XPATH,'//*[@id="formulario:valor:0"]')

xpath_checkbox_valor_calculado = (By.XPATH,'//*[@id="formulario:valor:1"]')

xpath_select_base = (By.XPATH,'//*[@id="formulario:tipoBaseMulta"]')

xpath_input_aliquota_multa = (By.XPATH,'//*[@id="formulario:aliquota"]')

xpath_select_credor_devedor = (By.XPATH,'//*[@id="formulario:credorDevedor"]')

# 

xpath_aba_ir=(By.XPATH,'//*[@id="formulario:j_id38:0:j_id41:18:j_id46"]')

xpath_pensao_alimenticia=(By.XPATH,'//*[@id="formulario:j_id38:0:j_id41:17:j_id46"]')

xpath_previdencia_privada=(By.XPATH,'//*[@id="formulario:j_id38:0:j_id41:16:j_id46"]')

xpath_contribuicao_social=(By.XPATH,'//*[@id="formulario:j_id38:0:j_id41:15:j_id46"]')

xpath_correcao_trabalhista=(By.XPATH,'//*[@id="formulario:corrigirDescontoReclamante"]')

xpath_sobre_salarios_pagos=(By.XPATH,'//*[@id="formulario:apurarSalariosPagos"]')

xpath_ocorrencias_inss=(By.XPATH,'//*[@id="formulario:ocorrencias"]')

xpath_aba_salarios_pagos=(By.XPATH,'//*[@id="formulario:tabOcorrenciasSalariosPagos_lbl"]')

xpath_regerar_inss=(By.XPATH,'//*[@id="formulario:regerar"]')

xpath_ativar_atividade_economica=(By.XPATH,'//*[@id="formulario:aliquotaEmpregador:0"]')

xpath_atividade_economica=(By.XPATH,'//*[@id="formulario:atividadesEconomicas"]')

xpath_erro_atividade_economica=(By.XPATH,'//*[@id="formulario:suggestionautoCompleteAtividadesNothingLabel"]/td')

xpath_aliquota_fixa=(By.XPATH,'//*[@id="formulario:aliquotaEmpregador:2"]')

xpath_selecionar_atividade_economica=(By.XPATH,'//*[@id="formulario:suggestionautoCompleteAtividades:suggest"]/tbody/tr[1]/td')

xpath_inicio_inss=(By.XPATH,'//*[@id="formulario:periodoInicialPAGOSInputDate"]')

xpath_final_inss=(By.XPATH,'//*[@id="formulario:periodoFinalPAGOSInputDate"]')

xpath_inicio_simples=(By.XPATH,'//*[@id="formulario:dataInicioSimplesInputDate"]')

xpath_final_simples=(By.XPATH,'//*[@id="formulario:dataTerminoSimplesInputDate"]')

xpath_adicionar_simples=(By.XPATH,'//*[@id="formulario:cmdIncluirPeriodoSimples"]')

xpath_confirmar_inss=(By.XPATH,'//*[@id="formulario:confirmarGeracao"]')

xpath_aba_fgts=(By.XPATH,'//*[@id="formulario:j_id38:0:j_id41:14:j_id46"]')

xpath_fgts_sim=(By.XPATH,'//*[@id="formulario:tipoDeVerba:0"]')

xpath_fgts_nao=(By.XPATH,'//*[@id="formulario:tipoDeVerba:1"]')

xpath_fgts_multa=(By.XPATH,'//*[@id="formulario:multa"]')

xpath_fgts_multa_40=(By.XPATH,'//*[@id="formulario:multaDoFgts:1"]')

xpath_fgts_multa_467=(By.XPATH,'//*[@id="formulario:multaDoArtigo467"]')

xpath_incidencia_fgts=(By.XPATH,'//*[@id="formulario:incidenciaDoFgts"]')

xpath_excluir_base_sobre_aviso=(By.XPATH,'//*[@id="formulario:excluirAvisoDaMulta"]')

xpath_aba_seguro_desemprego=(By.XPATH,'//*[@id="formulario:j_id38:0:j_id41:13:j_id46"]')

xpath_aba_salario_familia=(By.XPATH,'//*[@id="formulario:j_id38:0:j_id41:12:j_id46"]')

xpath_aba_cartao_ponto=(By.XPATH,'//*[@id="formulario:j_id38:0:j_id41:11:j_id46"]')

xpath_aba_verbas=(By.XPATH,'//*[@id="formulario:j_id38:0:j_id41:10:j_id46"]')

xpath_historico_salarial=(By.XPATH,'//*[@id="formulario:j_id38:0:j_id41:9:j_id46"]')

xpath_aba_ferias=(By.XPATH,'//*[@id="formulario:j_id38:0:j_id41:8:j_id46"]')

xpath_adicionar_ferias=(By.XPATH,'//*[@id="formulario:arquivo:add1"]')

xpath_confirmar_ferias=(By.XPATH,'//*[@id="formulario:j_id96"]')

xpath_erro_ferias=(By.XPATH,'//*[@id="formulario:arquivo:clean2"]')

xpath_aba_faltas=(By.XPATH,'//*[@id="formulario:j_id38:0:j_id41:7:j_id46"]')