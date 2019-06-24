# Citizenship Exploratory Visualizations

This is a repository containing a tool to create a word adjacency graph along with a webpage to show linked proficiency levels and visualize it all.

## Getting Started

These instructions will get you up and running on your local computer so you can change certain parameters and see how the graph looks

### Prerequisites

First, set up a python3 virtual environment

```
python3 -m venv /path/to/new/virtual/environment
source /path/to/new/virtual/environment/bin/activate
```

### Installing

Install the necessary python packages to run the create file with pip

```
pip install gensim
pip install collections
pip install nltk
pip install numpy
```



## Creating the data

To create an updated data.json file, run create.py

```
python create.py
```

### Changing create.py parameters

you can change three things in the create.py file to alter the graph. 

* the words that are removed from the corpus before we process any data, stored in the 's' variable on line 15
* the minumum number of times a pair of words must co-occurr within the window size to create a link in the graph, stored in the 'minumum_count_for_link' variable on line 20
* the size of the window, to create co-occurrence, this will look at the window-sized words before and after each word in the documents. Stored in word_window variable at line 21


## Running the Server

Once you have the new data.json file, generated, you can run the server to view it. From that same directory run:

```
python -m http.server
```

now go to http://localhost:8000/ on your favorite browser and you should see the new graph. If it looks unchanged sometimes it is cached in the browser, so open developer tools and reload the page to disable caching.

