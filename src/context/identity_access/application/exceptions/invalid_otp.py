from src.context.shared_kernel.application.exceptions import ApplicationException


class InvalidOtpError(ApplicationException):
    def __init__(self):
        super().__init__("Invalid OTP")
