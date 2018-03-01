
import sys
from Route import Route

class TestRoute:

    def __init__(self):
        pass

    def testgetPaceSecondsFromPossableAndMile(self):
        r = Route()

        r.AddSpeed(0, 6)
        r.AddSpeed(1, 12)
        r.AddSpeed(2, 18)

        r.CalculatePossibles()

        r.printPossables()

        pace = r.getPaceSecondsFromPossableAndMile(0.1, 0)
        sys.stdout.write(str(pace) + "\r\n")
        pace = r.getPaceSecondsFromPossableAndMile(0.1, 0.5)
        sys.stdout.write(str(pace) + "\r\n")
        pace = r.getPaceSecondsFromPossableAndMile(0.1, 1)
        sys.stdout.write(str(pace) + "\r\n")
        pace = r.getPaceSecondsFromPossableAndMile(0.1, 2)
        sys.stdout.write(str(pace) + "\r\n\r\n")

        pace = r.getPaceSecondsFromPossableAndMile(0.15, 0)
        sys.stdout.write(str(pace) + "\r\n")
        pace = r.getPaceSecondsFromPossableAndMile(0.15, 0.5)
        sys.stdout.write(str(pace) + "\r\n")
        pace = r.getPaceSecondsFromPossableAndMile(0.15, 1)
        sys.stdout.write(str(pace) + "\r\n")
        pace = r.getPaceSecondsFromPossableAndMile(0.15, 2)
        sys.stdout.write(str(pace) + "\r\n")
