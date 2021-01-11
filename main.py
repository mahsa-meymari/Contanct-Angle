import os
import numpy as np
import cv2


def find_edges(image, low=None, high=None, indices=False):
    edges = cv2.Canny(image, low, high)
    if not indices:
        return edges
    return np.argwhere(edges.T)


def crop(gray):
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, gray.shape[0], 100, 30, 10, 30)[0]
    c = circles[0]
    pad = 10
    radius = c[2]
    x, y = c[0], c[1]
    right = int(y + radius)
    left = int(y - radius)
    up = int(x - radius)
    down = int(x + radius)
    cropped = gray[left - pad: right + pad, up - pad:down + pad]
    return cropped


def find_line(img):
    line = cv2.HoughLinesP(img, 0.5, np.pi / 360, 5, minLineLength=img.shape[0] / 50,
                           maxLineGap=img.shape[0])[0]
    pt1 = (line[0][0], line[0][1])
    pt2 = (line[0][2], line[0][3])
    slope = (pt1[1] - pt2[1]) / (pt1[0] - pt2[0])
    intercept = pt1[1] - slope * pt1[0]
    pt3 = (0, int(slope * 0 + intercept))
    pt4 = (img.shape[1], int(slope * img.shape[1] + intercept))
    return slope, pt3, pt4


def main(path):
    # # # # # # # # # # # # #  # # # read the image # # # # # # # # # # # # # # #
    # Check if the file exists
    if not os.path.exists(path):
        raise FileNotFoundError(f'Couldn\'t find {path}, ''make sure you\'ve spelled it right')
    print(f'Analyzing {path}')

    # Read image as a grayscale numpy array
    gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite('result_steps/gray.jpg', gray)

    # # # # # # # # # # # # #  # # # find edges # # # # # # # # # # # # # # # # #
    blur = cv2.GaussianBlur(gray, (11, 11), 0)
    edges = find_edges(blur, 150, 200, indices=False)
    cv2.imwrite('result_steps/edges.jpg', edges)

    # # # # # # # # # # # # #  # # # crop # # # # # # # # # # # # # # # # # # # #
    pad = 10
    img_cropped = crop(gray)
    cv2.imwrite('result_steps/cropped.jpg', img_cropped)
    edges_cropped = crop(edges)

    # # # # # # # # # # # # #  # # # Surface # # # # # # # # # # # # # # # # # # #
    surface = cv2.cvtColor(img_cropped, cv2.COLOR_GRAY2RGB)
    temp = edges_cropped.copy()
    pad = int(pad - 0.2 * pad)
    temp[0 + pad: edges_cropped.shape[0] - pad, 0 + pad: edges_cropped.shape[1] - pad] = 0  # remove drop
    slope, pt3, pt4 = find_line(temp)
    cv2.line(surface, pt3, pt4, (0, 0, 255), 2)
    cv2.imwrite('result_steps/surface.jpg', surface)

    # # # # # # # # # # # # # Remove under surface # # # # # # # # # # # # # # # # #
    y = int(np.average([pt3[1], pt4[1]]))
    drop = img_cropped[:y, :]
    drop_edge = edges_cropped[:y, :]
    cv2.imwrite('result_steps/drop.jpg', drop)

    # # # # # # # # # # # # # Drop Width # # # # # # # # # # # # # # # # # # # # # #
    whites = np.nonzero(drop_edge[:, :])

    x_left = np.min(whites[1][np.where(whites[0] == np.max(whites[0]))])
    left = x_left, np.max(whites[0])

    x_right = np.max(whites[1][np.where(whites[0] == np.max(whites[0]))])
    right = x_right, np.max(whites[0])

    drop_width = cv2.cvtColor(drop_edge, cv2.COLOR_GRAY2RGB)
    drop_width = cv2.circle(drop_width, left, 3, (0, 0, 255), -1)
    drop_width = cv2.circle(drop_width, right, 3, (0, 0, 255), -1)
    cv2.imwrite('result_steps/dropEdge.jpg', drop_width)

    # # # # # # # # # # # # # Tangent Lines # # # # # # # # # # # # # # # # # # # # #
    thresh = 5
    left_img = drop_edge.copy()
    left_img[:, :int(left[0]) - thresh] = 0
    left_img[:, int(left[0]) + thresh:] = 0
    slope_tangent_left, pt3, pt4 = find_line(left_img)
    cv2.line(drop_width, pt3, pt4, (0, 0, 255), 2)

    right_img = drop_edge.copy()
    right_img[:, :int(right[0]) - thresh] = 0
    right_img[:, int(right[0]) + thresh:] = 0
    slope_tangent_right, pt3, pt4 = find_line(right_img)
    cv2.line(drop_width, pt3, pt4, (0, 0, 255), 2)
    cv2.imwrite('result_steps/tangent.jpg', drop_width)

    # # # # # # # # # # # # # Calculate Angles # # # # # # # # # # # # # # # # # # #
    theta_left = np.round(np.arctan(np.abs(slope_tangent_left)) * 180 / np.pi, 2)
    if slope_tangent_left > 0:
        theta_left = 180 - theta_left
    theta_right = np.round(np.arctan(np.abs(slope_tangent_right)) * 180 / np.pi, 2)
    if slope_tangent_right < 0:
        theta_right = 180 - theta_right
    drop_width = cv2.putText(drop_width, str(theta_left), left, cv2.FONT_HERSHEY_PLAIN, 0.75, (0, 255, 0), 1,
                             cv2.LINE_AA)
    drop_width = cv2.putText(drop_width, str(theta_right), (right[0] - 15, right[1]), cv2.FONT_HERSHEY_PLAIN, 0.75,
                             (0, 255, 0), 1, cv2.LINE_AA)
    cv2.imwrite('output.jpg', drop_width)
    print("left angle:{} \nright angle:{}".format(theta_left, theta_right))

path = "test_images/sample2.png"
main(path)
