
import os
os.environ["SM_FRAMEWORK"] = "tf.keras"

import segmentation_models as sm

import os
import cv2

import numpy as np
from matplotlib import pyplot as plt

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
from smooth_tiled_predictions import predict_img_with_smooth_windowing




def MODEL(path_image, path_model="sea-land_30_epochs_RESNET_backbone_batch16.hdf5"):
    BACKBONE = 'resnet34'
    preprocess_input = sm.get_preprocessing(BACKBONE)

    img = cv2.imread(path_image)  # N-34-66-C-c-4-3.tif, N-34-97-D-c-2-4.tif
    input_img = scaler.fit_transform(img.reshape(-1, img.shape[-1])).reshape(img.shape)
    input_img = preprocess_input(input_img)

# original_mask = cv2.imread("masks/im_2.tif")
# original_mask = original_mask[:,:,0]  #Use only single channel...
# #original_mask = to_categorical(original_mask, num_classes=n_classes)

    from keras.models import load_model

    model = load_model(path_model, compile=False)

    # size of patches
    patch_size = 256

    # Number of classes
    n_classes = 2

###################################################################################
    # Predict using smooth blending

    # Use the algorithm. The `pred_func` is passed and will process all the image 8-fold by tiling small patches with overlap, called once with all those image as a batch outer dimension.
    # Note that model.predict(...) accepts a 4D tensor of shape (batch, x, y, nb_channels), such as a Keras model.
    predictions_smooth = predict_img_with_smooth_windowing(
        input_img,
        window_size=patch_size,
        subdivisions=2,  # Minimal amount of overlap for windowing. Must be an even number.
        nb_classes=n_classes,
        pred_func=(
            lambda img_batch_subdiv: model.predict((img_batch_subdiv))
        )
    )

    final_prediction = np.argmax(predictions_smooth, axis=2)

    # Save prediction and original mask for comparison
    head_tail = os.path.split(path_image)
    # عدد الpathes ال فوق لحد ال folder ال فيه folder image, mask, histogram
    first = head_tail[0].split('/')[:-1]
    first = '/'.join([str(elem) for elem in first])
    last = head_tail[1].split('.')
    # must be create folder name masks
    file_path_mask = first + '/masks/' + last[0] + '.png'
    plt.imsave(file_path_mask, final_prediction)
