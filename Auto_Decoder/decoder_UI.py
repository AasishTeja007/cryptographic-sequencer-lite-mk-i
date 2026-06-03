# Import function from module
from .decoder_engine import decoder_core

# Decoder UI function
def auto_decoder():
    # Print UI tool name
    print("****CryptoGraphic Sequencer Lite MK-I (Decoder version)****")
    
    # UI core loop
    while True:
        
        # Encoded text input
        encoded_text = input("Enter the encoded_text (or 'exit' to quit): ").strip()
        
        # Exit option with goodbye statement
        if encoded_text.lower() == 'exit':
            print("Goodbye! Have a nice day!")
            break
        
        # Function call
        result_text, count_decode = decoder_core(encoded_text)
        
        # Print success statement
        print("Decoding successful!")
        
        # Print decoded layers count
        print(f"Decoding layers count: {count_decode}")
        
        # Print decoded human readable text
        print(f"Final decoded text: {result_text}")

# __name__ guard or execution guard
if __name__ == "__main__":
    
    # UI function call
    auto_decoder()