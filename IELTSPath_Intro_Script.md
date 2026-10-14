# Kịch bản thuyết trình IELTSPath: Báo cáo 1, Vision & Scope

Nhóm SEP490_G112 · Bám theo bộ slide `IELTSPath_Intro_Project.pdf` (20 trang) · Thời lượng: **16 đến 17 phút** thuyết trình + 5 đến 10 phút hỏi đáp.

Cách dùng: **Nói** là lời thoại gợi ý, nói tự nhiên chứ không học thuộc. **Ý chính** là điều bắt buộc phải nói được. **Show** là chỗ nên chỉ vào tài liệu hoặc sản phẩm thật của nhóm. **Ngoại lệ** là nhánh lỗi, nhánh không vui cần nhắc. **Chuyển** là câu nối sang slide sau.

## Trước khi lên: bốn thông điệp hội đồng chấm điểm

Theo góp ý của mentor, mức điểm đi theo bốn tầng: luồng chạy đúng (happy case) được khoảng 6 đến 7; bài toán hoàn chỉnh được 7 đến 8; có kỹ thuật mới và bắt đủ ngoại lệ được 8 đến 9; hiểu và tận dụng AI cho bài toán thì trên 9. Toàn bộ kịch bản xoay quanh bốn thông điệp sau, mỗi thông điệp gắn với một tầng:

1. **Bài toán thật, có chủ đích:** hệ thống sinh ra cho học viên của IELTS Space, giải đúng bảy khoảng trống, và nhóm **chủ động cắt** những gì không phải bài toán chính (thanh toán, kế toán).
2. **Luồng hoàn chỉnh và có ngoại lệ:** không chỉ nói đường đi đẹp, mà nói rõ chuyện gì xảy ra khi học viên làm sai, trượt, kẹt, nhập sai mã, hay một phần hệ thống lỗi.
3. **Microservice là cần thiết, không phải để khoe:** lý do gắn với chính bài toán này, và nhóm sẽ chứng minh bằng performance test.
4. **Hiểu AI, không chỉ gọi AI:** nhóm là kỹ sư, không làm ra AI. Nhóm hiểu tư tưởng của công cụ có sẵn (DeepTutor, mô hình ngôn ngữ), xác định đầu vào của hệ thống mình, và dùng nó để cá nhân hóa việc học.

Ba lưu ý về phong cách:
- **Không đọc lý thuyết.** Hội đồng không cần nghe định nghĩa microservice hay AI. Mỗi khi nói công nghệ, nói ngay nó giải quyết gì cho bài toán này.
- **Lồng ghép sản phẩm thật** ("đây là cái nhóm em đã làm") thay vì slide đơn thuần. Chuẩn bị sẵn file phân tích đối thủ và bản chạy thử.
- **Đổi tên file trước khi chiếu.** Nếu chiếu tài liệu làm cùng trung tâm, tạo bản sao và đổi tên, đừng để lộ chữ "Bản sao của...".

## Bảng thời gian

| Slide | Nội dung | Thời gian |
|---|---|---|
| 1 | Mở đầu | 0:30 |
| 2 | Bối cảnh | 0:45 |
| 3 | Người học điển hình | 0:45 |
| 4 | Vì sao cần làm ngay | 0:45 |
| 5 | Giải pháp hiện có | 1:00 |
| 6 | Khoảng trống | 0:45 |
| 7 | Sơ đồ bối cảnh hệ thống | 1:30 |
| 8 | Hiện trạng AS-IS | 0:30 |
| 9 | Giải pháp TO-BE | 0:45 |
| 10 | Học một bài | 1:15 |
| 11 | Practice và bài ôn | 1:30 |
| 12 | Giải pháp đề xuất | 1:00 |
| 13 | Một kênh cho hai lúc | 0:30 |
| 14 | Thẻ kích hoạt premium | 1:00 |
| 15 | Tính năng chính 1/2 | 1:00 |
| 16 | Tính năng chính 2/2 | 0:45 |
| 17 | Kiến trúc | 1:30 |
| 18 | Giới hạn phạm vi | 0:30 |
| 19 | Giá trị kỳ vọng | 0:30 |
| 20 | Kết thúc | 0:15 |

