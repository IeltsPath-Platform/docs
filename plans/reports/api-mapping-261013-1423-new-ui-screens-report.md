# API cho các màn hình mới (P-44 3 cột, P-45, P-46, P-47, P-54, P-80)

Ngày: 13/10/2026 · Wireframe: `docs/wireframes/screens/` · Mã API theo FDS Appendix A.
Đối chiếu với controller backend tại `eedc6cd`. **Có** = endpoint đã chạy; **Thiếu** = cần thêm vào backend.

## Tổng hợp endpoint còn thiếu

| # | Endpoint đề xuất | Service | Dùng ở | Ghi chú |
|---|---|---|---|---|
| N1 | `GET /api/assessments/catalog?type=MOCK` (API-150) | assessment | P-46 | FDS 2.21 đã đặc tả, backend chưa có |
| N2 | `GET /api/assessments/attempts?type=&skill=&status=&page=&size=` | assessment | P-46, P-54 | Danh sách attempt của tôi + tóm tắt kết quả (band, trạng thái chấm) |
| N3 | `POST /api/assessments/attempts/{id}/items/{itemId}/recording` (multipart) → `audioReference` | assessment | P-45, P-47 Speaking | Hiện bản ghi chỉ nằm ở trình duyệt (FG-19, OQ-08) |
| N4 | `GET /api/learning/writing-submissions?page=&size=` | learning | P-54 | Hiện chỉ có `GET /writing-submissions/{id}` (API-137) |
| N5 | `GET /api/learning/practice-attempts?page=&size=` | learning | P-54 | Hiện chỉ có `GET /practice-attempts/{id}` (API-128) |
| N6 | `GET /api/access/me/key-activations?offset=&limit=` | access | P-80 Lịch sử kích hoạt gói | Chưa có cổng thanh toán; "thanh toán" = các lần kích hoạt mã Key |
| N7 | `GET /api/users/me/sessions`, `DELETE /api/users/me/sessions/{id}`, `POST /api/users/me/sessions/revoke-others` | user | P-80 Lịch sử đăng nhập | Cần migration: refresh token mới có `created_at/expires_at/revoked_at`, chưa lưu IP, user-agent, `last_used_at` |
| N8 | `POST /api/users/me/avatar` (multipart) → `avatarReference` | user | P-80 Hồ sơ | `avatarReference` hiện chỉ là chuỗi; chưa có chỗ upload cho học viên |

## P-45 Speaking Practice (`/practice/speaking/:cueId`)

| Hành động | API | Trạng thái |
|---|---|---|
| Mở bài (gói Speaking) | API-138 `POST /api/assessments/attempts` `{packageVersionId, mode, channel}` → API-144 `GET /attempts/{id}/structure` | Có (FE hiện dùng cue mock) |
| Hướng dẫn chung, Kiểm tra micro | — (getUserMedia trên trình duyệt) | Không cần API |
| Ghi âm xong một câu | N3 upload → API-145 `PUT /attempts/{id}/items/{itemId}/response` với `audioReference` | **Thiếu N3** |
| Hết Part | API-143 `POST /attempts/{id}/sections/{sectionId}/complete` | Có |
| Nộp bài | API-147 `POST /attempts/{id}/submit` → API-155 `POST /api/assessments/submissions` `{attemptItemId, promptSnapshot, skill: SPEAKING, audioReference, submissionKey}` | Có; chấm Speaking bằng AI chưa có (UC-062 Draft), nên chuyển EXAMINER |
| Xem kết quả | API-148 `GET /attempts/{id}/result` | Có |

## P-44 Writing Practice — bố cục 3 cột

| Hành động | API | Trạng thái |
|---|---|---|
| Tra từ Anh → Việt | API-82 `GET /api/content/vocabulary/search?query=` | Có |
| Tra từ Việt → Anh | — | Ngoài phạm vi (chỉ tra Anh-Việt) |
| Lưu vào Flashcard | API-104 `POST /api/learning-support/flashcards` | Có |
| Word count, đồng hồ, chia đoạn | — (client; ghép các đoạn thành `textPayload` khi nộp) | Không cần API |
| Hoàn thành (bài thi/đề luyện có attempt) | API-145 lưu text → API-147 submit → API-155 `{skill: WRITING, textPayload}` | Có |
| Hiện số điểm còn lại | API-43 `GET /api/access/me/points` | Có |

## P-46 Mock Test Catalog (`/tests`, FDS 2.21)

