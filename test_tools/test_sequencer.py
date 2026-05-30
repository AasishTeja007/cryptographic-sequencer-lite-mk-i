import pytest
from Auto_Encoder.encoder_engine import encoder_core
from Auto_Decoder.decoder_engine import decoder_core

@pytest.mark.parametrize("test_layers", [1, 3, 5, 10, 20, 40])
def test_twin_tools(secret_text, test_layers):
    
    scrambled_text = encoder_core(secret_text, test_layers)
    
    recovered_text, recovered_count = decoder_core(scrambled_text)
    
    assert recovered_text == secret_text, "The decoded text does not match the original string!"
    assert recovered_count == test_layers, f"Expected {test_layers} layers to be stripped but got {recovered_count}"