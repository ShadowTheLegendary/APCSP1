Python project for APCSP class.
Instructions to run:

Install Rust from https://rust-lang.org/tools/install/
Install python

### Clone the repositories ###
```bash
git clone https://github.com/ShadowTheLegendary/APCSP1.git
git clone https://github.com/ShadowTheLegendary/karel-py.git

cd APCSP1
````
### Activate a .venv ###

Windows 11:
```
python -m venv .venv
.venv\Scripts\activate
```
Linux/Mac:
```
python3 -m venv .venv
source .venv/bin/activate
```
### Then ###
```
cd ..
cd karel-py
pip install maturin
maturin develop --release
cd ..
cd APCSP1
```
### Run ###
Windows 11
```
python main.py
```
Linux
```
python3 main.py
```