Nếu thiếu giờ, rút gọn slide 8, 13, 18 trước; ở slide 7 chỉ nói người dùng và gộp sáu hệ thống ngoài thành một câu. Không cắt slide 10, 11, 17: đó là chỗ ghi điểm (luồng, ngoại lệ, kiến trúc).

---

## Slide 1: Mở đầu

**Ý chính:** tên đề tài, cho ai, trọng tâm là cá nhân hóa việc ôn luyện.

**Nói:**
Kính chào hội đồng. Nhóm em là SEP490_G112, xin trình bày Báo cáo 1, Vision và Scope của đề tài **IELTSPath**. Đây là hệ thống ôn luyện IELTS cho học viên trung tâm IELTS Space. Hệ thống không thay giờ học trên lớp, mà bổ trợ bên cạnh và lấp khoảng thời gian học viên chờ lớp band mới. Bài toán cốt lõi nhóm em giải là **học tập thích ứng**: mỗi học viên ôn đúng chỗ mình yếu.

**Chuyển:** Em xin bắt đầu từ bối cảnh của trung tâm.

---

## Slide 2: Bối cảnh

**Ý chính:** học chính ở trên lớp; ngoài giờ lớp không có công cụ khớp nội dung trung tâm; cùng mục tiêu nhưng khác xuất phát.

**Nói:**
IELTS Space là trung tâm luyện thi IELTS tại Hà Nội, dạy theo lớp chia band. Ngoài giờ lớp, học viên tự ôn mà không có công cụ nào khớp với nội dung trung tâm dạy.
Có ba tình huống. **Học viên đang học** tự luyện giữa các buổi, bài làm không được chấm ngay, không biết sai vì thiếu kiến thức gì. **Học viên chờ lớp band mới** gần như không có gì để luyện và dễ ngừng học. Và **cùng mục tiêu, khác xuất phát**: hai bạn cùng nhắm 7.0, một bạn ở 5.0 cần củng cố nền, một bạn ở 6.5 cần luyện phần nâng cao. Mỗi người cần biết mình yếu ở đâu.

**Chuyển:** Cụ thể hơn, đây là hai học viên điển hình.

---

## Slide 3: Người học điển hình

**Ý chính:** Linh luyện không định hướng; Minh ngừng luyện khi chờ lớp.

**Nói:**
**Linh**, sinh viên năm hai, đang học lớp band 5.5, mục tiêu 6.5. Linh thấy điểm số nhưng không biết kỹ năng Reading nào làm mình mất điểm, nên không biết ôn gì trước buổi sau.
**Minh**, nhân viên văn phòng, xong lớp 5.5, đang chờ lớp 6.0. Trong lúc chờ không có bài để luyện, Minh mất nhịp, vào lớp mới phải khởi động lại, và chỉ rảnh buổi tối nên cần bài ngắn.
Hai bạn đại diện cho hai nhóm khách hàng hệ thống phục vụ: **học viên đang học** và **học viên đang chờ lớp**.

**Chuyển:** Vì sao phải giải quyết ngay bây giờ?

---

## Slide 4: Vì sao cần làm ngay

**Ý chính:** học viên đã luyện online rồi, vấn đề là luyện ở đâu; trung tâm cần kênh riêng.

**Nói:**
Học viên đã tự luyện online, nên câu hỏi là **luyện ở đâu**. Tài liệu phát tay không chấm ngay, không giải thích; web miễn phí không khớp band và nội dung lớp. Vì thế trung tâm cần một kênh riêng, bám đúng nội dung mình dạy.
Ngay từ đầu nhóm em đặt hai ràng buộc: hệ thống chỉ phục vụ học viên của trung tâm, và quyền dùng nội dung premium cấp bằng **thẻ kích hoạt qua đội sales**, không làm thanh toán hay kế toán. Lý do em sẽ trình bày ở slide 14.

