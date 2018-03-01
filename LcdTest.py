from LcdManager import LcdManager
import time


class LcdTest:

    def __init__(self):
        pass

    def testLcd(self):
        lcdM = LcdManager()
        lcdM.setEnduroScreen(1.35, 90, 12, 11, 6, 55.11, 12)
        time.sleep(5)
        lcdM.setEnduroScreen(12.35, -5, 12, 11.5, 6.5, 55.11, 12)
        time.sleep(5)
        lcdM.setEnduroScreen(12.35, -20, 12, 11.5, 540.1, 55.11, 12)
        time.sleep(5)
        lcdM.setEnduroScreen(12.35, -40, 12, 11.5, 606.5, 55.11, 12)
        time.sleep(5)
        lcdM.setEnduroScreen(12.35, -66, 12, 11.5, 1200.5, 55.11, 12)
        time.sleep(5)
        lcdM.setEnduroScreen(12.35, -666, 12, 11.5, 3000, 55.11, 12)
        time.sleep(5)
        lcdM.setEnduroScreen(12.35, -666, 12, 11.5, 3660, 55.11, 12)