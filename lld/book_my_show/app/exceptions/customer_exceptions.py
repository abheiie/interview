class CustomerNotFoundException(Exception):
    def __init__(self, id, message="Customer not found,", additional_info=None):
        super().__init__(message)
        self.id = id
        self.additional_info = additional_info or {}

    def __str__(self):
        return f"{super().__str__()} customer id - {self.id} {self.additional_info}"
