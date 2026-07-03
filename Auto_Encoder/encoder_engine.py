# Import base64 library
import base64

# From folder import helper function
from Cryptographic_Helper.caeser_helper import caeser_cipher_base64

# Encoder core function
def encoder_core(text: str, layers: int, secret_key: int) -> str:   # Type Hinting
    
    # Initialize normal text input to current data
    current_data = text.strip()
    
    # Core loop
    for i in range(layers):
        
        # Check data type of current data
        if isinstance(current_data, str):
            # If string, convert string to raw bytes
            data_bytes = current_data.encode('utf-8')
        else:
            # Else, bytes stay intact
            data_bytes = current_data
        
        # Encode the normal bytes
        encoded_bytes = base64.b64encode(data_bytes)
        
        # Convert the encoded bytes to encoded string
        encoded_string = encoded_bytes.decode('utf-8')
        
        # Encrypt the encoded string
        scrambled_string = caeser_cipher_base64(text=encoded_string, shift=secret_key, decrypt=False)
        
        # Update the encrypted string to current data
        current_data = scrambled_string
        
        # Print success statement for each encoded layer
        print(f"Layer {i + 1} has been encoded successfully...")
    
    # Return current data value
    return current_data