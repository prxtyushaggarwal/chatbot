# app2.py is an alias to app.py for standard execution
import runpy
from pathlib import Path

app_path = Path(__file__).parent / "app.py"
runpy.run_path(str(app_path), run_name="__main__")
