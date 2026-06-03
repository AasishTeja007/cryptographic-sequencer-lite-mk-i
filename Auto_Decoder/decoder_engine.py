# Import base64 library
import base64

# Decoder core function
def decoder_core(encoded_text: str) -> tuple[str, int]:   # Type Hinting
    
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
                # If string, convert encoded string to raw bytes
                data_bytes = current_data.encode('utf-8')
            else:
                # Else, encoded bytes stay intact
                data_bytes = current_data
            
            # Decode the encoded bytes
            decoded_bytes = base64.b64decode(data_bytes)
            
            # Convert the decoded bytes to normal string
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