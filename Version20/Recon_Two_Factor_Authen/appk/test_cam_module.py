# In your other module, import the module that defines the VideoCamera class
from camera import VideoCamera

# Create an instance of the VideoCamera class
camera = VideoCamera()

while True :
    # Call the get_frame method to set the jpeg_tobytes attribute
    camera.get_frame()
    print(camera.Verified)
    print(camera.image.shape)

    # Access the jpeg_tobytes attribute
    # jpeg_bytes = camera.image