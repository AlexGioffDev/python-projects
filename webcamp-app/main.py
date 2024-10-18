import cv2, time, pandas
from datetime import datetime
#First frame initialize to None
first_frame=None
status_list=[None, None]
frame_counter = 0
times=[]
video = cv2.VideoCapture(0)  # 0 usually is webcam for now 1 because i've phone connect to pc

df=pandas.DataFrame(columns=["Start", "End"])

while True:
    check, frame = video.read()
    status = 0

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray, (21, 21), 0)

    # give time to camera to stabilize
    if frame_counter < 10:
        frame_counter += 1
        continue

    # check if the first first frame is None
    # if is None give value to gray
    # the first cicle initialize frame
    # and move to other iteration
    if first_frame is None:
      first_frame = gray
      continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thres_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thres_frame = cv2.dilate(thres_delta, None, iterations=2)

    (cnts, _) = cv2.findContours(thres_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
      if cv2.contourArea(contour) < 10000:
        continue
      status=1
      #draw rectangle
      (x,y,w, h) = cv2.boundingRect(contour)
      cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255,0), 3)

    status_list.append(status)
    if status_list[-1]==1 and status_list[-2] == 0:
      times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2] == 1:
      times.append(datetime.now())

    
    cv2.imshow("Capturing", gray)
    cv2.imshow("Delta", delta_frame)
    cv2.imshow("Thresold Frame", thres_frame)
    cv2.imshow("Color frame", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
      if status == 1:
        times.append(datetime.now())
        break

for i in range(0, len(times), 2):
  if i + 1 < len(times):  # Assicurati che esista un valore di "End" corrispondente
        new_row = pandas.DataFrame({"Start": [times[i]], "End": [times[i + 1]]})
        df = pandas.concat([df, new_row], ignore_index=True)

df.to_csv("data/Times.csv")

video.release()
cv2.destroyAllWindows
