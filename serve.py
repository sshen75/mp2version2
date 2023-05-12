from flask import Flask, request, jsonify
import socket
import subprocess

app = Flask(__name__)

seed = 0

@app.route('/', methods = ['POST', 'GET'])
def resp():
    global seed
    if request.method == 'POST':
        print(f'POST: test')
        # start a separate process for running stress_cpu.py
        subprocess.Popen(['python', 'stress_cpu.py'])
        return 'Stressing CPU...'
    else:
        seed = socket.gethostname();
        print(f'GET: {seed}')
        return str(seed)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)