**Chuyển:** Thị trường đã có những gì?

---

## Slide 5: Giải pháp hiện có

**Ý chính:** ba cách hiện có, mỗi cách thiếu một mảnh; phân tích này nhóm làm cùng trung tâm.

**Nói:**
Nhóm em đã cùng phía trung tâm phân tích các giải pháp tương tự. Em tóm lại ba cách.
**STUDY4** có nhiều đề nhưng chỉ hiện điểm và số câu đúng, không giải thích vì sao sai hay học gì tiếp. **ELSA Speak** phản hồi nói rất tốt, nhưng chỉ tập trung kỹ năng nói. **Tự luyện tại IELTS Space** khớp nội dung lớp, nhưng không chấm và phản hồi ngay, không cho học viên biết mình yếu kiến thức nào.
Từ bảng so sánh này, nhóm em chọn ra những tính năng cần có cho hệ thống của mình.

**Show:** nếu có thời gian, mở nhanh file phân tích đối thủ đã làm cùng trung tâm (bản đã đổi tên) và nói "đây là bảng chi tiết nhóm em làm cùng trung tâm", rồi quay lại slide. Không đọc file.

**Chuyển:** Từ đó nhóm em rút ra bảy khoảng trống.

---

## Slide 6: Khoảng trống

**Ý chính:** bảy GAP là kim chỉ nam; mỗi tính năng sau này trả lời một GAP.

**Nói:**
Em nhấn bốn khoảng trống quan trọng nhất. **GAP-01**: không biết vì sao mình sai. **GAP-02**: lao vào làm đề khi chưa học kiến thức của dạng câu hỏi đó. **GAP-04**: không biết điểm kiến thức nào còn yếu. **GAP-05**: không có nội dung luyện ngoài giờ lớp và lúc chờ lớp. Ba khoảng trống còn lại là chỉ luyện được kỹ năng nói, thiếu động lực, và học từ vựng thiếu ngữ cảnh.
Mỗi tính năng ở phần sau đều trả lời ít nhất một khoảng trống ở đây.

**Chuyển:** Đây là hệ thống nhóm em đề xuất, nhìn từ bên ngoài.

---

## Slide 7: Sơ đồ bối cảnh hệ thống

**Ý chính:** ranh giới hệ thống: 5 người dùng và 6 hệ thống bên ngoài; mỗi bên gửi gì vào và nhận gì về.

**Cách đọc hình (nói trước 1 câu):** ở giữa là IELTSPath, gồm API Gateway và 9 service nghiệp vụ. Hộp xanh là **người dùng**, hộp xám là **hệ thống bên ngoài**. **Mũi tên liền màu xanh** là dữ liệu đi **vào** IELTSPath (request), **mũi tên nét đứt màu vàng** là IELTSPath **trả ra hoặc gửi đi** (response).

**Bảng tra nhanh (đọc lại trước khi lên, không đọc nguyên bảng trước hội đồng):**

| Tác nhân | Gửi vào IELTSPath (request) | IELTSPath trả về (response) |
|---|---|---|
| **Learner** (học viên, khách hoặc đã đăng nhập, dùng trình duyệt) | Đăng ký, đăng nhập, câu trả lời, bài luận, bài làm thi | Bài học, Practice và bài ôn, kết quả, phản hồi, mã đề thi |
| **Content Author** (tác giả nội dung) | Topic, điểm kiến thức, câu hỏi, gói đề, từ vựng, video | Danh sách và chi tiết nội dung |
| **Examiner** (giám khảo) | Điểm chấm tay, kết quả đã chốt | Bài làm và câu trả lời cần chấm |
| **Administrator** (quản trị) | Người dùng, vai trò, gói, thẻ kích hoạt, điều chỉnh điểm, kiểm duyệt | Hồ sơ người dùng, gói, thẻ và điểm |
| **Sale** (đội sales) | Yêu cầu tạo và thu hồi thẻ kích hoạt | Mã thẻ và trạng thái thẻ |
| **LLM Provider** | IELTSPath gửi: bài luận + đề bài | Điểm theo từng tiêu chí + nhận xét |
| **Speech Assessment Provider** | IELTSPath gửi: bản ghi âm Speaking, Shadowing + văn bản mẫu | Transcript, điểm phát âm và độ trôi chảy |
| **OAuth Identity Provider** | IELTSPath gửi: chuyển hướng đăng nhập, yêu cầu xác thực | Danh tính đã xác minh (ID token) |
| **Email Service** | IELTSPath gửi: link đặt lại mật khẩu, thông báo | Trạng thái gửi |
| **Firebase Cloud Messaging** | IELTSPath gửi: nhắc lịch học, báo đã chấm xong | Kết quả gửi, message id |
| **Media Storage** | IELTSPath gửi: tải lên bản ghi âm, hình ảnh, file nghe | mediaUrl hoặc objectKey |