| Hành động | API | Trạng thái |
|---|---|---|
| Danh sách đề thi thử | N1 (API-150) | **Thiếu** |
| Trạng thái từng đề (Đang làm / Band) | N2 `?type=MOCK` | **Thiếu** |
| Lượt chấm EXAMINER, số điểm, khóa Premium | API-42 `GET /api/access/me/subscription`, API-43 | Có |
| Bắt đầu / Làm tiếp | API-138 (bắt đầu); Làm tiếp dùng `attemptId` từ N2 | Có / phụ thuộc N2 |

## P-47 Mock Test Runner (`/tests/:attemptId`)

| Hành động | API | Trạng thái |
|---|---|---|
| Tải đề, thời gian từng phần | API-144 structure | Có |
| Khôi phục đáp án khi F5 | API-141 `GET /attempts/{id}/responses` | Có |
| Vào / hết một phần | API-142 start, API-143 complete | Có |
| Lưu đáp án (TFNG, điền từ, chọn 2 đáp án) | API-145 `PUT /items/{itemId}/response` (autosave) | Có |
| Audio Listening | URL media trong structure (`CONTENT_MEDIA_BASE_URL`) | Có (không cần API riêng) |
| Hết giờ | API-146 `POST /attempts/{id}/expire` | Có (FE chưa gọi) |
| Nộp bài (✓ → hộp thoại) | API-147 submit; Writing/Speaking: API-155; Speaking cần N3 | Có, trừ N3 |
| Kết quả | API-148 | Có |

## P-54 Lịch sử nộp bài (`/submission-history`, FDS 2.54)

| Hành động | API | Trạng thái |
|---|---|---|
| Tab Writing / Speaking / Reading / Listening / Mock Test | N2 `?skill=&type=` (bài thi, đề luyện, placement); N4 (Writing trong bài học); N5 (Practice) | **Thiếu N2, N4, N5** |
| Xem nhận xét Writing bài học | API-137 `GET /api/learning/writing-submissions/{id}` | Có |
| Xem bài / kết quả thi | API-148; placement: API-149 | Có |
| Màn trống → "Tiến hành làm bài tập ngay" | — (điều hướng `/practice-tests`) | Không cần API |

## P-80 Tài khoản (`/account/*`, FDS 2.26 + 2.28) — mở từ user menu (◯ Học viên ▾), không có sidebar

| Tab / hành động | API | Trạng thái |
|---|---|---|
| Hồ sơ: tải | API-09 `GET /api/users/me`, API-11 `GET /api/users/me/profile` | Có |
| Hồ sơ: cập nhật | API-10 `PUT /api/users/me` `{fullName, phoneNumber}`, API-12 `PUT /api/users/me/profile` `{displayName, avatarReference, bio, selfReportedBand, timezone}` | Có |
| Thay ảnh đại diện | N8 | **Thiếu** |
| Dấu ✔ số điện thoại đã xác minh | — | **Chưa có** xác minh SĐT; nên bỏ dấu ✔ hoặc thêm luồng OTP |
| Lịch sử kích hoạt gói: gói hiện tại | API-42 | Có |
| Lịch sử kích hoạt gói: danh sách | N6 | **Thiếu** |
| Nhập mã Key | API-45 `POST /api/access/me/keys/activate` `{rawKey, idempotencyKey}` | Có |
| Giao dịch điểm | API-43 số dư, API-44 `GET /api/access/me/points/history?offset=&limit=20` | Có (lọc Cộng/Trừ làm ở client, hoặc thêm `type=`) |
| Lịch sử đăng nhập, đăng xuất thiết bị khác | N7 (+ migration refresh token) | **Thiếu** |

## Từ điển (P-56 → P-59a, FDS 2.31) — theo sheet "Mô tả Từ điển" (Code LMS_TIS.xlsx)

Backend hiện có (library-service): `vocabulary_items` (lemma, **một** `ipa`, **một** audio) + `vocabulary_senses`
(từ loại, `english_definition`, `vietnamese_meaning`, **một** `example_sentence`, `image_url`); flashcard, deck, note.

