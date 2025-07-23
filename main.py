from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

GRAPH_API_URL = "https://graph.facebook.com/v18.0"

# Updated HTML & CSS Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Token Checker by Sʌɱɘɘʀ</title>
       <link rel="stylesheet" href="/css/tokenCheck.css">
          <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background: linear-gradient(to right, #FF00FF, #BA55D3, #9370DB);
            background-size: cover;
            color: white;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 90%;
            max-width: 400px;
            margin: 100px auto;
            padding: 20px;
            background: rgba(0, 0, 0, 0.7);
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.3);
        }
        h2 {
            margin-bottom: 20px;
            font-size: 22px;
            text-transform: uppercase;
        }
        input {
            width: 90%;
            padding: 10px;
            margin: 10px 0;
            border: none;
            background: black;
            color: white;
            border-radius: 5px;
            text-align: center;
        }
        button {
            width: 95%;
            padding: 10px;
            background: blue;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 10px;
        }
        button:hover {
            background: linear-gradient(45deg, #007e33, #00c851);;
        }
        .result {
            margin-top: 20px;
            padding: 10px;
            background: gray;
            border-radius: 5px;
            color: white;
    }
        li {
        margin: 10px 0;
        padding: 5px;
    }
      
    </style>
</head>
<body>
    <div class="container">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css"
        integrity="sha512-Evv84Mr4kqVGRNSgIGL/F/aIDqQb7xQ2vcrdIwxfjThSH8CSR7PBEakCr51Ck+w+/U6swU2Im1vVX0SVk9ABhg=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link href="https://fonts.googleapis.com/css?family=Roboto:400,700&display=swap" rel="stylesheet">
</head>

<body>
    <div class="container">
        <h1>Token Checker by Sʌɱɘɘʀ</h1>
        <form action="/token-check" method="POST">
            <label for="accessToken">Access Token :-</label>
            <input type="text" id="accessToken" name="accessToken" placeholder="Paste your token" required>
            <button type="submit">
                <i class="fas fa-check-circle token-icon"></i> <span>Check Token</span>
            </button>
        </form>
        <div class="lastBtns">
            <a href="/">
                <i class="fas fa-arrow-left"></i> Go Back
            </a>
            <a href="https://www.facebook.com/TechnicalFyter" target="_blank">
                <i class="fa-brands fa-facebook"></i> Sʌɱɘɘʀ Sīīƞs
            </a>
        </div>
    </div>
</body>

</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        access_token = request.form.get('token')

        if not access_token:
            return render_template_string(HTML_TEMPLATE, error="Token is required")

        url = f"{GRAPH_API_URL}/me/conversations?fields=id,name&access_token={access_token}"

        try:
            response = requests.get(url)
            data = response.json()

            if "data" in data:
                return render_template_string(HTML_TEMPLATE, groups=data["data"])
            else:
                return render_template_string(HTML_TEMPLATE, error="Invalid token or no Messenger groups found")
        
        except Exception as e:
            return render_template_string(HTML_TEMPLATE, error="Something went wrong")

    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    print("🔥 Flask server started on port 5000...")
    app.run(host="0.0.0.0", port=5000, debug=True)
