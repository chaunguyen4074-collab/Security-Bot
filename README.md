# Telegram Bot Tín Hiệu Đầu Tư Chứng Khoán

## 1. Giới thiệu

Có thể test thử BOT tại Telegram: @Goiphanmem1nhom2_bot

Đây là project FinTech Bot được xây dựng bằng Python và Telegram Bot.

Bot có chức năng lấy dữ liệu giá cổ phiếu từ Vietcap API, tính toán một số chỉ báo kỹ thuật và trả về tín hiệu BUY, SELL hoặc HOLD thông qua Telegram.

## 2. Chức năng

- Lấy dữ liệu lịch sử cổ phiếu từ Vietcap API.
- Tính EMA20.
- Tính EMA50.
- Tính RSI14.
- Tính trung bình khối lượng 20 phiên.
- Sinh tín hiệu BUY / SELL / HOLD.
- Tra cứu giá cổ phiếu bằng Telegram.
- Tra cứu tín hiệu kỹ thuật bằng Telegram.
- Xử lý mã cổ phiếu không hợp lệ.

## 3. Công nghệ sử dụng

- Python
- Pandas
- Requests
- python-dotenv
- python-telegram-bot
- Vietcap API
- Telegram Bot API

## 4. Cấu trúc project

text
Nhom2-BOT/
│
├── vietcap_api.py
├── strategy.py
├── telegram_bot.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md

## 5. Các lệnh Telegram
/start
/help
/price FPT
/signal FPT

## 6. Lưu ý

Project được xây dựng cho mục đích học tập và minh họa quy trình xây dựng FinTech Bot.

Các tín hiệu BUY / SELL / HOLD là kết quả của thuật toán kỹ thuật được lập trình trong project và không phải khuyến nghị đầu tư cá nhân.