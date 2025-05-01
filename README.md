import matplotlib

matplotlib.use('TkAgg', force=True)
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import time  # 產生檔案名稱


def extract_single_channel(image: np.ndarray, channel: str) -> np.ndarray:
    """提取指定顏色通道並置其他通道"""
    channel_index = {'red': 0, 'green': 1, 'blue': 2}.get(channel.lower(), 0)
    single_channel = np.zeros_like(image)
    single_channel[:, :, channel_index] = image[:, :, channel_index]
    return single_channel


def plot_channels(image_path: str, save_path: str = None) -> None:
    """主函數：載入圖像並可視化顏色通道"""
    # 檢查輸入影像是否存在
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"錯誤：檔案 '{image_path}' 不存在！")

    # 載入圖像並檢查有效性
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"錯誤：檔案 '{image_path}' 無法解析為有效圖像！")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    print(f"圖片載入成功，大小: {image.shape}")

    # 提取顏色通道
    channels = {
        'Original': image,
        'Red Channel': extract_single_channel(image, 'red'),
        'Green Channel': extract_single_channel(image, 'green'),
        'Blue Channel': extract_single_channel(image, 'blue')
    }

    # 建立顏色佈局
    fig, axs = plt.subplots(2, 2, figsize=(12, 12))
    fig.suptitle('Image Color Channel Visualization', fontsize=18, y=0.95)

    # 動態繪製子圖
    for (title, channel_img), ax in zip(channels.items(), axs.ravel()):
        ax.imshow(channel_img)
        ax.set_title(title, fontsize=14)
        ax.axis('off')

    plt.tight_layout()

    # 自動產生保存路徑（如果未指定）
    if save_path is None:
        base_dir = os.path.dirname(image_path)
        filename = f"processed_{os.path.splitext(os.path.basename(image_path))[0]}_{time.strftime('%Y%m%d%H%M%S')}.png"
        save_path = os.path.join(base_dir, filename)

    # 儲存圖像並驗證
    try:
        plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"圖像已保存至: {save_path}")
    except Exception as e:
        raise IOError(f"保存失敗：{str(e)}")

    # 顯示圖像
    plt.show(block=True)


if __name__ == "__main__":
    input_image_path = r"H:\Download\balloons.jpg"  # 替換為實際路徑

    # 自動產生儲存路徑
    plot_channels(input_image_path)

    # 手動指定儲存路徑
    # output_path = r"H:\Download\custom_plot.png"  # 路徑
    # plot_channels(input_image_path, save_path=output_path)
