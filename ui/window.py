import sys, subprocess
from pathlib import Path
from PySide6 import QtWidgets

sys.path.append(str(Path(__file__).resolve().parent.parent))
from modules import downloader as dl

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application de téléchargement de vidéo youtube")
        self.setGeometry(100, 100, 700, 500)
        self.setup_ui()
        self.setup_connections()
        self.show_liste()

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self) # Crée un layout horizontal (QH)
        self.champ_ajout_lien = QtWidgets.QLineEdit()
        self.btn_ajout_lien = QtWidgets.QPushButton("Ajouter")
        self.liste_lien = QtWidgets.QListWidget()
        self.btn_retirer_element = QtWidgets.QPushButton("-")
        self.btn_retirer_tout = QtWidgets.QPushButton("Supprimer tout les liens")
        self.btn_lancer_dl = QtWidgets.QPushButton("Lancer le téléchargement")
        self.messageErreur = QtWidgets.QMessageBox()
        self.messageErreur.setWindowTitle("Message d'erreur")
        self.btn_ouvrir_repertoire = QtWidgets.QPushButton("Ouvrir le répertoire")
        
        # Ajout des éléments au layout de base
        self.layout.addWidget(self.champ_ajout_lien)
        self.layout.addWidget(self.btn_ajout_lien)
        self.layout.addWidget(self.liste_lien)
        self.layout.addWidget(self.btn_retirer_tout)
        self.layout.addWidget(self.btn_lancer_dl)
        self.layout.addWidget(self.btn_ouvrir_repertoire)
        
    def default_values(self):
        self.liste_lien.addItems(dl.get_content_list())
        # for item in self.liste_lien:
        #     item.addWidget(self.btn_retirer_element)

    def setup_connections(self):
        self.btn_ajout_lien.clicked.connect(self.add_link)
        self.btn_retirer_tout.clicked.connect(self.delete_link)
        self.btn_lancer_dl.clicked.connect(self.launch_download)
        self.btn_ouvrir_repertoire.clicked.connect(self.open_directory)

    def add_link(self):
        url = self.champ_ajout_lien.text().strip()
        if not url:
            return

        dl.add_content_list(url)
        self.add_item_widget(url)
        self.champ_ajout_lien.clear()

    def add_item_widget(self, text):
        item_widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout(item_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        label = QtWidgets.QLabel(text)
        btn_supprimer = QtWidgets.QPushButton("Supprimer")
        btn_supprimer.setFixedWidth(80)

        layout.addWidget(label)
        layout.addStretch()
        layout.addWidget(btn_supprimer)

        list_item = QtWidgets.QListWidgetItem(self.liste_lien)
        list_item.setSizeHint(item_widget.sizeHint())

        self.liste_lien.addItem(list_item)
        self.liste_lien.setItemWidget(list_item, item_widget)

        # Connexion du bouton à une fonction lambda qui supprime l'élément
        btn_supprimer.clicked.connect(lambda: self.remove_item(list_item, text))

    def remove_item(self, item, text):
        row = self.liste_lien.row(item)
        self.liste_lien.takeItem(row)
        dl.remove_content_list(text)  # Tu dois avoir une fonction qui supprime une URL spécifique dans ton fichier
        
    def delete_link(self):
        dl.delete_content_list()
        self.liste_lien.clear()

    def launch_download(self):
        liste = dl.get_content_list()
        if len(liste) == 0:
            # self.messageErreur.setWindowTitle("Message d'erreur")
            self.messageErreur.setText("Aucun lien dans la liste, veuillez ajouter un lien pour pouvoir continuer")
            return self.messageErreur.show()
        else : 
            dl.create_dir()
        dl.download_link(liste)
        dl.delete_content_list()
        self.liste_lien.clear()

    def show_liste(self):
        for lien in dl.get_content_list():
            self.add_item_widget(lien)

    def open_directory(self):
        subprocess.Popen(["explorer", str(dl.DOWNLOAD_DIR)])

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = App()
    win.show()
    app.exec_() # Lance l'application
