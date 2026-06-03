# Import base64 library
import base64

# Auto encoder function
def auto_encoder():
    # Print UI tool name
    print("****CryptoGraphic Sequencer Lite MK-I (Encoder Version)****")
    
    # Encoder UI loop
    while True:
        
        # Normal text input
        normal_text = input("Enter the normal text (or 'exit' to quit): ").strip()
        
        # Exit option with goodbye statement
        if normal_text.lower() == 'exit':
            print("Goodbye! Have a nice day!")
            break
        
        # Error handling block
        try:
            # Encode layer count input
            encode_count = int(input("Enter the number of encodings: ").strip())
        
        # Catch value error and continue    
        except ValueError:
            print(f"That is not a valid value. Enter a valid whole number")
            continue
        
        # Initialize normal text input to current data
        current_data = normal_text
        
        # Encoder core loop
        for i in range(encode_count):
            
            # Check data type of current data
            if isinstance(current_data, str):
                # If string, convert string to raw bytes
                data_bytes = current_data.encode('utf-8')
            else:
                # Else, bytes stay intact
                data_bytes = current_data
            
            # Encode the raw bytes
            encoded_bytes = base64.b64encode(data_bytes)
            
            # Convert the encoded bytes to encoded string
            encoded_string = encoded_bytes.decode('utf-8')
            
            # Update current data with encoded string
            current_data = encoded_string
            
            # Print layer encode success statement
            print(f"Layer {i + 1} has been encoded successfully...")
        
        # Print success statement    
        print("Encoding successful!")
        
        # Print encoded layers count
        print(f"Total encode count: {encode_count}")
        
        # Print final encoded non-human readable text
        print(f"Final encoded text: {current_data}")

# __name__ guard or execution guard        
if __name__ == "__main__":
    
    # Encoder function call
    auto_encoder()