from machine import SPI, Pin
from camera import Camera
from time import sleep_ms, sleep

CAM_SCK = 18
CAM_MISO = 16
CAM_MOSI = 19
CAM_CS = 17



def initialize_camera():
    try:
        spi_bus = SPI(0, sck=Pin(CAM_SCK),
                      miso=Pin(CAM_MISO),
                      mosi=Pin(CAM_MOSI))

        cs = Pin(CAM_CS, Pin.OUT)

        cam = Camera(spi_bus=spi_bus,
                     cs=cs)
        print("Camera initialized succesfully!")
        return cam
    except Exception as e:
        print(f"Error initializing camera: {e}")


def assemble_image(generator, output_file_path):
    with open(output_file_path, 'wb') as image_file:
        for chunk in generator:
            sleep_ms(200)
            image_file.write(chunk)


cam = initialize_camera()
sleep_ms(2000)
cam.capture_jpg()
sleep_ms(2000)
generator = cam.generateJPG(chunk_size=1024)
sleep_ms(2000)
assemble_image(generator, 'output.jpg')