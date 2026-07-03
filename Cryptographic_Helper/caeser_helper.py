# Define a helper function using caesar cipher encryption and decryption
def caeser_cipher_base64(text, shift, decrypt=False):
    """
    Caesar cipher function to encrypt and decrypt encoded text
    
    Args:
        text (str): Encoded text to encrypt and decrypt
        shift (int): Positive shift/Right shift to move characters right to encrypt and Negative shift/Left shift to move characters left to decrypt
        decrypt (bool): Boolean value flag to trigger decryption. Defaults to False which means it encrypts instead of decrypt but when set to True, then it decrypts

    Returns:
        str : Returns the given string as encrypted for encoder and decrypted string for decoder
    """
    # All characters used in Base64
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    # Condition: Flag set to True
    if decrypt:
        # The shift value becomes negative/left shift
        shift = -shift
    
    # Limit of base64 characters
    shift = shift % 64
    
    # Brand new alphabet string
    shifted_chars = base64_chars[shift:] + base64_chars[:shift]
    
    # Translation look-up memory dictionary
    trans_table = str.maketrans(base64_chars, shifted_chars)
    
    # Returns final encrypted string
    return text.translate(trans_table)