from .encoder_engine import encoder_core

def auto_encoder():
    print("****CryptoGraphic Sequencer Lite MK-I (Encoder Version)****")
    
    while True:
        normal_text = input("Enter the text (or 'exit' to quit): ").strip()
        
        if normal_text.lower() == 'exit':
            print("Goodbye! Have a nice day!")
            break
        
        try:
            encode_count = int(input("Enter the number of encoding(s): ").strip())
        except ValueError:
            print("The given value is invalid. Enter a valid whole number")
            continue
        
        result_text = encoder_core(normal_text, encode_count)
        
        print("Encoding successful!")
        print(f"Encoding layers count: {encode_count}")
        print(f"Final encoded text: {result_text}")
        
if __name__ == "__main__":
    auto_encoder()