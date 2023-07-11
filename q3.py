import time
import matplotlib.pyplot as plt
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
val=[]
cnt = 0
drawnow=1
adc.start_adc(0,gain=GAIN)
print('reading ADS1x15 channel')
plt.ion()

def makefig():
    plt.ylim(-5000,5000)
    plt.title('osciloscope')
    plt.grid(1)
    plt.ylabel('ADC outputs')
    plt.plot(val,'ro-',label='channel 0')
    plt.legend(loc='lower right')
    while(True):
        value = adc.get_last_result()
        print('channel 0:{0}'.format(value))
        time.sleep(int(value))
        drawnow(makefig)
        plt.pause(.000001)
        cnt = cnt+1
        if(cnt>50):
            val.pop(0)