Với 5 người dùng, người dùng là bên **gửi yêu cầu** và IELTSPath **trả kết quả**. Với 6 hệ thống bên ngoài thì ngược lại: IELTSPath là bên **gọi đi**, hệ thống ngoài **trả kết quả**.

**Nói:**
Đây là sơ đồ bối cảnh hệ thống. Ở giữa là IELTSPath, gồm API Gateway và 9 service. Mũi tên liền màu xanh là dữ liệu đi vào hệ thống, mũi tên nét đứt màu vàng là hệ thống trả ra.
Bên trái và phía trên là **năm người dùng**.
- **Học viên** gửi vào thông tin đăng ký, đăng nhập, câu trả lời, bài luận và bài thi; hệ thống trả về bài học, Practice, bài ôn, kết quả, phản hồi và mã đề thi.
- **Tác giả nội dung** đưa vào topic, điểm kiến thức, câu hỏi, gói đề, từ vựng và video; hệ thống trả lại danh sách và chi tiết nội dung để quản lý. Đây chính là kho đề gắn điểm kiến thức mà luồng ôn tập dùng.
- **Giám khảo** nhận từ hệ thống các bài làm cần chấm, và gửi lại điểm chấm tay cùng kết quả đã chốt.
- **Quản trị viên** quản lý người dùng, vai trò, gói, thẻ kích hoạt, điểm và kiểm duyệt cộng đồng; hệ thống trả về các hồ sơ tương ứng.
- **Đội sales** chỉ gửi yêu cầu tạo hoặc thu hồi thẻ kích hoạt, và nhận về mã thẻ cùng trạng thái thẻ. Không có luồng tiền nào đi qua đây, đúng với quyết định cắt nghiệp vụ tài chính.

Bên phải và phía dưới là **sáu hệ thống bên ngoài**. Ở đây IELTSPath là bên gọi đi.
- **LLM Provider**: hệ thống gửi bài luận kèm đề bài, nhận về điểm theo từng tiêu chí IELTS và nhận xét. Đây là phản hồi Writing bằng AI.
- **Speech Assessment Provider**: hệ thống gửi bản ghi âm Speaking, Shadowing kèm văn bản mẫu, nhận về transcript, điểm phát âm và độ trôi chảy.
- **OAuth Identity Provider**: hệ thống chuyển hướng người dùng đi đăng nhập, nhận về danh tính đã xác minh dưới dạng ID token.
- **Email Service**: hệ thống gửi link đặt lại mật khẩu và thông báo, nhận về trạng thái gửi.
- **Firebase Cloud Messaging**: hệ thống gửi nhắc lịch học và báo đã chấm xong, nhận về kết quả gửi.
- **Media Storage**: hệ thống tải lên bản ghi âm, hình ảnh, file nghe, nhận về đường dẫn để lưu lại.

Điểm em muốn nhấn: nhóm em **không tự làm AI hay hạ tầng gửi thông báo**. Nhóm xác định rõ đầu vào, đầu ra với từng dịch vụ bên ngoài và tích hợp vào đúng chỗ cần.

