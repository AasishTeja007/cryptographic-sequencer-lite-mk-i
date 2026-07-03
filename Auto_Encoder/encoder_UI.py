# Relative import function from module
from .encoder_engine import encoder_core

# Encoder UI function
def auto_encoder():
    # Print UI tool name
    print("****CryptoGraphic Sequencer Lite MK-I (Encoder Version)****")
    
    # UI core loop
    while True:
        # Normal text input
        normal_text = input("Enter the text (or 'exit' to quit): ").strip()
        
        # Exit option with goodbye statement
        if normal_text.lower() == 'exit':
            print("Goodbye! Have a nice day!")
            break
        
        # Error handling block
        try:
            # Encode layers count input
            encode_count = int(input("Enter the number of encoding(s): ").strip())
            
            # Secret key value input
            encrypt_count = int(input("Enter the encryption count: ").strip())
        
        # Catch value error and continue    
        except ValueError:
            print("The given value is invalid. Enter a valid whole number")
            continue
        
        # Function call
        result_text = encoder_core(normal_text, encode_count, encrypt_count)
        
        # Print success statement
        print("Encoding successful!")
        
        # Print encoded layers count
        print(f"Encoding layers count: {encode_count}")
        
        # Print encoded non-human readable text
        print(f"Final encoded text: {result_text}")

# __name__ guard or execution guard        
if __name__ == "__main__":
    
    # UI function call
    auto_encoder()