# Import base64 library
import base64

# Decoder function
def auto_decoder():
    # Print UI tool name
    print("****CryptoGraphic Sequencer MK-I (Decoder Version)****")
    
    # Decoder UI loop
    while True:
        
        # Encoded text input
        encoded_text = input("Enter the encoded text (or 'exit' to quit): ").strip()
        
        # Exit option with goodbye statement
        if encoded_text.lower() == 'exit':
            print("Goodbye! Have a nice day!")
            break
        
        # Initialize encoded text input to current data
        current_data = encoded_text
        
        # Initialize decode count to zero
        decode_count = 0
        
        # Decoder core loop
        while True:
            
            # Error handling block
            try:
                # Check data type of current data
                if isinstance(current_data, str):
                    # If string, convert encoded string to raw encoded bytes
                    data_bytes = current_data.encode('utf-8')
                else:
                    # Else, encoded bytes stay intact
                    data_bytes = current_data
                
                # Decode the encoded bytes    
                decoded_bytes = base64.b64decode(data_bytes)
                
                # Convert the decoded bytes to decoded string
                decoded_string = decoded_bytes.decode('utf-8')
                
                # Safety check for infinity loop
                if decoded_string == current_data:
                    break
                
                # Update current data with decoded string
                current_data = decoded_string
                
                # Update the decode count with each one iteration
                decode_count += 1
                
                # Print layer decode success statement
                print(f"Layer {decode_count} has been decoded successfully...")
            
            # Safety exit when input is corrupted    
            except Exception:
                break
        
        # Check if decode count is greater than zero    
        if decode_count > 0:
            
            # If yes, print decode success statement
            print("Decoding successful!")
            
            # Print decoded layers count
            print(f"Total decode count: {decode_count}")
            
            # Print final decoded human readable text
            print(f"Final decoded text: {current_data}")
        else:
            # Else, print fail safe statement
            print("Text decoding failed. This might not be Base64")
            
# __name__guard or execution guard
if __name__ == "__main__":
    
    # Decoder function call
    auto_decoder()