**Nếu bị hỏi:**
- *"Learner ghi guest, vậy khách chưa đăng ký dùng được à?"* Theo slide 18 (LI-02), hệ thống không làm học thử cho khách chưa đăng ký. Cần thống nhất trong nhóm "guest" ở đây nghĩa là gì trước khi lên, ví dụ khách chỉ mới đăng ký tài khoản và chưa kích hoạt thẻ premium.
- *"Dịch vụ ngoài lỗi thì sao?"* Chỉ trả lời điều nhóm đã thiết kế. Ví dụ kết quả thi đi qua hàng đợi tin nhắn nên được xử lý lại. Với LLM hay giọng nói lỗi, nếu chưa có thiết kế xử lý thì trả lời "đây là ngoại lệ nhóm đang bổ sung".

**Chuyển:** So sánh cách học viên đang làm với cách làm mới.

---

## Slide 8: Hiện trạng (AS-IS)

**Ý chính:** chữ đỏ là điểm đau; hai điểm đau lớn là không phản hồi và hết lớp thì dừng.

**Nói:**
Hiện nay giáo viên dạy theo band và phát tài liệu. Học viên tự làm, không được chấm ngay. Học viên làm thêm đề web miễn phí, chỉ thấy điểm, rồi tự đoán điểm yếu. Hết lớp thì không có nội dung để luyện, mất nhịp. Các ô chữ đỏ là điểm đau.

**Chuyển:** Với IELTSPath thì khác thế nào?

---

## Slide 9: Giải pháp (TO-BE)

**Ý chính:** ba vai trò; nhánh đỏ là nhánh ôn điểm yếu.

**Nói:**
Đội sales cấp thẻ, học viên nhập thẻ vào học, hệ thống ghi log và mở premium. Học viên học từng lesson đến khi đạt, rồi làm Practice. Practice chấm và hiện lời giải ngay. Nếu có điểm kiến thức dưới 70%, học viên rẽ vào **nhánh đỏ**: làm bài ôn đúng điểm yếu đó. Cuối cùng là thi cuối topic, nhận xét theo tiêu chí IELTS.

**Chuyển:** Em đi sâu vào hai luồng cốt lõi, cũng là nơi nhóm em xử lý nhiều ngoại lệ nhất.

---

## Slide 10: Học một bài (1/2)

**Ý chính:** làm đạt mới được đi tiếp; sai thì có gợi ý nhưng chưa lộ lời giải.

**Nói:**
Học viên mở bài tiếp theo trong topic. Bài học gồm lý thuyết, bài đọc hoặc nghe và bài tập. Lý thuyết và bài tập gói gọn trong một lesson. Học viên nộp bài, hệ thống chấm và **ghi kết quả lần nộp đầu**, vì lần đầu mới phản ánh đúng mức hiểu bài.
Nếu đúng dưới 70%, hệ thống đánh dấu câu sai và hiện gợi ý nhưng **chưa hiện lời giải**, để học viên phải tự nghĩ lại. Đạt rồi mới xem đáp án. Khi mọi bài tập đều đạt, hệ thống mở bài tiếp, mở Practice và cập nhật mức nắm vững.

**Ngoại lệ (nói rõ):**
- Nếu còn bài ôn đang chờ thì phải làm bài ôn trước, không học vượt được.
- Làm lại bao nhiêu lần cũng không ghi đè kết quả lần đầu, nên học viên không "cày điểm" được.
- Lời giải bị khóa đến khi đạt, nên không chép đáp án để qua bài.

**Chuyển:** Hoàn thành bài thì sang Practice.

---

## Slide 11: Practice và bài ôn (2/2)

**Ý chính:** đây là trái tim của học tập thích ứng: sai ở điểm kiến thức nào thì ôn đúng điểm đó.

