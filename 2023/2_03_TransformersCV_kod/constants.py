## DATA PREPROCESSING CONSTANTS

TARGET_IMAGE_SIZE = 64  # We'll resize input images to this size
PATCH_SIZE = 8   # Size of the patches to be extract from the input images
PATCHES_COUNT = (TARGET_IMAGE_SIZE // PATCH_SIZE) ** 2 # The total number of patches that will be created from each image
PROJECTION_DIMENSIONS = 32 # Encoder output vector size. Each integer will be converted into vector of projection_dim len

# NETWORK CONFIGURATION CONSTANTS

TRANSFORMER_NEURONS_COUNT = PROJECTION_DIMENSIONS # Size of the dense layers in each transformer block
CLASSIFIER_NEURONS_COUNT = 1024 # Size of the deep dense layers of the final classifier
TRANSFORMER_LAYERS = 8 # How many transformer blocks will be generated
HEADS_NUMBER = 4 # Number of heads (h) of each multi-head attention block
DROPOUT_RATE = 0.1 # Droput used throughout the application

# NETWORK TRAINING CONSTANTS

LEARNING_RATE = 0.001
ADAMW_WEIGHT_DECAY = 0.0001
BATCH_SIZE = 256
EPOCHS = 100