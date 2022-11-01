### How to use
First, go to the root directory and create a virtual environment. The only version I've tested this with is Python 3.8, 
but any later version should work

`python -m venv ./venv`

Next, activate it and install the dependencies

`source ./venv/bin/activate`

`pip install -r requirements.txt`

To run the pipeline, simply run the `pipeline.py` folder.
You will have to have a `.env` file with the `REPLICATE_API_TOKEN` variable though