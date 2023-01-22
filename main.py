# dump-environment


import os
import logging

import sanic


""" 
Environment
"""
DEBUG_MODE = os.getenv('DEBUG','false') == "true"                           # Enable global DEBUG logging
DEV_MODE = os.getenv('DEV_MODE','false') == "true"                          # Sanic develpoment mode

SECRET = os.getenv('SECRET','')

LOGFORMAT = "%(asctime)s %(funcName)-10s [%(levelname)s] %(message)s"       # Log format


app = sanic.Sanic("dump-environment")       # A Sanic instance


@app.route("/", methods=['GET'])
async def handler(request):
    e = [f"{k} = {v}" for k,v in os.environ.items()]
    return sanic.text("\n".join(e)+"\n")


def main():
    # Enable logging. INFO is default
    logging.basicConfig(level=logging.DEBUG if DEBUG_MODE else logging.INFO, format=LOGFORMAT)     # Default logging level

    app.run(host="0.0.0.0", port=8000, access_log=DEBUG_MODE, motd=DEBUG_MODE, dev=DEV_MODE)      # Run a single worker on port 8000


if __name__ == '__main__':
    main()