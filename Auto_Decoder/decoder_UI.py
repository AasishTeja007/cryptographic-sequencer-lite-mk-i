from .decoder_engine import decoder_core

def auto_decoder():
    print("****CryptoGraphic Sequencer Lite MK-I (Decoder version)****")
    
    while True:
        encoded_text = input("Enter the encoded_text (or 'exit' to quit): ").strip()
        
        if encoded_text.lower() == 'exit':
            print("Goodbye! Have a nice day!")
            break
        
        result_text, count_decode = decoder_core(encoded_text)
        
        print("Decoding successful!")
        print(f"Decoding layers count: {count_decode}")
        print(f"Final decoded text: {result_text}")
        
if __name__ == "__main__":
    auto_decoder()