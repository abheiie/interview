class SerializerException(Exception):
    def __init__(self, serializer, message="Bad Request,", additional_info=None):
        super().__init__(message)
        self.serializer_errors = serializer.errors
        self.additional_info = additional_info or {}

    def __str__(self):
        return f"{super().__str__()} errors - {self.id} {self.additional_info}"
