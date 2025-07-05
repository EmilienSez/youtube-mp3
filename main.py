from PySide6 import QtWidgets
from ui.window import App  # Assure-toi que window.py contient la classe App

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = App()
    win.show()
    app.exec_()  # C'est ici que la boucle d'événements doit être appelée