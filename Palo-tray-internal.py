import sys
import time
import threading
import subprocess
import webbrowser
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
import sys
import os

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)


SERVER = "192.168.100.20"
PING_INTERVAL = 5
#print(resource_path("photo.png"))
#print(QIcon(resource_path('green.png')).isNull())
open_link_action = QAction("Autenticate to internal")
open_link_action.triggered.connect(lambda: webbrowser.open("https://palo-alto-portal.aws.cellebrite.local/authenticate"))

class PingTrayApp:
    def __init__(self):
        self.app = QApplication(sys.argv)

        # Check system tray availability
        if not QSystemTrayIcon.isSystemTrayAvailable():
            QMessageBox.critical(None, "Error", "System tray is not available.")
            sys.exit(1)

        QApplication.setQuitOnLastWindowClosed(False)

        self.icon_online = QIcon(resource_path('green.png'))
        self.icon_offline = QIcon(resource_path('red.png'))

        if self.icon_online.isNull() or self.icon_offline.isNull():
            QMessageBox.critical(None, "Error", "Icon files not found or invalid.")
            sys.exit(1)

        self.tray_icon = QSystemTrayIcon(self.icon_offline)
        self.tray_icon.setToolTip("Initializing ping monitor...")
        self.tray_icon.setVisible(True)

        self.menu = QMenu()
        open_link_action = QAction("Autenticate to internal")
        exit_action = QAction("Exit")
        open_link_action.triggered.connect(lambda: webbrowser.open("https://palo-alto-portal.aws.cellebrite.local/authenticate"))
        exit_action.triggered.connect(self.exit_app)
        self.menu.addAction(open_link_action)
        self.menu.addAction(exit_action)
        self.tray_icon.setContextMenu(self.menu)
        
        self.running = True
        self.thread = threading.Thread(target=self.ping_loop, daemon=True)
        self.thread.start()

        self.app.exec_()

    def ping_server(self, host):
        param = "-n" if sys.platform.startswith("win") else "-c"
        try:
            subprocess.check_output(["ping", param, "1", host], stderr=subprocess.DEVNULL,creationflags=subprocess.CREATE_NO_WINDOW) # added this line to hide window in windows i didnt check on mac ",creationflags=subprocess.CREATE_NO_WINDOW"
            return True
        except subprocess.CalledProcessError:
            return False

    def ping_loop(self):
        while self.running:
            status = self.ping_server(SERVER)
            icon = self.icon_online if status else self.icon_offline
            text = f"You have access to internal resurces" if status else f"Please sign-in to have access"
            self.tray_icon.setIcon(icon)
            self.tray_icon.setToolTip(text)
            time.sleep(PING_INTERVAL)

    def exit_app(self):
        self.running = False
        self.tray_icon.hide()
        self.app.quit()
        

if __name__ == "__main__":
    #print ("running the application ")
    PingTrayApp()