**Nói:**
Practice nộp một lần, chấm và hiện lời giải ngay. Mỗi câu hỏi được gắn với một **điểm kiến thức**. Nếu điểm kiến thức nào dưới 70%, hệ thống tạo bài ôn riêng cho điểm đó, và chặn các bài cùng skill cho đến khi ôn xong.
Bài ôn lấy câu hỏi từ kho đề, theo đúng **band của khóa học** và đúng **điểm kiến thức bị hổng**, ưu tiên bộ câu học viên chưa gặp. Vì khóa học đã chia theo band và câu hỏi đã gắn điểm kiến thức ngay trong dữ liệu, hệ thống lấy được ngay câu tương tự mà không phải tìm kiếm lại.
Mức nắm vững của mỗi điểm kiến thức nhóm em không tự nghĩ ra công thức, mà **port từ DeepTutor**, một nền tảng học tập mã nguồn mở. Nhóm em đọc và hiểu cách nó tính, rồi đưa vào hệ thống với đầu vào là kết quả đúng sai của học viên.

**Ngoại lệ (nói rõ):**
- Trượt bài ôn thì quay về ôn lại lý thuyết đúng điểm kiến thức đó, làm quick-check, rồi sang bộ câu mới.
- **Trượt hai bộ hoặc hết đề** thì bài ôn được bỏ qua, để học viên không bị kẹt mãi.
- Một điểm kiến thức đã có bài ôn đang chờ thì không tạo thêm bài ôn trùng.

**Nếu hỏi sâu về cách tính mức nắm vững:** lấy tối đa 5 lần làm gần nhất, lần càng mới trọng số càng lớn (0.5 đến 1.0). Mức nắm vững bằng tổng trọng số các lần đúng chia tổng trọng số. Mới 1 lần thì tối đa 50%, mới 2 lần tối đa 80%, để một lần làm đúng chưa được tính là đã vững.

**Chuyển:** Gộp lại, đây là giải pháp nhóm em đề xuất.

---

## Slide 12: Giải pháp đề xuất

**Ý chính:** năm bước; khóa học theo band, bài học nằm trong khóa.

**Nói:**
Một, **kiểm tra đầu vào** ước lượng band hiện tại và gợi ý khóa phù hợp. Hai, **học kiến thức trước**: mỗi khóa thuộc một band, gồm các topic và bài học. Bài học không gắn band riêng mà ăn theo khóa, vì cùng chủ đề "cây cối" thì bài của band 5 và band 8 phải khác nhau. Ba, **luyện tập**, câu sai được ghi theo điểm kiến thức bị hổng. Bốn, **ôn tập trúng đích**. Năm, **phản hồi và thi thử**.
Học viên đặt mục tiêu 8.0 vẫn đi qua các band thấp hơn trước. Bài kiểm tra đầu vào chỉ cho biết học viên đang ở đâu, còn chọn học gì là quyền của học viên.

**Chuyển:** Kênh này phục vụ ai?

---

## Slide 13: Một kênh cho hai lúc

**Ý chính:** hai nhóm học viên, đội sales, và cam kết không theo dõi học viên.

**Nói:**
**Học viên đang học** ôn lại kiến thức trên lớp và nhận bài ôn đúng điểm yếu. **Học viên chờ lớp** giữ nhịp qua game, cộng đồng và từ vựng qua video. Đội sales cấp thẻ kích hoạt.
Nhóm em cam kết **không theo dõi học viên**: không có dashboard cho giáo viên hay trung tâm. Dữ liệu học chỉ dùng để chọn bài ôn và để học viên tự xem.

**Chuyển:** Còn phần premium hoạt động thế nào?

---

## Slide 14: Thẻ kích hoạt premium

**Ý chính:** chủ động cắt nghiệp vụ tài chính; hệ thống chỉ cấp thẻ và ghi log.

**Nói:**
Đây là một quyết định nhóm em đưa ra có chủ đích. Thay vì làm cổng thanh toán, hệ thống chỉ **phát hành thẻ**. Ví dụ admin tạo một lô 500 thẻ theo gói premium, giao cho các sales. Bán thẻ thế nào, thu tiền thế nào, tháng này bán được bao nhiêu là việc của trung tâm. Hệ thống không làm hóa đơn, kế toán hay thống kê doanh thu.
Hệ thống chỉ **ghi log**: thẻ nào, tài khoản nào, kích hoạt lúc nào. Khi có thắc mắc, sales chỉ cần tra: thẻ này được dùng lúc nào, bởi ai, thế là xong. Cách này đóng gói trọn luồng premium và giữ nhóm tập trung vào bài toán chính là cá nhân hóa việc học.

