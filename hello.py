from flask import Flask, render_template, url_for, request, jsonify
import sqlite3
import datetime
import psutil

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        disk= psutil.disk_usage('/').percent

        inserir_valores_no_banco(ram, cpu, disk)

        return jsonify(ram=ram, cpu=cpu, disk=disk)

    return render_template('index.html')


def inserir_valores_no_banco(ram, cpu, disk):
    connection = sqlite3.connect('dados_mainframe.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO data (created, ram, cpu, disk) VALUES (?, ?, ?, ?)', (str(datetime.datetime.now()), ram, cpu, disk))

    connection.commit()
    connection.close()

if __name__ == '__main__':
    app.run(debug=True)