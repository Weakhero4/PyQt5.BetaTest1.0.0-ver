import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
class mainwindows(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Booking Ticket Fill up Form")

        self.setLayout(qtw.QVBoxLayout())

        my_label = qtw.QLabel("My Fill up information")
        self.layout().addWidget(my_label)
        my_label.setFont(qtg.QFont('Gotham',20))

        my_names = qtw.QLabel("Your Name: ")
        self.layout().addWidget(my_names)
        my_names.setFont(qtg.QFont('Time New Roman' , 15))

        my_name = qtw.QLineEdit()
        my_name.setObjectName("name_field")
        my_name.setText("")
        self.layout().addWidget(my_name)

        my_ages = qtw.QLabel("Your Age:")
        self.layout().addWidget(my_ages)
        my_ages.setFont(qtg.QFont('Time New Roman' , 15))

        my_age = qtw.QSpinBox(self, value = 18 , maximum = 200 , minimum = 0 , singleStep = 1)
        self.layout().addWidget(my_age)
        my_age.setFont(qtg.QFont('Time New Roman' , 15))

        my_addresss = qtw.QLabel("Your Address:")
        self.layout().addWidget(my_addresss)
        my_addresss.setFont(qtg.QFont('Time New Roman' , 15))

        my_address = qtw.QLineEdit()
        my_address.setObjectName("name_field")
        my_address.setText("")
        self.layout().addWidget(my_address)

        my_genders = qtw.QLabel("Your Gender:")
        self.layout().addWidget(my_genders)
        my_genders.setFont(qtg.QFont('Time New Roman' , 15))

        
        my_gender = qtw.QComboBox(self)
        my_gender.addItem("Male")
        my_gender.addItem("Female")
        my_gender.addItem("Bisexual")
        my_gender.addItem("Lesbian")
        self.layout().addWidget(my_gender)
        
        my_destinations = qtw.QLabel("Your Destination:")
        self.layout().addWidget(my_destinations)
        my_destinations.setFont(qtg.QFont('Time New Roman' , 15))

        my_destination = qtw.QComboBox(self)
        my_destination.addItem("CDO - DAVAO")
        my_destination.addItem("CDO - OZAMIS")
        my_destination.addItem("CDO - CAMIGUIN")
        self.layout().addWidget(my_destination)

        my_payments = qtw.QLabel("Your Payment Methods")
        self.layout().addWidget(my_payments)
        my_payments.setFont(qtg.QFont('Time New Roman' , 15))

        my_payment = qtw.QComboBox(self,editable = True , insertPolicy = qtw.QComboBox.InsertAtBottom)
        my_payment.addItem("Cash")
        my_payment.addItem("GCash")
        my_payment.addItem("PayPal")
        my_payment.addItem("Debit cards")
        my_payment.addItem("Credit Cards")
        my_payment.addItem("Direct debit")
        my_payment.addItem("Bank transfers")
        my_payment.addItem("Mobile payments")
        my_payment.addItem("Mobile payments: e-wallets")
        my_payment.addItem("Mobile payments: payment Links")
        self.layout().addWidget(my_payment)
        

        my_cashs = qtw.QLabel("Cash:")
        self.layout().addWidget(my_cashs)
        my_cashs.setFont(qtg.QFont('Time New Roman' , 15))

        my_cash = qtw.QDoubleSpinBox(self,value = 0 , maximum = 10000000000 , minimum = 5000 , singleStep = 1000)
        self.layout().addWidget(my_cash)
        my_cash.setFont(qtg.QFont('Time New Roman' , 15))


        #Create a button 
        my_button = qtw.QPushButton("SUBMIT",clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        def press_it():
            #ADd name to label
            information_form = qtw.QLabel("Information Paper")
            self.layout().addWidget(information_form)
            information_form.setFont(qtg.QFont('Time New Roman' , 15))


            user_input_name = qtw.QLabel("Name:")
            self.layout().addWidget(user_input_name)
            user_input_name.setFont(qtg.QFont('Time New Roman' , 15))

            user_input_age = qtw.QLabel("Age:")
            self.layout().addWidget(user_input_age)
            user_input_age.setFont(qtg.QFont('Time New Roman' , 15))

            user_input_address = qtw.QLabel("Address:")
            self.layout().addWidget(user_input_address)
            user_input_address.setFont(qtg.QFont('Time New Roman' , 15))

            
            user_input_gender = qtw.QLabel("Gender:")
            self.layout().addWidget(user_input_gender)
            user_input_gender.setFont(qtg.QFont('Time New Roman' , 15))

            user_input_destination = qtw.QLabel("Destination")
            self.layout().addWidget(user_input_destination)
            user_input_destination.setFont(qtg.QFont('Time New Roman' , 15))

            user_input_payment = qtw.QLabel("Payment Methods")
            self.layout().addWidget(user_input_payment)
            user_input_payment.setFont(qtg.QFont('Time New Roman' , 15))

            user_input_money = qtw.QLabel("Money:")
            self.layout().addWidget(user_input_money)
            user_input_money.setFont(qtg.QFont('Time New Roman' , 15))

            user_input_name.setText(f'Name: {my_name.text()}')
            user_input_age.setText(f'Age: {my_age.value()}')
            user_input_address.setText(f'Address: {my_address.text()}')
            user_input_gender.setText(f'Gender: {my_gender.currentText()}')
            user_input_destination.setText(f'Destination: {my_destination.currentText()}')
            user_input_payment.setText(f'Payment Methods: {my_payment.currentText()}')
            user_input_money.setText(f'Money: {my_cash.value()}')
            
            #Clear the entry box 
            my_name.setText("")
            my_address.setText("")


        self.show()

student_information = qtw.QApplication([])
mw = mainwindows()

student_information.exec()
