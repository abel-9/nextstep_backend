from src.context.shared_kernel.application.exceptions import ApplicationException


class OtpExpiredError(ApplicationException):
    def __init__(self):
        super().__init__("OTP has expired")
