# PACER Notebooks
The PACER Notebooks repository is a collection of introductory Jupyter notebooks for how to interact with a [PACER](https://github.com/NatLabRockies/alfalfa) instance via the [alfalfa-client](https://github.com/NatLabRockies/alfalfa-client) Python library.

## Setup
1. Download this repository and save it to a folder on your computer.
1. Install [poetry](https://python-poetry.org/docs/#installing-with-the-official-installer).
1. Open your command line interface and navigate to this folder.
1. Run `poetry install` (this project requires Python 3.11+ to run)
1. Run `poetry run jupyter lab` to launch JupyterLab or interact with notebooks in an editor (ex: VSCode) that supports Jupyter Notebooks natively.
1. In the browser window with jupyter lab in it select the `twobldgs.ipynb` or the `simple_run.ipynb` file.
1. If you are running the PACER server locally no changes are required. If not, change the `host` in the second cell ('http://localhost' by default) to the url of your PACER server. (Trailing slashes in the URL can lead to errors. This will be fixed in the future but as of now it is still a bug)
1. You can now run the contents of the notebook. (Note: the `twobldgs.ipynb` notebook runs two models simultaneously, this means your PACER server will need at least two workers)

## Installation Troubleshooting
### Poetry is not using the correct version of Python
1. Run `poetry env list` to list the current environments poetry has created
1. If there is one with the incorrect version of python run `poetry env remove {environment name}`
1. Run `poetry env use 3.11` (replace 3.11 with whatever version of python 3.11 or higher you would like to use)
1. If that fails you may need to make sure that you have that version of python installed and if using pyenv make sure it is configured correctly.
1. Run `poetry install` hopefully with no problems this time
