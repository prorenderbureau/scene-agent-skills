"""Convenience entry point; canonical adapter is bundled with scene-toolkit."""
from pathlib import Path
import runpy

if __name__=='__main__':
    runpy.run_path(str(Path(__file__).resolve().parents[1]/'skills/scene-toolkit/scripts/archicad_inventory.py'),run_name='__main__')
