### Creating the env - ensure you are running the anaconda `4.5.x +`
```
conda env create -f environment_unit_test.yml
```

### Updating the env after adding new packages
```
conda env update -f environment_unit_test.yml
```

### Starting the env
```
conda activate unit_test_env
```

### Stopping the env
```
conda deactivate
```

### Running Locally - ensure you are using python `3.x +`
```
python app.py
```
