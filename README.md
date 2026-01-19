# Project HVAC - Intelligent Systems

## 📦 Cài đặt thư viện

```bash
pip install opencv-python pandas numpy
```

## 🔧 Git Commands - Hướng dẫn sử dụng Git

### 📝 Commit (Lưu thay đổi local)

```bash
# 1. Kiểm tra file nào đã thay đổi
git status

# 2. Add file muốn commit
git add .                    # Add tất cả file
git add <tên-file>          # Add file cụ thể
git add data/               # Add cả folder

# 3. Commit với message
git commit -m "Mô tả những gì bạn đã thay đổi"
```

### ⬆️ Push (Đẩy code lên GitHub)

```bash
# Push lên branch hiện tại
git push

# Hoặc push lên branch main
git push origin main

# Với --no-verify nếu có lỗi hooks
git push --no-verify
```

### ⬇️ Pull (Lấy code mới từ GitHub về)

```bash
# Pull code mới về
git pull

# Hoặc pull từ branch main
git pull origin main

# Với --no-verify nếu có lỗi hooks
git pull --no-verify
```

### 🔄 Quy trình làm việc thường dùng

```bash
# 1. Lấy code mới nhất về
git pull

# 2. Làm việc, chỉnh sửa code...

# 3. Kiểm tra thay đổi
git status

# 4. Add file
git add .

# 5. Commit
git commit -m "Mô tả thay đổi"

# 6. Push lên GitHub
git push
```

### 💡 Lệnh Git hữu ích khác

```bash
# Xem lịch sử commit
git log

# Xem lịch sử commit gọn
git log --oneline

# Xem thay đổi chưa commit
git diff

# Hủy thay đổi chưa add
git checkout -- <tên-file>

# Xem các branch
git branch

# Tạo branch mới
git branch <tên-branch>

# Đổi branch
git checkout <tên-branch>

# Tạo và đổi branch mới
git checkout -b <tên-branch>

# Merge branch
git merge <tên-branch>

# Xem remote repository
git remote -v
```

## 📁 Cấu trúc Project

```
project_hvac/
├── data/                   # Dữ liệu (quản lý bởi Git LFS)
│   ├── sensor_data_90.csv
│   └── animals/
├── notebooks/              # Jupyter notebooks
├── reports/                # Báo cáo
├── src/                    # Source code
├── main.py                 # File chính
└── README.md              # File này
```

## 🚀 Git LFS (Large File Storage)

Project này sử dụng Git LFS để quản lý các file lớn trong folder `data/`.

### Các loại file được track bởi LFS:
- `*.csv` - File dữ liệu
- `*.jpg`, `*.png`, `*.jpeg` - File ảnh

### Kiểm tra Git LFS:
```bash
# Xem version
git lfs version

# Xem file nào đang được track
git lfs ls-files

# Xem cấu hình LFS
cat .gitattributes
```
