# pdfymerge_from_epson
This small script merges two PDFs (front and backsided) scans from Epsom.

to install make sure you've got a venv:

` python -m venv venv `

activate it:

`.\venv\Scripts\activate`

then run 

`pip install requirements.txt`

# usage

first doc: front page, in order
second doc: back pages, in reverse list order

```
python main.py first_doc_path second_doc_path file_name
```
