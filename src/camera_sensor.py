import cv2

cam = cv2.VideoCapture(0)

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

window_name = 'Camera He Thong Thong Minh'
cv2.namedWindow(window_name)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    out.write(frame)

    cv2.imshow(window_name, frame)

    if cv2.waitKey(1) == ord('q'):
        break
    if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
        break

cam.release()
out.release()
cv2.destroyAllWindows()