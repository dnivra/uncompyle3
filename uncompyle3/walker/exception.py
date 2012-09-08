from uncompyle3.exception import UncompyleError


class WalkerError(UncompyleError):
    """
    Base exception class for all walker errors.
    """
    pass

class UnknownParameterError(WalkerError):
    """
    Raise when walker engine encounters unknown string
    formatting parameter.
    """
