# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** [Điền Họ và Tên]  
> **Mã Sinh Viên / Mã Học viên:** [Điền MSSV]  
> **Chủ đề Lựa chọn:** [Điền tên chủ đề đã chọn từ docs/DANH_SACH_DE_TAI.md hoặc Đề tài Mở]  

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 4/ 5 | Bài toán có yêu cầu chia nhỏ nhiều bước suy luận nối tiếp nhau không? |
| **2. Tool Interaction** | 5/ 5 | Hệ thống có cần kết nối với MCP Server / Cơ sở dữ liệu bên ngoài không? |
| **3. Dynamic Decision** | 4/ 5 | Bước tiếp theo có phụ thuộc vào kết quả quan sát bước trước không? |
| **4. Long Horizon Goal** | 3/ 5 | Hệ thống có phải giữ mục tiêu xuyên suốt qua nhiều lượt xử lý không? |
| **TỔNG ĐIỂM AGENTIC FIT** | 16**/ 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Chào bạn, bạn có thể giới thiệu quy chế học vụ cơ bản của Đại học VinUni không?",
    "action_type": "FINAL_ANSWER",
    "thought": "Gemini phản hồi trực tiếp bằng văn bản (không cần gọi công cụ).",
    "output": "Chào bạn! Rất vui được hỗ trợ bạn. Dưới đây là tóm tắt một số điểm cốt lõi trong quy chế và quy định học vụ tại Đại học VinUni:\n\n---\n\n### 1. **Hệ thống Tín chỉ và Chương trình Đào tạo**\n* **Đơn vị tích lũy:** Sinh viên tích lũy kiến thức theo **Tín chỉ (Credit)**.\n* **Cấu trúc chương trình:** Gồm các môn học Đại cương (General Education), Môn cơ sở ngành, Môn chuyên ngành và các hoạt động Trải nghiệm/Thực tập (Internship/Capstone Project).\n* **Ngôn ngữ giảng dạy:** 100% bằng tiếng Anh (trừ một số môn Lý luận chính trị và Quốc phòng an ninh theo quy định của Bộ GD&ĐT).\n\n---\n\n### 2. **Hệ thống Đánh giá và Thang điểm**\n* **Thang điểm chữ & Điểm trung bình tích lũy (GPA):**\n  * Đánh giá kết quả học tập qua thang điểm chữ (A+, A, A-, B+, B, B-, C+, C, C-, D, F).\n  * Điểm trung bình học kỳ (GPA) và điểm trung bình tích lũy (CGPA) được tính theo thang điểm **4.0**.\n* **Điều kiện qua môn:** Thường yêu cầu sinh viên đạt điểm tổng kết môn học từ điểm D (1.0/4.0) trở lên, kết hợp với các điều kiện tham gia lớp học và hoàn thành bài thi/bài tập lớn.\n\n---\n\n### 3. **Quy định Cảnh báo Học tập & Buộc thôi học**\n* **Cảnh báo học tập (Academic Probation):** Phát sinh khi điểm CGPA rơi xuống dưới mức quy định (thường là dưới 2.0/4.0) trong một học kỳ. Sinh viên rơi vào diện này sẽ nhận được hỗ trợ đặc biệt từ Cố vấn học tập (Academic Advisor).\n* **Điều kiện duy trì:** Nếu sinh viên không cải thiện GPA sau thời gian cảnh báo học tập theo quy định, có thể đối mặt với mức xử lý học vụ cao hơn hoặc buộc thôi học.\n\n---\n\n### 4. **Liêm chính Học thuật (Academic Integrity)**\n* VinUni áp dụng tiêu chuẩn rất nghiêm ngặt về **Liêm chính Học thuật**:\n  * Nghiêm cấm mọi hình thức gian lận, đạo văn (plagiarism), nộp bài hộ, hoặc sử dụng trái phép các công cụ hỗ trợ mà không được giảng viên cho phép.\n  * Mọi vi phạm sẽ bị xử lý theo Hội đồng Kỷ luật Học thuật (từ tính điểm 0 bài thi đến đình chỉ/đuổi học).\n\n---\n\n### 5. **Hỗ trợ Sinh viên & Tư vấn Học tập**\n* **Cố vấn Học tập (Academic Advisor):** Mỗi sinh viên đều được phân công Cố vấn Học tập để hỗ trợ lập kế hoạch học tập, chọn môn, tư vấn tâm lý học thuật và định hướng nghề nghiệp.\n* **Trung tâm Hỗ trợ Học tập (Academic Support Center):** Cung cấp các dịch vụ gia sư (Peer Tutoring), xưởng viết (Writing Lab), workshop kĩ năng học tập.\n\n---\n\nNếu bạn cần tư vấn cụ thể hơn về hồ sơ học tập cá nhân hoặc muốn **đặt lịch hẹn với Cố vấn Học tập**, bạn chỉ cần cung cấp **Mã sinh viên** cho mình nhé!",
    "latency_ms": 7929.17
  },
  {
    "step": 1,
    "query": "Hãy tra cứu thông tin học vụ của sinh viên SV2026001.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "academic_query",
    "arguments": {
      "student_id": "SV2026001"
    },
    "observation": {
      "status": "SUCCESS",
      "student_id": "SV2026001",
      "data": {
        "full_name": "Nguyễn Văn An",
        "class": "AI-K4",
        "gpa": 3.85,
        "email": "an.nv@vinuni.edu.vn",
        "status": "Đang học",
        "advisor": "PGS.TS Nguyễn Văn A"
      }
    },
    "latency_ms": 2503.4
  },
  {
    "step": 2,
    "query": "Hãy tra cứu thông tin học vụ của sinh viên SV2026001.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Kết quả tra cứu cho sinh viên SV2026001 (Nguyễn Văn An): Lớp AI-K4, GPA: 3.85, Email: an.nv@vinuni.edu.vn, Trạng thái: Đang học, Cố vấn: PGS.TS Nguyễn Văn A.",
    "latency_ms": 10.0
  },
  {
    "step": 1,
    "query": "Hãy đặt lịch hẹn tư vấn học tập cho sinh viên SV2026001 với TS. Trần Văn A vào lúc 14:00 ngày 2026-09-25.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "schedule_appointment",
    "arguments": {
      "advisor_name": "TS. Trần Văn A",
      "student_id": "SV2026001",
      "datetime_str": "2026-09-25 14:00"
    },
    "observation": {
      "status": "SUCCESS",
      "booking_id": "BK-SV2026001-99",
      "student_id": "SV2026001",
      "datetime": "2026-09-25 14:00",
      "advisor": "TS. Trần Văn A",
      "message": "Đặt lịch thành công cho sinh viên SV2026001 với TS. Trần Văn A vào lúc 2026-09-25 14:00."
    },
    "latency_ms": 3081.71
  },
  {
    "step": 2,
    "query": "Hãy đặt lịch hẹn tư vấn học tập cho sinh viên SV2026001 với TS. Trần Văn A vào lúc 14:00 ngày 2026-09-25.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Đặt lịch thành công cho sinh viên SV2026001 với TS. Trần Văn A vào lúc 2026-09-25 14:00.",
    "latency_ms": 10.0
  },
  {
    "step": 1,
    "query": "Kiểm tra điểm GPA của sinh viên SV2026001, nếu GPA đạt từ 3.5 trở lên thì hãy đăng ký đặt lịch tư vấn học bổng với PGS. Lê Thị B vào lúc 09:00 ngày 2026-10-01.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "schedule_appointment",
    "arguments": {
      "student_id": "SV2026001",
      "datetime_str": "14:00 15/09/2026",
      "advisor_name": "PGS.TS Nguyễn Văn A"
    },
    "observation": {
      "status": "SUCCESS",
      "booking_id": "BK-SV2026001-99",
      "student_id": "SV2026001",
      "datetime": "14:00 15/09/2026",
      "advisor": "PGS.TS Nguyễn Văn A",
      "message": "Đặt lịch thành công cho sinh viên SV2026001 với PGS.TS Nguyễn Văn A vào lúc 14:00 15/09/2026."
    },
    "latency_ms": 895.39
  },
  {
    "step": 2,
    "query": "Kiểm tra điểm GPA của sinh viên SV2026001, nếu GPA đạt từ 3.5 trở lên thì hãy đăng ký đặt lịch tư vấn học bổng với PGS. Lê Thị B vào lúc 09:00 ngày 2026-10-01.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Đặt lịch thành công cho sinh viên SV2026001 với PGS.TS Nguyễn Văn A vào lúc 14:00 15/09/2026.",
    "latency_ms": 10.0
  },
  {
    "step": 1,
    "query": "Cho tôi xem thông tin học vụ và điểm số của mã sinh viên SV9999999.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "academic_query",
    "arguments": {
      "student_id": "SV9999999"
    },
    "observation": {
      "status": "NOT_FOUND",
      "message": "Không tìm thấy dữ liệu sinh viên có mã 'SV9999999'"
    },
    "latency_ms": 2329.53
  },
  {
    "step": 2,
    "query": "Cho tôi xem thông tin học vụ và điểm số của mã sinh viên SV9999999.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Không tìm thấy dữ liệu sinh viên có mã 'SV9999999'",
    "latency_ms": 10.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [ ] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** ___ / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** ___ lượt.
- **Kết quả đẩy Repo nộp bài:** [ ] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
