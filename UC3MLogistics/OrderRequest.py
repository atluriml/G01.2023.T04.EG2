import json
from datetime import datetime


class OrderRequest:
    def __init__( self, idcode, phoneNumber ):
        self.__phoneNumber = phoneNumber
        self.__idcode = idcode
        justnow = datetime.utcnow()
        self.__timeStamp = datetime.timestamp(justnow)

    def __str__(self):
        return "OrderRequest:" + json.dumps(self.__dict__)

    @property
    def Phone( self ):
        return self.__phoneNumber
    @Phone.setter
    def Phone( self, value ):
        self.__phoneNumber = value

    @property
    def PRODUCT_CODE( self ):
        return self.__idcode
    @PRODUCT_CODE.setter
    def PRODUCT_CODE( self, value ):
        self.__idcode = value
