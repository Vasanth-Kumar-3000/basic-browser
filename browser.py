from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class Browser(QMainWindow):
    def __init__(self, *args, **kwargs):
        """
        Initializes the browser window with a base URL, URL bar, go button, back
        button, forward button, and reload button. The base URL is set to
        https://www.google.com by default. The URL bar is set to accept input as
        well as to navigate to the input URL when the Enter key is pressed. The
        go button is set to navigate to the input URL when clicked. The back
        button is set to go back to the previous page when clicked. The forward
        button is set to go forward to the next page when clicked. The reload
        button is set to reload the current page when clicked. The window is
        then shown with the title "Basic Browser".
        """
        super(Browser, self).__init__(*args, **kwargs)

        # Initialize the browser
        self.browser = QWebEngineView()

        # Set the base URL
        base_url = "https://www.google.com"
        self.browser.setUrl(QUrl(base_url))

        # Set up the window and layout
        self.window = QWidget()
        self.window.setWindowTitle("Basic Browser")
        self.layout = QVBoxLayout()
        self.horizontalLayout = QHBoxLayout()

        # URL bar setup using QLineEdit for simplicity
        self.url_bar = QLineEdit()
        self.url_bar.setText(base_url)  # Set the base URL in the text field as well
        self.url_bar.setMaximumHeight(30)
        self.horizontalLayout.addWidget(self.url_bar)

        # Connect the URL bar to navigation
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        # Go button setup
        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)
        self.go_btn.clicked.connect(self.navigate_to_url)
        self.horizontalLayout.addWidget(self.go_btn)

        # Back button setup
        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)
        self.back_btn.clicked.connect(self.browser.back)
        self.horizontalLayout.addWidget(self.back_btn)

        # Forward button setup
        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.horizontalLayout.addWidget(self.forward_btn)

        # Reload button setup
        self.reload_btn = QPushButton("Reload")
        self.reload_btn.setMinimumHeight(30)
        self.reload_btn.clicked.connect(self.browser.reload)
        self.horizontalLayout.addWidget(self.reload_btn)

        # Add horizontal layout to main layout
        self.layout.addLayout(self.horizontalLayout)

        # Add browser widget to the layout
        self.layout.addWidget(self.browser)

        # Set layout to the window and make it the central widget
        self.window.setLayout(self.layout)
        self.setCentralWidget(self.window)

        # Show the window
        self.show()

    # Navigation method
    def navigate_to_url(self):
        url = self.url_bar.text()  # Get the URL from the URL bar
        self.browser.setUrl(QUrl(url))  # Navigate to the URL


        
app=QApplication([])
window=Browser()
app.exec_()
        
        
        