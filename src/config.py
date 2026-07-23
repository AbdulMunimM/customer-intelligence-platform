from pathlib import Path

# ==========================================================
# PROJECT ROOT
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ==========================================================
# DATA DIRECTORIES
# ==========================================================

DATA = PROJECT_ROOT / "data"

RAW_DATA = DATA / "raw"
PROCESSED_DATA = DATA / "processed"
OUTPUTS = DATA / "outputs"

# ==========================================================
# MODELS
# ==========================================================

MODELS = PROJECT_ROOT / "models"

# ==========================================================
# REPORTS
# ==========================================================

REPORTS = PROJECT_ROOT / "reports"
FIGURES = REPORTS / "figures"

# ==========================================================
# CREATE FOLDERS IF THEY DON'T EXIST
# ==========================================================

RAW_DATA.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA.mkdir(parents=True, exist_ok=True)
OUTPUTS.mkdir(parents=True, exist_ok=True)

MODELS.mkdir(parents=True, exist_ok=True)

REPORTS.mkdir(parents=True, exist_ok=True)
FIGURES.mkdir(parents=True, exist_ok=True)