from enum import IntEnum, unique


@unique
class AccountType(IntEnum):
    Cheque = 1,
    HomeLoan = 2,
    CreditCard = 3,
    Saving = 4

    @staticmethod
    def parse(val):
        case ={
            'CHEQUE': AccountType.Cheque,
            'HOMELOAN': AccountType.HomeLoan,
            'CREDITCARD': AccountType.CreditCard,
            'SAVING': AccountType.Saving
        }
        return case.get(str(val).upper(), "NOT IMPLEMENTED")
