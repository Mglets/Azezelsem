
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def display_trimix_image():
    # Load the Trimix image
    trimix_image = mpimg.imread( 0102.jpeg)

    # Display the image
    plt.imshow(trimix_image)
    plt.show()
