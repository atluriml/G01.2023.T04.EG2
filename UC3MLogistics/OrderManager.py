"""Order Manager File"""
import json
from UC3MLogistics.OrderManagementException import order_management_exception
from UC3MLogistics.OrderRequest import order_request

EVEN_POS_WEIGHT = 1
ODD_POS_WEIGHT = 3


class order_manager:
    """ order manager class """

    def __init__(self):
        pass

    def validate_ean13(self, ean13):
        """ validate function """
        # confirm that the length is 13
        if len(ean13) != 13:
            return False

        # confirm that every character is a number
        # and also calculate the check digit
        sum = 0
        for i in range(0, len(ean13), 1):
            if not ean13[i].isnumeric():
                return False
            if i == len(ean13) - 1:
                continue
            if i % 2 == 0:  # if the position is even, the weight is 3
                sum += (EVEN_POS_WEIGHT * int(ean13[i]))
            else:
                sum += (ODD_POS_WEIGHT * int(ean13[i]))

        # validate checkdigit
        if sum % 10 == 0:
            expected_checkdigit = (int(sum / 10) * 10) - sum
        else:
            expected_checkdigit = ((int(sum / 10) + 1) * 10) - sum
        if not expected_checkdigit == int(ean13[-1]):
            return False

        return True

    def read_product_code_from_json(self, f_i):
        """ read_product_code_from_json function """
        try:
            with open(f_i) as file:
                data = json.load(file)
        except FileNotFoundError as error:
            raise order_management_exception("Wrong file/file path") from error
        except json.JSONDecodeError as error:
            raise order_management_exception \
                ("JSON Decode Error - Wrong JSON Format") from error

        try:
            product = data["id"]
            p_h = data["phoneNumber"]
            req = order_request(product, p_h)
        except KeyError as error:
            raise order_management_exception \
                ("JSON Decode Error - Invalid JSON Key") from error
        if not self.validate_ean13(product):
            raise order_management_exception("Invalid PRODUCT code")

        # Close the file
        return req
