import base64

def encoder_core(text: str, layers: int) -> str:
    
    current_data = text.strip()
    
    for i in range(layers):
        
        if isinstance(current_data, str):
            data_bytes = current_data.encode('utf-8')
        else:
            data_bytes = current_data
            
        encoded_bytes = base64.b64encode(data_bytes)
            
        encoded_string = encoded_bytes.decode('utf-8')
            
        current_data = encoded_string
            
        print(f"Layer {i + 1} has been encoded successfully...")
            
    return current_data