import base64

def auto_encoder():
    print("****CryptoGraphic Sequencer Lite MK-I (Encoder Version)****")
    
    while True:
        normal_text = input("Enter the normal text (or 'exit' to quit): ").strip()
        
        if normal_text.lower() == 'exit':
            print("Goodbye! Have a nice day!")
            break
        
        try:
            encode_count = int(input("Enter the number of encodings: ").strip())
        except ValueError:
            print(f"That is not a valid value. Enter a valid whole number")
            continue
        
        current_data = normal_text
        
        for i in range(encode_count):
            if isinstance(current_data, str):
                data_bytes = current_data.encode('utf-8')
            else:
                data_bytes = current_data
                
            encoded_bytes = base64.b64encode(data_bytes)
            
            encoded_string = encoded_bytes.decode('utf-8')
            
            current_data = encoded_string
            
            print(f"Layer {i + 1} has been encoded successfully...")
            
        print("Encoding successful!")
        print(f"Total encode count: {encode_count}")
        print(f"Final encoded text: {current_data}")
        
auto_encoder()