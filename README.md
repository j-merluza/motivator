# 🔥 MotivateMe

Motivational quote generator. This is fun little project intended to make people smile but also, wanted to build a small project so I can test out publishing this as a package on GitHub so other users within the company can pip install. This is to help get an idea of how we can build and distribute programs as we move towards having a code base.

Motivational quotes were downloaded from this website url and manually converted to a json file: https://sharpquotes.com/download-45500-famous-motivational-quotes-database-in-excel-and-pdf/#:~:text=Download%2045500%20Famous%20Motivational%20Quotes%20Database%20in%20Excel,class%20is%20running%20the%20country.%20...%20More%20items


# 🔧 Installation

Install this package straight from the GitHub repo. This package was not uploaded to pypi, however can be downloaded using the repo https link like so. This is basically cloning the repo to your site packages but it is also installing the required files based on the distribution and .toml file. 

```
pip install git+https://github.com/j-merluza/motivator.git
```

# ❓ How to use

Open any python file or jupyter notebook.

1. Import

```python
from motivate.me import MotivateMe
```

2. Instantiate the object.

```python
# you can use any variable name here.
motivateme = MotivateMe()
```

3. Call attributes, you can get the quote, author and category.

```python
quote = motivateme.quote
author = motivateme.author

print(f"{quote} - {author}")

```