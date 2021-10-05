## INSTALLATION
**pip install -r requirements.txt**  
<br />

## ABOUT

My first project with use of *Flask*, *html* and *css (at least styling)*.
The purpose of project was to learn basics of mentioned tools.
<br />

### Program uses two types of ciphering:
<br/>

**1. BINARY** -> takes user input and change each of characters into its bianry representation *(file -> b_coder.py)*
<br />

**2. SHIFT (Caesar)** -> takes user input, change each of characters into its ascii representation and adds to each of them given **shift order** (from range 1 - 10 *default=3*) *(file -> s_coder.py)*
<br />

**3. STEGANOGRAPHY** -> takes user input and encodes it into image uploaded by user. To encode/decode *stegano* module were used. *(file -> i_coder.py)*
Used method - LSB *(Least Significant Bit)* *https://pypi.org/project/stegano/*
<br />

## HOW TO
1. Download project / clone git. 
2. Open *cmd/powershell* with project's directory.
3. Make sure you made **INSTALLATION** step.
4. Command: *flask run* 
5. Open shown address.
6. Play around