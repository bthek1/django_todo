# gunicorn_config.py

import multiprocessing

bind = "0.0.0.0:8000"  # Address and port to bind to
# workers = multiprocessing.cpu_count() * 2 + 1  # Number of worker processes
workers = 1  # Number of worker processes
