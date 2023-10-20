import os
import sys
from pathlib import Path

import yaml
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThreadPool
from PyQt5.QtGui import QIcon, QPixmap

from iblrig.gui.tools import Worker
from iblrig.path_helper import load_settings_yaml
from iblrig.tools import get_anydesk_id
from iblrig.version_management import get_local_version
from iblrig.constants import BASE_DIR
from iblrig.gui.ui_wizard import Ui_wizard

VERSION = str(get_local_version())
WIZARD_PNG = str(Path(BASE_DIR).joinpath('iblrig', 'gui', 'wizard.png'))
IBL_PNG = str(Path(BASE_DIR).joinpath('iblrig', 'gui', 'ibl_logo.png'))

if os.name == 'nt':  # Set the AppUserModelID on Windows
    from ctypes import windll
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(f'IBL.iblrig.wizard.{VERSION}')


class RigWizard(QtWidgets.QMainWindow, Ui_wizard):
    def __init__(self, *args, **kwargs):
        super(RigWizard, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.settings = QtCore.QSettings()
        self.move(self.settings.value("pos", self.pos(), QtCore.QPoint))

        self.iblrig_settings = load_settings_yaml()
        file_settings = Path(BASE_DIR).joinpath('settings', 'hardware_settings.yaml')
        self.hardware_settings = yaml.safe_load(file_settings.read_text())

        self.uiLabelIBL.setPixmap(QPixmap(IBL_PNG))
        self.uiLabelVersionValue.setText(get_local_version().base_version)

        # get AnyDesk ID
        anydesk_worker = Worker(get_anydesk_id)
        anydesk_worker.signals.result.connect(self._on_get_anydesk_id_result)
        QThreadPool.globalInstance().tryStart(anydesk_worker)

    @QtCore.pyqtSlot(object)
    def _on_get_anydesk_id_result(self, anydesk_id: str | None):
        """
        Handle the result of obtaining the computer's AnyDesk ID.
        """
        if anydesk_id:
            self.uiLabelAnyDeskValue.setEnabled(True)
            self.uiLabelAnyDeskValue.setText(anydesk_id)

    def closeEvent(self, event) -> None:
        self.settings.setValue("pos", self.pos())


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("IBLRIG Wizard")
    app.setOrganizationName("International Brain Laboratory")
    app.setOrganizationDomain("internationalbrainlab.org")
    app.setApplicationVersion(VERSION)
    app.setWindowIcon(QIcon(WIZARD_PNG))
    app.setStyle("Fusion")
    w = RigWizard()
    w.show()
    app.exec()


if __name__ == "__main__":
    main()
