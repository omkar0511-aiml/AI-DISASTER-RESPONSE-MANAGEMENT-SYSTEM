from datetime import datetime
import uuid


def get_current_timestamp():
    """
    Returns the current timestamp.
    """
    return datetime.now()


def generate_unique_id():
    """
    Generates a unique ID.
    """
    return str(uuid.uuid4())