# A Dockerfile is a text document that contains all the commands
# a user could call on the command line to assemble an image.

FROM python:3.9.4-buster

# Our Debian with python is now installed.
# Imagine we have folders /sys, /tmp, /bin etc. there
# like we would install this system on our laptop.

RUN mkdir app

# We create folder named build for our stuff.

WORKDIR /app

# Basic WORKDIR is just /
# Now we just want to our WORKDIR to be /build

COPY . .

# FROM [path to files from the folder we run docker run]
# TO [current WORKDIR]
# to the WORKDIR

RUN pip install --no-cache-dir -r requirements.txt

# OK, now we pip install our requirements

EXPOSE 8000

# Now we just want to our WORKDIR to be /build/app for simplicity
# We could skip this part and then type
# python -m uvicorn main.app:app ... below


CMD python ./backend/main.py

# This command runs our uvicorn server
# See Troubleshoots to understand why we need to type in --host 0.0.0.0 and --port 80