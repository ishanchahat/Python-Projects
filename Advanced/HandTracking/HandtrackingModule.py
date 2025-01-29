import cv2
import mediapipe as mp
import time



class handDetector():
    def __init__(self,mode=False, maxHands = 2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        
    
    def findHands(self,img,draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        if results.multi_hand_landmarks:
            for handLandmarks in results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img, handLandmarks, self.mpHands.HAND_CONNECTIONS)
        
    # for id, lm in enumerate(handLandmarks.landmark):
    #             #print(id,lm)
    #     h, w, c = img.shape
    #     cx,cy = int(lm.x * w), int(lm.y*h)
    #     print(id, cx, cy)
    #             #if id == 0:
    #     cv2.circle(img, (cx,cy) , 15, (255,0,255),cv2.FILLED)

def main():
    pTime = 0
    cTime = 0

    while True:
        success, img = cap.read()
        cap = cv2.VideoCapture(0)
        cTime = time.time()                
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img,str(int(fps)),(10,70), cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),6)

    
        cv2.imshow("Image", img)
        cv2.waitKey(1)
    


if __name__ == "__main__":
    main()