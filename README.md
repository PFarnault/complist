# complist
complist is a python tool creating an incidence matrix out of several list files.  

## Description of the package
complist retrieve unique values from multiple .xlsx, .xls and .csv files that are in the `data/` folder. These files are asumed to be one-dimensional lists of values which correspond to vertices of a graph, you can see the files that are currently in the `data` folder for examples. Note that the function will absorb any entry as a point of interest which means that headers should be removed if your lists have some. Generated column of the incidence matrix are named after the files' names. 

## Usage
Use the `.yml` file to load the dependencies with your local python distribution. Activate it, then the function should be called the following way: 
```{cmd}
python main.py <data-dir> [--format] [--output] 
```
`<data-dir` is the path to the input folder, in this case `data/` but you can change it if you need. 

`[--format]` is an option to determine the file extension, it currently accept `"excel"` and `"csv"` and the default option is the excel

`[--output]` is an option to determine the output file. Make sure that the extension name you choose is coherent with the --format option. Default output is `complist.xlsx`. 

## remarks 

- The incidence matrix only tell if two elements are linked, it does not mention any direction or weights. 



