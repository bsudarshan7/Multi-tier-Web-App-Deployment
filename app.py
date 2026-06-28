from flask import Flask, render_template
import psutil
import socket
import platform
from datetime import datetime
from database import save_metrics, get_metrics

app = Flask(__name__)


@app.route("/")
def dashboard():

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    hostname = socket.gethostname()

    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    os_name = platform.system()
    os_version = platform.release()
    processor = platform.processor()

    save_metrics(
        hostname,
        cpu,
        memory,
        disk
    )

    return render_template(
        "dashboard.html",
        cpu=cpu,
        memory=memory,
        disk=disk,
        hostname=hostname,
        current_time=current_time,
        os_name=os_name,
        os_version=os_version,
        processor=processor
    )


@app.route("/history")
def history():

    records = get_metrics()

    return render_template(
        "history.html",
        records=records
    )


if __name__ == "__main__":
    app.run(debug=True)