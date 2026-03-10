---
name: inet-vps-connect
description: "Kiểm tra và kết nối nhanh các VPS Linux của INET (Ubuntu, Debian...) sử dụng file .env để lấy IP/User/Port và tải file .pem về để làm khoá."
metadata:
  version: "1.0"
---

# INET VPS Connect

## Mục tiêu
- Cung cấp một bộ quy trình chuẩn để truy cập và kiểm tra (health, connectivity) cho mọi VPS Linux (Ubuntu) từ nhà cung cấp INET.
- Cho phép người dùng lưu tham số (IP, User, Port) vào `.env` để tái sử dụng, đồng thời nhận đường dẫn file `.pem` tuỳ ý do người dùng tải từ web (không commit file `.pem` vào source).
- Cho phép agent tự đọc `.env` và SSH bằng tool lệnh của hệ thống.

## Thiết lập Môi trường (.env)
Đảm bảo project có file `.env` chứa các cấu hình kết nối. 

**Ví dụ:**
```env
INET_VPS_IP=103.72.97.38
INET_VPS_USER=root
INET_VPS_PORT=24700
```

## Hướng dẫn kết nối cơ bản & Chẩn đoán sơ bộ

### 1. External Check (Kiểm tra từ bên ngoài)
Trường hợp host "chết hẳn" hoặc bị DDoS, hãy thử các lệnh sau từ local:

```bash
# Lấy biến từ env
export $(grep -v '^#' .env | xargs)

# 1. Ping
ping -c 4 $INET_VPS_IP || ping -n 4 $INET_VPS_IP
# 2. Curl HTTP / SSH check ping (Timeout 5s)
curl -sI --connect-timeout 5 http://$INET_VPS_IP:$INET_VPS_PORT
```

Nếu thất bại toàn bộ -> **VPS unreachable**. Gọi User dùng _VNC Console trên INET Panel_ để restart, vì không agent nào có thể truy cập hệ thống đang sập mạng (trừ khi dùng được Web Automation trên panel nhà cung cấp).

### 2. Login Server (SSH)
Nếu IP có mạng, hãy kết nối sử dụng file `.pem` (User cần định tuyến file `.pem` nếu agent yêu cầu):

```bash
# ssh -i <PEM_FILE_PATH> -o StrictHostKeyChecking=no -p <PORT> <USER>@<IP>
ssh -i "path_to_pem_file.pem" -o StrictHostKeyChecking=no -p $INET_VPS_PORT $INET_VPS_USER@$INET_VPS_IP
```

### 3. VPS Checkup (Health & Disks)
Ngay sau khi login bằng SSH được từ Local, tiến hành các command kiểm tra thông thường (skill `vps-checkup`):

```bash
# Kiểm tra tài nguyên đĩa cứng
df -h
# Kiểm tra process ngốn tài nguyên nếu treo RAM
top -b -n 1 | head -n 20
# Lịch sử journalctl nếu service chết đột ngột
journalctl -p 3 -xb --no-pager
# Xem log Docker (nếu chạy bằng Docker)
docker ps -a
```