**Ngoại lệ (nói rõ):**
- Mỗi thẻ chỉ dùng một lần; nhập lại thẻ đã dùng hoặc mã không hợp lệ thì bị từ chối.
- Mọi lần kích hoạt đều có log để truy vết khi tranh chấp.

**Chuyển:** Đến danh sách tính năng.

---

## Slide 15: Tính năng chính (1/2)

**Ý chính:** nhóm tính năng học và đánh giá; AI dùng đúng chỗ; FE-12 bổ sung con người.

**Nói:**
**FE-01** kiểm tra đầu vào. **FE-02** khóa học theo band, bài học đa kỹ năng. **FE-03** luyện tập thích ứng và ôn tập, chính là luồng em vừa trình bày. **FE-05** bài thi topic, khóa học và tiến độ cá nhân. **FE-11** thi thử đủ bốn kỹ năng.
Về AI, nhóm em dùng đúng chỗ máy làm tốt hơn người về tốc độ. **FE-04** dùng mô hình ngôn ngữ chấm Writing theo bốn tiêu chí IELTS và chỉ ra điểm cần cải thiện. **FE-10** dùng dịch vụ chấm giọng nói để trả transcript, điểm phát âm và độ trôi chảy. Đầu vào là bài viết, bản ghi âm và tiêu chí IELTS; đầu ra là phản hồi để học viên sửa.
Còn **FE-12, phản hồi Writing bằng giáo viên**, là phần nhóm em bổ sung: AI cho phản hồi nhanh mọi lúc, giáo viên cho nhận xét sâu và đáng tin hơn khi học viên cần.

**Chuyển:** Nhóm tính năng thứ hai để học viên không bỏ cuộc.

---

## Slide 16: Tính năng chính (2/2) và điểm thú vị

**Ý chính:** giữ nhịp luyện; bốn điểm thú vị đều phục vụ học tập thích ứng.

**Nói:**
**FE-06** game từ vựng, ngữ pháp thi đấu thời gian thực. **FE-07** từ vựng qua video và flashcard. **FE-08** cộng đồng người học có kiểm duyệt. **FE-09** thẻ kích hoạt.
Bốn điểm em muốn hội đồng chú ý: **gợi ý cho câu sai** mà không lộ lời giải; **thang ôn tập** từ set có gợi ý đến ôn lý thuyết rồi set mới; **lưu câu hỏi khó thành flashcard** gắn với điểm kiến thức; và **chuỗi ngày học liên tục** để giữ nhịp lúc chờ lớp.

**Chuyển:** Để chạy được những thứ này, nhóm em chọn kiến trúc microservice. Em xin giải thích vì sao bài toán này cần nó.

---

## Slide 17: Kiến trúc

**Ý chính:** microservice vì bài toán này cần, không phải vì công nghệ mới; và sẽ chứng minh bằng số liệu.

