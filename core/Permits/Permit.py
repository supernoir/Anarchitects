from random import randint

from core.Permits.permittype import PermitType


class Permit:

    def __init__(self, request):
        self.request = request

    def cointoss(self):
        flip = randint(0, 1)
        if flip == 1:
            return False
        else:
            return True

    def process_request(self, request):
        if request == PermitType.BUILDING:
            return self.cointoss()
        elif request == PermitType.DEMOLITION:
            return self.cointoss()
        else:
            return False

    def print_permit_process_result(self,request):
        result = self.process_request(request)
        print(result)
        if result is True:
            print(f'Your request ({request}) was granted!')
        else:
            print(f'Your request ({request}) was not granted!')


testPermit = Permit(PermitType.DEMOLITION)
testPermit.process_request(PermitType.DEMOLITION)
testPermit.print_permit_process_result(PermitType.DEMOLITION)
testPermit.print_permit_process_result(PermitType.BUILDING)
testPermit.print_permit_process_result(PermitType.CHANGETYPE)