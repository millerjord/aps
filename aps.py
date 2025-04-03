from flask import Flask, request
import platform
import psutil
import socket
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    user_info = {
        'OS Version': platform.platform(),
        'Logged-in User': psutil.users()[0].name if psutil.users() else 'N/A',
        'Hostname': socket.gethostname(),
        'Boot Time': datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"),
    }
    html_content = "<h1>Congratulations, you have successfully been onboared to APS</h1>"
    html_content += "<h3>System Information</h3>"
    html_content += "<ul>"
    for key, value in user_info.items():
        html_content += f"<li><strong>{key}:</strong> {value}</li>"
    html_content += "</ul>"
    
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

