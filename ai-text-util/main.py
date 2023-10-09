from flask import Flask, render_template, request
import requests

app = Flask(__name__)
 
@app.route('/')
def indexGet():
  return render_template("index.html",data={})
  
@app.route('/generate', methods=['POST'])
def index():
  url = 'https://article-extractor-and-summarizer.p.rapidapi.com/summarize-text'
  
  if request.method == 'POST':
    givenText = request.form.get('text')
    

    body = { 
      'lang': 'en',
      'text': givenText
    }
    headers = {
      'content-type': 'application/json',
      'X-RapidAPI-Key': '6f3e97e015mshd53ee240a428611p14e653jsn43fcb79a144f',
      'X-RapidAPI-Host': 'article-extractor-and-summarizer.p.rapidapi.com'
    }
    response = requests.post(url, json=body, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
      # Parse the JSON response
      data = response.json()

      return render_template('index.html', data=data)
 

    return "Error While Fetching From API!"


app.run(host='0.0.0.0', port=81)










 