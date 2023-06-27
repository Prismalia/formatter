# Prismalia Formatter

The ultimate Prismalia formatter for Python.

## How to install?

Follow these steps to install and use the Prismalia formatter.

1. Clone this repo
2. Run `make install`

### VSCode integration

To integrate the formatter with VSCode:

1. Install the black extension
2. Go into Settings (ctrl-,) and search for black
3. Under `Python > Formatting: Black Path` add /home/yann/.local/bin/pformat. Replace yann with your name.

### Vim integration

[Complete this section.]

## Practical advice

As a personal preference, I like to bind the formatter to `<C-c> f`. This
particular binding is optional but having one is not! To go faster, make sure
to have this functionality a couple of key strokes away.

## What's under the hood?

### cblack - The uncompromising Python formatter*

### isort

### move_imports


## Contribution

This is a collaborative effort to improve the code quality of our Python scripts.
As a result, your help and contribution is welcome. Before merging your branch,
document all your changes and make sure the tests are green. Happy coding!


### TODO

-   Ignore move_imports when encountering #FMT: off
