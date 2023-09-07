# BOILER PLATE CODE

### Some recommendation
- Use Linux based system Ubuntu is preferred
- Use `vscode` as IDE
- Install extensions
    - `Python`
    - `Editorconfig`
    - `Makefile Tools`
    - `EditorConfig for VS Code`
    - `Even Better TOML`
    - `black`
    - `isort`

- To install and build the environment run the following
    `make install`
***make should be installed in your system***

- To install any new libraries run the following
    `poetry add <package name>`
***don't directly use pip cause we are using poetry as environment management tool***
***environment should be active***

- on git commit pre-commit will run automatically, pre-commit may have failed
checks and it will fix it but you have to git add and commit again just use the
similar commit message.
