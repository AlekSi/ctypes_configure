import os
import tempfile
import shutil
import atexit


class TempDir:
    def __init__(self, prefix):
        self.dir = tempfile.mkdtemp(prefix=prefix)
        self.pid = os.getpid()
        atexit.register(self.cleanup)

    def __str__(self):
        return self.dir

    def join(self, fname):
        return os.path.join(self.dir, fname)

    def cleanup(self):
        if self.pid == os.getpid():
            shutil.rmtree(self.dir)
