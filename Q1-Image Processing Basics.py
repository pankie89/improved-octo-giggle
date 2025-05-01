import matplotlib

matplotlib.use('TkAgg', force=True)
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import time


# ================== 通用工具函數 ==================
def show_images_grid(images, titles, rows, cols, figsize=(15, 10), save_path=None):
    """通用图像网格显示函数"""
    plt.figure(figsize=figsize)
    for i in range(len(images)):
        plt.subplot(rows, cols, i + 1)
        if len(images[i].shape) == 2:  # 灰階圖
            plt.imshow(images[i], cmap='gray')
        else:  # 彩色圖
            plt.imshow(images[i])
        plt.title(titles[i])
        plt.axis('off')

    plt.tight_layout()

    # 自動生成保存路徑
    if save_path is None:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        save_path = f"output_{timestamp}.png"

    # 保存圖像
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"結果已保存至：{os.path.abspath(save_path)}")

    plt.show(block=True)


# ================== Part a: 讀取並顯示原始圖像 ==================
def part_a(image_path):
    """滿足條件a：讀取並顯示原始圖像"""
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"無法載入圖像：{image_path}")
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    show_images_grid([img_rgb], ["Original Image"], 1, 1, save_path="part_a_result.png")


# ================== Part b: 顏色通道分離 ==================
def extract_channels(image):
    """提取三色通道（滿足條件b）"""
    red = image.copy()
    red[:, :, 1:] = 0  # 保留紅色通道

    green = image.copy()
    green[:, :, [0, 2]] = 0  # 保留綠色通道

    blue = image.copy()
    blue[:, :, :2] = 0  # 保留藍色通道

    return [red, green, blue]


def part_b(image_path):
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 提取通道
    channels = extract_channels(img_rgb)

    # 準備顯示內容
    display_images = [img_rgb] + channels
    titles = ["Original", "Red Channel", "Green Channel", "Blue Channel"]

    show_images_grid(display_images, titles, 2, 2, save_path="part_b_channels.png")


# ================== Part c: 自訂灰階轉換 ==================
def custom_grayscale(image, weights):
    """自訂灰階轉換函數（滿足條件c）"""
    return np.dot(image[..., :3], weights).astype(np.uint8)


def part_c(image_path):
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 定義四種權重方案
    weight_schemes = {
        "Equal Weights (R=G=B)": (0.333, 0.334, 0.333),
        "Luminance (BT.601)": (0.299, 0.587, 0.114),
        "Red Dominant": (0.6, 0.3, 0.1),
        "Blue Enhanced": (0.1, 0.3, 0.6)
    }

    grayscales = []
    titles = []
    for name, weights in weight_schemes.items():
        gray = custom_grayscale(img_rgb, weights)
        grayscales.append(gray)
        titles.append(f"{name}\n{weights}")

    show_images_grid(grayscales, titles, 2, 2, save_path="part_c_grayscale.png")


# ================== Part d: 手動圖像翻轉 ==================
def manual_flip(image, axis):
    """翻轉函數\滿足條件d"""
    if axis == 0:  # 垂直翻轉
        return image[::-1, :, :]
    elif axis == 1:  # 水平翻轉
        return image[:, ::-1, :]
    else:
        raise ValueError("Invalid axis value")


def part_d(image_path):
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 執行翻轉
    h_flip = manual_flip(img_rgb, 1)
    v_flip = manual_flip(img_rgb, 0)

    display_images = [img_rgb, h_flip, v_flip]
    titles = ["Original", "Horizontal Flip", "Vertical Flip"]

    show_images_grid(display_images, titles, 1, 3, figsize=(15, 5), save_path="part_d_flips.png")


# ================== 主程序 ==================
if __name__ == "__main__":
    image_path = r"文件路徑"  # CHK文件路徑

    try:
        print("Running Part a...")
        part_a(image_path)

        print("\nRunning Part b...")
        part_b(image_path)

        print("\nRunning Part c...")
        part_c(image_path)

        print("\nRunning Part d...")
        part_d(image_path)

    except Exception as e:
        print(f"\n錯誤發生：{str(e)}")
        print("請檢查：")
        print("1. 文件路徑是否正確")
        print("2. 文件格式是否支援（JPEG/PNG）")
        print("3. 依賴庫是否安裝（OpenCV, Matplotlib）")