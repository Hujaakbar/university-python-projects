import sys

import cv2

IS_WINDOWS = False

if sys.platform.lower().startswith("win"):
    import winsound

    IS_WINDOWS = True


def main(*, min_object_size: int = 6_000, is_external_webcam: bool = False) -> None:
    camera: cv2.VideoCapture = cv2.VideoCapture(int(is_external_webcam))
    count = 0
    while camera.isOpened():
        count += 1
        if count == 1:
            print("Camera is activated")
            print("To quite press 'q'")
        _ret1, frame1 = camera.read()
        _ret2, frame2 = camera.read()

        moving_objects = compare_frames(frame1, frame2)
        highlight_moving_object(moving_objects, min_object_size, frame1)

        # To quit the window, Please press the key, 'q' on keyboard
        if cv2.waitKey(10) == ord("q"):
            break


def compare_frames(frame1, frame2):  # noqa: ANN001, ANN201
    difference = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(difference, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    moving_objects, _ = cv2.findContours(
        dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )
    return moving_objects


def highlight_moving_object(moving_objects, min_object_size, frame) -> None:  # noqa: ANN001
    for moving_object in moving_objects:
        if cv2.contourArea(moving_object) < min_object_size:
            continue
        x_coord, y_coord, width, hight = cv2.boundingRect(moving_object)
        cv2.rectangle(
            frame,
            (x_coord, y_coord),
            (x_coord + width, y_coord + hight),
            (0, 255, 0),
            2,
        )
        if IS_WINDOWS:
            winsound.Beep(500, 300)

        cv2.imshow("Motion Detector", frame)


if __name__ == "__main__":
    main()
