# Import base64 library
import base64

# From folder import helper function
from Cryptographic_Helper.caeser_helper import caeser_cipher_base64

# Decoder core function
def decoder_core(encoded_text: str, secret_key: int) -> tuple[str, int]:   # Type Hinting
    
    # Initialize encoded text input to current data
    current_data = encoded_text.strip()
    
    # Initialize decount code to zero
    decode_count = 0
    
    # Core loop
    while True:
        
        # Error handling block
        try:
            # Check data type of current data
            if isinstance(current_data, str):
                # If string, decrypt the current data
                unshifted_layer = caeser_cipher_base64(text=current_data, shift=secret_key, decrypt=True)
            else:
                # Else, current data stays intact
                unshifted_layer = current_data
            
            # Check data type of decrypted data
            if isinstance(unshifted_layer, str):
                # If string, convert decrypted string to raw bytes
                data_bytes = unshifted_layer.encode('utf-8')
            else:
                # Else, decrypted bytes stay intact
                data_bytes = unshifted_layer
            
            # Decode the decrypted bytes
            decoded_bytes = base64.b64decode(data_bytes)
            
            # Convert the decrypted bytes to normal string
            decoded_string = decoded_bytes.decode('utf-8')
            
            # Safety check for infinity loop
            if decoded_string == current_data:
                break
            
            # Update current data after each iteration
            current_data = decoded_string
            
            # Update decode count after each iteration
            decode_count += 1
            
            # Print success statement for each decoded layer
            print(f"Layer {decode_count} has been decoded successfully...")
        
        # Safety exit when input is corrupted    
        except Exception:
            break
    
    # Return current data and decode count values    
    return current_data, decode_count