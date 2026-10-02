# -*- coding: utf-8 -*-
"""
Script to create the first half of master_reading_b2.md:
- Section 1: Overview & Matrix
- Section 2: Reading Mechanics (Skimming, Scanning, Parsing, Context Clues)
- Section 3: Question Types 1 to 5 with full B2 Academic Examples & Explanations
"""
import os

target_path = os.path.join(r"d:\projectbuild\hoctienganh", "06_reading", "master_reading_b2.md")

content = r"""# PHẦN 6: KỸ NĂNG ĐỌC HIỂU HỌC THUẬT B2 (B2 READING MASTERY)
## CHIẾN LƯỢC TOÀN DIỆN CHINH PHỤC VSTEP READING (TARGET 7.0 - 8.5)

---

## MỤC LỤC CHI TIẾT
1. [TỔNG QUAN ĐỊNH DẠNG & MA TRẬN ĐỀ THI VSTEP READING](#1-tổng-quan-định-dạng--ma-trận-đề-thi-vstep-reading)
   - 1.1. Cấu trúc định lượng 4 bài đọc
   - 1.2. Thang đo độ khó từ vựng và chủ đề học thuật
   - 1.3. Chiến lược phân bổ thời gian 60 phút (Quy tắc 13 - 2)
   - 1.4. Ma trận phân bố dạng câu hỏi trong 40 câu
2. [PHƯƠNG PHÁP & KỸ THUẬT ĐỌC HỌC THUẬT CHUYÊN SÂU](#2-phương-pháp--kỹ-thuật-đọc-học-thuật-chuyên-sâu)
   - 2.1. Skimming: Đọc quét lấy ý chính, cấu trúc văn bản và luận điểm
   - 2.2. Scanning: Đọc định vị thông tin chi tiết, số liệu và thuật ngữ
   - 2.3. Intensive Reading: Kỹ thuật bóc tách cú pháp câu đa mệnh đề phức tạp
   - 2.4. Context Clues & Phân tích hình thái từ: Đoán nghĩa từ vựng chuyên ngành
3. [CẨM NANG CHI TIẾT 10 DẠNG CÂU HỎI VSTEP READING](#3-cẩm-nang-chi-tiết-10-dạng-câu-hỏi-vstep-reading)
   - Dạng 1: Main Idea / Primary Purpose / Best Title (Ý chính, Mục đích tổng quát, Tiêu đề)
   - Dạng 2: Factual Details / Direct Comprehension (Thông tin chi tiết trực tiếp)
   - Dạng 3: Negative Factual Details (Dạng phủ định: EXCEPT / NOT mentioned)
   - Dạng 4: Pronoun Reference (Từ quy chiếu đại từ)
   - Dạng 5: Vocabulary in Context (Từ vựng trong văn cảnh học thuật)
   - Dạng 6: Inference Questions (Câu hỏi suy luận ngầm)
   - Dạng 7: Sentence Simplification / Paraphrasing (Câu tương đương ý nghĩa)
   - Dạng 8: Author's Tone / Attitude / Purpose (Mục đích, giọng điệu, thái độ tác giả)
   - Dạng 9: Sentence Insertion (Chèn câu vào mạch văn bản)
   - Dạng 10: Structural & Rhetorical Function (Tổ chức lập luận & Tóm tắt văn bản)
4. [BỘ 5 BẪY KINH ĐIỂN & CHIẾN THUẬT LOẠI SUY (POE)](#4-bộ-5-bẫy-kinh-điển--chiến-thuật-loại-suy-poe)
   - 4.1. Bẫy 1: Verbatim Matching (Bẫy từ vựng y hệt bài đọc)
   - 4.2. Bẫy 2: Extreme Modifiers (Bẫy từ ngữ khẳng định tuyệt đối)
   - 4.3. Bẫy 3: True in Reality, Not in Text (Đúng với thực tế ngoài đời nhưng bài không nói)
   - 4.4. Bẫy 4: Reversed Cause-and-Effect (Bẫy đảo lộn quan hệ nhân quả)
   - 4.5. Bẫy 5: Half-Right, Half-Wrong (Nửa đầu đúng, nửa đuôi sai thông tin)
   - 4.6. Ma trận loại suy 4 bước (Process of Elimination Heuristics)
5. [BÀI THI THỬ MẪU HOÀN CHỈNH B2 (FULL MINI-TEST: 10 CÂU ĐỦ 10 DẠNG)](#5-bài-thi-thử-mẫu-hoàn-chỉnh-b2-full-mini-test-10-câu-đủ-10-dạng)
   - Bài đọc học thuật: *Circadian Rhythms and Cognitive Performance in the Modern Workplace*
   - Bộ 10 câu hỏi chuẩn hóa
   - Bảng đáp án, dịch nghĩa phân tích chuyên sâu từng câu & lý do loại phương án sai
6. [KẾ HOẠCH LUYỆN ĐỌC ĐẠT ĐIỂM 7.0 - 8.5 VSTEP TRONG 30 NGÀY](#6-kế-hoạch-luyện-đọc-đạt-điểm-70---85-vstep-trong-30-ngày)
   - Quy trình đọc ngược (Reverse Engineering Method)
   - Biểu mẫu nhật ký sửa lỗi (Reading Error Log)
   - Checklist 7 bước kiểm soát bài đọc trước khi nộp

---

## 1. TỔNG QUAN ĐỊNH DẠNG & MA TRẬN ĐỀ THI VSTEP READING

Bài thi Đọc hiểu VSTEP (Định dạng Đánh giá năng lực tiếng Anh từ Bậc 3 đến Bậc 5 theo Khung NLNN 6 bậc dùng cho Việt Nam) là một trong những phần thi mang tính quyết định điểm số cao nhất nếu thí sinh nắm vững chiến lược kỹ thuật.

### 1.1. Cấu trúc định lượng 4 bài đọc
- **Tổng thời gian thi:** 60 phút (không có thời gian nghỉ giữa các bài).
- **Tổng số câu hỏi:** 40 câu hỏi trắc nghiệm khách quan (mỗi câu 4 lựa chọn A, B, C, D).
- **Hình thức thi:** Hoàn toàn trên máy tính (Computer-based test).
- **Độ dài toàn bài:** Khoảng 1.900 – 2.050 từ.

| Bài đọc | Độ dài trung bình | Độ khó CEFR tương đương | Lĩnh vực văn bản | Đặc điểm văn phong |
| :--- | :--- | :--- | :--- | :--- |
| **Passage 1** | ~400 – 450 từ | **B1 - B1+** | Đời sống xã hội, tiểu sử, du lịch, giáo dục thường nhật | Văn miêu tả, tường thuật, từ vựng thông dụng, câu đơn & câu ghép |
| **Passage 2** | ~450 – 500 từ | **B1+ - B2** | Khoa học thường thức, công nghệ ứng dụng, tâm lý học hành vi, môi trường | Văn thuyết minh, phân tích sự kiện, giải thích nguyên nhân - kết quả |
| **Passage 3** | ~500 – 550 từ | **B2** | Kinh tế, biến đổi xã hội, lịch sử văn minh, y học cộng đồng | Báo chí học thuật (academic journalism), cấu trúc lập luận đối chứng |
| **Passage 4** | ~500 – 600 từ | **B2 - C1** | Nghiên cứu khoa học chuyên sâu, sinh thái học, triết học, nhân học | Văn bản nghiên cứu (research papers), mật độ thuật ngữ trừu tượng cao, câu phức nhiều tầng |

### 1.2. Thang đo độ khó từ vựng và chủ đề học thuật
Để đạt ngưỡng **B2 (Bậc 4)**, thí sinh cần làm đúng tối thiểu **24/40 câu** (tương đương 6.0 điểm Reading). Để tạo vùng đệm an toàn tuyệt đối bù cho kỹ năng Nói/Nghe, mục tiêu tối ưu của bạn là **28 – 32/40 câu (7.0 – 8.0 điểm)**.
- **Tầng từ vựng:** Chiếm 70% là từ vựng thuộc Oxford 3000/5000 ở cấp độ B1-B2 và Academic Word List (AWL). 15% là từ vựng C1/chuyên ngành (không yêu cầu phải biết trước mà dựa vào ngữ cảnh suy luận).
- **Đặc trưng cú pháp:** Sử dụng nhiều câu phức chứa mệnh đề quan hệ rút gọn, cấu trúc đảo ngữ nhấn mạnh, câu bị động khách quan, và các cấu trúc nhượng bộ/đối lập đa tầng.

### 1.3. Chiến lược phân bổ thời gian 60 phút (Quy tắc 13 - 2)
Lỗi tử huyệt của 80% thí sinh VSTEP là sa đà vào Passage 1-2, dẫn đến thiếu thời gian ở Passage 3-4 và phải đánh lụi 10-15 câu cuối. Bạn phải tuân thủ nghiêm ngặt **Quy tắc 13 - 2**:

$$\text{Tổng 60 phút} = 4 \times (\text{13 phút xử lý} + \text{1 phút kiểm tra}) + \text{4 phút dự phòng tổng thể}$$

```
   [00:00 - 13:00] : Passage 1 (Tối đa 13 phút - Mục tiêu: 9/10 câu đúng)
   [13:00 - 14:00] : Review nhanh Passage 1
   [14:00 - 27:00] : Passage 2 (Tối đa 13 phút - Mục tiêu: 8/10 câu đúng)
   [27:00 - 28:00] : Review nhanh Passage 2
   [28:00 - 41:00] : Passage 3 (Tối đa 13 phút - Mục tiêu: 7/10 câu đúng)
   [41:00 - 42:00] : Review nhanh Passage 3
   [42:00 - 56:00] : Passage 4 (Tối đa 14 phút - Mục tiêu: 6-7/10 câu đúng)
   [56:00 - 60:00] : 4 phút rà soát toàn bộ bài thi, chắc chắn không bỏ trống ô nào!
```

> **Nguyên tắc "Bỏ buông có chiến thuật":** Nếu gặp 1 câu hỏi suy luận hoặc từ vựng mà sau 60 giây phân tích vẫn chưa chọn được phương án, **chọn ngay 1 phương án khả dĩ nhất, ghi chú lại số câu ra nháp (hoặc flag trên phần mềm thi), và lập tức bước sang câu tiếp theo**. Tuyệt đối không để 1 câu khó cướp đi thời gian làm 3 câu dễ phía sau!

### 1.4. Ma trận phân bố dạng câu hỏi trong 40 câu

```
+--------------------------------------------+-----------------------+---------------------+
| Dạng câu hỏi                              | Số câu trung bình/đề  | Mức độ khó (CEFR)   |
+--------------------------------------------+-----------------------+---------------------+
| 1. Main Idea / Title / Primary Purpose     | 4 câu (1 câu/bài)     | B1 - B2             |
| 2. Factual Details (Chi tiết trực tiếp)   | 10 - 12 câu           | B1 - B2             |
| 3. Negative Details (EXCEPT / NOT)        | 4 - 6 câu             | B2                  |
| 4. Pronoun Reference (Từ quy chiếu)        | 3 - 4 câu             | B1 - B2             |
| 5. Vocabulary in Context (Từ vựng ngữ cảnh)| 6 - 8 câu             | B1 - B2+            |
| 6. Inference (Suy luận ngầm)               | 4 - 6 câu             | B2 - C1             |
| 7. Sentence Simplification (Paraphrase)   | 2 - 3 câu             | B2                  |
| 8. Author's Tone / Purpose / Attitude     | 2 - 3 câu             | B2 - C1             |
| 9. Sentence Insertion (Chèn câu)          | 1 - 2 câu             | B2                  |
| 10. Organization / Summary                | 1 - 2 câu             | B2 - C1             |
+--------------------------------------------+-----------------------+---------------------+
```

---

## 2. PHƯƠNG PHÁP & KỸ THUẬT ĐỌC HỌC THUẬT CHUYÊN SÂU

### 2.1. Skimming: Đọc quét lấy ý chính, cấu trúc văn bản và luận điểm
Skimming không phải là "đọc lướt vô định", mà là quá trình thu thập **Khung xương tư duy (Cognitive Skeleton)** của tác giả trong vòng **60 – 90 giây đầu tiên** trước khi làm bài.

#### Các bước thực hiện Skimming chuẩn B2:
1. **Đọc Tiêu đề (Title) & Tiểu mục (Subheadings):** Định hình ngay chủ đề lớn và phạm vi thảo luận.
2. **Đọc kỹ Đoạn Mở đầu (Introduction):** Đặc biệt chú ý câu cuối cùng của đoạn 1 — đây thường là **Thesis Statement (Câu luận đề)**, nêu rõ 2-3 ý chính sẽ được triển khai.
3. **Đọc Câu chủ đề (Topic Sentence) của từng đoạn thân bài:** Thường nằm ở câu đầu tiên hoặc câu thứ hai (sau câu dẫn nhập). Nếu câu đầu bắt đầu bằng liên từ đối lập (*However, But, In contrast*), ý chính thực sự nằm ở vế sau liên từ.
4. **Đọc 1-2 câu cuối của Đoạn Kết luận (Conclusion):** Nắm bắt thông điệp đọng lại hoặc hướng phát triển tương lai mà tác giả khẳng định.

```
       [Đoạn 1: Mở đầu] ------------> Xác định Thesis Statement (Luận điểm trung tâm)
             |
       [Đoạn 2: Thân bài 1] --------> Đọc Topic sentence (Ý chính 1)
             |
       [Đoạn 3: Thân bài 2] --------> Đọc Topic sentence (Ý chính 2)
             |
       [Đoạn 4: Thân bài 3] --------> Đọc Topic sentence (Ý chính 3)
             |
       [Đoạn 5: Kết bài] -----------> Đọc Kết luận & Khuyến nghị của tác giả
```

### 2.2. Scanning: Đọc định vị thông tin chi tiết, số liệu và thuật ngữ
Scanning là kỹ thuật dò tìm từ khóa (Keywords) trong đoạn văn mà **không cần đọc hiểu toàn bộ câu chữ trên đường dò**. Mắt bạn di chuyển theo hình chữ Z hoặc lượn sóng từ trên xuống dưới.

#### Kỹ thuật phân loại từ khóa khi Scanning:
- **Hard Keywords (Từ khóa cứng - Không thể bị paraphrase):**
  - Tên riêng người, địa danh, tổ chức: *Dr. Robert Sternberg, United Nations, Antarctica*.
  - Số liệu, năm tháng, phần trăm, thời gian: *in 1984, 45%, 18th century, $2.5 billion*.
  - Thuật ngữ chuyên môn viết hoa hoặc đặt trong ngoặc kép: *"neuroplasticity", "greenwashing"*.
  - *Hành động:* Định vị các từ này cực nhanh trong vòng 3-5 giây.
- **Soft Keywords (Từ khóa mềm - Thường xuyên bị paraphrase):**
  - Động từ chỉ hành động, tính từ đánh giá, danh từ chung: *accelerate, hazardous, consequence, obstacle*.
  - *Hành động:* Khi câu hỏi chứa từ khóa mềm, bạn phải chủ động suy nghĩ sẵn trong đầu các từ đồng nghĩa (synonyms) hoặc cách diễn đạt tương đương trước khi scan bài:
    - *harmful effects* $\rightarrow$ *detrimental impacts, adverse consequences, hazardous repercussions*.
    - *significant increase* $\rightarrow$ *exponential growth, dramatic surge, sharp rise*.

### 2.3. Intensive Reading: Kỹ thuật bóc tách cú pháp câu đa mệnh đề phức tạp
Đoạn văn B2-C1 trong VSTEP thường có những câu dài 40-60 từ chứa nhiều thành phần bổ nghĩa lồng ghép. Nếu đọc thụ động từ trái sang phải, thí sinh sẽ bị quá tải bộ nhớ ngắn hạn. Kỹ thuật bóc tách cú pháp (**Sentence Parsing**) giúp bẻ gãy câu phức tạp thành bộ khung đơn giản.

#### Quy trình 3 bước bóc tách câu phức:
1. **Tìm Chủ ngữ chính (Core Subject) và Động từ chính (Core Verb):** Bỏ qua tạm thời các mệnh đề phụ.
2. **Khoanh vùng và đặt trong dấu ngoặc đơn các thành phần bổ ngữ phụ:**
   - Mệnh đề quan hệ: *(which is characterized by...)*
   - Cụm phân từ rút gọn: *(having been discovered in 1995,...)*
   - Mệnh đề trạng ngữ: *(although recent clinical trials suggest otherwise,...)*
   - Thành phần đồng vị ngữ giữa 2 dấu phẩy/gạch ngang: *(— an unprecedented phenomenon —)*
3. **Đọc bộ khung lõi trước, sau đó ghép các thành phần bổ nghĩa vào sau.**

> **Ví dụ phân tích:**
> *Sentence:* "Despite widespread initial skepticism from mainstream aerodynamic engineers, the revolutionary propulsion system, which was conceptualized by a clandestine consortium of independent physicists, ultimately demonstrated an efficiency that surpassed all theoretical benchmarks."
> 
> - **Thành phần phụ 1 (Nhượng bộ):** *[Despite widespread initial skepticism from mainstream aerodynamic engineers]*
> - **Chủ ngữ cốt lõi (Core Subject):** **the revolutionary propulsion system**
> - **Thành phần phụ 2 (Mệnh đề quan hệ bổ nghĩa):** *[which was conceptualized by a clandestine consortium of independent physicists]*
> - **Động từ cốt lõi (Core Verb):** **ultimately demonstrated**
> - **Tân ngữ cốt lõi (Core Object):** **an efficiency**
> - **Thành phần phụ 3 (Mệnh đề so sánh):** *[that surpassed all theoretical benchmarks]*
> 
> $\rightarrow$ **Ý cốt lõi:** Hệ thống đẩy mới rốt cuộc đã chứng minh hiệu suất vượt mọi tiêu chuẩn lý thuyết (dù ban đầu bị hoài nghi).

### 2.4. Context Clues & Phân tích hình thái từ: Đoán nghĩa từ vựng chuyên ngành
Trong đề VSTEP B2, chắc chắn bạn sẽ gặp từ mới. Thí sinh điểm cao không phải là người biết mọi từ trên đời, mà là người có năng lực suy luận nghĩa chính xác từ ngữ cảnh.

#### 5 Manh mối ngữ cảnh (Context Clues) kinh điển:
1. **Manh mối Định nghĩa / Diễn giải (Definition / Restatement Clues):**
   - Dấu hiệu: Dấu gạch ngang `—`, dấu hai chấm `:`, dấu ngoặc đơn `()`, từ khóa *that is, in other words, known as, defined as, refers to*.
   - *Ví dụ:* "Entomophagy — **the human practice of consuming insects as food** — is gaining traction as a sustainable protein solution." $\rightarrow$ *Entomophagy* là tục lệ ăn côn trùng.
2. **Manh mối Tương phản / Nhượng bộ (Contrast Clues):**
   - Dấu hiệu: *However, in contrast, unlike, whereas, while, on the other hand, conversely, rather than*.
   - *Ví dụ:* "While his predecessor was known for his **profligate** spending habits, the new CEO adopted an exceptionally frugal approach to company expenses." $\rightarrow$ *Frugal* (tiết kiệm) đối lập với *profligate*, suy ra *profligate* = hoang phí, tiêu xài xa xỉ.
3. **Manh mối Tương đồng / Liệt kê (Similarity & Series Clues):**
   - Dấu hiệu: *Similarly, likewise, and other, such as, for instance*.
   - *Ví dụ:* "The mountain trail was fraught with hazards, such as precipitous cliffs, **treacherous** ice patches, and erratic weather." $\rightarrow$ Nằm trong chuỗi các mối nguy hiểm (*hazards*), suy ra *treacherous* mang nét nghĩa nguy hiểm rình rập, không an toàn.
4. **Manh mối Nguyên nhân - Kết quả (Cause and Effect Clues):**
   - Dấu hiệu: *Because, therefore, consequently, leading to, as a result of, thus*.
   - *Ví dụ:* "Because the drought was so prolonged, the reservoir was completely **depleted**, forcing the municipal government to ration potable water." $\rightarrow$ Vì hạn hán kéo dài nên hồ chứa nước cạn kiệt (*depleted* = emptied / used up).
5. **Phân tích Hình thái học (Morphological Breakdown - Prefix / Root / Suffix):**
   - Tách từ thành Tiền tố (Prefix) + Gốc từ (Root) + Hậu tố (Suffix).
   - *Ví dụ:* **Irrevocable**
     - Prefix: *Ir-* = Không (not)
     - Root: *voc / voke* = Tiếng gọi, lời nói (voice, call)
     - Suffix: *-able* = Có thể
     - $\rightarrow$ *Irrevocable* = Không thể gọi lại/thu hồi được $\rightarrow$ Không thể thay đổi / Không thể hoàn tác (unalterable).

---

## 3. CẨM NANG CHI TIẾT 10 DẠNG CÂU HỎI VSTEP READING

Mỗi bài đọc VSTEP gồm 10 câu hỏi trắc nghiệm. Dưới đây là phân tích chi tiết toàn bộ 10 dạng câu hỏi chuẩn hóa cùng quy trình xử lý, bẫy tâm lý và ví dụ minh họa học thuật.

---

### DẠNG 1: MAIN IDEA / PRIMARY PURPOSE / BEST TITLE (Ý CHÍNH, MỤC ĐÍCH TỔNG QUÁT, TIÊU ĐỀ)

#### 1. Dấu hiệu nhận biết
- *What is the main idea / primary purpose of the passage?*
- *Which of the following would be the best title for the reading?*
- *The author's main concern in the passage is to...*
- *What is paragraph 2 mainly about?*

#### 2. Quy trình 4 bước xử lý chuẩn
- **Bước 1: Để câu hỏi này làm cuối cùng của bài đọc!** Sau khi đã làm xong các câu hỏi chi tiết từ câu 2 đến câu 9, bạn đã hiểu sâu 70-80% nội dung văn bản. Trả lời Main Idea lúc này chỉ mất 15-20 giây và độ chính xác đạt gần 100%.
- **Bước 2: Tổng hợp Thesis Statement và các Topic Sentences.** Đối chiếu câu chủ đề đoạn 1 và các đoạn thân bài.
- **Bước 3: Kiểm tra phạm vi (Scope Check).** Ý chính phải bao quát toàn bộ bài đọc:
  - Loại phương án **Too Narrow (Quá hẹp):** Chỉ nhắc đến một chi tiết của riêng đoạn 2 hoặc đoạn 3.
  - Loại phương án **Too Broad (Quá rộng):** Phạm vi khái quát vượt ra ngoài bài đọc (ví dụ: bài chỉ nói về AI trong y tế nhưng đáp án nói về toàn bộ nền văn minh nhân loại).
  - Loại phương án **Off-topic / Inaccurate (Lạc đề hoặc sai lệch quan điểm tác giả).**
- **Bước 4: Đối chiếu động từ chỉ mục đích (nếu hỏi Purpose):**
  - *To argue / advocate:* Tranh biện, bảo vệ 1 quan điểm cụ thể.
  - *To explain / illustrate:* Giải thích cơ chế, minh họa hiện tượng.
  - *To compare / contrast:* So sánh đối chiếu 2 trường phái/sự vật.
  - *To warn / critique:* Cảnh báo rủi ro, phê phán hạn chế.

#### 3. Bẫy kinh điển
- **Bẫy "Topic Sentence nhầm":** Đoạn 1 mở đầu bằng một câu chuyện hoặc một quan điểm lỗi thời (*Historically, people believed that...*), sau đó câu cuối đoạn 1 mới lật ngược vấn đề (*However, modern empirical research reveals...*). Thí sinh đọc vội câu đầu sẽ chọn sai ý chính!

#### 4. Ví dụ học thuật B2 & Phân tích chuyên sâu
> **Text Snippet:**
> "For decades, industrial agricultural practices have achieved unprecedented crop yields through intensive synthetic fertilization and chemical pest management. However, this productivity has incurred profound ecological debts, including the depletion of topsoil microorganisms and severe nitrogen runoff into aquatic ecosystems. In response, agroecology has emerged not merely as an alternative farming technique, but as a holistic paradigm that integrates ecological principles into agricultural production. By mimicking natural ecological processes—such as polyculture cropping, organic composting, and biological pest control—agroecology revitalizes soil fertility, enhances biodiversity, and bolsters resilience against climatic volatility. While critics argue that widespread adoption may temporarily depress global food output, accumulating evidence suggests that diversified agroecological systems can deliver comparable yields over the long term while definitively securing environmental sustainability."
>
> **Question:** *Which of the following best expresses the main idea of the passage?*
> A. The catastrophic effects of synthetic fertilization on global soil quality.
> B. The emergence and long-term sustainability benefits of agroecology compared to industrial agriculture.
> C. Why agroecological farming will inevitably cause a global food crisis.
> D. A technical comparison between polyculture cropping and biological pest control.
>
> **Phân tích:**
> - **A sai (Too Narrow):** Chỉ là chi tiết tiêu cực của nông nghiệp công nghiệp được nhắc ở câu 1-2 để làm nền.
> - **C sai (Distorted / Contrary):** Bài viết nêu critics lo ngại sản lượng giảm tạm thời, nhưng tác giả kết luận agroecology đem lại sản lượng tương đương và bền vững lâu dài. C khẳng định "inevitably cause a global food crisis" là bóp méo thông tin.
> - **D sai (Too Narrow):** Polyculture và biological pest control chỉ là 2 kỹ thuật nhỏ minh họa ở giữa đoạn.
> - **B đúng (Accurate & Comprehensive):** Bao quát toàn bộ tiến trình: từ hạn chế của nông nghiệp công nghiệp đến sự xuất hiện của nông nghiệp sinh thái (agroecology) và lợi ích bền vững lâu dài của nó.

---

### DẠNG 2: FACTUAL DETAILS / DIRECT COMPREHENSION (THÔNG TIN CHI TIẾT TRỰC TIẾP)

#### 1. Dấu hiệu nhận biết
- *According to paragraph X, what / why / how / when...?*
- *The author states that...*
- *Which of the following is true about X, according to the passage?*

#### 2. Quy trình 4 bước xử lý chuẩn
- **Bước 1:** Đọc câu hỏi, xác định **Keywords** (tên riêng, thuật ngữ, hành động chính).
- **Bước 2:** Scan bài đọc để tìm vị trí xuất hiện của keywords hoặc từ đồng nghĩa trong đoạn được chỉ định.
- **Bước 3:** Đọc kỹ **1 câu trước, câu chứa từ khóa và 1 câu sau** (Context Window 3 câu). Áp dụng Sentence Parsing để nắm vững quan hệ ngữ nghĩa.
- **Bước 4:** Đối chiếu với 4 đáp án. **Đáp án đúng luôn là một sự diễn đạt lại (Paraphrase) của thông tin trong bài, KHÔNG BAO GIỜ dùng nguyên vẹn 100% câu chữ.**

#### 3. Bẫy kinh điển
- **Bẫy Verbatim Matching (Bẫy sao chép y nguyên):** Đáp án sai chứa y nguyên cụm từ khó trong bài nhưng bị tráo đổi chủ ngữ, động từ hoặc đảo lộn vị trí điều kiện khiến ý nghĩa sai hoàn toàn.

#### 4. Ví dụ học thuật B2 & Phân tích chuyên sâu
> **Text Snippet:**
> "Urban heat islands (UHIs) occur when metropolitan areas experience significantly warmer temperatures than surrounding rural locales. While dense concentrations of concrete and asphalt absorb and re-emit solar radiation, the extensive loss of vegetative cover further impedes the natural cooling mechanism of evapotranspiration. Consequently, ambient urban air temperatures during nocturnal hours can remain up to 5 degrees Celsius higher than in neighboring forested outskirts."
>
> **Question:** *According to the passage, what is one major reason why urban areas maintain higher nighttime temperatures?*
> A. Rural areas absorb more solar radiation during daytime hours.
> B. Asphalt and concrete prevent ambient air from circulating vertically.
> C. The reduction of vegetation disrupts the natural cooling process of evapotranspiration.
> D. Forests release excessive heat during nighttime hours into metropolitan regions.
>
> **Phân tích:**
> - Scan từ khóa: *higher nighttime temperatures / nocturnal hours*.
> - Đoạn văn giải thích 2 nguyên nhân: (1) Bê tông/nhựa đường hấp thụ và tỏa nhiệt; (2) Sự mất đi của thảm thực vật cản trở quá trình bốc thoát hơi nước làm mát tự nhiên (*evapotranspiration*).
> - Đối chiếu đáp án:
>   - A sai: Ngược thông tin (đô thị hấp thụ nhiệt nhiều hơn nông thôn).
>   - B sai: Bài không nói bê tông ngăn không khí lưu thông theo phương thẳng đứng.
>   - D sai: Vô lý và trái ngược hoàn toàn với văn bản.
>   - **C đúng:** Paraphrase hoàn hảo cụm *"the extensive loss of vegetative cover further impedes the natural cooling mechanism of evapotranspiration"* $\rightarrow$ *"The reduction of vegetation disrupts the natural cooling process of evapotranspiration"*.

---

### DẠNG 3: NEGATIVE FACTUAL DETAILS (DẠNG PHỦ ĐỊNH: EXCEPT / NOT MENTIONED)

#### 1. Dấu hiệu nhận biết
- *All of the following are mentioned as benefits of X EXCEPT...*
- *Which of the following is NOT stated in paragraph X?*
- *The author mentions all of the following as causes of Y, EXCEPT...*

#### 2. Quy trình 4 bước xử lý chuẩn
- **Bước 1:** Nhìn rõ từ **EXCEPT / NOT** (thường được in hoa trong đề thi).
- **Bước 2:** Xác định vùng thông tin trong đoạn văn (thường là một chuỗi liệt kê 3-4 ý, có liên từ *firstly, additionally, furthermore, along with, such as*).
- **Bước 3:** Sử dụng **Chiến thuật Kiểm tra Loại trừ (Checklist Elimination):** Lần lượt tìm kiếm 4 phương án trong bài:
  - Nếu phương án nào xuất hiện trong bài $\rightarrow$ Gạch bỏ (vì đây là thông tin ĐÚNG).
  - Phương án nào KHÔNG ĐƯỢC NHẮC ĐẾN hoặc BỊ NÓI SAI SỰ THẬT $\rightarrow$ **Đó chính là đáp án cần chọn!**
- **Bước 4:** Xác nhận lại lần cuối phương án đã chọn có thực sự vắng mặt hoặc sai lệch không.

#### 3. Bẫy kinh điển
- Thí sinh đọc lướt quá nhanh bỏ qua chữ EXCEPT, thấy đáp án A có trong bài mừng quá khoanh luôn, dẫn đến mất điểm oan uổng!

#### 4. Ví dụ học thuật B2 & Phân tích chuyên sâu
> **Text Snippet:**
> "To mitigate the mounting crisis of microplastic contamination, researchers have proposed several interventions. Firstly, the implementation of advanced membrane bioreactors in municipal wastewater facilities can capture synthetic microfibers before they reach marine ecosystems. Secondly, the industrial manufacturing sector is urged to replace non-biodegradable polymer packaging with mycelium-based composites. Additionally, rigorous governmental regulations, such as taxes on single-use polyethylene containers, have demonstrated measurable reductions in consumer disposal. However, direct mechanical filtration of open oceanic gyres remains economically unviable due to prohibitive energy requirements."
>
> **Question:** *According to the passage, all of the following are viable strategies to reduce microplastic pollution EXCEPT:*
> A. Installing advanced membrane bioreactors in municipal water treatment plants.
> B. Substituting mycelium composites for non-biodegradable packaging materials.
> C. Utilizing direct mechanical filtration systems to extract plastics from ocean gyres.
> D. Imposing financial levies on single-use plastic containers.
>
> **Phân tích:**
> - Tìm 4 phương án trong đoạn trích:
>   - A có trong bài: *"advanced membrane bioreactors in municipal wastewater facilities can capture..."* $\rightarrow$ Loại A.
>   - B có trong bài: *"replace non-biodegradable polymer packaging with mycelium-based composites"* $\rightarrow$ Loại B.
>   - D có trong bài: *"taxes on single-use polyethylene containers"* (taxes = financial levies) $\rightarrow$ Loại D.
>   - C: Trong bài viết rõ: *"mechanical filtration of open oceanic gyres remains economically unviable"* (lọc cơ học trực tiếp ở đại dương là KHÔNG KHẢ THI về mặt kinh tế do tốn năng lượng) $\rightarrow$ C không phải là viable strategy.
>   - **Chọn C!**

---

### DẠNG 4: PRONOUN REFERENCE (TỪ QUY CHIẾU ĐẠI TỪ)

#### 1. Dấu hiệu nhận biết
- *The word "it / they / them / which / this" in paragraph X refers to...*
- *The phrase "the latter / the former" in line Y refers to...*

#### 2. Quy trình 4 bước xử lý chuẩn
- **Bước 1:** Xác định vị trí của đại từ trong bài và xác định **tính chất ngữ pháp** của đại từ:
  - *It / this / that:* Quy chiếu danh từ số ít hoặc cả một mệnh đề phía trước.
  - *They / them / these / those:* Quy chiếu danh từ số nhiều (người hoặc vật).
  - *Which:* Thường quy chiếu danh từ ngay trước nó (hoặc cả mệnh đề trước dấu phẩy).
- **Bước 2:** Đọc ngược lại câu trước đó (hoặc nửa đầu của câu hiện tại), tìm tất cả các danh từ/cụm danh từ phù hợp về mặt số ít/số nhiều.
- **Bước 3: Phương pháp Thay thế Thử nghiệm (Substitution Test):** Lắp từng danh từ vào vị trí của đại từ và dịch nghĩa. Xem câu có logic và mạch lạc về ngữ nghĩa không.
- **Bước 4:** Loại trừ các danh từ bị ngăn cách bởi các cấu trúc đối lập hoặc đóng vai trò phụ không thể làm chủ thể.

#### 3. Bẫy kinh điển
- **Bẫy Danh từ Gần nhất (Proximity Trap):** Danh từ đứng ngay sát trước đại từ thường là "bẫy", trong khi danh từ chủ ngữ thực sự đứng ở đầu câu trước.

#### 4. Ví dụ học thuật B2 & Phân tích chuyên sâu
> **Text Snippet:**
> "When cognitive scientists investigated the neural mechanisms underlying bilingualism, they discovered that managing two linguistic systems simultaneously requires constant executive control. Although monolinguals often demonstrate larger vocabularies in their single language, bilingual individuals exhibit superior conflict-resolution skills and attentional flexibility. Consequently, **they** tend to suffer cognitive decline associated with Alzheimer's disease up to four to five years later than their unilingual peers."
>
> **Question:** *The word "they" in the passage refers to:*
> A. cognitive scientists
> B. linguistic systems
> C. monolinguals
> D. bilingual individuals
>
> **Phân tích:**
> - "They" là đại từ nhân xưng số nhiều làm chủ ngữ cho hành động *"tend to suffer cognitive decline... four to five years later"* (có xu hướng bị suy giảm nhận thức muộn hơn 4-5 năm).
> - Danh từ số nhiều ở câu trước gồm: *monolinguals* (người đơn ngữ), *bilingual individuals* (người song ngữ), *conflict-resolution skills*, *attentional flexibility*.
> - Lắp thử vào câu:
>   - Kỹ năng (skills) không thể "suffer cognitive decline" $\rightarrow$ Loại B.
>   - Các nhà khoa học (cognitive scientists) ở câu đầu tiên chỉ là người nghiên cứu, không phải người bị suy giảm nhận thức muộn hơn $\rightarrow$ Loại A.
>   - So sánh hai đối tượng ở câu trước: Người đơn ngữ (monolinguals) có từ vựng rộng hơn, NHƯNG người song ngữ (bilingual individuals) có khả năng giải quyết xung đột nhận thức tốt hơn. Vì vậy, người song ngữ chính là người trì hoãn được bệnh Alzheimer $\rightarrow$ Loại C.
>   - **D đúng (bilingual individuals).**

---

### DẠNG 5: VOCABULARY IN CONTEXT (TỪ VỰNG TRONG VĂN CẢNH HỌC THUẬT)

#### 1. Dấu hiệu nhận biết
- *The word "X" in paragraph Y is closest in meaning to...*
- *In stating that [...], the author means that the phenomenon is...*

#### 2. Quy trình 4 bước xử lý chuẩn
- **Bước 1: Tuyệt đối không chỉ dịch nghĩa gốc trong từ điển!** Một từ tiếng Anh có nhiều nét nghĩa tùy thuộc ngữ cảnh (polysemy).
- **Bước 2:** Đọc câu chứa từ đó, xác định **từ loại** (Verb, Noun, Adj) và **sắc thái biểu cảm** (Tích cực +, Tiêu cực -, hay Trung tính 0).
- **Bước 3:** Sử dụng **Kỹ thuật Che từ (Blanking Technique):** Dùng tay che từ cần hỏi lại, đọc cả câu và tự điền một từ tiếng Anh đơn giản (hoặc một từ tiếng Việt) phù hợp nhất với logic của câu.
- **Bước 4:** Lắp 4 đáp án vào vị trí của từ và chọn phương án bảo toàn sự trôi chảy, mạch lạc logic của toàn bộ câu văn.

#### 3. Bẫy kinh điển
- **Bẫy Nghĩa phổ biến nhất (Primary Meaning Trap):** Đề thi cố tình đưa nghĩa thông dụng nhất của từ ở trình độ A2/B1 vào đáp án A, nhưng trong văn bản học thuật B2, từ đó lại được dùng với nghĩa chuyên biệt thứ 2 hoặc thứ 3!
  - *Ví dụ:* Từ "address" thông thường là "địa chỉ nhà", nhưng trong văn cảnh học thuật B2 nó là động từ mang nghĩa "giải quyết vấn đề" (*deal with / tackle / resolve*).

#### 4. Ví dụ học thuật B2 & Phân tích chuyên sâu
> **Text Snippet:**
> "Despite fierce initial resistance from traditional educational institutions, online collaborative platforms have steadily gained widespread acceptance. The sudden shift toward remote instruction during international emergencies merely served to **catalyze** a transformation that was already underway, forcing even conservative universities to integrate digital curricula."
>
> **Question:** *The word "catalyze" in the passage is closest in meaning to:*
> A. accelerate
> B. prevent
> C. evaluate
> D. terminate
>
> **Phân tích:**
> - Ngữ cảnh: Việc chuyển sang dạy trực tuyến trong tình trạng khẩn cấp quốc tế chỉ đóng vai trò làm [CATALYZE] một sự chuyển đổi vốn đã diễn ra từ trước, buộc cả các trường đại học bảo thủ cũng phải tích hợp chương trình số hóa.
> - Gốc từ: *Catalyst* (chất xúc tác trong hóa học). Động từ *catalyze* = đóng vai trò chất xúc tác $\rightarrow$ làm cho quá trình diễn ra nhanh hơn / thúc đẩy.
> - Đối chiếu 4 phương án:
>   - A. accelerate: tăng tốc, thúc đẩy nhanh chóng (+).
>   - B. prevent: ngăn chặn (-).
>   - C. evaluate: đánh giá (0).
>   - D. terminate: chấm dứt (-).
>   - **A đúng (accelerate).**

---
"""

with open(target_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Part 1 of Reading Master written successfully. Bytes:", len(content))
