from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_ip_info(ip):
    # API fields for detailed data
    url = f"http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,regionName,city,zip,lat,lon,timezone,isp,org,as,query"
    try:
        response = requests.get(url, timeout=5)
        return response.json()
    except:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        ip_address = request.form.get('ip_address')
        if ip_address:
            data = get_ip_info(ip_address.strip())
    
    return render_template('index.html', data=data)

# Vercel needs 'app' to be exported
if __name__ == '__main__':
    app.run(debug=True)