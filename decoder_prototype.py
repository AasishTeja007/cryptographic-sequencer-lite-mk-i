import base64

def auto_decoder():
    print("****CryptoGraphic Sequencer MK-I (Decoder Version)****")
    
    while True:
        encoded_text = input("Enter the encoded text (or 'exit' to quit): ").strip()
        
        if encoded_text.lower() == 'exit':
            print("Goodbye! Have a nice day!")
            break
        
        current_data = encoded_text
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
            
        if decode_count > 0:
            print("Decoding successful!")
            print(f"Total decode count: {decode_count}")
            print(f"Final decoded text: {current_data}")
        else:
            print("Text decoding failed. This might not be Base64")
            
auto_decoder()