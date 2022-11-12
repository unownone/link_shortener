import bjoern
from app import app
import os

bjoern.run(app, "0.0.0.0", int(os.getenv("PORT", 8000)), reuse_port=True)
