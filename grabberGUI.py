import sys
import challongegrabber
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                          QMainWindow, QAction, QPushButton,
                          QGridLayout, QLineEdit, QTextEdit)

class GUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initGUI()
    
    def initGUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        self.setLayout(grid)

        challongeText = 'Challonge Website:'

        challongeLabel = QLabel(challongeText, self)
        grid.addWidget(challongeLabel, 0, 0)
        
        self.addressBar = QLineEdit()
        grid.addWidget(self.addressBar, 1, 0)

        searchButton = QPushButton("Get Data", self)
        searchButton.clicked.connect(self.buttonClicked)
        grid.addWidget(searchButton, 1, 1)

        self.statusLabel = QLabel('', self)
        grid.addWidget(self.statusLabel, 0, 2)

        self.outputResults = QTextEdit()
        grid.addWidget(self.outputResults, 4, 0, 3, 2)

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle("Results Grabber")
        self.show()
    
    def buttonClicked(self):
        website = str(self.addressBar.text())
        bracket = challongegrabber.ChallongeGrabber(website)

        if bracket.error == 1:
            self.statusLabel.setText('Website read failed')
        elif bracket.error == 2:
            self.statusLabel.setText('Unknown Error')
        else:
            self.statusLabel.setText('')
        
        listPlayers = bracket.get_list_of_players()

        #yes, this isn't the best.
        listPlacings = ['1st: ', '2nd: ', '3rd: ', '4th: ']
        listPlacings.extend(['5th: '] * 2)
        listPlacings.extend(['7th: '] * 2)
        listPlacings.extend(['9th: '] * 4)
        listPlacings.extend(['13th: '] * 4)
        listPlacings.extend(['17th: '] * 8)
        listPlacings.extend(['25th: '] * 8)
        listPlacings.extend(['33rd: '] * 16)
        listPlacings.extend(['49th: '] * 16)
        listPlacings.extend(['65th: '] * 32)

        bracketResults = [j + i for i, j in zip(listPlayers, listPlacings)]

        stringPlayers = "\n".join(bracketResults)

        self.outputResults.setText(stringPlayers)


    
def main():
    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


