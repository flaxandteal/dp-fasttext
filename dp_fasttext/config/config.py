import os
from dp4py_config.section import Section

# APP Config

APP_CONFIG = Section("App config")
APP_CONFIG.title = "dp-fastText"

ML_CONFIG = Section("ML Config")
ML_CONFIG.supervised_model_filename = os.environ.get("SUPERVISED_MODEL_FILENAME",
                                                     "./test_models/ons_supervised.bin")

ML_CONFIG.unsupervised_model_filename = os.environ.get("UNSUPERVISED_MODEL_FILENAME",
                                                       "./test_models/ons_supervised.vec")
