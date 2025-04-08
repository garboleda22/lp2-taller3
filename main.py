from flask import Flask, render_template, redirect
import pandas as pd

# Buscar en ThingSpeak estaciones meteorológicas:
# https://thingspeak.mathworks.com/channels/public
# Ejemplos:
# https://thingspeak.mathworks.com/channels/870845
# https://thingspeak.mathworks.com/channels/1293177
# https://thingspeak.mathworks.com/channels/12397

URLs = [
  "https://thingspeak.mathworks.com/channels/870845/feeds.csv:8000"
  "https://thingspeak.mathworks.com/channels/1293177/feeds.csv:8000"
  "https://thingspeak.mathworks.com/channels/12397/feeds.csv:8000"
]

app = Flask(__name__)

def descargar (url);
  df = pd.read_csv(url)
  df["created_at"] = pd.to_datetime (df["created_at"])
  df.drop(["entry_ed", "field5", "field6"])

@app.route("/")
def index ():
  return render_template("index.html")

# Programa Principal
if __name__ == '__main__':   
  for url in URLs:
    descargar(url)s
  # Ejecuta la app
  app.run(host='0.0.0.0', debug=True)
