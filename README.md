
# Word Count

How often are different words used in English classical literature?  This study compares the relative word usage in the works of several famous authors.



## Transparency Exercise

This analysis contains clean Python code, but the code is not easily reproducible and the data transformations themselves are not transparant.  In this exercise, we'll try to make it more accessible:

  1. Using DVC, add links to the raw data (the zip file), hosting the data yourself on a DVC remote (e.g. gdrive, ssh, etc).

    - `dvc init`: https://dvc.org/doc/command-reference/init 

    - `dvc add`: https://dvc.org/doc/command-reference/add

    - `dvc remote add`: https://dvc.org/doc/command-reference/remote/add

    - `dvc push`: https://dvc.org/doc/command-reference/push 
    
  2. Add conda info (`environment.yml`) to get code dependencies to run the analysis.
  4. Alter the script so it puts the results into a `results` directory
  4. Alter the script so it puts the data into stages in `data` subdirectories: `data/raw`, `data/processed`, and `data/final`.
  5. Split the script into smaller scripts, breaking it into places that naturally input in the beginning and output at the end.
  6. Make a shell script (.sh or .bat) that calls the scripts in order.  

## Further Reading

  - Cookiecutter Data Science Structure https://drivendata.github.io/cookiecutter-data-science/ 