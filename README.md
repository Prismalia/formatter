# Prismalia Formatter
The ultimate Prismalia formatter for Python

## How to install?
Follow these steps to install and use the Prismalia formatter.

1. Clone this repo
2. Run `make install`

### VSCode integration
To integrate the formatter with VSCode:
1. Install the black extension
2. Go into Settings (ctrl-,) and search for black
3. Under `Python > Formatting: Black Path` add /home/yann/.local/bin/pformat. Replace yann with your name.


## Contribution
This is a collaborative effort to improve the code quality of our Python scripts.
As a result, your help and contribution is welcome. Before merging your branch,
document all your changes and make sure the tests are green. Happy coding!

### TODO
- Ignore move_imports when encountering #FMT: off
