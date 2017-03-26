#!/usr/bin/env python

import os
import random
from datetime import datetime, timedelta
import string
import subprocess
import sys
from threading import Timer
import time
import urllib

USERNAME = 'user'

user_name = os.getlogin()
cur_dir = os.getcwd()

SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

b_g = "http://lorempixel.com/600/400"


def random_string(N):
    return ''.join(
        random.SystemRandom().choice(
            string.ascii_uppercase + string.digits
        ) for _ in range(N)
    )


def set_desktop_background():
    filename = "/tmp/" + random_string(10) + ".jpg"
    urllib.urlretrieve(b_g, filename)
    process = subprocess.Popen(
        SCRIPT % filename,
        shell=True
    )
    time.sleep(60)
    whats_this()
    try:
        os.remove(filename)
    except OSError:
        pass


def whats_this():
    now = datetime.now()
    rand_time = now + timedelta(
        hours=random.randrange(24),
        minutes=random.randrange(60),
        seconds=random.randrange(60)
    )
    secs = (rand_time - now).total_seconds()
    t = Timer(secs, set_desktop_background)
    t.start()


if user_name == USERNAME and sys.platform == 'darwin':
    # Only for these users on macOS / OSX
    whats_this()
