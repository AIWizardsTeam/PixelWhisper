from .dependency import *

def add_gauss_noise(encode_image, **kwargs):
    """
        Add Gaussian noise to the image.

        Parameters
        ----------
        mean : float, optional
        Mean of the Gaussian distribution to generate noise (default is 0).
        var : float, optional
        Variance of the Gaussian distribution to generate noise (default is 0.1).
    """
    mean = kwargs.get('mean', 0)
    var = kwargs.get('var', 0.1)
    sigma = var**0.5
    gauss = np.random.normal(mean, sigma, encode_image.shape)
    return encode_image +  gauss
    

def median_filter(noise_image, filter_size):
    image = cv2.copyMakeBorder(noise_image, 0, 0, 0, 0, cv2.BORDER_CONSTANT)
    return cv2.medianBlur(image, filter_size)
