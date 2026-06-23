from pathlib import Path

WEBAPP_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = WEBAPP_DIR.parent

MODEL_PATH = PROJECT_ROOT / "results_class_weight" / "final" / "mosquito_convnextv2_tiny_final.pth"
TEST_METRICS_PATH = PROJECT_ROOT / "results_class_weight" / "final" / "test_metrics.json"
CV_BEST_PARAMS_PATH = PROJECT_ROOT / "results_class_weight" / "cv" / "cv_best_params.json"

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif", ".tif", ".tiff"}
MAX_UPLOAD_MB = 16
TOP_K = 5

IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]
