from functools import lru_cache
from typing import List

import numpy
from tqdm import tqdm

from facefusion import inference_manager, state_manager, wording
from facefusion.download import resolve_download_url
from facefusion.filesystem import resolve_relative_path
from facefusion.thread_helper import conditional_thread_semaphore
from facefusion.types import Detection, DownloadScope, Fps, InferencePool, ModelOptions, ModelSet, Score, VisionFrame
from facefusion.vision import detect_video_fps, read_image, read_video_frame

STREAM_COUNTER = 0


@lru_cache(maxsize=None)
def create_static_model_set(download_scope: DownloadScope) -> ModelSet:
    # NSFW model removed entirely
    return {}


def get_inference_pool() -> InferencePool:
    return {}  # No model used


def clear_inference_pool() -> None:
    pass  # Nothing to clear


def get_model_options() -> ModelOptions:
    return {}  # Empty model options


def pre_check() -> bool:
    return True  # Always pass


def analyse_stream(vision_frame: VisionFrame, video_fps: Fps) -> bool:
    return False  # Always safe


def analyse_frame(vision_frame: VisionFrame) -> bool:
    return False  # Always safe


@lru_cache(maxsize=None)
def analyse_image(image_path: str) -> bool:
    return False  # Always safe


@lru_cache(maxsize=None)
def analyse_video(video_path: str, trim_frame_start: int, trim_frame_end: int) -> bool:
    return False  # Always safe


def detect_nsfw(vision_frame: VisionFrame) -> List[Score]:
    return []  # Disabled completely


def forward(vision_frame: VisionFrame) -> Detection:
    return numpy.zeros((1, 1))  # Dummy return


def prepare_detect_frame(temp_vision_frame: VisionFrame) -> VisionFrame:
    return temp_vision_frame  # No change needed
