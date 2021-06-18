from PyQt5.QtWidgets import QApplication
from reddragons.visao import Processamento
from reddragons.estruturas import ModelService
import sys
from reddragons.interface import GUI_main
from reddragons.utils import Logger
from reddragons.utils import VIDEO_PATH

if __name__ == '__main__':
    model = ModelService()
    visao = Processamento(model)
    visao.alterar_src(VIDEO_PATH)
    app = QApplication(sys.argv)
    window = GUI_main(visao, model)
    window.show()
    print (Logger()._fps_mean)
    sys.exit(app.exec_())
