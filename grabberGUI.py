import sys
import challongegrabber
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                          QMainWindow, QAction, QPushButton,
                          QGridLayout, QLineEdit, QTextEdit)

""" This is a program for controlling the GUI for the results grabber
    using PyQt5."""
class GUI(QWidget):
    def __init__(self):

        #initialise the parent class
        super().__init__()

        self.initGUI()
    
    def initGUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        self.setLayout(grid)

        challongeLabel = QLabel('Input a Challonge Bracket Website:', self)
        grid.addWidget(challongeLabel, 0, 0)
        
        self.addressBar = QLineEdit()
        grid.addWidget(self.addressBar, 1, 0)

        searchButton = QPushButton("Get Data", self)
        searchButton.clicked.connect(self.buttonClicked)
        grid.addWidget(searchButton, 1, 1)

        self.statusLabel = QLabel('', self)
        grid.addWidget(self.statusLabel, 2, 1)

        self.outputResults = QTextEdit()
        grid.addWidget(self.outputResults, 4, 0, 3, 2)

        self.numPlayers = QLabel('', self)
        grid.addWidget(self.numPlayers, 9, 0)

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle("Results Grabber")
        self.show()
    
    """ This code is executed when the 'Get Data' button is pressed. """
    def buttonClicked(self):
        website = self.addressBar.text()
        listPlayers = []

        bracket = challongegrabber.ChallongeGrabber(website)
        
        #Some error handling
        if bracket.error == 1:
            self.statusLabel.setText('Website read failed')
        elif bracket.error == 2:
            self.statusLabel.setText('Unknown Error')
        else:
            self.statusLabel.setText('')
            listPlayers = bracket.get_list_of_players()
        
        if bracket.error == 3:
            self.statusLabel.setText('No data available')
        

        listPlacings = self.generateListPlacings()

        #combine the player and placing strings
        bracketResults = [j + i for i, j in zip(listPlayers, listPlacings)]
        stringPlayers = "\n".join(bracketResults)

        #Output the player data
        self.outputResults.setText(stringPlayers)
        self.numPlayers.setText("Number of Players: " + str(bracket.get_number_of_players()))

    """ Generates 127 double elimination bracket placings.
        TODO: make this automatic so any bracket size is easily
        accomodated."""
    def generateListPlacings(self):
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
        listPlacings.extend(['96th: '] * 32)

        return listPlacings


def main():
    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


