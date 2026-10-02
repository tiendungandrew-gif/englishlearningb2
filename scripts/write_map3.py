# -*- coding: utf-8 -*-
import os

vocab_map = """# B2 VOCABULARY MAP: MA TRẬN 30 CHỦ ĐỀ TRỌNG TÂM

## 1. Mô hình Kim tự tháp Từ vựng B2
- **Tầng 1 (General High-Frequency Words - 2.500 từ):** Nền tảng giao tiếp căn bản A1-B1.
- **Tầng 2 (Academic Word List - AWL 570 word families):** Nhóm từ học thuật chuyển giao lên B2/C1 (e.g., analyze, establish, significant, potential, impact).
- **Tầng 3 (Topic-specific Lexis & Collocations):** Vốn từ chuyên biệt theo 30 chủ đề xã hội, văn hóa, công nghệ, môi trường.

## 2. Danh mục 30 Chủ đề Trọng tâm & Tần suất trong VSTEP

| STT | Chủ đề (Topic) | Tần suất xuất hiện | Kỹ năng trọng tâm |
|---|---|---|---|
| 1 | Education (Giáo dục & Đào tạo) | Rất cao | Writing Task 2, Speaking Part 3, Reading |
| 2 | Work & Career (Việc làm & Nghề nghiệp) | Rất cao | Speaking Part 1 & 2, Writing Task 1 (Cover letter), Reading |
| 3 | Technology (Công nghệ & Đổi mới) | Rất cao | Writing Task 2, Reading Passage 3/4 |
| 4 | Artificial Intelligence (Trí tuệ nhân tạo) | Đang tăng mạnh | Writing Task 2, Speaking Part 3 |
| 5 | Environment (Môi trường & Hệ sinh thái) | Rất cao | Writing Task 2, Reading Passage 1/2 |
| 6 | Climate Change (Biến đổi khí hậu & Nóng lên toàn cầu) | Cao | Reading, Writing Task 2 |
| 7 | Health & Healthcare (Sức khỏe & Y tế) | Cao | Speaking Part 1, Writing Task 2, Listening |
| 8 | Society & Social Issues (Xã hội & Vấn đề xã hội) | Cao | Writing Task 2, Speaking Part 3 |
| 9 | Family & Parenting (Gia đình & Nuôi dạy con) | Cao | Speaking Part 1 & 2, Writing Task 2 |
| 10 | Relationships (Các mối quan hệ cá nhân & xã hội) | Trung bình | Speaking Part 1, Reading |
| 11 | Communication (Giao tiếp trực tiếp & gián tiếp) | Trung bình | Speaking Part 3, Writing Task 2 |
| 12 | Media & Advertising (Truyền thông & Quảng cáo) | Cao | Writing Task 2, Reading |
| 13 | Internet & Social Networks (Internet & Mạng xã hội) | Rất cao | Speaking Part 1 & 3, Writing Task 2 |
| 14 | Science & Scientific Discovery (Khoa học & Phát minh) | Cao | Reading Passage 3/4, Listening Part 3 |
| 15 | Economy & Finance (Kinh tế & Tài chính cá nhân) | Trung bình - Cao | Reading, Writing Task 2 |
| 16 | Business & Entrepreneurship (Doanh nghiệp & Khởi nghiệp) | Trung bình | Reading, Writing Task 1 & 2 |
| 17 | Transportation (Giao thông & Phương tiện công cộng) | Cao | Speaking Part 1 & 2, Writing Task 2 |
| 18 | Travel & Exploration (Du lịch & Khám phá) | Cao | Speaking Part 1 & 2, Writing Task 1 |
| 19 | Tourism & Ecotourism (Ngành du lịch & Du lịch sinh thái) | Cao | Reading, Writing Task 2 |
| 20 | Culture & Traditional Customs (Văn hóa & Phong tục) | Cao | Speaking Part 3, Reading Passage 2 |
| 21 | Entertainment & Leisure (Giải trí & Nghỉ ngơi) | Cao | Speaking Part 1, Listening Part 1/2 |
| 22 | Government & Public Services (Chính phủ & Dịch vụ công) | Trung bình | Writing Task 2, Reading |
| 23 | Law & Regulations (Pháp luật & Quy định xã hội) | Trung bình | Reading, Writing Task 2 |
| 24 | Crime & Punishment (Tội phạm & Biện pháp xử phạt) | Trung bình | Writing Task 2, Reading |
| 25 | Globalization (Toàn cầu hóa & Hội nhập) | Cao | Writing Task 2, Speaking Part 3 |
| 26 | Urbanization & Megacities (Đô thị hóa & Thành phố lớn) | Cao | Reading, Writing Task 2 |
| 27 | Food & Nutrition (Thực phẩm & Chế độ ăn uống) | Cao | Speaking Part 1 & 2, Reading |
| 28 | Lifestyle & Work-Life Balance (Lối sống & Cân bằng) | Rất cao | Speaking Part 1 & 2, Writing Task 2 |
| 29 | Sports & Physical Fitness (Thể thao & Rèn luyện) | Trung bình | Speaking Part 1, Listening |
| 30 | Energy & Natural Resources (Năng lượng & Tài nguyên) | Cao | Reading Passage 3/4, Writing Task 2 |

## 3. Công thức học Từ vựng B2 theo Chiều Sâu
Không học từ vựng đơn lẻ (isolated words). Mỗi từ vựng phải được mở rộng theo công thức 4 bước:
`Word (Phát âm + Nghĩa)` ➔ `Word Family (Noun/Verb/Adj/Adv)` ➔ `Collocations & Dependent Prepositions` ➔ `B2 Example Sentence in VSTEP Context`.
"""

with open(r"00_master_maps\03_vocabulary_map.md", "w", encoding="utf-8") as f:
    f.write(vocab_map)

print("03_vocabulary_map.md written.")
