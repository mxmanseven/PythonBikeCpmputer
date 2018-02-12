# route optione:
# speed, known, reset
#
# speed
#  start miliage,
#  speed (mph)
#
# known
#  miliage
#
# reset
#  start mile
#  end mile


from enum import Enum

class RouteType(Enum):
    SpeedChange = 1
    MiliageReset = 2
    KnownControl = 3
    EndBy = 4

