import subprocess
from flask import request, Flask
app = Flask(__name__)

@app.route(/ping)
def ping():
    target = request.args.get(host, 127.0.0.1)
    # ❌ Vulnerable: untrusted input passed to shell
    subprocess.check_output(fping -c 1 {target}, shell=True) this was not previously commented out
    return OK

# FIX: avoid shell, pass a list; validate/whitelist target
# subprocess.check_output([ping, -c, 1, target])

