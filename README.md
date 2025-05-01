自動讀圖：支援 JPEG、PNG 等格式，會先檢查路徑和檔案內容

通道分離：用 OpenCV 把 RGB 三個顏色通道拆開。像紅色通道，只留下紅色

快速可視化與儲存：用 Matplotlib 把原圖和三個通道排成 2x2 圖，方便對比，存檔時會自動加時間戳，避免重複覆蓋
錯誤處理：讀不到圖檔時，會跳出明確的錯誤訊息，不會整個程式關掉
以下是將此代碼開源時需要特別標註的關鍵點，尤其針對新手需修改的配置部分：

--
以下是將代碼開源時需特別標註的注意事項，以**清晰標籤+可視化指引**呈現：

---

### 📁 文件路徑標註（代碼內提示）
```python
# ================== 必改區域 ==================
if __name__ == "__main__":
    # [!重要!] 替換為你的圖片路徑，保持原始字符串格式(r"")
    input_path = r"H:\你的資料夾\你的圖片.jpg"  # 例: r"C:\Users\Name\Pictures\test.jpg"
    
    # [!可選!] 自定義輸出路徑，留空則自動生成
    # output_path = r"你的自訂路徑\output.png"
```

---

### 📝 README.md）
```markdown
## 🚀 快速開始

### 1. 路徑設定
- 用記事本打開 `Q1-Image Processing Basics.py`
- 找到第125行修改為你的圖片路徑：
  ```python
  input_path = r"你的實際路徑/圖片名稱.jpg"  # [!紅色標註!]
  ```

### 2. 路徑格式注意
- Windows範例：`r"C:\\Users\\test.png"` 或 `r"C:/Users/test.png"`
- 禁止使用中文路徑和特殊符號：`錯誤❌: r"桌面/測試圖.jpg"`

### 3. 測試圖片建議
- 測試用圖片建議尺寸：512x512~1024x1024
- 支援格式：`.jpg`、`.png`（不支援WebP/HEIC）
```

---

### 🛠️ 配置檔案範例
在目錄添加 `config.ini`：
```ini
[paths]
; [!修改這裡!]
input_image = "C:/path/to/your/image.jpg"  
output_dir = "results/"
```

在代碼中讀取配置：
```python
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
image_path = config['paths']['input_image']
```

---

### 🚨 常見錯誤處理指南
在README.md添加故障排除：
```markdown
## 🔧 疑難排解

| 錯誤現象 | 解決方案 | 圖示 |
|---------|----------|-----|
| 找不到文件 | 右鍵檔案→屬性→複製完整路徑 | [![路徑示意](https://via.placeholder.com/100x30?text=點我看圖示)]() |
| 黑屏/花屏 | 檢查圖片是否損毀，用[IrfanView](https://www.irfanview.com/)驗證 | |
| 中文亂碼 | 重命名檔案為全英文 | |
```

---

### 🌟 可視化指引技巧
1. 在代碼倉庫添加**路徑設定截圖**：
   - 紅色框標註需修改的程式區塊
   - GIF動畫展示修改過程

2. 提供**測試用圖片**：
   ```bash
   test_images/
   ├── sample1.jpg  # 標準測試圖
   └── sample2.png  # 透明背景測試
   ```

3. 在關鍵程式區塊添加emoji標記：
   ```python
   def load_image(path):
       # 🚩新手注意：路徑錯誤最常發生在這裡！
       if not os.exists(path):
           raise Error("檔案不存在") 
   ```

---

透過**分級提示+可視化指引**，即使非技術用戶也能快速定位需修改的區域，大幅降低上手門檻。
