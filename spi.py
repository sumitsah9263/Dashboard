import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import csv



print("Inside Spi")
def spi1():
    SPI_PORT   = 0
    SPI_DEVICE = 0
    mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


    fieldnames = ["ecg_value"]
    with open('/home/larkai/Downloads/larkai/ecg_data.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    ii=0
    while True:
        # print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
        time.sleep(0.01)
#         print("pushing======================>",mcp.read_adc(0),ii)
        with open('/home/larkai/Downloads/larkai/ecg_data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            info = {"ecg_value": mcp.read_adc(0)}
            csv_writer.writerow(info)
            ii+=1


spi1()
