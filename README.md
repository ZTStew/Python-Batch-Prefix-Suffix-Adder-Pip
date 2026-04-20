# Python Batch Prefix Suffix Adder (Pip)
---
## Description:
Program adds a user specified Prefix or Suffix to all files or every directory in the working directory

---
## Usage:
(explanation of how to use the program)
1. Navigate to desired folder in terminal
2. Run `add_prefix` || `prefix` || `add_suffix` || `suffix` + required arguments
3. *Files get automatically renamed*

---
## Arguments:
- `--help`: (Optional) Lists all program arguments
- `--test`: (Optional) Declare if the application should run in test mode [0 -> production (default) | 1 -> test mode].
- `--prefix`: (Optional) Declares that the user given prefix should be added
- `--suffix`: (Optional) Declares that the user given suffix should be added
- `--type`: (Required) Identifies if program will add the prefix/suffix to files or directories

---
## Test Settings:
python main.py -t 1 -pf _ -sf 11 -ty file
python main.py -t 1 -pf _ -sf 11 -ty dir

---
## Program Installation:
Program functions using `pip`'s install tool
- Creating executable: run `pip install .` in `./Python-Batch-Prefix-Suffix-Adder-Pip`
