from enum import Enum

class PermitType(Enum):
    BUILDING = "building"
    DEMOLITION = "demolition"
    CHANGETYPE = "changetype"
    CHANGEUSE = "changeuse"
    BUILDABOVELIMIT = "buildabovelimit"
