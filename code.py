import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image
from numpy import uint8

class mouseParam:
    def __init__(self, input_img_name):
        self.mouseEvent = {"w":None, "h":None, "event":None} #マウス入力用のパラメータ
        cv2.setMouseCallback(input_img_name, self.__CallBackFunc, None) #マウス入力の設定
    
    def __CallBackFunc(self, eventType, w, h, flags, userdata): #コールバック関数 
        self.mouseEvent["w"] = w
        self.mouseEvent["h"] = h
        self.mouseEvent["event"] = eventType
    
    def getEvent(self): #マウスイベントを返す関数
        return self.mouseEvent["event"]                

    def getPos(self): #xとyの座標を返す関数
        return (self.mouseEvent["h"], self.mouseEvent["w"])


if __name__ == "__main__":
    plt.ion() #インタラクティブモードを有効にする
    image = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE) #入力画像をグレースケールに変換しimageにセット
    cv2.imshow("original", image)
    
    S1 = S2 = S3 = S14 = np.zeros(shape=(image.shape)) #配列の初期化

    fshift = np.fft.fftshift(np.fft.fft2(image)) #フーリエ変換
    mag = 20*np.log(np.abs(fshift))
    mag2 = (mag - np.min(mag)) * 255 / (np.max(mag) - np.min(mag))
    newma = np.uint8(mag2)
    cv2.imshow("fft",newma)
    
    cv2.imshow("click",S2) #コールバックの設定
    mouseData = mouseParam("click")
    
    while 1:
        cv2.waitKey(20)
        
        if mouseData.getEvent() == cv2.EVENT_LBUTTONDOWN: #左クリックごとに表示
            h1,w1 = mouseData.getPos()
            S2[h1:h1+20, w1:w1+20] = 255
            S1[h1:h1+20, w1:w1+20] = 1.0
            S3[:,:] = 0
            S3[mouseData.getPos()] = 1
            
            S1_iff = np.fft.ifft2(np.fft.fftshift(fshift*S1)) #逆変換(累積)
            S1_abs = np.abs(S1_iff) 
            S1max = np.max(S1_abs)
            S1min = np.min(S1_abs)
            S14 = (S1_abs - S1min ) * 255/(S1max - S1min)
            
            S3 = np.abs(np.fft.ifft2(np.fft.fftshift(S3*np.fft.fft2(image)))) #逆変換(単独)
            S3 = (S3 - S3.min()) * 255 / (S3.max() - S3.min())
            
        cv2.imshow("ifft",S14.astype(uint8))
        cv2.imshow("ifft_single",S3.astype(uint8))
        cv2.imshow("click",S2)

        if mouseData.getEvent() == cv2.EVENT_RBUTTONDOWN: #右クリックで終了
            break
            
    plt.close()
    cv2.destroyAllWindows()
