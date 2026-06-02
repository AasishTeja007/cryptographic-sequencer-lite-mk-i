# CryptoGraphic Sequencer Lite MK-I (Base64 Version)

* A custom twin set of automated data conversion utilities designed to handle `multi encoding and decoding` of `base64 scheme` which can be hectic and time consuming when done manaully. Inspired by `Batman's arkham gadgets` and `Ironman's suits`. `Lite` name is used as this twin suite does encoding and decoding of base64 layers but not encryption and decryption. This custom twin tools suite only `encodes` or `decodes` normal text only. Can't encode or decode images and videos.

* This repository also includes testing using `pytest`, `fixtures` and `parameterization` with multiple test inputs. It serves as a portfolio for `SDET(Software Development Engineer in Test)` showcasing clean data structures, modular design with python and automation framework.

* Also included prototypes of both encoder and decoder which shows initial stage development of these custom twin tools. This utility suite was specifically built to automate the repetative multi encoding and decoding in ctf games like `OverTheWire(OTW)` and in that `Bandit` challenge.

## Security Liability Disclaimer

* This custom utility is developed strictly for `educational purposes`, `CTF wargaming automation` and `authorized security validation exercises`. The author assumes no liability for any `unauthorized` or `improper` or `malicious` utilization of this software. All architectural components and concepts were engineered to demonstrate `data automation`, `data conversion` and `robust testing frameworks`.

## Key Features

* **Twin-Utility Suite:** Robust twin suite including a `deterministic encoder` and a `heuristic decoder`.
* **Deterministic Encoder:** Converts human-readable text into encoded text by adding user-defined number of `base64` layers with `for loop`.
* **Heuristic Decoder:** Converts encoded text back into human-readable text by peeling of all the `base64` layers autonomously with `while loop`.
* **Robust Modular Framework:** `Engine` and `UI` of both `Encoder` and `Decoder` are engineered separately and used `try/except` block to catch errors without breaking the loop.

## Cybersecurity and Purple team operator architecture

* The custom twin tools suite security utility was engineered to replicate both real world offensive and defensive security operations, showing the `Purple Team` lifecycle.

* **Offensive Simulation (Red Team):** Threat actors or Red team operators frequently use multi-layered data obfuscation to infiltrate the malicious payload to bypass network detection layers and anti-virus software. This custom `Deterministic Encoder` simulates this process by dynamically adding user-defined base64 layers to the text autonomously, making it hard to be detected and completely unreadable to humans.

* **Defensive Simulation (Blue Team):** Cyber defenders or Blue team operators frequently use multi-layered deobfuscation when a suspicious payload is detected inside network logs to remove the layers to detect actual payload as manual decoding wastes time in critical situations. This custom `Heuristic Decoder` simulates this process by rapidly peeling away the base64 layers autonomously until the human-readable payload is exposed which saves critical time and completely readable to humans.

## High tech automated testing armor architecture

* The entire data pipeline is tested using `pytest` utilized automation suite combining with fixture and parameterization for battle testing with clean data and multiple inputs.

* **Framework:** Testing is done with `pytest` framework. The command used to run the test is `python -m pytest -v`.
* **Design Patterns:** Testing done by test text `secret message` using `fixture` and with test values (or layers) `1, 3, 5, 10, 20, 40` using `parameterization` while the fixture is shared through `conftest` file.
* **Execution Flags:** The flags used in this command are - `-m` in python which is `module (or library module)` to search for pytest module in current environment. `-v` in pytest for `verbose mode` to give result as passed or failed.

## Project Architecture

```text
CryptoGraphic Sequencer Lite MK-I (Base64 Version)/
├── Auto_Decoder/                 # Decoder package folder
│   ├── __init__.py               # Python package
│   ├── decoder_engine.py         # Core logic engine
│   └── decoder_UI.py             # Interactive terminal UI
├── Auto_Encoder/                 # Encoder package folder
│   ├── __init__.py               # Python package
│   ├── encoder_engine.py         # Core logic engine
│   └── encoder_UI.py             # Interactive terminal UI
├── test_tools/                   # Test directory
│   ├── conftest.py               # Shared Ironman and Batman fixture
│   └── test_sequencer.py         # Parameterized test cases
├── .gitignore                    # Protects repository from local environment and cache files
├── decoder_prototype.py          # Original decoder initial development version
├── encoder_prototype.py          # Original encoder initial development version
└── requirements.txt              # Required project dependencies (pytest==9.0.3)
```

## Local Installation and Setup

1. Clone the repository to your local machine and navigate to the project work.
2. Initialize and activate your virtual environment:
```bash
python -m venv .venv
.venv/Scripts/activate
```
3. Install dependencies:
```bash
python -m pip install -r requirements.txt
```
4. Execute the test suite
```bash
python -m pytest -v
```