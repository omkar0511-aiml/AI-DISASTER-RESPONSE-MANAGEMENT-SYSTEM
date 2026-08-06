class DisasterResponseException(Exception):
    """
    Base exception class for the AI Disaster Response System.
    """

    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)