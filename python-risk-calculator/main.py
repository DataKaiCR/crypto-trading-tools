import numpy as np
from PyQt5 import QtWidgets, QtCore

class PositionSizeCalculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Create input fields
        self.account_size_input = QtWidgets.QLineEdit()
        self.account_size_input.setPlaceholderText("Enter trading account size")
        self.account_size_input.setFixedWidth(200)
        self.account_size_input.setAlignment(QtCore.Qt.AlignRight)
        self.account_size_input.setStyleSheet("background-color: #F9F9F9;")

        self.account_risk_input = QtWidgets.QLineEdit()
        self.account_risk_input.setPlaceholderText("Enter risk percentage")
        self.account_risk_input.setFixedWidth(200)
        self.account_risk_input.setAlignment(QtCore.Qt.AlignRight)
        self.account_risk_input.setStyleSheet("background-color: #F9F9F9;")

        self.entry_price_input = QtWidgets.QLineEdit()
        self.entry_price_input.setPlaceholderText("Enter entry price")
        self.entry_price_input.setFixedWidth(200)
        self.entry_price_input.setAlignment(QtCore.Qt.AlignRight)
        self.entry_price_input.setStyleSheet("background-color: #F9F9F9;")

        self.stop_loss_price_input = QtWidgets.QLineEdit()
        self.stop_loss_price_input.setPlaceholderText("Enter stop loss price")
        self.stop_loss_price_input.setFixedWidth(200)
        self.stop_loss_price_input.setAlignment(QtCore.Qt.AlignRight)
        self.stop_loss_price_input.setStyleSheet("background-color: #F9F9F9;")

        self.leverage_input = QtWidgets.QLineEdit()
        self.leverage_input.setPlaceholderText("Enter leverage amount")
        self.leverage_input.setFixedWidth(200)
        self.leverage_input.setAlignment(QtCore.Qt.AlignRight)
        self.leverage_input.setStyleSheet("background-color: #F9F9F9;")

        # Dynamic text change detection
        self.account_size_input.textChanged.connect(self.calculate)
        self.account_risk_input.textChanged.connect(self.calculate)
        self.entry_price_input.textChanged.connect(self.calculate)
        self.stop_loss_price_input.textChanged.connect(self.calculate)
        self.leverage_input.textChanged.connect(self.calculate)


        # Create labels to display the results
        self.risk_amount_label = QtWidgets.QLabel("")
        self.volume_label = QtWidgets.QLabel("")
        self.position_size_label = QtWidgets.QLabel("")
        self.stop_loss_label = QtWidgets.QLabel("")
        self.margin_label = QtWidgets.QLabel("")


        # Create a layout and add the input fields and button
        layout = QtWidgets.QFormLayout()
        layout.addRow("Trading Account Size (USD)", self.account_size_input)
        layout.addRow("Risk per Trade (%)", self.account_risk_input)
        layout.addRow("Entry Price (USD)", self.entry_price_input)
        layout.addRow("Stop Loss Price (USD)", self.stop_loss_price_input)
        layout.addRow("Leverage (x)", self.leverage_input)

        layout.addRow("Risk Amount (USD)", self.risk_amount_label)
        layout.addRow("Volume (Unit)", self.volume_label)
        layout.addRow("Position Size (USD)", self.position_size_label)
        layout.addRow("Stop Loss (%)", self.stop_loss_label)
        layout.addRow("Account Margin (USD)", self.margin_label)

        self.setLayout(layout)

    def calculate(self):
        # Get user input
        if self.account_size_input.text() and self.account_risk_input.text() and self.entry_price_input.text() and self.stop_loss_price_input.text() and self.leverage_input.text():
            account_size = float(self.account_size_input.text())
            risk_percentage = float(self.account_risk_input.text()) / 100
            entry_price = float(self.entry_price_input.text())
            stop_loss_price = float(self.stop_loss_price_input.text())
            leverage = float(self.leverage_input.text())
        else:
            return
        # Calculate risk amount per trade
        risk_amount = account_size * risk_percentage

        # Calculate distance to stop
        stop_distance = abs(entry_price - stop_loss_price)

        # Calculate stop loss percentage
        stop_percentage = abs((stop_loss_price / entry_price) - 1)

        # Calculate position value
        position_value = risk_amount / stop_percentage

        # Calculate volume (position size)
        volume = position_value / entry_price
        ##volume = ((account_size * risk_percentage) / (entry_price - stop_loss_price)) * entry_price

        # Calculate account margin
        account_margin = account_size / leverage


        # Display results
        self.stop_loss_label.setText(f"{stop_percentage:.2f}")
        self.margin_label.setText(f"{account_margin:.2f}")
        self.volume_label.setText(f"{volume:.2f}")
        self.position_size_label.setText(f"{position_value:.2f}")
        self.risk_amount_label.setText(f"{risk_amount:.2f}")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    calculator = PositionSizeCalculator()
    calculator.show()
    app.exec_()
