import zbarlight
import os
import sys
import PIL

print 'Program Started!'
try:
    print 'Taking picture:'
    qr_count = len(os.listdir('qr_codes'))
    print 'Booting System: with counter:', qr_count
    os.system('sudo fswebcam -d /dev/video'+sys.argv[0]+' -q qr_codes/qr_'+str(qr_count)+'.jpg')
    print 'Picture taken!'
    picture_taken = True;

except:
    picture_taken = False;
    print 'Picture couldn\'t be taken because', sys.exc_info()[0]


if (picture_taken):
    print 'Scanning image...'
    f = open('qr_codes/qr_'+str(qr_count)+'.jpg','rb')
    qr = PIL.Image.open(f);
    qr.load()

    codes = zbarlight.scan_codes('qrcode',qr)
    if(codes==None):
        os.remove('qr_codes/qr_'+str(qr_count)+'.jpg')
        print 'No QR code found'
    else:
        print 'QR code(s):'
        print codes
        f = open('qr_code_messages.txt','a')
        for i in range(len(codes)):
            f.write(codes[i])
            if(i!=len(codes)-1):
                f.write('^')
        f.write('~')
