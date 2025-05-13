## MOVIE RECOMMENDATION SYSTEM
This app recommends related movies according to the input provided.

## REQUIREMENTS FOR THIS PROJECT
1. Virtual environment (python3 virtual environment or conda): To run .ipynb file
2. Install numpy, pandas, nltk, sklearn, streamlit and pickle in the virtual environment

Follow these steps to set up the project locally:

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/repository-name.git
cd repository-name
```

## 2. EXTRACT *.ZIP FILES
They are .pkl and .csv files needed for the data.

## 3. Create your API key:

Go to [OMDb API](https://www.omdbapi.com/apikey.aspx) and create your API key.
In app.py, modify the API key variable by replacing 'your_key' with the key you just created:

```python
omdb_api = 'your_key'
```
## 4. RUN THE FOLLOWING COMMAND ON YOUR BASH:
```bash
streamlit run app.py
```
