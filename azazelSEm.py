import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def display_azazel_sem_image():
    # Load the Azazel SEM image
    azazel_sem_image = mpimg.imread( 'OIG2.jpeg' )

    # Display the image
    plt.imshow(azazel_sem_image)
    plt.show()
