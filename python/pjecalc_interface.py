from pjecalc_bibliotecas import *
from pjecalc_funcoes import *
from pjecalc_calculo import calculo
from pjecalc_calculo_externo import calculoExterno

warnings.filterwarnings('ignore', category=UserWarning, module='pandas')

class PjeCalcAutomatizacao(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.verificar_pjecalc_ativo()
        self.file_path = None

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        style1 = '''
            QCheckBox::indicator {
                width: 12px;
                height: 12px;
                border: 0.5px solid black;
                border-radius: 2px;
            }

            QCheckBox {
                font-family: 'Josefin Sans Bold';  /* Use o nome real da fonte, não o caminho do arquivo */
                font-size: 13px;
                color: black;
            }

            QCheckBox::indicator:unchecked {
                background: black;
            }

            QCheckBox::indicator:checked {
                background: #6cff5c;
            }

            QLineEdit{
                color:white;
                font-size: 11px;
                height: 100px;
            }

                '''
        
        style2 = '''
            QCheckBox::indicator {
                width: 15px;
                height: 15px;
                border: 0.5px solid white;
                border-radius: 2px;
            }

            QCheckBox {
                font-family: 'Josefin Sans Bold';  /* Use o nome real da fonte, não o caminho do arquivo */
                font-size: 16px;
                color: white;
            }

            QCheckBox::indicator:unchecked {
                background: white;
            }

            QCheckBox::indicator:checked {
                background: #6cff5c;
            }

            QLabel{
                color: white;
                font-size: 16px;
                font-family: 'Josefin Sans Bold';
            }

            QPushButton{
                font-family: 'Josefin Sans Bold';
                font-size: 20px;
                color: black;
                background: white;
                border: 2px solid white;
                border-radius: 4px;
                padding: 5px;
            }

            QLineEdit{
                color:white;
                font-size: 11px;
            }
                '''        

        layout = QVBoxLayout(central_widget)

        self.setWindowTitle('PjeCalc Automatização')
        self.setFixedSize(560, 515)
        self.center_on_screen()
        self.setStyleSheet('background-color: black')    

        titulo = QLabel('AUTO CALC')
        titulo.setAlignment(Qt.AlignHCenter)
        titulo.setStyleSheet('color: white')
        fonte = QFont('Josefin Sans Bold', 30)
        titulo.setFont(fonte)

        linha = QFrame()
        linha.setFrameShape(QFrame.HLine)
        linha.setFrameShadow(QFrame.Sunken)
        linha.setStyleSheet('border: 4px solid red')

        quadros_layout = QHBoxLayout()

        # Quadro 1
        quadro1 = QFrame()
        quadro1_layout = QVBoxLayout(quadro1)
        quadro1.setStyleSheet('background:white; margin-top:5px;border-radius: 2px;')

        # Adiciona checkboxes ao Quadro 1
        checkbox_vars = {
            'Verbas': False,
            'Faltas': False,
            'Férias': False,
            'Histórico Salarial': False,
            'Cartão de Ponto': False,
            'Salário-família': False,
            'Seguro-desemprego': False,
            'FGTS': False,
            'Contribuição Social': False,
            'Previdência Privada': False,
            'Pensão Alimentícia': False,
            'Imposto de Renda': False,
            'Multas e Indenizações': False,
            'Honorários': False,
            'Custas Judiciais': False,
            'Correção, Juros e Multa': False
        }        

        self.checkboxes = []
        for name, checked in checkbox_vars.items():
            checkbox = QCheckBox(name)
            checkbox.setChecked(checked)
            checkbox.setStyleSheet(style1)
            self.checkboxes.append(checkbox)
            quadro1_layout.addWidget(checkbox)

        # Defina a altura do Quadro 1
        quadro1.setFixedHeight(435)  # Ajuste a altura conforme necessário
        quadro1.setFixedWidth(230)  # Ajuste a altura conforme necessário

        # Quadro 2
        quadro2 = QFrame()
        quadro2_layout = QVBoxLayout(quadro2)
        quadro2_layout.setContentsMargins(0, 0, 0, 0)

        titulo2 = QLabel('SELECIONE:')
        titulo2.setStyleSheet('color: white')
        fonte2 = QFont('Josefin Sans Bold', 12)
        titulo2.setFont(fonte2)

        checkbox2_1 = QCheckBox('CÁLCULO')
        checkbox2_1.clicked.connect(lambda: self.toggle_checkboxes(self.checkbox2_1))
        checkbox2_1.setStyleSheet(style2)
        self.checkbox2_1 = checkbox2_1

        checkbox2_2 = QCheckBox('CÁLCULO EXTERNO')
        checkbox2_2.clicked.connect(lambda: self.toggle_checkboxes(checkbox2_2))
        checkbox2_2.setStyleSheet(style2)
        self.checkbox2_2 = checkbox2_2

        checkbox2_3 = QCheckBox('TESTE DE VARIÁVEIS')
        checkbox2_3.clicked.connect(lambda: self.toggle_checkboxes(checkbox2_3))
        checkbox2_3.setStyleSheet(style2)
        self.checkbox2_3 = checkbox2_3

        linha2_1 = QFrame()
        linha2_1.setFrameShape(QFrame.HLine)
        linha2_1.setStyleSheet('border: 1px solid red')

        checkbox2_4 = QCheckBox('PJE-CALC ATIVO')
        checkbox2_4.setStyleSheet(style2)
        checkbox2_4.setEnabled(False)
        self.checkbox2_4 = checkbox2_4  # Adicione esta linha para definir o atributo da classe

        linha2_2 = QFrame()
        linha2_2.setFrameShape(QFrame.HLine)
        linha2_2.setStyleSheet('border: 1px solid red;')

        label_quadro2 = QLabel('ESCOLHA O ARQUIVO:')
        label_quadro2.setStyleSheet(style2)

        self.nome_arquivo_edit = QLineEdit('Nenhum arquivo selecionado! Clique Aqui.')
        self.nome_arquivo_edit.setStyleSheet(style2)
        self.nome_arquivo_edit.setReadOnly(True)
        self.nome_arquivo_edit.mousePressEvent = self.salvar_diretorio_json

        linha2_3 = QFrame()
        linha2_3.setFrameShape(QFrame.HLine)
        linha2_3.setStyleSheet('border: 1px solid red;')      

        self.avisos = QLineEdit()
        self.avisos.setStyleSheet(style1)  
        self.avisos.setAlignment(Qt.AlignCenter)

        botao_executar = QPushButton('EXECUTAR')
        botao_executar.clicked.connect(self.iniciar_pjecalc)  # Conecta o botão à função executar
        botao_executar.setStyleSheet(style2)

        quadro2_layout.addSpacing(5)
        quadro2_layout.addWidget(titulo2)
        quadro2_layout.addSpacing(5)  # Adicione o espaçamento desejado
        quadro2_layout.addWidget(checkbox2_1)
        quadro2_layout.addSpacing(5)  # Adicione o espaçamento desejado
        quadro2_layout.addWidget(checkbox2_2)
        quadro2_layout.addSpacing(5)  # Adicione o espaçamento desejado
        quadro2_layout.addWidget(checkbox2_3)
        quadro2_layout.addSpacing(5)  # Adicione o espaçamento desejado
        quadro2_layout.addWidget(linha2_1)
        quadro2_layout.addSpacing(10)  # Adicione o espaçamento desejado
        quadro2_layout.addWidget(checkbox2_4)
        quadro2_layout.addSpacing(10)  # Adicione o espaçamento desejado
        quadro2_layout.addWidget(linha2_2)
        quadro2_layout.addSpacing(10)  # Adicione o espaçamento desejado
        quadro2_layout.addWidget(label_quadro2)
        quadro2_layout.addSpacing(5)  # Adicione o espaçamento desejado
        quadro2_layout.addWidget(self.nome_arquivo_edit)
        quadro2_layout.addSpacing(10)  # Adicione o espaçamento desejado
        quadro2_layout.addWidget(linha2_3)
        quadro2_layout.addSpacing(10)
        quadro2_layout.addWidget(self.avisos)        
        quadro2_layout.addStretch(1)
        quadro2_layout.addWidget(botao_executar)

        # Adiciona os widgets ao layout horizontal
        quadros_layout.addSpacing(20)
        quadros_layout.addWidget(quadro1)
        quadros_layout.addSpacing(20)
        quadros_layout.addWidget(quadro2)
        quadros_layout.addSpacing(20)

        layout.addWidget(titulo)
        layout.addWidget(linha)
        layout.addLayout(quadros_layout)

        self.nome_arquivo_label = self.nome_arquivo_edit
           
    def verificar_pjecalc_ativo(self):
        nome_processo_javaw = 'javaw.exe'

        # Obtenha a referência à checkbox2_4
        checkbox2_4 = self.checkbox2_4  # Supondo que a checkbox2_4 seja um atributo da classe

        for processo in psutil.process_iter(attrs=['pid', 'name']):
            if nome_processo_javaw.lower() in processo.info['name'].lower():
                # Marque a checkbox2_4
                checkbox2_4.setChecked(True)
                return

    def encerrar_processo(self, nome_processo):  # Adicione o argumento self
        for processo in psutil.process_iter(attrs=['pid', 'name']):
            if nome_processo.lower() in processo.info['name'].lower():
                try:
                    processo_pje = psutil.Process(processo.info['pid'])

                    processo_pje.terminate()

                    processo_pje.wait()

                except Exception as e:
                    self.avisos.clear()
                    self.avisos.setText(f'Erro ao encerrar o processo {nome_processo}: {e}')

    def programa_iniciado(self, nome_processo_javaw):
        for processo in psutil.process_iter(attrs=['name']):
            if nome_processo_javaw.lower() in processo.info['name'].lower():
                return True
        return False
    
    def aguardar_inicio_programa(self, nome_processo_javaw):
        while not self.programa_iniciado(nome_processo_javaw):
            time.sleep(1)

    def iniciar_pjecalc(self):
        caminho_arquivo_bat = 'C:/Users/user/Downloads/arquivosPASTAS/pjecalc-windows64-2.12.0/iniciarPjeCalc.bat'
        nome_processo_javaw = 'javaw.exe'
        nome_processo_firefox = 'firefox.exe'

        # Obtenha a referência às checkboxes
        checkbox2_4 = self.checkbox2_4
        checkbox2_3 = self.checkbox2_3
        
        # Verificar se o PjeCalc já está ativo com base no estado das checkboxes
        if checkbox2_4.isChecked() or checkbox2_3.isChecked():
            pass  # Não é necessário iniciar novamente
        else:
            self.avisos.clear()
            self.avisos.setText('Iniciando Pje-Calc')  
            
            # Iniciar o processo do PjeCalc
            subprocess.Popen(caminho_arquivo_bat, shell=True)

            # Aguardar o início dos processos javaw.exe e firefox.exe
            self.aguardar_inicio_programa(nome_processo_javaw)
            self.aguardar_inicio_programa(nome_processo_firefox)

            # Marcar a checkbox2_4 após iniciar o Pje-Calc
            checkbox2_4.setChecked(True)

            # Encerrar o processo firefox.exe se necessário
            self.encerrar_processo(nome_processo_firefox)

        # Manipulação de checkboxes e arquivo JSON
        try:
            with open('json/escolha_calculos.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        # Atualizar o caminho do arquivo no JSON
        if hasattr(self, 'file_path') and self.file_path:
            data['caminho_arquivo'] = self.file_path

        # Atualizar os valores das checkboxes no JSON
        checkbox_status = {checkbox.text(): checkbox.isChecked() for checkbox in self.checkboxes}
        
        for checkbox, value in checkbox_status.items():
            data[checkbox] = value

        # SALVAR OS DADOS
        with open('json/escolha_calculos.json', 'w') as file:
            json.dump(data, file, indent=4)
    
        # Chamar cálculo
        self.chamar_calculo()

    def toggle_checkboxes(self, checkbox_clicked):
        # Desmarcar os outros checkboxes se o checkbox clicado for marcado
        if checkbox_clicked.isChecked():
            if checkbox_clicked == self.checkbox2_1:
                self.checkbox2_2.setChecked(False)
                self.checkbox2_3.setChecked(False)
            elif checkbox_clicked == self.checkbox2_2:
                self.checkbox2_1.setChecked(False)
                self.checkbox2_3.setChecked(False)
            elif checkbox_clicked == self.checkbox2_3:
                self.checkbox2_1.setChecked(False)
                self.checkbox2_2.setChecked(False)

    def chamar_calculo(self):
        if not self.checkbox2_1.isChecked() and not self.checkbox2_2.isChecked() and not self.checkbox2_3.isChecked():
            self.avisos.setText('Selecione o tipo de Cálculo')  
        elif self.nome_arquivo_edit.text() == 'Nenhum arquivo selecionado! Clique aqui.':
            self.avisos.setText('Selecione o arquivo')
        elif self.checkbox2_1.isChecked():
            self.avisos.clear()
            calculo()
            self.avisos.setText('Execução do Cálculo Concluída!')  
        elif self.checkbox2_2.isChecked():
            self.avisos.clear()
            calculoExterno()
            self.avisos.setText('Execução do Cálculo Externo Concluída!')  
        elif self.checkbox2_3.isChecked():
            self.avisos.clear()
            testeDeVariaveis()
            self.avisos.setText('Execução dos Testes Concluída!')  

    def center_on_screen(self):
        screen_geometry = QApplication.desktop().screenGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 3
        self.move(x, y)

    def salvar_diretorio_json(self,_):

        self.file_path, _ = QFileDialog.getOpenFileName(self, '', '', 'Arquivos Excel (*.xlsm);;Todos os Arquivos (*)')
        if self.file_path:
            nome_arquivo = os.path.basename(self.file_path)
            self.nome_arquivo_label.setText(f'{nome_arquivo}')

            # Carregue o conteúdo atual do arquivo JSON
            try:
                with open('json/escolha_calculos.json', 'r') as file:
                    dados_existentes = json.load(file)
            except FileNotFoundError:
                dados_existentes = {}

            # Adicione o caminho do arquivo aos dados existentes
            dados_existentes['caminho_arquivo'] = self.file_path

            # Salve o arquivo JSON com os dados atualizados
            with open('json/escolha_calculos.json', 'w') as file:
                json.dump(dados_existentes, file, indent=4)
   
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PjeCalcAutomatizacao()
    window.show()
    sys.exit(app.exec_())