**Nói:**
Nhóm em không trình bày lý thuyết microservice, mà nói vì sao **bài toán này** cần nó.
Một, **kiểu tải rất khác nhau**. Game thi đấu realtime có nhiều người chơi gửi dữ liệu liên tục, chấm Writing bằng AI phản hồi chậm, còn luồng học cần nhanh và ổn định. Nếu gộp chung, một trận game đông người hay một hàng chờ chấm AI có thể làm chậm việc học. Tách riêng thì mỗi phần chịu tải riêng.
Hai, **phần cá nhân hóa thay đổi nhiều nhất**. Cách tính điểm yếu và chọn bài ôn cần thử nghiệm liên tục, tách riêng để thay đổi mà không đụng tới thi cử, nội dung hay tài khoản.
Ba, **mỗi phần giữ dữ liệu của mình**. Nội dung, kết quả thi, bằng chứng học tập, thẻ kích hoạt do các bên khác nhau thay đổi và có kiểu dữ liệu khác nhau. Mỗi service có cơ sở dữ liệu riêng nên ranh giới rõ, và phần cá nhân hóa có đủ dữ liệu riêng để phân tích.
Bốn, **cô lập lỗi**. Game hay cộng đồng lỗi thì học viên vẫn học được. Kết quả thi được gửi qua hàng đợi tin nhắn nên được lưu và xử lý lại, không mất.
Đi cùng microservice là trách nhiệm **chứng minh nó chịu được tải**. Nhóm em sẽ có performance test: giả lập nhiều người dùng đồng thời, đo thời gian phản hồi, RAM và CPU của từng service.

> Quan trọng: chỉ nói "sẽ có" nếu chưa chạy. Repo hiện chưa có kết quả performance test. Nếu nhóm đã đo trước buổi trình bày, thay bằng số liệu thật, ví dụ "với N người dùng đồng thời, thời gian phản hồi là X ms". Đừng đưa con số chưa đo.

**Chuyển:** Để giữ phạm vi khả thi, đây là những gì nhóm em không làm.

---

## Slide 18: Giới hạn phạm vi

**Ý chính:** nói "không" có lý do.

**Nói:**
Em nhấn bốn mục. **LI-01** không theo dõi học viên. **LI-03** không có thanh toán, kế toán, như em đã giải thích. **LI-06** không thay kỳ thi IELTS chính thức, kết quả thi thử chỉ là ước lượng. **LI-09** chưa làm app di động, bản đầu tập trung web để kiểm chứng luồng học trước.

**Chuyển:** Cuối cùng là giá trị mang lại.

---

## Slide 19: Giá trị kỳ vọng

**Ý chính:** giá trị cho học viên và cho trung tâm.

**Nói:**
Với **học viên**: bài ôn khớp band và nội dung trên lớp, biết điểm yếu và việc cần ôn tiếp, không ngừng luyện lúc chờ lớp. Phản hồi Writing, Speaking từ AI có ngay, nhận xét của giáo viên có khi cần.
Với **IELTS Space**: mở rộng việc học ra ngoài giờ lớp bằng nội dung của chính trung tâm, học viên vào lớp mới với kiến thức đã ôn trước, bài tự ôn chấm tự động không thêm việc cho giáo viên, sales tra log thẻ ngay.

---

## Slide 20: Kết thúc

**Nói:**
Tóm lại, IELTSPath giúp học viên IELTS Space ôn **đúng chỗ yếu** và **không đứt nhịp** giữa các lớp. Nhóm em giải bài toán học tập thích ứng với luồng hoàn chỉnh có xử lý ngoại lệ, kiến trúc được chọn vì bài toán cần, và AI được dùng đúng chỗ. Nhóm em xin cảm ơn hội đồng và sẵn sàng trả lời câu hỏi.

**Show (nếu hội đồng muốn xem):** mở bản chạy thử luồng người học: nộp bài sai, thấy gợi ý, làm Practice dưới 70%, thấy bài ôn được tạo. Chạy thử trước buổi trình bày; nếu không chắc chạy ổn thì không mở.

---

## Mẹo trình bày

- Mở bằng Linh và Minh, không mở bằng định nghĩa.
- Ở slide 10, 11, 14, nói phần **Ngoại lệ** thành tiếng. Đây là chỗ phân biệt "chạy được" với "hoàn chỉnh".
- Mỗi khi nhắc công nghệ, nói ngay một câu "nó giải quyết gì cho học viên hoặc trung tâm".
- Không nói điều chưa làm như đã làm. Bị hỏi điều chưa chắc thì trả lời "nhóm chưa kiểm chứng điều này, đó là hướng tiếp theo".
- Slide 8 đến 11 là sơ đồ, dừng lâu hơn để hội đồng đọc.