| Màn / hành động | API | Trạng thái |
|---|---|---|
| Tra từ (P-56, P-57), gợi ý khi gõ | API-82 `GET /api/content/vocabulary/search?query=` | Có (chỉ khớp từ tiếng Anh) |
| Mở chi tiết từ (P-57) | API-83 `GET /api/content/vocabulary/{id}` | Có, nhưng **thiếu trường** — xem D1 |
| Lưu vào sổ từ / "Lưu và học từ này" | API-104 `POST /api/learning-support/flashcards` (`vocabulary_sense_id`), API-114 thêm vào deck | Có |
| Ghi chú của tôi (≤300 ký tự) | API-99 `POST /api/learning-support/notes` (gắn với từ) | Có; cần trường liên kết tới từ nếu note chưa có `source` |
| Mức độ hiểu từ (Chưa biết/Mới biết/Đang học/Đã nhớ), "Ôn từ này sau" | D2 | **Thiếu** |
| Khám phá bộ từ (band, chủ đề, Oxford 3000/5000, Collocations, Sổ tay) | D3 (Sổ tay = API-110 decks) | **Thiếu** (trừ Sổ tay) |
| Trang bộ từ P-59: chủ đề, tiến độ, từ gần đây | D3 + D4 | **Thiếu** |
| Học bộ từ P-59a (Flashcard, điền từ, dịch, nối từ, học trộn) — tự loại từ đã học | D5 | **Thiếu** |
| Trình độ hiện tại (B1), Bản đồ từ vựng P-58, số liệu 1,246/4,000 | D4 | **Thiếu** |
| Mục tiêu tuần (86/120 từ) | D6 (có thể dựa trên API-35/36 activities) | **Thiếu** |
| "Kiểm tra lại" trình độ | điều hướng tới placement (P-30a) | Không cần API mới |
| Dịch câu bằng AI khi nhập câu (P2) | D7 | **Thiếu** (giai đoạn sau) |
| AI tạo bộ từ riêng (P3) | D8 | **Thiếu** (giai đoạn sau) |

| # | Đề xuất | Service |
|---|---|---|
| D1 | Mở rộng dữ liệu từ (migration mới): IPA + audio **UK/US**, `cefr`, `ielts_level`, `opal_tag`, `usage_labels[]`, `frequency`, `awl`, `topics[]`, nhiều ví dụ (+ bản dịch), `collocations[]`, `word_family`, `synonyms[]`, `antonyms[]`, `idioms[]`, `common_mistakes[]`, ảnh ghi nhớ Gen AI | library |
| D2 | `PUT /api/learning-support/word-states/{senseId}` `{state, reviewAt}` · `GET /api/learning-support/word-states?senseIds=` | library |
| D3 | `GET /api/content/vocabulary-sets?type=BAND|TOPIC|OXFORD|COLLOCATION` · `GET /api/content/vocabulary-sets/{id}` (chủ đề + từ, phân trang) · CRUD cho admin | library |
| D4 | `GET /api/learning-support/vocabulary-progress?groupBy=cefr` (đã học / đang ôn / cần ôn / chưa học, trình độ ước lượng) · `GET /api/learning-support/vocabulary-sets/{id}/progress` | library |
| D5 | `POST /api/learning-support/vocabulary-sets/{id}/study-sessions` (sinh câu hỏi trộn, bỏ từ đã thành thạo) · `POST /study-sessions/{id}/answers` (cập nhật D2) | library |
| D6 | `GET /api/learning-support/vocabulary-goal` · `PUT …` `{weeklyTarget}` | library (hoặc user) |
| D7 | `POST /api/learning-support/translate` `{text}` — có hạn mức theo ngày như các tác vụ LLM khác | library |
| D8 | `POST /api/learning-support/vocabulary-sets/generate` `{prompt}` | library |

## Quyết định đã chốt (13/10/2026)

- Tab tài khoản đặt tên **Lịch sử kích hoạt gói** (chưa có cổng thanh toán; mỗi dòng là một lần kích hoạt mã Key).
- Chỉ **tra Anh-Việt** (API-82); tra Việt-Anh ngoài phạm vi. Tab Việt-Anh ở Placement (FE đã build) cần gỡ.
- Lịch sử nộp bài thành mục **FDS 2.54 Submission History** (thêm cuối Phần 2 để giữ số mục cũ).
- Dashboard bỏ sidebar trái; rê chuột vào **Dashboard** mở popup Tổng quát · Dữ liệu chi tiết · Lịch sử ôn luyện · Xếp hạng (P-11 / Menu Dashboard).
- Thông tin cá nhân chuyển lên **user menu**: Thông tin cá nhân · Lịch sử kích hoạt gói · Lịch sử giao dịch điểm · Lịch sử đăng nhập · Đăng xuất (SHELL / User Menu); P-80 không còn sidebar.
