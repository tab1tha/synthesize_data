The purpose of this repo is to explore data synthesizers.

## setup
Install the ipykernel extension in order to be able to run the Jupyter notebooks. VS code will prompt you to do this when you open the folder for the first time.

## DataSynthesizer
[docs](https://github.com/DataResponsibly/DataSynthesizer/blob/master/notebooks/DataSynthesizer__correlated_attribute_mode.ipynb)
- independent attribute mode works well. The variation of the variables in the synthetic dataset are similar to those in the original dataset.
- correlated attribute mode fails to work in Pyodide. It seems to require multiprocessing which is not supported by Pyodide.
