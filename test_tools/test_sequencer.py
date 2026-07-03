# Import pytest library
import pytest

# From folder import function
from Auto_Encoder.encoder_engine import encoder_core

# From folder import function
from Auto_Decoder.decoder_engine import decoder_core

# Create parameters to test the encoder and decoder with parameters of layers and keys
@pytest.mark.parametrize("test_layers", [1, 3, 5, 10, 20, 40])
@pytest.mark.parametrize("secret_key", [1, 2, 4, 10, 24, 42])

# Parameterize function
def test_twin_tools(secret_text, test_layers, secret_key):
    
    # Encoder function call
    scrambled_text = encoder_core(secret_text, test_layers, secret_key)
    
    # Decoder function call
    recovered_text, recovered_count = decoder_core(scrambled_text, secret_key)
    
    # Test if decoded text is given normal text input (also with failed case statement)
    assert recovered_text == secret_text, "The decoded text does not match the original string!"
    
    # Test if decode count is same number of given test parameters (also with failed case statement)
    assert recovered_count == test_layers, f"Expected {test_layers} layers to be stripped but got {recovered_count}"