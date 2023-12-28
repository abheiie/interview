class InvalidSymbolException(Exception):
    def __init__(self, message="Invalid Symbol", additional_info=None):
        super().__init__(message)
        self.additional_info = additional_info

    def __str__(self):
        return f"{super().__str__()} (Additional Info: {self.additional_info})"
