from .animatediff.logger import logger
from .animatediff.nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
from .animatediff.model_utils import get_available_motion_models, Folders
import folder_paths

if len(get_available_motion_models()) == 0:
    logger.error(f"No motion models found. Please download one and place in: {folder_paths.get_folder_paths(Folders.ANIMATEDIFF_MODELS)}")

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
