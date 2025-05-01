自動讀圖：支援 JPEG、PNG 等格式，會先檢查路徑和檔案內容

通道分離：用 OpenCV 把 RGB 三個顏色通道拆開。像紅色通道，只留下紅色

快速可視化與儲存：用 Matplotlib 把原圖和三個通道排成 2x2 圖，方便對比，存檔時會自動加時間戳，避免重複覆蓋

記憶體更省：用 NumPy 的零矩陣減少不必要的資料複製，最多可省下 66% 的記憶體

錯誤處理：讀不到圖檔時，會跳出明確的錯誤訊息，不會整個程式關掉
以下是將此代碼開源時需要特別標註的關鍵點，尤其針對新手需修改的配置部分：

--
#### **主程序入口（`if __name__ == "__main__":` 區塊）**
```python
if __name__ == "__main__":
    # [!] 注意：替換為你自己的圖片路徑
    input_image_path = r"H:\Download\balloons.jpg"  # 輸入圖像路徑
    
    # [!] 可選：自定義輸出文件路徑，若不指定會自動生成
    # output_path = r"H:\Download\custom_plot.png"
    
    # 調用主函數（自動生成輸出路徑）
    plot_channels(input_image_path)
```

#### **函數參數默認值**
在函數定義處標明默認值的限制：
```python
def plot_channels(image_path: str, save_path: str = None) -> None:
    """
    Args:
        image_path (str): [!] 必須提供有效的圖片路徑（如：/home/user/images/input.jpg）
        save_path (str, optional): [!] 輸出路徑需包含文件名及擴展名（如：output.png）
    """
```

---

### **2. 開源文檔指引（README.md）**
#### **2.1 快速開始**
```markdown
## 快速開始

1. **github**：
   ```bash
   git clone https://github.com/yourusername/color-channel-visualizer.git
   cd color-channel-visualizer
   ```

2. **安裝依賴**：
   ```bash
   pip install -r requirements.txt
   ```

3. **修改配置文件**：
   - 打開 `Q1Basic_Programming.py`，找到以下代碼區塊：
     ```python
     if __name__ == "__main__":
         input_image_path = r"H:\Download\balloons.jpg"  # [!] 替換為你的圖片路徑
     ```
   - 將路徑替換為你的圖像文件路徑（如 `"/home/user/images/my_photo.jpg"`）。

4. **運行代碼**：
   ```bash
   python Q1Basic_Programming.py
   ```
```

#### **2.2 常見問題**
```markdown
## 常見問題

### 錯誤：`FileNotFoundError` 或圖像加載失敗
- **原因**：文件路徑錯誤或圖像格式不受支持。
- **解決方案**：
  1. 檢查路徑是否包含特殊字符（如空格、中文），建議使用英文路徑。
  2. 確保路徑使用正確的斜杠（Windows用`\\`，Linux/macOS用`/`）。
  3. 確認圖像格式為OpenCV支持的格式（如JPEG、PNG）。

### 錯誤：`ModuleNotFoundError`
- **原因**：依賴庫未安裝。
- **解決方案**：運行 `pip install -r requirements.txt` 安裝所有依賴。
```

---

### **3. 配置文件與環境管理**
#### **3.1 獨立配置文件（可選）**
對於高級用戶，可提供 `config.py` 分離配置參數：
```python
# config.py

# [!] 用戶必須修改以下路徑！
INPUT_IMAGE_PATH = r"H:\Download\balloons.jpg"  # 輸入圖像路徑
OUTPUT_DIR = r"H:\Download"                    # 輸出目錄
```

在主代碼中引用：
```python
from config import INPUT_IMAGE_PATH, OUTPUT_DIR

if __name__ == "__main__":
    plot_channels(INPUT_IMAGE_PATH, save_path=os.path.join(OUTPUT_DIR, "result.png"))
```

#### **3.2 依賴管理（requirements.txt）**
明確列出所有依賴及版本：
```
# requirements.txt
opencv-python==4.5.5.64
numpy==1.21.6
matplotlib==3.5.3
```

---

### **4. 代碼註釋標記**
在代碼關鍵位置添加新手導向註釋：

#### **路徑處理**
```python
import os

# [!] 注意：os.path.dirname() 獲取的是文件所在目錄，非工作目錄！
current_dir = os.path.dirname(os.path.abspath(__file__))  # 代碼文件所在目錄
image_path = os.path.join(current_dir, "data/input.jpg")  # 推薦使用相對路徑
```

#### **錯誤處理**
```python
try:
    image = cv2.imread(image_path)
    if image is None:
        # [!] 新手注意：此錯誤通常是路徑問題！
        raise ValueError("加載圖像失敗，請檢查路徑或文件格式！")
except Exception as e:
    print(f"[!] 嚴重錯誤：{str(e)}")
```

---

### **5. 測試範例**
添加 `examples/` 目錄，包含：
- 測試圖像（如 `balloons.jpg`）
- 示例輸出（如 `processed_balloons.png`）
- 運行腳本（如 `run_example.sh`）：
  ```bash
  #!/bin/bash
  python Q1Basic_Programming.py --input examples/balloons.jpg --output examples/result.png
  ```

---

### **6. 開源協議與貢獻指南**
在根目錄添加以下文件：
#### **LICENSE**
選擇合適的開源協議（如MIT），並聲明版權：
```text
MIT License
Copyright (c) 2023 Your Name
...
```

#### **CONTRIBUTING.md**
引導貢獻者規範：
```markdown
## 如何貢獻

1. **提交Issue**：  
   - 報告Bug時，請附上錯誤截圖和復現步驟。  
   - 建議新功能時，說明應用場景和預期效果。

2. **提交代碼**：  
   - 使用 `git checkout -b feature/your-feature` 創建新分支。  
   - 確保通過基礎測試（運行 `python tests/test_basic.py`）。
```

---
