import psutil
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

def index():
    cpu_usage = psutil.cpu_percent(interval=1)
    mem_percent = psutil.virtual_memory().percent
    Message = None
    if cpu_usage > 80 or mem_percent > 80:
        Message = "High CPU or Memory usage detected! Please UpScale the server."
    else:
        Message = "CPU and Memory usage are normal."
    return render_template('index.html', cpu_metric=cpu_usage, mem_metric=mem_percent, message=Message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
