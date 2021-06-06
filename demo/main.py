import pyb, sensor, image, time, math

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)  # we run out of memory if the resolution is much bigger...
sensor.skip_frames(30)
sensor.set_auto_gain(False)         # must turn this off to prevent image washout...
sensor.set_auto_whitebal(False)     # must turn this off to prevent image washout...
clock = time.clock()

uart = pyb.UART(3, 9600, timeout_char = 1000)
uart.init(9600, bits = 8, parity = None, stop = 1, timeout_char = 1000)

while(True):
   img = sensor.snapshot()
   for tag in img.find_apriltags():                     # defaults to TAG36H11
      uart.write(("ID = %d\r\n" % tag.id()).encode())   # 輸出ID