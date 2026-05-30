import base64

def decoder_core(encoded_text: str) -> tuple[str, int]:
    
    current_data = encoded_text.strip()
    decode_count = 0
    
    while True:
        try:
            if isinstance(current_data, str):
                data_bytes = current_data.encode('utf-8')
            else:
                data_bytes = current_data
                
            decoded_bytes = base64.b64decode(data_bytes)
            
            decoded_string = decoded_bytes.decode('utf-8')
            
            if decoded_string == current_data:
                break
            
            current_data = decoded_string
            decode_count += 1
            print(f"Layer {decode_count} has been decoded successfully...")
            
        except Exception:
            break
        
    return current_data, decode_count