from pjecalc_bibliotecas import *

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
    QPushButton:hover {
        background-color: #BFBFBF; /* Cor de fundo ao passar o mouse */
        border-color: #BFBFBF; /* Cor da borda ao passar o mouse */
    }
    QLineEdit{
        color:white;
        font-size: 11px;
    }
        '''  