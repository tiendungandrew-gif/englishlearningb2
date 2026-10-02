# -*- coding: utf-8 -*-
import sys

ex_content = """
---

## 11. BÀI TẬP THỰC HÀNH MẪU TỪ B1 -> B2 (VSTEP FORMAT)

### Bài tập 1: Xử lý Bẫy Đổi ý (Part 1 - Short Announcement)
* **Audio Transcript:**
  "Attention all passengers on flight VN 245 bound for Da Nang. The departure gate was initially scheduled as Gate 12. However, due to unexpected aircraft maintenance on the tarmac, please proceed immediately to Gate 19. Boarding will commence in approximately fifteen minutes. We apologize for the inconvenience."
* **Question:** Where should passengers go to board the plane?
  * A. Gate 12
  * B. Gate 15
  * C. Gate 19
  * D. Gate 24
* **Phân tích bẫy:**
  * Phương án A (Gate 12) là **Bẫy Đổi Ý** (kế hoạch ban đầu). Tín hiệu 'However' đảo chiều sang Gate 19.
  * Phương án B (15) là con số gây nhiễu từ 'fifteen minutes'.
  * **Đáp án đúng:** **C. Gate 19**.

---

### Bài tập 2: Xử lý Paraphrasing & Phủ định ngầm (Part 2 - Extended Conversation)
* **Audio Transcript:**
  - *Woman:* "Have you reviewed Professor Miller's reading list for the environmental economics seminar?"
  - *Man:* "Yes, but frankly speaking, I barely managed to comprehend the empirical data in Chapter 4. Most of the theoretical models seemed completely detached from real-world applications."
  - *Woman:* "I felt the exact same way. That's why I think we ought to consult the teaching assistant before submitting our critiques."
* **Question:** What was the man's opinion of Chapter 4?
  * A. He found the empirical data easily applicable to daily life.
  * B. He struggled to understand the statistical findings.
  * C. He completely agreed with all the theoretical models.
  * D. He decided to skip the professor's seminar.
* **Phân tích bẫy & Paraphrase:**
  * Audio dùng: *"barely managed to comprehend the empirical data"*.
  * Đáp án đúng B2 đã được **Paraphrase**: *"struggled to understand the statistical findings"* (*barely comprehend* = *struggled to understand*; *empirical data* = *statistical findings*).
  * Phương án A trái ngược hoàn toàn (*detached from real-world applications*).
  * **Đáp án đúng:** **B**.

---

## 12. CHECKLIST 5 BƯỚC LUYỆN LISTENING B2 ĐẠT 7.0+
1. **Bước 1 (Pre-listening - 15 giây vàng):** Quét nhanh câu hỏi, gạch chân 2 loại Keywords (Anchor keywords không đổi & Action keywords dễ bị paraphrase), dự đoán ngữ cảnh và loại từ cần nghe.
2. **Bước 2 (Active Listening):** Tập trung 100% bắt mạch bài nói, chú ý các Signpost words (từ chỉ dẫn chuyển ý), không dừng lại bối rối nếu lỡ mất 1 từ.
3. **Bước 3 (Elimination & Note-taking):** Vận dụng ghi chú tốc ký ở Part 3; gạch bỏ dứt khoát các phương án verbatim (bẫy lặp lại từ y hệt nhưng sai logic) và bẫy đổi ý.
4. **Bước 4 (Post-listening Transcript Analysis):** Mở transcript ra đọc lại sau khi làm xong đề, đánh dấu các từ vựng mới, hiện tượng nuốt âm/nối âm và cụm từ paraphrase của câu đúng.
5. **Bước 5 (Shadowing):** Bật audio nghe lại lần cuối và nói nhại theo (Shadowing) theo đúng ngữ điệu và tốc độ của người bản xứ để khắc sâu phản xạ thính giác.
"""

with open(r"05_listening\master_listening_b2.md", "a", encoding="utf-8") as f:
    f.write(ex_content)

print("Appended listening exercises successfully.")
