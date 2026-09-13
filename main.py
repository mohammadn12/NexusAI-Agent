import os
import sys
from flask import Flask

# Flask ऐप को शुरू किया जा रहा है
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="hi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Nexus App - Live</title>
        <style>
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                text-align: center; 
                margin: 0;
                padding-top: 100px; 
                background-color: #0f172a; 
                color: #f8fafc;
            }
            .container {
                max-width: 600px;
                margin: 0 auto;
                background: #1e293b;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            }
            h1 { color: #38bdf8; font-size: 2.5rem; margin-bottom: 10px; }
            p { color: #94a3b8; font-size: 1.2rem; }
            .badge {
                display: inline-block;
                background-color: #22c55e;
                color: white;
                padding: 6px 16px;
                border-radius: 20px;
                font-weight: bold;
                font-size: 0.9rem;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Nexus App Live! 🎉</h1>
            <p>आपकी वेबसाइट Render पर सफलतापूर्वक लाइव हो चुकी है।</p>
            <div class="badge">SUCCESSFUL</div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    # Render के लिए पोर्ट सेट किया गया है
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
