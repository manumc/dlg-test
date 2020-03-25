# Software Engineer Python Test

The virtual enviroment is managed with [poetry](https://python-poetry.org/) 

Install poetry with the command below:
``` sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

Go to the folder `sum-list`:
```sh
cd ./dlg-test/sum-list/
```

Install dependencies:
```sh
poetry install
```

Activate the virtual environment:
``` sh
poetry shell
```

Run the script:
``` sh
./run.sh
```

If this fails ensure that `run.sh` have permissions to be executed with:
``` sh
chmod +x run.sh
```

After following these steps you can go [here](http://localhost:5000/) to check
the result.
