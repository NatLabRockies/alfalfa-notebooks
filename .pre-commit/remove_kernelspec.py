# When sharing ipynb files, the files have a few settings that are
# specific to the user that are not removed by the nbstripout pre-commit file.
# This script is run with pre-commit and removes the kernelspec and language_info
# from the ipynb files.
# Author: Nicholas Long

# To use, place this file in a .pre-commit file in the root. Add
# the following to the .pre-commit-config.yaml

#   - repo: local
#     hooks:
#       - id: remove-version-metadata
#         name: remove version metadata from ipynb files
#         entry: python .pre-commit/remove_kernelspec.py
#         language: system
#         types: [jupyter]


import sys

import nbformat


def remove_kernelspec(filepath):
    with open(filepath, encoding="utf-8") as f:
        notebook = nbformat.read(f, as_version=nbformat.NO_CONVERT)

    # Remove metadata.kernelspec
    if notebook.get("metadata", {}).get("kernelspec"):
        del notebook["metadata"]["kernelspec"]

    # Remove the python version too
    if notebook.get("metadata", {}).get("language_info", {}).get("version"):
        del notebook["metadata"]["language_info"]["version"]

    # Save the cleaned notebook
    with open(filepath, "w", encoding="utf-8") as f:
        nbformat.write(notebook, f)


if __name__ == "__main__":
    for file in sys.argv[1:]:
        remove_kernelspec(file)
