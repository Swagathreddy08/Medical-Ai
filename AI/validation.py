
def validate_healthcare_request(user_input: str):

    if not user_input or not user_input.strip():
        return {
            "valid": False,
            "message": "Please describe your health concern."
        }

    if len(user_input) > 2000:
        return {
            "valid": False,
            "message": "Your message is too long."
        }

    return {
        "valid": True,
        "message": "Input accepted for further assessment."
    }
