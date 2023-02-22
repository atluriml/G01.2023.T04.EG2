import json
from .OrderMangementException import OrderManagementException
from .OrderRequest import OrderRequest

EVEN_POS_WEIGHT = 1
ODD_POS_WEIGHT = 3

class OrderManager:

    def __init__(self):
        pass

    def ValidateEAN13( self, eAn13 ):

        # confirm that the length is 13
        if len(eAn13) != 13:
            return False

        # confirm that every character is a number
        # and also calculate the check digit
        sum = 0
        for i in range(0, len(eAn13), 1):
            if not eAn13[i].isnumeric():
                return False
            elif i == len(eAn13) - 1:
                continue
            elif i % 2 == 0: # if the position is even, the weight is 3
                sum += (EVEN_POS_WEIGHT * int(eAn13[i]))
            else:
                sum += (ODD_POS_WEIGHT * int(eAn13[i]))

        # validate checkdigit
        if sum % 10 == 0:
            expected_checkdigit = (int(sum / 10) * 10) - sum
        else:
            expected_checkdigit = ((int(sum / 10) + 1) * 10) - sum
        if not expected_checkdigit == int(eAn13[-1]):
            return False

        return True

    def ReadproductcodefromJSON( self, fi ):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise OrderManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            PRODUCT = DATA["id"]
            PH = DATA["phoneNumber"]
            req = OrderRequest(PRODUCT, PH)
        except KeyError as e:
            raise OrderManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.ValidateEAN13(PRODUCT):
            raise OrderManagementException("Invalid PRODUCT code")

        # Close the file
        return req