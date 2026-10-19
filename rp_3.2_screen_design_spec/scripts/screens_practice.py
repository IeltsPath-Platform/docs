"""Wireframes: practice catalog and skill workspaces (P-41…P-44a). Content is mock data in the FE."""
import screens_exam_account
from wf import PRIMARY, PRIMARY_SOFT, INK, MUTED, LINE, SOFT, CANVAS, DARK, MEDIA
from chrome import (navbar, mobile_nav, footer, consult_fab, screen, mobile_screen, phone, eyebrow,
                    DESKTOP_W, MOBILE_W)


def catalog_base(p, h, dim=False):
    y = navbar(p, role="learner", active="Luyện tập 4 kỹ năng", child="Reading")
    # sidebar
    p.zone(14, y + 28, "A")
    p.card(40, y + 24, 260, 640, r=16)
    p.text(64, y + 44, 220, 50, "<b>LUYỆN ĐỀ</b><br><font style='font-size:12px' color='#6B7280'>The IELTS Space</font>", size=18, valign="top")
    p.text(64, y + 110, 200, 20, "KỸ NĂNG", size=12, color=PRIMARY, bold=True)
    p.rect(60, y + 136, 220, 42, fill=PRIMARY, stroke=PRIMARY, r=10, value="📖 Reading ˄", color="#FFFFFF", size=14, bold=True, align="left")
    for i, t in enumerate(("• Bài lẻ", "   ◉ Passage 1", "   ○ Passage 2", "   ○ Passage 3", "○ Full đề")):
        p.text(84, y + 186 + i * 28, 190, 24, t, size=13, color=INK if i != 1 else PRIMARY)
    for i, t in enumerate(("🎧 Listening ˅", "✎ Writing ˅", "🎤 Speaking ˅")):
        p.text(70, y + 336 + i * 44, 200, 30, t, size=14)
    p.text(64, y + 480, 200, 20, "NGUỒN TÀI LIỆU", size=12, color=PRIMARY, bold=True)
    for i, t in enumerate(("☑ The IELTS Space PRO  [PRO]", "☐ Actual Tests", "☐ Các nguồn khác")):
        p.text(70, y + 510 + i * 32, 220, 26, t, size=13)
    # banner
    mx, mw = 330, 1070
    p.zone(mx - 30, y + 24, "B")
    p.rect(mx, y + 24, mw, 200, fill=PRIMARY, stroke=PRIMARY, r=24)
    p.img(mx + 40, y + 44, 150, 160, "Owl mascot SVG")
    p.text(mx + 300, y + 60, 600, 40, "<b>Chưa biết mình đang ở band nào?</b>", size=26, color="#FFFFFF")
    p.text(mx + 300, y + 104, 600, 24, "Test đầu vào và khám phá trình độ IELTS hiện tại của bạn.", size=15, color="#FFFFFF")
    p.rect(mx + 300, y + 144, 170, 46, fill="#FFFFFF", stroke="#FFFFFF", r=23, value="▶ TEST NGAY ✦", color=PRIMARY, bold=True, size=14)
    # controls
    p.zone(mx - 30, y + 250, "C")
    p.rect(mx, y + 250, 250, 46, fill="#FFFFFF", stroke=LINE, r=23)
    p.rect(mx + 4, y + 254, 124, 38, fill=PRIMARY, stroke=PRIMARY, r=19, value="Bài chưa làm", color="#FFFFFF", size=13, bold=True)
    p.text(mx + 132, y + 254, 114, 38, "Bài đã làm", size=13, align="center")
    p.rect(mx + mw - 320, y + 250, 320, 46, fill="#FFFFFF", stroke=LINE, r=23, value="🔍 Tìm tên bài tập", color=MUTED, size=13, align="left")
    # cards
    p.zone(mx - 30, y + 320, "D")
    cw = (mw - 40) // 3
    cards = [("MIỄN PHÍ", "Passage 1", "Vitamins - To supplement or not?", ["Gap Filling", "Match Information", "Yes/No/Not Given"]),
             ("MIỄN PHÍ", "Passage 1", "The Evolutionary Mystery: Crocodile…", ["Gap Filling", "Matching Features"]),
             ("PRO", "Passage 3", "How Does Watching Sports Influenc…", ["Summary Completion", "Multiple Choice"])]
    for i, (tag, badge, title, bullets) in enumerate(cards):
        cx = mx + i * (cw + 20)
        p.card(cx, y + 320, cw, 350, r=16)
        p.img(cx + 1, y + 321, cw - 2, 170, "Test image")
        p.rect(cx + cw - 90, y + 330, 80, 24, fill=DARK if tag == "PRO" else "#FFFFFF", stroke=DARK, r=4, value=tag, size=11,
               color="#FFFFFF" if tag == "PRO" else INK, bold=True)
        p.rect(cx + 1, y + 490, cw - 2, 179, fill=PRIMARY, stroke=PRIMARY, r=0)
        p.chip(cx + 20, y + 504, badge, "outline")
        p.text(cx + 20, y + 538, cw - 40, 26, f"<b>{title}</b>", size=15, color="#FFFFFF")
        for j, b in enumerate(bullets):
            p.text(cx + 20, y + 572 + j * 24, cw - 40, 22, "• " + b, size=13, color="#FFFFFF")
    consult_fab(p, 1240, h - 140)
    footer(p, h - 64)
    return y


def catalog_page(p, h, next_screen):
    """Desktop practice catalog (shared by P-41 and P-43 / Catalog); cards open `next_screen`."""
    catalog_base(p, h)
    p.text(330, 1000 - 40, 1070, 30, f"All cards are MOCK_PRACTICE_CARDS (no API yet). Click / Enter / Space on a card → {next_screen}. Filters: skill (sidebar + ?skill=), tab, search.", size=12, italic=True)


def p43_catalog(f):
    h = 1080
    catalog_page(screen(f, "P-43", "Catalog", "Practice", h=h), h, "Mode Select")


def p41(f):
    h = 1080
    p = screen(f, "P-41", "Populated", "Practice Catalog", h=h)
    catalog_page(p, h, "P-41a")
    p = mobile_screen(f, "P-41", "Practice Catalog", 2, h=820)
    ox = phone(p, 0, "Populated · 375", h=820)
    y = mobile_nav(p, ox=ox)
    p.rect(ox, y, MOBILE_W, 40, fill=PRIMARY_SOFT, stroke=LINE, r=0, value="Listening · <u><b>Reading</b></u> · Writing · Speaking", size=12)
    y += 52
    p.card(ox + 12, y, 351, 90, r=12)
    p.text(ox + 24, y + 10, 320, 70, "<b>LUYỆN ĐỀ</b> — sidebar xếp lên đầu (kỹ năng + nguồn)", size=13, valign="top")
    p.rect(ox + 12, y + 104, 351, 150, fill=PRIMARY, stroke=PRIMARY, r=16, value="<b>Chưa biết mình đang ở band nào?</b><br>▶ TEST NGAY ✦", color="#FFFFFF", size=14)
    p.rect(ox + 12, y + 268, 351, 40, fill="#FFFFFF", stroke=LINE, r=20, value="Bài chưa làm | Bài đã làm", size=12)
    p.rect(ox + 12, y + 316, 351, 40, fill="#FFFFFF", stroke=LINE, r=20, value="🔍 Tìm tên bài tập", color=MUTED, size=12, align="left")
    p.card(ox + 12, y + 370, 351, 300, r=14)
    p.img(ox + 13, y + 371, 349, 140, "Test image")
    p.rect(ox + 13, y + 510, 349, 158, fill=PRIMARY, stroke=PRIMARY, r=0, value="<b>Vitamins - To supplement or not?</b><br>• Gap Filling • …", color="#FFFFFF", size=13)
    ox = phone(p, 1, "Mode select (P-41a) · 375", h=820)
    p.overlay(MOBILE_W, 820, ox=ox)
    p.card(ox + 12, 120, 351, 560, r=16)
    p.text(ox + 28, 136, 320, 26, "<b>Vitamins - To supplement…</b>", size=15, color=PRIMARY)
    p.rect(ox + 12, 180, 351, 500, fill=PRIMARY, stroke=PRIMARY, r=0)
    p.text(ox + 28, 190, 320, 24, "Lựa chọn chế độ làm bài", size=14, color="#FFFFFF", bold=True)
    for i, t in enumerate(("Thi thử", "Luyện tập")):
        p.rect(ox + 28, 226 + i * 180, 319, 164, fill="#FFFFFF", stroke="#FFFFFF" if i else PRIMARY_SOFT, r=12, sw=3 if i == 0 else 1,
               value=f"<b>{t}</b><br>(mô tả)", size=13)
    p.rect(ox + 28, 600, 319, 52, fill="#FFFFFF", stroke="#FFFFFF", r=26, value="BẮT ĐẦU LÀM BÀI", color=PRIMARY, bold=True, size=14)


def mode_select_dialog(p, h):
    """Exam / practice mode dialog over the dimmed catalog (shared by P-41a and P-43 / Mode Select)."""
    catalog_base(p, h)
    p.overlay(DESKTOP_W, h)
    x, y, w = 330, 170, 780
    p.card(x, y, w, 640, r=20)
    p.zone(x - 13, y + 20, "A")
    p.text(x + 32, y + 22, w - 100, 34, "<b>Vitamins - To supplement or not?</b>", size=22, color=PRIMARY)
    p.text(x + w - 56, y + 24, 30, 30, "✕", size=18, color=MUTED, align="center")
    p.rect(x, y + 80, w, 560, fill=PRIMARY, stroke=PRIMARY, r=0)
    p.text(x + 32, y + 100, 500, 26, "<b>Lựa chọn chế độ làm bài</b>", size=17, color="#FFFFFF")
    p.zone(x - 13, y + 150, "B")
    for i, (t, d) in enumerate((("Thi thử", "Tập trung như phòng thi thật. Không có Highlight, Note, tra từ hay Flashcard."),
                                 ("Luyện tập", "Học chủ động với các hỗ trợ phù hợp cho từng kỹ năng và xem lại tiến độ của bạn."))):
        cx = x + 32 + i * 366
        p.rect(cx, y + 146, 350, 330, fill="#FFFFFF", stroke=PRIMARY_SOFT if i == 0 else "#FFFFFF", r=16, sw=4 if i == 0 else 1)
        if i == 0:
            p.chip(cx + 16, y + 160, "Thi thử", "solid")
        p.img(cx + 24, y + 196, 302, 140, "Preview " + ("exam UI" if i == 0 else "practice workspace"))
        p.text(cx + 24, y + 350, 302, 28, f"<b>{t}</b>", size=18, align="center")
        p.text(cx + 24, y + 384, 302, 70, d, size=13, color=MUTED, align="center", valign="top")
    p.text(x + 32, y + 482, 600, 20, "aria-pressed: the selected card has a thick border (default Thi thử)", size=12, color="#FFFFFF", italic=True)
    p.zone(x - 13, y + 540, "C")
    p.rect(x + w / 2 - 160, y + 540, 320, 56, fill="#FFFFFF", stroke="#FFFFFF", r=28, value="BẮT ĐẦU LÀM BÀI", color=PRIMARY, bold=True, size=17)


def p41a(f):
    h = 1080
    mode_select_dialog(screen(f, "P-41a", "Populated", "Practice Mode Select", h=h), h)


def p43_mode_select(f):
    h = 1080
    mode_select_dialog(screen(f, "P-43", "Mode Select", "Practice", h=h), h)


def workspace_bar(p, y, mode="Luyện tập", progress="1/5 câu · 20%", right=True):
    p.zone(14, y + 18, "A")
    p.rect(0, y, DESKTOP_W, 72, fill="#FFFFFF", stroke=LINE, r=0)
    p.rect(40, y + 16, 110, 40, fill="#FFFFFF", stroke=DARK, r=20, value="← Thoát", size=14, bold=True)
    p.chip(420, y + 24, mode, "active")
    p.rect(520, y + 18, 140, 36, fill=PRIMARY_SOFT, stroke=PRIMARY_SOFT, r=18, value="🕒 00:12:40", size=14, color=PRIMARY, bold=True)
    p.text(690, y + 12, 330, 20, f"Tiến độ   {progress}", size=12, color=MUTED)
    p.progress(690, y + 40, 330, 20)
    if right:
        p.rect(1180, y + 16, 150, 40, fill="#FFFFFF", stroke=DARK, r=10, value="🗒 Ghi chú (0)", size=13)
        p.rect(1344, y + 16, 44, 40, fill="#FFFFFF", stroke=DARK, r=10, value="⚙", size=16)
    return y + 72


def question_map(p, x, y, n=5, active=1):
    p.card(x, y, 220, 290, r=14)
    p.text(x + 16, y + 12, 140, 18, "QUESTION MAP", size=11, color=PRIMARY, bold=True)
    p.text(x + 16, y + 32, 180, 24, "<b>Bản đồ câu hỏi</b>", size=15)
    for i in range(n):
        p.rect(x + 16 + (i % 3) * 64, y + 100 + (i // 3) * 54, 56, 44, fill=PRIMARY_SOFT if i + 1 == active else "#FFFFFF",
               stroke=PRIMARY if i + 1 == active else LINE, r=8, value=str(i + 1), size=14, bold=True)
    p.btn(x + 16, y + 226, 88, 40, "← Back", "secondary", size=13)
    p.btn(x + 116, y + 226, 88, 40, "Next →", size=13)


def reading(p, y, mode):
    y = workspace_bar(p, y, mode, right=mode == "Luyện tập")
    p.zone(14, y + 24, "B")
    question_map(p, 30, y + 24)
    cx = 270
    if mode == "Luyện tập":
        p.zone(cx - 26, y + 24, "C")
        p.card(cx, y + 24, 560, 140, r=14)
        p.text(cx + 20, y + 36, 200, 18, "PRACTICE TOOLS", size=11, color=PRIMARY, bold=True)
        p.text(cx + 20, y + 56, 240, 24, "<b>Công cụ hỗ trợ</b>", size=15)
        p.text(cx + 280, y + 40, 270, 36, "Bôi đen một đoạn trong bài đọc để bắt đầu.", size=11, color=MUTED, align="right")
        for i, t in enumerate(("✎ Highlight", "🗒 Note", "文 Tra từ vựng", "▤ Tạo Flashcard")):
            p.rect(cx + 20 + i * 132, y + 92, 124, 36, fill="#FFFFFF", stroke=LINE, r=8, value=t, size=13)
        p.text(cx + 20, y + 132, 200, 24, "▤ Thẻ đã lưu", size=13)
        py = y + 184
    else:
        py = y + 24
    p.zone(cx - 26, py, "D")
    p.card(cx, py, 560, 700 - (py - y), r=14)
    p.text(cx + 24, py + 16, 400, 18, "READING · BÀI ĐỌC MINH HỌA", size=11, color=PRIMARY, bold=True)
    p.text(cx + 24, py + 38, 400, 34, "<b>Snow Makers</b>", size=26)
    for i, L in enumerate("ABCD"):
        yy = py + 90 + i * 110
        if yy + 90 > y + 690:
            break
        p.text(cx + 24, yy, 24, 24, f"<b>{L}.</b>", size=14)
        if i == 1 and mode == "Luyện tập":
            p.rect(cx + 50, yy + 2, 300, 14, fill="#FEF08A", stroke="#E5C100", r=2)
        p.lines(cx + 50, yy + 4, 480, 4, gap=22)
    ax = 850
    p.zone(ax - 26, y + 24, "E")
    p.card(ax, y + 24, 560, 560, r=14)
    p.text(ax + 24, y + 44, 400, 30, "<b>Question 1 of 5</b>", size=22, color=PRIMARY)
    p.text(ax + 24, y + 80, 520, 20, "Choose the correct heading for each paragraph from the list below.", size=12, color=MUTED)
    p.card(ax + 24, y + 110, 512, 280, r=10)
    p.text(ax + 40, y + 120, 300, 22, "<b>List of Headings</b>", size=13)
    for i, t in enumerate(("i. Considering ecological costs", "ii. Modifications to the design…", "iii. The need for different varieties…", "iv. …", "x. Snow formation in nature")):
        p.rect(ax + 40, y + 150 + i * 46, 480, 36, fill="#FFFFFF", stroke=LINE, r=6, value=t, size=12, align="left")
    p.rect(ax + 24, y + 410, 512, 100, fill="#FFFFFF", stroke=PRIMARY, r=10, sw=2)
    p.text(ax + 40, y + 420, 400, 22, "<b>1. Paragraph C</b>   ⚑", size=14)
    p.rect(ax + 40, y + 452, 480, 40, fill="#FFFFFF", stroke=DARK, r=8, value="Chưa chọn đáp án ˅", color=MUTED, size=13, align="left")
    p.text(ax + 24, y + 520, 300, 20, "Đã chọn 0/5 câu", size=12, color=MUTED)


def p42(f):
    h = 960
    for mode, frame in (("Luyện tập", "Practice Mode"), ("Thi thử", "Exam Mode")):
        p = screen(f, "P-42", frame, "Reading Practice Test", h=h)
        y = navbar(p, role="learner", active="Luyện tập 4 kỹ năng", child="Reading")
        reading(p, y, mode)
        if mode == "Thi thử":
            p.text(270, h - 110, 560, 40, "Thi thử: hides Practice Tools, the Ghi chú button, Floating Notes and dialogs; ⚙ settings remain.", size=12, italic=True)
        footer(p, h - 64)
    p = mobile_screen(f, "P-42", "Reading Practice Test", 1, h=820)
    ox = phone(p, 0, "Practice · 375", h=820)
    y = mobile_nav(p, ox=ox)
    p.rect(ox, y, MOBILE_W, 60, fill="#FFFFFF", stroke=LINE, r=0)
    p.rect(ox + 12, y + 12, 80, 36, fill="#FFFFFF", stroke=DARK, r=18, value="← Thoát", size=12)
    p.text(ox + 100, y + 12, 200, 36, "Luyện tập · 🕒 00:12:40", size=12, bold=True)
    p.rect(ox + 316, y + 12, 44, 36, fill="#FFFFFF", stroke=DARK, r=8, value="⚙", size=14)
    y += 72
    p.card(ox + 12, y, 351, 110, r=12)
    p.text(ox + 24, y + 8, 320, 90, "<b>Bản đồ câu hỏi</b><br>[1][2][3][4][5]  ← Back · Next →", size=13, valign="top")
    p.card(ox + 12, y + 124, 351, 300, r=12)
    p.text(ox + 24, y + 134, 300, 24, "<b>Snow Makers</b>", size=16)
    p.lines(ox + 24, y + 170, 320, 9, gap=26)
    p.card(ox + 12, y + 438, 351, 200, r=12)
    p.text(ox + 24, y + 448, 320, 24, "<b>Question 1 of 5</b>", size=15, color=PRIMARY)
    p.rect(ox + 24, y + 490, 327, 40, fill="#FFFFFF", stroke=DARK, r=8, value="Chưa chọn đáp án ˅", color=MUTED, size=12, align="left")
    p.text(ox, 830, MOBILE_W, 20, "Ba cột xếp dọc (map → passage → câu hỏi)", size=11, color=MUTED, italic=True, align="center")


def dialog_over_reading(f, pid, title, w, h_dialog, body):
    h = 960
    p = screen(f, pid, "Populated", title, h=h)
    y = navbar(p, role="learner", active="Luyện tập 4 kỹ năng", child="Reading")
    reading(p, y, "Luyện tập")
    footer(p, h - 64)
    p.overlay(DESKTOP_W, h)
    x, yy = (DESKTOP_W - w) // 2, 140
    p.card(x, yy, w, h_dialog, r=18)
    p.text(x + w - 50, yy + 22, 26, 26, "✕", size=17, color=MUTED, align="center")
    body(p, x, yy, w)
    return p


def p42a(f):
    def body(p, x, y, w):
        p.zone(x - 13, y + 20, "A")
        p.text(x + 32, y + 22, w - 100, 30, "<b>Tạo Flashcard</b>", size=22)
        p.text(x + 32, y + 56, w - 64, 40, "Lưu từ vựng và ảnh minh họa trên trình duyệt này. Chưa đồng bộ tài khoản.", size=13, color=MUTED, valign="top")
        p.zone(x - 13, y + 110, "B")
        yy = p.field(x + 32, y + 104, w - 64, "Từ / cụm từ *", "snow gun  (prefilled from the selection)")
        p.text(x + 32, yy, 300, 20, "<b>Nghĩa / định nghĩa *</b>", size=14)
        p.rect(x + 32, yy + 24, w - 64, 64, fill="#FFFFFF", stroke=DARK, r=8)
        p.text(x + 32, yy + 100, 300, 20, "<b>Ví dụ / ngữ cảnh</b>", size=14)
        p.rect(x + 32, yy + 124, w - 64, 64, fill="#FFFFFF", stroke=DARK, r=8, value="(sentence from the passage)", color=MUTED, size=12, align="left", valign="top")
        p.btn(x + 32, yy + 224, 180, 40, "🖼 Chọn ảnh", "secondary", size=13)
        p.text(x + 224, yy + 232, 300, 24, "PNG, JPG hoặc WebP · tối đa 1 MB", size=12, color=MUTED)
        p.zone(x - 13, yy + 290, "C")
        p.text(x + 32, yy + 280, w - 64, 20, "Errors: “Nhập từ vựng và nghĩa trước khi lưu.” / “Không lưu được: bộ nhớ đầy…”", size=11, color=MUTED, italic=True)
        p.btn(x + w - 212, yy + 300, 180, 46, "Lưu Flashcard")
    dialog_over_reading(f, "P-42a", "Create Flashcard", 620, 600, body)


def p42b(f):
    def body(p, x, y, w):
        p.zone(x - 13, y + 20, "A")
        p.text(x + 32, y + 22, w - 100, 30, "<b>Tra từ vựng</b>", size=22)
        p.text(x + 32, y + 56, w - 64, 24, "Từ điển nhỏ của bài đọc. Có thể tra cứu thêm trên Wiktionary.", size=13, color=MUTED)
        p.chip(x + 32, y + 92, "Tra Anh-Việt", kind="active", w=150)
        p.zone(x - 13, y + 140, "B")
        p.text(x + 32, y + 140, w - 64, 30, "<b>snow gun</b>", size=20)
        p.text(x + 32, y + 176, w - 64, 30, "máy phun tuyết", size=16)
        p.text(x + 32, y + 216, w - 64, 40, "Not in the glossary: “Chưa có nghĩa trong từ điển của bài. Hãy chọn một từ/cụm từ ngắn hoặc mở trang tra cứu bên dưới.”", size=12, color=MUTED, italic=True, valign="top")
        p.zone(x - 13, y + 276, "C")
        p.link(x + 32, y + 276, 400, "↗ Wiktionary (new tab)")
    dialog_over_reading(f, "P-42b", "Dictionary Lookup", 520, 330, body)


def p42c(f):
    def body(p, x, y, w):
        p.zone(x - 13, y + 20, "A")
        p.text(x + 32, y + 22, w - 100, 30, "<b>Flashcard đã lưu (2)</b>", size=22)
        p.zone(x - 13, y + 80, "B")
        for i, (word, mean) in enumerate((("snow gun", "máy phun tuyết"), ("condenses", "ngưng tụ"))):
            p.card(x + 32, y + 76 + i * 110, w - 64, 96, r=12)
            p.img(x + 44, y + 86 + i * 110, 76, 76, "img")
            p.text(x + 136, y + 88 + i * 110, w - 200, 70, f"<b>{word}</b><br>{mean}<br><i>example …</i>", size=13, valign="top")
        p.text(x + 32, y + 310, w - 64, 44, "Empty: “Chưa có thẻ. Chọn từ trong bài đọc và nhấn “Tạo Flashcard”.” · localStorage read errors use role=alert.", size=12, color=MUTED, italic=True, valign="top")
    dialog_over_reading(f, "P-42c", "Saved Flashcards", 600, 380, body)


def p42d(f):
    h = 960
    p = screen(f, "P-42d", "Populated", "Floating Notes", h=h)
    y = navbar(p, role="learner", active="Luyện tập 4 kỹ năng", child="Reading")
    reading(p, y, "Luyện tập")
    footer(p, h - 64)
    x, yy, w = 900, 300, 420
    p.card(x, yy, w, 470, r=14, stroke=DARK, sw=2)
    p.zone(x - 13, yy + 10, "A")
    p.rect(x, yy, w, 48, fill=SOFT, stroke=DARK, r=14, value="⠿ <b>Ghi chú</b>            —   ✕", size=14, align="left")
    p.text(x + 16, yy + 54, w - 32, 20, "Kéo thanh tiêu đề để di chuyển  ◀ ▶", size=11, color=MUTED)
    p.zone(x - 13, yy + 90, "B")
    p.text(x + 16, yy + 84, w - 32, 20, "Đoạn B · “water vapour condenses…”", size=12, color=PRIMARY)
    p.text(x + 16, yy + 108, 300, 20, "<b>Nội dung ghi chú</b>", size=13)
    p.rect(x + 16, yy + 132, w - 32, 80, fill="#FFFFFF", stroke=DARK, r=8)
    p.btn(x + w - 156, yy + 222, 140, 40, "Lưu ghi chú", size=13)
    p.text(x + 16, yy + 270, w - 32, 20, "Ghi chú giữ trong phiên làm bài; tải lại trang sẽ xóa.", size=11, color=MUTED, italic=True)
    p.zone(x - 13, yy + 300, "C")
    for i in range(2):
        p.card(x + 16, yy + 300 + i * 76, w - 32, 66, r=8)
        p.text(x + 28, yy + 306 + i * 76, w - 100, 54, f"<b>Đoạn {'BC'[i]}</b> · 10:2{i}<br>note text …", size=12, valign="top")
        p.text(x + w - 60, yy + 316 + i * 76, 30, 30, "🗑", size=14)


def p43(f):
    # Exam runner under the site header (no footer): audio bar pinned above the question navigator.
    h = 804
    p = screen(f, "P-43", "Listening", "Practice", h=h)
    y = navbar(p, role="learner", active="Luyện tập 4 kỹ năng", child="Listening")  # site header (y = 116)
    # A · top bar
    p.rect(0, y, DESKTOP_W, 48, fill=SOFT, stroke=LINE, r=0)
    p.zone(14, y + 11, "A")
    p.rect(66, y + 12, 24, 24, fill="#FFFFFF", stroke=DARK, r=24, value="✕", size=12, bold=True)
    p.rect(694, y + 8, 100, 32, fill=PRIMARY, stroke=PRIMARY, r=32, value="⏱ 00:01:32", color="#FFFFFF", size=14, bold=True)
    p.rect(1311, y + 7, 107, 34, fill="#FFFFFF", stroke=LINE, r=34, value="⚙ Cài đặt", size=13, bold=True)
    # B · tools
    p.zone(102, y + 232, "B")
    p.text(124, y + 204, 80, 22, "<b>Công cụ</b>", size=12, align="center")
    p.rect(133, y + 232, 62, 37, fill=PRIMARY, stroke=PRIMARY, r=6, value="⚑", color="#FFFFFF", size=18)
    p.rect(133, y + 286, 62, 74, fill="#FFFFFF", stroke=PRIMARY, r=8, value="✎<br>Highlight<br>Phím (H)", size=11)
    # C · question group
    p.zone(205, y + 178, "C")
    p.rect(1268, y + 43, 4, 102, fill=MEDIA, stroke=MEDIA, r=2)
    p.text(235, y + 176, 500, 32, "<b>Questions 21 - 26</b>", size=22)
    p.text(235, y + 226, 600, 22, "Choose the correct letter, <b>A</b>, <b>B</b> or <b>C</b>.", size=15)
    p.rect(234, y + 279, 32, 32, fill=PRIMARY_SOFT, stroke=PRIMARY_SOFT, r=32, value="21", color=PRIMARY, size=14, bold=True)
    p.text(281, y + 279, 800, 32, "Why did Gwen and Felix decide to do a project on refill points?", size=15)
    options = ("They had seen a campaign about plastic bottles.",
               "They had been unable to find water on a hot day.",
               "They had found that only three buildings on campus had fountains.")
    for i, label in enumerate(options):
        cy = y + 348 + i * 40
        p.text(246, cy - 12, 20, 24, "ABC"[i], size=15, align="center")
        p.rect(274, cy - 11, 22, 22, fill="#FFFFFF", stroke=DARK, r=22)
        p.text(306, cy - 12, 800, 24, label, size=15)
    p.rect(234, y + 482, 32, 32, fill=PRIMARY_SOFT, stroke=PRIMARY_SOFT, r=32, value="22", color=PRIMARY, size=14, bold=True)
    p.text(281, y + 482, 900, 32, "What did the students find out about the university's online map of fountains?", size=15)
    p.text(281, y + 526, 900, 22, "Câu 22–26 cuộn trong vùng nội dung; thanh audio và bảng câu hỏi luôn cố định. ✕ → P-41.", size=11, color=MUTED, italic=True)
    # D · audio player
    p.zone(184, y + 578, "D")
    p.rect(214, y + 569, 1060, 65, fill="#FFFFFF", stroke=LINE, r=0)
    p.progress(214, y + 567, 1060, 22, h=6)
    p.rect(442, y + 563, 14, 14, fill=PRIMARY, stroke="#FFFFFF", r=14, sw=2)
    p.text(230, y + 588, 110, 24, "01:31 / 06:50", size=12, color=MUTED)
    p.text(338, y + 588, 24, 24, "🔊", size=14, align="center")
    p.progress(366, y + 597, 60, 70, h=6)
    p.rect(688, y + 587, 28, 28, fill="#FFFFFF", stroke=DARK, r=28, value="↺5", size=11, bold=True)
    p.rect(726, y + 584, 34, 34, fill=PRIMARY, stroke=PRIMARY, r=34, value="❚❚", color="#FFFFFF", size=11, bold=True)
    p.rect(770, y + 587, 28, 28, fill="#FFFFFF", stroke=DARK, r=28, value="↻5", size=11, bold=True)
    p.rect(1115, y + 580, 142, 41, fill="#FFFFFF", stroke=LINE, r=41, value="⏱ Tốc độ: <b>1x</b>", size=13)
    # E · question navigator + finish
    p.rect(0, y + 634, DESKTOP_W, 54, fill=SOFT, stroke=LINE, r=0)
    p.zone(14, y + 648, "E")
    p.rect(98, y + 643, 314, 43, fill="#FFFFFF", stroke=PRIMARY, r=8)
    for i in range(10):
        p.text(112 + i * 28.5, y + 643, 28, 43, str(21 + i), size=13, color=PRIMARY, bold=True, align="center")
    p.btn(1265, y + 644, 125, 40, "Hoàn thành", "disabled", size=14)


def p43_reading(f):
    # Reading runner: tools | passage | statements, under the site header (no footer).
    h = 804
    p = screen(f, "P-43", "Reading", "Practice", h=h)
    y = navbar(p, role="learner", active="Luyện tập 4 kỹ năng", child="Reading")  # site header (y = 116)
    # A · top bar
    p.rect(0, y, DESKTOP_W, 48, fill=SOFT, stroke=LINE, r=0)
    p.zone(14, y + 11, "A")
    p.rect(66, y + 12, 24, 24, fill="#FFFFFF", stroke=DARK, r=24, value="✕", size=12, bold=True)
    p.rect(694, y + 8, 100, 32, fill=PRIMARY, stroke=PRIMARY, r=32, value="⏱ 00:06:37", color="#FFFFFF", size=14, bold=True)
    p.rect(1177, y + 7, 124, 34, fill="#FFFFFF", stroke=LINE, r=34, value="🗒 Xem note", size=13, bold=True)
    p.rect(1311, y + 7, 107, 34, fill="#FFFFFF", stroke=LINE, r=34, value="⚙ Cài đặt", size=13, bold=True)
    # B · tools
    p.zone(22, y + 168, "B")
    p.text(0, y + 200, 70, 22, "<b>Công cụ</b>", size=12, align="center")
    p.rect(4, y + 224, 62, 74, fill="#FFFFFF", stroke=PRIMARY, r=8, value="✎<br>Highlight<br>Phím (H)", size=11)
    p.rect(4, y + 308, 62, 74, fill="#FFFFFF", stroke=PRIMARY, r=8, value="🗒<br>Notes<br>Phím (N)", size=11)
    p.rect(4, y + 392, 62, 74, fill="#FFFFFF", stroke=PRIMARY, r=8, value="文<br>Tra từ vựng<br>Phím (T)", size=10)
    # C · passage
    p.card(76, y + 56, 640, 570, r=14)
    p.zone(56, y + 62, "C")
    p.text(76, y + 72, 640, 30, "<b>The Lord Howe Island stick insect</b>", size=18, align="center")
    for top, n in ((116, 7), (275, 6), (413, 5), (530, 4)):
        p.lines(96, y + top, 600, n, gap=21)
    p.rect(706, y + 64, 4, 190, fill=MEDIA, stroke=MEDIA, r=2)
    # D · questions
    p.card(736, y + 56, 700, 570, r=14)
    p.zone(722, y + 62, "D")
    p.rect(1424, y + 64, 4, 180, fill=MEDIA, stroke=MEDIA, r=2)
    p.text(756, y + 66, 500, 28, "<b>Questions 1 - 7</b>", size=18)
    intro = ("Do the following statements agree with the information given in Reading Passage 1?",
             "Choose <b>TRUE</b> if the statement agrees with the information",
             "Choose <b>FALSE</b> if the statement contradicts the information",
             "Choose <b>NOT GIVEN</b> if there is no information on this")
    for i, line in enumerate(intro):
        p.text(756, y + 102 + i * 20, 660, 20, line, size=13)
    statements = ("Fewer than half of the adult stick insects spotted during the recent survey were taken into captivity.",
                  "On Ball's Pyramid, adult stick insects feed on a variety of plants at night.",
                  "Nymphs and adults of the Lord Howe Island stick insect are active at different times of the day.",
                  "The stick insect had already died out on Lord Howe Island before the Makambo was stranded there.")
    for q, statement in enumerate(statements):
        qy = y + 190 + q * 126
        p.rect(756, qy, 26, 26, fill=PRIMARY_SOFT, stroke=PRIMARY_SOFT, r=26, value=str(q + 1), color=PRIMARY, size=12, bold=True)
        p.text(790, qy, 630, 26, statement, size=13)
        for i, label in enumerate(("TRUE", "FALSE", "NOT GIVEN")):
            if q == 3 and i:  # the pinned bottom bar covers the rest of Q4
                break
            cy = qy + 47 + i * 28
            p.rect(764, cy - 10, 20, 20, fill="#FFFFFF", stroke=DARK, r=20)
            p.text(796, cy - 12, 300, 24, label, size=14)
    # E · question navigator + finish
    p.rect(0, y + 634, DESKTOP_W, 54, fill=SOFT, stroke=LINE, r=0)
    p.zone(14, y + 648, "E")
    p.rect(98, y + 643, 372, 43, fill="#FFFFFF", stroke=PRIMARY, r=8)
    for i in range(13):
        p.text(106 + i * 28, y + 643, 28, 43, str(i + 1), size=13, color=PRIMARY, bold=True, align="center")
    p.btn(1265, y + 644, 125, 40, "Hoàn thành", "disabled", size=14)


def p43_listening_exam(f):
    # Real-exam Listening runner (Thi thử): exam bar with audio player, section band, table-completion questions.
    # Table geometry is taken from the reference screenshot (1860px wide) and scaled to the 1440px frame.
    h = 804
    p = screen(f, "P-43", "Listening Exam", "Practice", h=h)
    y = navbar(p, role="learner", active="Luyện tập 4 kỹ năng", child="Listening")  # site header (y = 116)

    def sx(v):
        return int(v * 0.774 + 0.5)

    def sy(v):
        return y + 52 + int((v - 82) * 0.774 + 0.5)

    # A · exam bar
    p.rect(0, y, DESKTOP_W, 52, fill="#FFFFFF", stroke=LINE, r=0)
    p.zone(14, y + 13, "A")
    p.rect(60, y + 14, 24, 24, fill="#FFFFFF", stroke=DARK, r=24, value="✕", size=12, bold=True)
    p.text(100, y + 4, 700, 22, "<b>Section 1: Beginner bookbinding courses</b>", size=14)
    p.rect(100, y + 28, 108, 20, fill="#FFFFFF", stroke=LINE, r=20, value="🔊 Audio player", size=11)
    p.text(218, y + 28, 200, 20, "10 minutes remaining", size=12)
    # B · section band
    p.rect(0, y + 52, DESKTOP_W, 80, fill=SOFT, stroke=LINE, r=0)
    p.zone(14, y + 79, "B")
    p.text(52, y + 64, 400, 26, "<b>Part 1</b>", size=16)
    p.text(52, y + 92, 700, 24, "Read the text and answer questions 1-10", size=14)
    # C · questions
    p.text(18, sy(218) - 12, 300, 24, "<b>Questions 1–10</b>", size=15)
    p.text(18, sy(258) - 12, 500, 24, "Complete the table below.", size=14)
    p.text(18, sy(301) - 12, 800, 24, "Write <b>ONE WORD AND/OR A NUMBER</b> for each answer.", size=14)
    p.text(sx(23), sy(364) - 15, sx(1480), 30, "<b>Beginner bookbinding courses</b>", size=18, align="center")
    cols, rows = (23, 191, 621, 1108, 1503), (404, 460, 564, 697, 802)
    for r in range(4):
        for c in range(4):
            p.rect(sx(cols[c]), sy(rows[r]), sx(cols[c + 1]) - sx(cols[c]), sy(rows[r + 1]) - sy(rows[r]), fill="#FFFFFF", stroke=DARK, r=0)
    for c, head in enumerate(("Course", "Details", "Cost", "Notes")):
        p.text(sx(cols[c]), sy(404), sx(cols[c + 1]) - sx(cols[c]), sy(460) - sy(404), f"<b>{head}</b>", size=14, align="center")
    for left, cy, w, label in (
            (36, 512, 150, "Saturday Taster"), (212, 494, 300, "• one day"), (212, 524, 150, "• make a small"),
            (634, 512, 20, "£"), (842, 512, 200, "(includes materials)"), (1122, 512, 105, "tutor: Lydia"),
            (36, 631, 150, "Evening Course"), (212, 597, 300, "• six weeks"), (212, 627, 400, "• make a notebook with a hard cover"),
            (212, 657, 200, "• last session: make a"), (634, 631, 60, "£120 ("), (887, 631, 215, "required when booking)"),
            (1122, 631, 200, "Tuesday evenings"),
            (36, 749, 150, "Summer School"), (212, 731, 130, "• five days in"), (212, 761, 75, "• up to"), (478, 761, 80, "people"),
            (634, 749, 125, "£175 (covers"), (951, 749, 120, "each day)"),
            (1135, 731, 62, "• own"), (1388, 731, 80, "needed"), (1135, 761, 125, "• booking: by"), (1453, 761, 50, "only")):
        p.text(sx(left), sy(cy) - 10, sx(w), 20, label, size=14)
    inputs = ((360, 509, 181, 29), (651, 499, 180, 27), (1231, 499, 180, 27), (425, 644, 179, 27), (697, 617, 180, 27),
              (343, 717, 180, 27), (288, 747, 179, 27), (762, 736, 179, 27), (1198, 717, 179, 27), (1263, 747, 178, 27))
    for n, (ix, iy, iw, ih) in enumerate(inputs, 1):
        p.rect(sx(ix), sy(iy), sx(iw), int(ih * 0.774 + 0.5), fill="#FFFFFF", stroke=PRIMARY if n == 1 else DARK, r=6,
               sw=2 if n == 1 else 1, value=str(n), size=13, bold=True)
    p.text(1414, sy(524) - 12, 24, 24, "🔖", size=16)
    # D · previous / next
    p.zone(1290, y + 570, "D")
    p.rect(1323, y + 555, 54, 54, fill=DARK, stroke=DARK, r=6, value="←", color="#FFFFFF", size=24)
    p.rect(1385, y + 555, 54, 54, fill=PRIMARY, stroke=PRIMARY, r=6, value="→", color="#FFFFFF", size=24)
    # E · part bar + submit
    p.rect(0, y + 634, DESKTOP_W, 54, fill=SOFT, stroke=LINE, r=0)
    p.zone(14, y + 648, "E")
    p.text(46, y + 648, 60, 26, "<b>Part 1</b>", size=13)
    p.rect(106, y + 646, 28, 30, fill="#FFFFFF", stroke=PRIMARY, r=4)
    for i in range(10):
        p.rect(108 + i * 28.5, y + 636, 24, 4, fill=MEDIA, stroke=MEDIA, r=2)
        p.text(106 + i * 28.5, y + 646, 28, 30, str(i + 1), size=13, align="center")
    p.rect(1389, y + 634, 51, 54, fill=MEDIA, stroke=LINE, r=0, value="✓", size=22, bold=True)


READING_RESULT = dict(
    frame="Reading Result", tab="Reading", band="3.0", ok=7, bad=33, skip=0, total=40, time="00:01:29",
    mascot="Đề IELTS hơi khó bạn nhỉ, mình cố tiếp cùng nhau nha, từ từ sẽ giỏi thôi!",
    # (question type, number of questions, correct, wrong, skipped)
    types=(("Matching Information", 6, 1, 5, 0), ("Multiple choice (Many Answers)", 2, 1, 1, 0),
           ("Multiple Choice (One Answer)", 4, 1, 3, 0), ("Yes - No - Not Given", 5, 2, 3, 0),
           ("True - False - Not Given", 7, 2, 5, 0), ("Summary Completion", 16, 0, 16, 0)),
    advice={"Summary Completion": "Đoán loại từ cần điền (danh từ, động từ, số), tìm trong bài và tuân thủ giới hạn số từ.",
            "Matching Information": "Gạch từ khoá từng ý rồi quét theo đoạn; một đoạn có thể được chọn nhiều lần.",
            "Multiple Choice (One Answer)": "Loại 2 đáp án sai rõ ràng trước, đối chiếu từng đáp án còn lại với bài.",
            "True - False - Not Given": "False là bài nói ngược lại, Not Given là bài không nhắc tới — tìm câu liên quan trước.",
            "Yes - No - Not Given": "Tìm từ thể hiện quan điểm tác giả (believe, should…) thay vì chỉ nhìn sự kiện.",
            "Multiple choice (Many Answers)": "Chọn đúng số đáp án đề yêu cầu và kiểm chứng từng đáp án với bài."},
    # (label, time used, seconds used, seconds suggested)
    time_card=dict(of="/ 60:00", line="Bạn nộp bài sau ~2 giây/câu — nhiều khả năng đã đoán đáp án.",
                   rows=(("Passage 1 · 13 câu", "0:28", 28, 1200), ("Passage 2 · 13 câu", "0:31", 31, 1200),
                         ("Passage 3 · 14 câu", "0:30", 30, 1200)), ref="~20:00",
                   tip="Gợi ý: chia 60 phút thành 20 / 20 / 20 phút cho 3 passage."),
)

# ~80% correct: the screen switches from "fix the weak spots" to "what is left to reach the next band"
READING_RESULT_HIGH = dict(
    frame="Reading Result High", tab="Reading", band="7.0", next_band="7.5", need=1, ok=32, bad=8, skip=0, total=40, time="00:54:20",
    mascot="Tuyệt vời! Bạn làm rất tốt, giữ phong độ này nhé!",
    types=(("Matching Information", 6, 5, 1, 0), ("Multiple choice (Many Answers)", 2, 2, 0, 0),
           ("Multiple Choice (One Answer)", 4, 3, 1, 0), ("Yes - No - Not Given", 5, 4, 1, 0),
           ("True - False - Not Given", 7, 5, 2, 0), ("Summary Completion", 16, 13, 3, 0)),
    advice={"Summary Completion": "Soát lại giới hạn số từ, chính tả và số ít / số nhiều trước khi chuyển câu.",
            "Matching Information": "Với các đoạn còn lại sau khi loại trừ, quét lại từ khoá để chắc không bỏ sót.",
            "Multiple Choice (One Answer)": "Với đáp án còn lại sau khi loại trừ, đối chiếu từng từ khoá với bài trước khi chốt.",
            "True - False - Not Given": "Chỉ chọn False khi bài nói ngược lại rõ ràng; không có thông tin thì là Not Given.",
            "Yes - No - Not Given": "Tách ý kiến tác giả khỏi thông tin sự kiện; tìm từ chỉ quan điểm trước khi chọn.",
            "Multiple choice (Many Answers)": "Đã làm tốt: kiểm chứng từng đáp án với bài để giữ phong độ."},
    time_card=dict(of="/ 60:00", line="Bạn còn dư 5 phút 40 giây — dùng để soát lại các câu chưa chắc.",
                   rows=(("Passage 1 · 12/13 đúng", "17:30", 1050, 1200), ("Passage 2 · 11/13 đúng", "18:10", 1090, 1200),
                         ("Passage 3 · 9/14 đúng", "18:40", 1120, 1200)), ref="~20:00",
                   tip="Gợi ý: Passage 3 tốn thời gian nhất và sai 5 câu — đọc câu hỏi trước khi đọc bài."),
)

# ~95% correct: nothing left to "fix", only stray mistakes; the screen invites a harder test
LISTENING_RESULT_TOP = dict(
    frame="Listening Result Top", tab="Listening", band="8.5", next_band="9.0", need=1, ok=38, bad=2, skip=0, total=40, time="00:38:20",
    mascot="Xuất sắc! Gần như tuyệt đối — bạn đã sẵn sàng cho thử thách cao hơn!", cta="Thử đề khó hơn",
    types=(("Map, Diagram Label", 6, 5, 1, 0), ("Summary Completion", 20, 19, 1, 0),
           ("Multiple Choice (One Answer)", 5, 5, 0, 0), ("Matching Features", 5, 5, 0, 0),
           ("Multiple choice (Many Answers)", 4, 4, 0, 0)),
    advice={"Map, Diagram Label": "Soát lại các từ chỉ vị trí (opposite, next to, behind) và điểm xuất phát trên bản đồ.",
            "Summary Completion": "Soát chính tả, số ít / số nhiều và giới hạn số từ trước khi chuyển đáp án.",
            "Multiple Choice (One Answer)": "Đã làm trọn vẹn — giữ thói quen gạch từ khoá trước khi nghe.",
            "Matching Features": "Đã làm trọn vẹn — giữ thói quen đọc trước danh sách lựa chọn.",
            "Multiple choice (Many Answers)": "Đã làm trọn vẹn — giữ thói quen loại trừ từng đáp án."},
    time_card=dict(of="/ ~40:00", line="Bạn nghe trọn audio và còn 1 phút 40 giây để soát đáp án.",
                   rows=(("Section 1 · 10/10 đúng", "9:30", 570, 600), ("Section 2 · 10/10 đúng", "9:40", 580, 600),
                         ("Section 3 · 9/10 đúng", "9:50", 590, 600), ("Section 4 · 9/10 đúng", "9:20", 560, 600)), ref="~10:00",
                   tip="Gợi ý: 2 câu sai nằm ở Section 3–4 — giữ tập trung đến hết audio."),
)

LISTENING_RESULT = dict(
    frame="Listening Result", tab="Listening", band="2.5", ok=5, bad=34, skip=1, total=40, time="00:01:05",
    mascot="Đề IELTS hơi khó bạn nhỉ, mình cố tiếp cùng nhau nha, từ từ sẽ giỏi thôi!",
    types=(("Map, Diagram Label", 6, 1, 5, 0), ("Summary Completion", 20, 0, 20, 0),
           ("Multiple Choice (One Answer)", 5, 1, 4, 0), ("Matching Features", 5, 1, 4, 0),
           ("Multiple choice (Many Answers)", 4, 2, 1, 1)),
    advice={"Summary Completion": "Đoán loại từ cần điền trước khi nghe; ghi đúng chính tả và tuân thủ giới hạn số từ.",
            "Map, Diagram Label": "Xác định điểm xuất phát; nghe các từ chỉ vị trí (opposite, next to, behind) để lần theo.",
            "Multiple Choice (One Answer)": "Gạch từ khoá cả 3 đáp án trước khi nghe; cẩn thận khi người nói đổi ý (but, actually…).",
            "Matching Features": "Đọc trước danh sách lựa chọn; chúng thường xuất hiện theo thứ tự — đừng kẹt ở câu đã lỡ.",
            "Multiple choice (Many Answers)": "Chọn đúng số đáp án đề yêu cầu và loại trừ từng đáp án trong lúc nghe."},
    time_card=dict(of="/ ~40:00", line="Bạn nộp bài sau 1 phút 5 giây, trong khi audio dài khoảng 30 phút.",
                   rows=(("Section 1 · 10 câu", "0:16", 16, 450), ("Section 2 · 10 câu", "0:16", 16, 450),
                         ("Section 3 · 10 câu", "0:16", 16, 450), ("Section 4 · 10 câu", "0:17", 17, 450)), ref="~7:30",
                   tip="Gợi ý: nghe hết audio và tranh thủ đọc trước câu hỏi của section kế tiếp."),
)


def result_page(f, cfg):
    # Result screen shared by Reading and Listening: score summary + per-type table (reference screens), plus a diagnosis.
    # Sample figures. Two modes, chosen by the overall % correct:
    #   under 70%  -> types under 50% get advice (relearn the method), banner = biggest weak spot
    #   70% and up -> types under 80% get advice (fine-tune), banner = distance to the next band
    #   90% and up -> every type that is not perfect gets advice (check the details), banner = band gap + a harder test
    types, total = cfg["types"], cfg["total"]
    ok, bad, skip = cfg["ok"], cfg["bad"], cfg["skip"]
    high = ok / total >= 0.7
    top = ok / total >= 0.9                      # near-perfect: only a few stray mistakes are left
    thr = 1.0 if top else (0.8 if high else 0.5)
    ranked = sorted(types, key=lambda r: r[2] / r[1])
    weak = [r for r in ranked if r[2] / r[1] < thr]
    if high:
        pool = [r for r in ranked if r[3] > 0]                                          # lowest % correct first
        first, second = pool[0], (pool[1] if len(pool) > 1 else None)
    else:
        first = max(types, key=lambda r: r[3])                                          # most wrong answers
        second = min((r for r in types if r is not first), key=lambda r: r[2] / r[1])  # then the lowest % correct
    prio = {r[0]: n for n, r in enumerate((first, second), 1) if r is not None and (high or r[2] / r[1] < 0.5)}
    ch = max(310, 68 + 46 * len(weak) + 32)   # height of the two insight cards
    shift = 48 * (6 - len(types))             # the reference table has 6 rows; every missing row pulls the rest up
    h = 164 - shift + 966 + ch + 72
    p = screen(f, "P-43", cfg["frame"], "Practice", h=h)
    y = navbar(p, role="learner", active="Luyện tập 4 kỹ năng", child=cfg["tab"])  # site header (y = 116)
    z = y + 48
    zd = z - shift
    # A · top bar
    p.rect(0, y, DESKTOP_W, 48, fill=SOFT, stroke=LINE, r=0)
    p.zone(14, y + 11, "A")
    p.rect(66, y + 12, 24, 24, fill="#FFFFFF", stroke=DARK, r=24, value="✕", size=12, bold=True)
    # B · result summary
    p.card(120, z + 24, 520, 140, r=14)
    p.img(140, z + 36, 200, 116, "Linh vật")
    p.text(360, z + 60, 260, 70, cfg["mascot"], size=14)
    p.rect(120, z + 180, 520, 124, fill=PRIMARY, stroke=PRIMARY, r=14)
    p.text(120, z + 198, 520, 26, "<b>Band Score:</b>", size=16, color="#FFFFFF", align="center")
    p.text(120, z + 226, 520, 60, f"<b>{cfg['band']}</b>", size=44, color="#FFFFFF", align="center")
    p.card(660, z + 24, 660, 280, r=14)
    p.zone(646, z + 30, "B")
    p.text(684, z + 38, 300, 24, "<b>Kết quả làm bài</b>", size=14)
    p.text(1100, z + 34, 196, 16, "Thời gian làm bài", size=10, color=MUTED, align="right")
    p.text(1100, z + 50, 196, 20, f"<b>{cfg['time']}</b>", size=13, align="right")
    p.rect(660, z + 76, 660, 1, fill=LINE, stroke=LINE, r=0)
    p.cell("", "ellipse;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#9CA3AF;strokeWidth=14;", 700, z + 100, 150, 150)
    p.cell("", f"shape=mxgraph.basic.partConcEllipse;startAngle=0;endAngle={ok / total:g};arcWidth=0.0854;fillColor=#123AB5;strokeColor=none;", 693, z + 93, 164, 164)
    p.text(700, z + 147, 150, 30, f"<b>{ok}/{total}</b>", size=22, align="center")
    p.text(700, z + 178, 150, 20, "câu đúng", size=13, align="center")
    for i, (dot, label) in enumerate(((PRIMARY, f"Đúng: <b>{ok} câu</b>"), ("#9CA3AF", f"Sai: <b>{bad} câu</b>"), (MEDIA, f"Bỏ qua: <b>{skip} câu</b>"))):
        p.rect(890, z + 125 + i * 36, 10, 10, fill=dot, stroke=dot, r=10)
        p.text(908, z + 120 + i * 36, 160, 20, label, size=13)
    p.btn(1090, z + 130, 200, 40, f"Xem {bad} câu sai" if high else "Sửa từng bước", size=13)
    p.btn(1090, z + 184, 200, 40, "Xem giải thích", "secondary", size=13)
    if top:
        note = f"Đúng {ok}/{total} câu ({round(ok / total * 100)}%) — gần như tuyệt đối, chỉ còn {bad} câu để chạm mốc tối đa."
    elif high:
        note = f"Đúng {ok}/{total} câu ({round(ok / total * 100)}%) — chỉ còn vài chỗ cần mài sắc, xem gợi ý bên dưới."
    else:
        note = f"Chỉ đúng {ok}/{total} câu — xem phân tích bên dưới để biết nên cải thiện gì trước."
    p.text(684, z + 268, 612, 24, note, size=12, color=MUTED, italic=True)
    p.rect(120, z + 320, 1200, 56, fill="#FFFFFF", stroke=LINE, r=12, dashed=True,
           value="Bạn có muốn đề xuất bài tập này đến các bạn khác có cùng level với bạn không?   👍   👎", size=12)
    # C · detail table with a verdict and a next step per question type
    p.card(120, z + 396, 1200, 380 - shift, r=14)
    p.zone(106, z + 404, "C")
    p.text(140, z + 408, 400, 28, "<b>Bảng dữ liệu chi tiết</b>", size=14)
    p.rect(121, z + 444, 1198, 40, fill=SOFT, stroke=SOFT, r=0)
    for left, w, head in ((140, 320, "Loại câu hỏi"), (470, 90, "Số câu hỏi"), (640, 80, "Sai"), (720, 80, "Bỏ qua"),
                          (830, 170, "Tỉ lệ đúng"), (1010, 110, "Đánh giá"), (1130, 180, "Gợi ý")):
        p.text(left, z + 444, w, 40, f"<b>{head}</b>", size=12, align="left" if left == 140 else "center")
    p.rect(560, z + 444, 80, 40, fill=PRIMARY, stroke=PRIMARY, r=0, value="Đúng", color="#FFFFFF", size=12, bold=True)
    for i, (name, count, right, wrong, skipped) in enumerate(types):
        ry = z + 484 + i * 48
        pct = round(right / count * 100)
        if name in prio:
            p.rect(121, ry, 1198, 47, fill=PRIMARY_SOFT, stroke=PRIMARY_SOFT, r=0)
        p.text(140, ry, 320, 48, f"<b>{name}</b>", size=13)
        if name in prio:
            p.rect(330, ry + 14, 68, 20, fill=PRIMARY, stroke=PRIMARY, r=20, value=f"Ưu tiên {prio[name]}", color="#FFFFFF", size=10, bold=True)
        p.text(470, ry, 90, 48, f"<b>{count}</b>", size=13, align="center")
        p.rect(585, ry + 9, 30, 30, fill=PRIMARY_SOFT, stroke=PRIMARY_SOFT, r=30, value=str(right), color=PRIMARY, size=12, bold=True)
        p.rect(665, ry + 9, 30, 30, fill=MEDIA, stroke=LINE, r=30, value=str(wrong), color=INK, size=12, bold=True)
        p.rect(745, ry + 9, 30, 30, fill="#FFFFFF", stroke=LINE, r=30, value=str(skipped), color=MUTED, size=12)
        p.rect(850, ry + 20, 120, 8, fill=MEDIA, stroke=MEDIA, r=8)
        if pct:
            p.rect(850, ry + 20, max(8, int(120 * pct / 100)), 8, fill=PRIMARY, stroke=PRIMARY, r=8)
        p.text(976, ry + 14, 36, 20, f"{pct}%", size=11, color=MUTED)
        if pct < 20:
            p.rect(1030, ry + 13, 90, 22, fill=DARK, stroke=DARK, r=22, value="Rất yếu", color="#FFFFFF", size=11, bold=True)
        elif pct < 50:
            p.rect(1030, ry + 13, 90, 22, fill="#FFFFFF", stroke=DARK, r=22, value="Yếu", size=11, bold=True)
        elif pct < 60:
            p.rect(1030, ry + 13, 90, 22, fill=SOFT, stroke=LINE, r=22, value="Trung bình", size=11)
        elif pct < 80:
            p.rect(1030, ry + 13, 90, 22, fill=SOFT, stroke=LINE, r=22, value="Khá", size=11, bold=True)
        elif top and pct >= 95:
            p.rect(1030, ry + 13, 90, 22, fill=PRIMARY, stroke=PRIMARY, r=22, value="Xuất sắc", color="#FFFFFF", size=11, bold=True)
        else:
            p.rect(1030, ry + 13, 90, 22, fill=PRIMARY_SOFT, stroke=PRIMARY, r=22, value="Tốt", color=PRIMARY, size=11, bold=True)
        if (wrong == 0) if top else (high and pct >= 80):
            p.text(1130, ry + 14, 180, 20, "✓ Giữ phong độ", size=12, color=MUTED, align="center")
        else:
            p.text(1130, ry + 14, 180, 20, "<u>Luyện dạng này ›</u>", size=12, color=PRIMARY, align="center")
        p.rect(121, ry + 47, 1198, 1, fill=LINE, stroke=LINE, r=0)
    # D · insights
    p.zone(88, zd + 798, "D")
    p.text(120, zd + 796, 700, 30, "<b>Phân tích & gợi ý cho bạn</b>", size=20)
    if top:
        sub = f"Dựa trên {total} câu bạn vừa làm — gần như tuyệt đối, chỉ còn vài chi tiết nhỏ để chạm mốc tối đa."
    elif high:
        sub = f"Dựa trên {total} câu bạn vừa làm — hệ thống chỉ ra điểm mạnh và việc nhỏ cần làm để lên band cao hơn."
    else:
        sub = f"Dựa trên {total} câu bạn vừa làm — hệ thống chỉ ra điểm yếu và việc nên làm tiếp theo."
    p.text(120, zd + 828, 900, 20, sub, size=13, color=MUTED)
    p.rect(120, zd + 862, 1200, 84, fill=PRIMARY_SOFT, stroke=PRIMARY, r=14, sw=2)
    if top:
        p.text(144, zd + 876, 920, 26, f"<b>Band {cfg['band']} — chỉ còn {cfg['need']} câu đúng nữa là đạt Band {cfg['next_band']}.</b>", size=15)
        p.text(144, zd + 906, 920, 22, f"Các câu sai còn lại nằm ở: {' và '.join(r[0] for r in pool)}. Soát lại để chạm mốc tối đa.", size=13)
    elif high:
        p.text(144, zd + 876, 920, 26, f"<b>Bạn đang ở Band {cfg['band']} — chỉ cần thêm {cfg['need']} câu đúng để lên Band {cfg['next_band']}.</b>", size=15)
        p.text(144, zd + 906, 920, 22, f"Dễ lấy thêm điểm nhất: {first[0]} (đúng {first[2]}/{first[1]}, còn sai {first[3]} câu).", size=13)
    else:
        p.text(144, zd + 876, 920, 26, f"<b>Ưu tiên số 1: {first[0]}</b> — đúng {first[2]}/{first[1]} câu, chiếm {round(first[1] / total * 100)}% tổng số câu của bài.", size=15)
        p.text(144, zd + 906, 920, 22, "Đây là dạng đang kéo điểm của bạn xuống nhiều nhất: cải thiện dạng này sẽ giúp tăng band nhanh nhất.", size=13)
    cta = cfg["cta"] if top else f"Luyện {first[0]}"
    bw = 224 if len(cta) <= 26 else 264
    p.btn(1300 - bw, zd + 884, bw, 40, cta, size=12)
    p.card(120, zd + 966, 590, ch, r=14)
    title = "Chỉ còn vài chi tiết nhỏ" if top else ("Còn mất điểm ở đâu?" if high else "Vì sao bạn mất điểm?")
    hint = ("Các dạng chưa đạt trọn điểm — soát lại để chạm mốc tối đa" if top
            else "Các dạng đúng dưới 80% — tinh chỉnh để lên band cao hơn" if high
            else "Các dạng đúng dưới 50% — nên học lại phương pháp làm bài")
    p.text(140, zd + 980, 400, 24, f"<b>{title}</b>", size=14)
    p.text(140, zd + 1004, 540, 18, hint, size=11, color=MUTED)
    for i, (name, count, right, _wrong, _skipped) in enumerate(weak):
        ry = zd + 1034 + i * 46
        pct = round(right / count * 100)
        p.text(140, ry, 215, 20, f"<b>{name}</b>", size=12)
        p.rect(360, ry + 7, 100, 6, fill=MEDIA, stroke=MEDIA, r=6)
        if pct:
            p.rect(360, ry + 7, max(6, int(100 * pct / 100)), 6, fill=PRIMARY, stroke=PRIMARY, r=6)
        p.text(468, ry, 110, 20, f"<b>{pct}%</b> · {right}/{count}", size=11, color=MUTED)
        p.text(590, ry, 100, 20, "<u>Xem cách làm ›</u>", size=11, color=PRIMARY, align="right")
        p.text(140, ry + 22, 550, 18, cfg["advice"][name], size=11, color=MUTED)
    fine = ", ".join(r[0] for r in ranked if r[2] / r[1] >= thr)
    if fine:
        label = ("✓ Các dạng làm trọn vẹn (đúng 100%)" if top else "✓ Các dạng còn lại đã rất tốt (từ 80% trở lên)" if high
                 else "✓ Các dạng còn lại đang ổn (từ 50% trở lên)")
        p.text(140, zd + 1034 + len(weak) * 46 + 2, 550, 30 if high else 16, f"{label}: {fine}", size=11, color=MUTED, italic=True,
               valign="top" if high else "middle")
    tc = cfg["time_card"]
    p.card(730, zd + 966, 590, ch, r=14)
    p.text(750, zd + 980, 400, 24, "<b>Quản lý thời gian</b>", size=14)
    p.text(750, zd + 1008, 300, 36, f"<b>{cfg['time']}</b> <font color='#6B7280' style='font-size:14px'>{tc['of']}</font>", size=26)
    p.text(750, zd + 1050, 550, 36, tc["line"], size=12, color=MUTED)
    step = 36 if len(tc["rows"]) <= 3 else 30
    for i, (label, used, used_s, ref_s) in enumerate(tc["rows"]):
        ry = zd + 1100 + i * step
        p.text(750, ry, 160, 24, label, size=12)
        p.rect(920, ry + 8, 210, 8, fill=MEDIA, stroke=MEDIA, r=8)
        p.rect(920, ry + 8, max(8, int(210 * used_s / ref_s)), 8, fill=PRIMARY, stroke=PRIMARY, r=8)
        p.text(1140, ry, 160, 24, f"{used} / {tc['ref']}", size=12, color=MUTED, align="right")
    p.rect(750, zd + 966 + ch - 50, 550, 32, fill=SOFT, stroke=LINE, r=8, value=tc["tip"], size=11, align="left")
    p.text(120, zd + 966 + ch + 20, 740, 20, "Số liệu phân tích ở màn này là dữ liệu minh họa; kết quả thật được tính từ bài vừa làm.", size=11, color=MUTED, italic=True)
    p.btn(1000, zd + 966 + ch + 12, 140, 36, "Làm lại bài", "secondary", size=13)
    p.btn(1160, zd + 966 + ch + 12, 160, 36, "Về danh mục", size=13)


def p43_reading_result(f):
    result_page(f, READING_RESULT)


def p43_reading_result_high(f):
    result_page(f, READING_RESULT_HIGH)


def p43_listening_result(f):
    result_page(f, LISTENING_RESULT)


def p43_listening_result_top(f):
    result_page(f, LISTENING_RESULT_TOP)


WRITING_RESULT = dict(
    task="Writing Task 1 · Line graph", time="00:19:42", time_limit="20:00",
    # (criterion, meaning, band, what went well, what to improve)
    criteria=(("Task Achievement", "Hoàn thành yêu cầu đề bài", 6.5, "Nêu đủ xu hướng chính và có overview rõ ràng.",
               "Một vài số liệu ở mốc 2000 và 2010 chưa chính xác."),
              ("Coherence & Cohesion", "Mạch lạc và liên kết", 6.0, "Bố cục 4 đoạn rõ ràng, mỗi đoạn một ý chính.",
               "Từ nối còn lặp (while, whereas); chuyển ý giữa hai thân bài chưa mượt."),
              ("Lexical Resource", "Vốn từ vựng", 5.5, "Từ vựng đủ để mô tả biểu đồ.",
               "Lặp “increase” 6 lần, thiếu từ đồng nghĩa (rise, climb, grow)."),
              ("Grammatical Range & Accuracy", "Ngữ pháp", 6.0, "Có dùng câu phức và câu so sánh.",
               "7 lỗi mạo từ và chia thì, chủ yếu ở đoạn thân bài.")),
    # measured automatically from the text: (label, value, note)
    metrics=(("Số từ", "187", "tối thiểu 150 ✓"), ("Số đoạn", "4", "Intro · Overview · Body 1 · Body 2"),
             ("Từ/câu trung bình", "19", "ổn định cho Task 1"), ("Từ nối đã dùng", "9", "while ×3 · whereas ×2 · overall ×1"),
             ("Từ lặp nhiều nhất", "increase ×6", "nên đa dạng hóa")),
    essay=("The line graph illustrates the fruit production, measured in millions of tonnes, in four different countries (Spain, Turkey, France, and Germany) "
           "over a 40-year period from 1970 to 2010. Overall, while Turkey and France showed a general increase in fruit production, Spain and Germany experienced a decline.",
           "Turkey's production increased steadily, and France's production also {v}increased{/v} to about 8 million tonnes. "
           "In contrast, Germany's output {g}decrease{/g} sharply after 2000, {c}so{/c} it ended at the lowest level of the four countries."),
    fixes=(("Ngữ pháp", "decrease → decreased", "Mô tả quá khứ (1970–2010) dùng thì quá khứ đơn."),
           ("Từ vựng", "increased (lần 2) → rose", "Tránh lặp từ; dùng rise / climb / grow."),
           ("Mạch lạc", "so → whereas", "Dùng từ nối đối lập khi so sánh hai quốc gia.")),
)


def band_round(avg):
    # IELTS rounding: the average of the four criteria goes to the nearest half band (x.25 -> x.5, x.75 -> next whole band)
    return int(avg * 2 + 0.5) / 2


def p43_writing_result(f):
    # Writing result by the four IELTS criteria. Criterion bands come from the grader (teacher / AI); the overall band, the
    # text measures and the "what if" band are computed. Sample figures.
    cfg = WRITING_RESULT
    crit = cfg["criteria"]
    bands = [c[2] for c in crit]
    band = band_round(sum(bands) / 4)
    low = min(range(4), key=lambda i: bands[i])
    after = list(bands)
    after[low] += 1.0
    band_after = band_round(sum(after) / 4)
    yellow = "#FDE68A"
    kinds = {"Ngữ pháp": yellow, "Từ vựng": PRIMARY_SOFT, "Mạch lạc": MEDIA}
    h = 1604
    p = screen(f, "P-43", "Writing Result", "Practice", h=h)
    y = navbar(p, role="learner", active="Luyện tập 4 kỹ năng", child="Writing")  # site header (y = 116)
    z = y + 48
    # A · top bar
    p.rect(0, y, DESKTOP_W, 48, fill=SOFT, stroke=LINE, r=0)
    p.zone(14, y + 11, "A")
    p.rect(66, y + 12, 24, 24, fill="#FFFFFF", stroke=DARK, r=24, value="✕", size=12, bold=True)
    # B · overall band + the four criteria + measures taken from the text
    p.rect(120, z + 24, 520, 312, fill=PRIMARY, stroke=PRIMARY, r=14)
    p.text(120, z + 52, 520, 26, "<b>Band Score:</b>", size=16, color="#FFFFFF", align="center")
    p.text(120, z + 84, 520, 80, f"<b>{band:.1f}</b>", size=60, color="#FFFFFF", align="center")
    p.text(120, z + 180, 520, 22, "Trung bình 4 tiêu chí, làm tròn theo quy tắc IELTS", size=13, color="#FFFFFF", align="center")
    terms = " + ".join(f"{b:.1f}" for b in bands)
    p.text(120, z + 206, 520, 24, f"({terms}) / 4 = {sum(bands) / 4:.2f} → {band:.1f}", size=14, color="#FFFFFF", align="center", bold=True)
    p.text(160, z + 262, 440, 44, "Bài viết khá tốt! Từ vựng là phần cần nâng thêm để lên band cao hơn.", size=14, color="#FFFFFF", align="center")
    p.card(660, z + 24, 660, 312, r=14)
    p.zone(646, z + 30, "B")
    p.text(684, z + 38, 300, 24, "<b>Kết quả chấm bài</b>", size=14)
    p.text(1000, z + 38, 296, 22, cfg["task"], size=12, color=MUTED, align="right")
    p.rect(660, z + 76, 660, 1, fill=LINE, stroke=LINE, r=0)
    for i, (name, _meaning, b, _good, _bad) in enumerate(crit):
        ry = z + 92 + i * 40
        p.text(684, ry, 232, 24, f"<b>{name}</b>", size=13)
        p.rect(926, ry + 8, 210, 8, fill=MEDIA, stroke=MEDIA, r=8)
        p.rect(926, ry + 8, int(210 * b / 9), 8, fill=PRIMARY, stroke=PRIMARY, r=8)
        p.text(1142, ry, 44, 24, f"<b>{b:.1f}</b>", size=14, align="right")
        if i == low:
            p.rect(1192, ry + 2, 120, 20, fill=DARK, stroke=DARK, r=20, value="Cần cải thiện nhất", color="#FFFFFF", size=10, bold=True)
    p.text(684, z + 256, 612, 20, "Điểm từng tiêu chí do giáo viên / AI chấm (thang 0–9).", size=11, color=MUTED, italic=True)
    p.btn(684, z + 284, 200, 36, "Xem bài đã sửa", size=13)
    p.btn(900, z + 284, 160, 36, "Viết lại bài", "secondary", size=13)
    p.text(1070, z + 284, 232, 36, f"Thời gian: <b>{cfg['time']}</b> / {cfg['time_limit']}", size=12, color=MUTED, align="right")
    p.card(120, z + 352, 1200, 100, r=14)
    p.text(140, z + 360, 700, 20, "Số đo tự động từ bài viết", size=11, color=MUTED)
    for i, (label, value, note) in enumerate(cfg["metrics"]):
        mx = 140 + i * 236
        p.text(mx, z + 380, 220, 16, label, size=11, color=MUTED)
        p.text(mx, z + 394, 220, 28, f"<b>{value}</b>", size=20)
        p.text(mx, z + 424, 220, 18, note, size=10, color=MUTED)
    # C · detail by criterion
    p.zone(88, z + 470, "C")
    p.text(120, z + 468, 700, 30, "<b>Chi tiết theo từng tiêu chí</b>", size=20)
    for i, (name, meaning, b, good, bad) in enumerate(crit):
        cx, cy = 120 + (i % 2) * 610, z + 510 + (i // 2) * 176
        p.card(cx, cy, 590, 160, r=14, stroke=PRIMARY if i == low else LINE, sw=2 if i == low else 1)
        p.rect(cx + 20, cy + 20, 64, 64, fill=PRIMARY_SOFT, stroke=PRIMARY, r=64, value=f"{b:.1f}", color=PRIMARY, size=18, bold=True)
        p.text(cx + 100, cy + 18, 300, 22, f"<b>{name}</b>", size=14)
        p.text(cx + 100, cy + 42, 300, 18, meaning, size=11, color=MUTED)
        if i == low:
            p.rect(cx + 430, cy + 18, 140, 20, fill=DARK, stroke=DARK, r=20, value="Cần cải thiện nhất", color="#FFFFFF", size=10, bold=True)
        p.text(cx + 20, cy + 94, 550, 20, f"<b>✓ Làm tốt:</b> {good}", size=11)
        p.text(cx + 20, cy + 114, 550, 20, f"<b>△ Cần cải thiện:</b> {bad}", size=11)
        p.text(cx + 400, cy + 136, 170, 16, "<u>Xem lỗi liên quan ›</u>", size=11, color=PRIMARY, align="right")
    # D · the essay, marked up
    p.zone(88, z + 888, "D")
    p.text(120, z + 886, 800, 30, "<b>Bài viết của bạn đã được đánh dấu</b>", size=20)
    p.card(120, z + 928, 760, 300, r=14)
    for i, (label, colour) in enumerate(kinds.items()):
        p.rect(140 + i * 96, z + 944, 86, 20, fill=colour, stroke=colour, r=4, value=label, size=10, bold=True)
    marks = {"{g}": f"<span style='background-color:{yellow}'>", "{v}": f"<span style='background-color:{PRIMARY_SOFT}'>",
             "{c}": f"<span style='background-color:{MEDIA}'>"}
    for i, para in enumerate(cfg["essay"]):
        for key, tag in marks.items():
            para = para.replace(key, tag)
        for key in ("{/g}", "{/v}", "{/c}"):
            para = para.replace(key, "</span>")
        p.text(140, z + 980 + i * 100, 720, 90, para, size=13, valign="top")
    p.card(900, z + 928, 420, 300, r=14)
    p.text(920, z + 940, 380, 22, f"<b>Gợi ý sửa ({len(cfg['fixes'])})</b>", size=14)
    for i, (kind, change, why) in enumerate(cfg["fixes"]):
        fy = z + 982 + i * 80
        p.rect(920, fy, 76, 20, fill=kinds[kind], stroke=kinds[kind], r=20, value=kind, size=10, bold=True)
        p.text(920, fy + 26, 380, 22, f"<b>{change}</b>", size=13)
        p.text(920, fy + 48, 380, 32, why, size=11, color=MUTED, valign="top")
    # E · what to do first
    p.zone(88, z + 1244, "E")
    p.text(120, z + 1242, 600, 30, "<b>Việc nên làm trước</b>", size=20)
    p.rect(120, z + 1282, 1200, 84, fill=PRIMARY_SOFT, stroke=PRIMARY, r=14, sw=2)
    p.text(144, z + 1296, 920, 26, f"<b>Ưu tiên: {crit[low][0]} ({bands[low]:.1f})</b> — tiêu chí thấp nhất của bài.", size=15)
    p.text(144, z + 1326, 920, 22, f"Nâng thêm 1.0 ở tiêu chí này (lên {after[low]:.1f}) sẽ đưa Band từ {band:.1f} lên {band_after:.1f} nếu các tiêu chí khác giữ nguyên.", size=13)
    p.btn(1036, z + 1304, 264, 40, "Học từ vựng miêu tả xu hướng", size=12)
    p.text(120, z + 1390, 740, 20, "Điểm 4 tiêu chí do giáo viên / AI chấm; Band tổng và số đo được tính tự động. Số liệu ở màn này là dữ liệu minh họa.", size=11, color=MUTED, italic=True)
    p.btn(1000, z + 1382, 140, 36, "Viết lại bài", "secondary", size=13)
    p.btn(1160, z + 1382, 160, 36, "Về danh mục", size=13)


def p43_reading_explanation(f):
    # Reading explanation, opened from the result ("Xem giải thích"): passage with the answer located | questions marked right / wrong |
    # step-by-step explanation of the current question | question strip coloured by result. Sample figures matching Reading Result.
    h = 804
    p = screen(f, "P-43", "Reading Explanation", "Practice", h=h)
    y = navbar(p, role="learner", active="Luyện tập 4 kỹ năng", child="Reading")  # site header (y = 116)
    # A · top bar
    p.rect(0, y, DESKTOP_W, 48, fill=SOFT, stroke=LINE, r=0)
    p.zone(14, y + 11, "A")
    p.rect(66, y + 12, 24, 24, fill="#FFFFFF", stroke=DARK, r=24, value="✕", size=12, bold=True)
    p.text(104, y + 10, 520, 28, "<b>Reading · Passage 1 — The World Cup ball</b>", size=14)
    p.rect(694, y + 8, 100, 32, fill=PRIMARY, stroke=PRIMARY, r=32, value="⏱ 00:01:29", color="#FFFFFF", size=14, bold=True)
    p.text(808, y + 10, 160, 28, "Band Score: <b>3.0</b>", size=13, color=PRIMARY)
    p.rect(1000, y + 7, 124, 34, fill="#FFFFFF", stroke=LINE, r=34, value="🗒 Xem note", size=13, bold=True)
    p.rect(1134, y + 7, 107, 34, fill="#FFFFFF", stroke=LINE, r=34, value="⚙ Cài đặt", size=13, bold=True)
    p.rect(1251, y + 7, 167, 34, fill="#FFFFFF", stroke=LINE, r=34, value="↗ Chia sẻ bài làm", size=13, bold=True)
    # B · passage, the sentence holding the answer is highlighted
    p.card(8, y + 56, 690, 570, r=14)
    p.zone(14, y + 62, "B")
    p.text(8, y + 72, 690, 30, "<b>The World Cup ball</b>", size=20, align="center")
    p.text(24, y + 116, 658, 86, "<span style='background-color:#E8EDFB'>Shortly before the 2010 World Cup began, Brazil's goalkeeper Júlio César complained to journalists that the official ball was like one you might buy in a supermarket.</span> He wasn't alone. Gianluigi Buffon, another goalkeeper, called it shameful to use such a ball in so important a competition, and Robinho, Júlio César's team-mate in the Brazil squad, added: 'For sure the guy who designed this ball never played football.'", size=13, valign="top")
    for top, n in ((214, 6), (368, 6), (522, 4)):
        p.lines(24, y + top, 658, n, gap=22)
    p.rect(690, y + 64, 4, 150, fill=MEDIA, stroke=MEDIA, r=2)
    # C · questions, the learner's pick and the correct answer
    p.card(706, y + 56, 726, 328, r=14)
    p.zone(690, y + 62, "C")
    p.text(726, y + 62, 500, 26, "<b>Questions 1 - 7</b>", size=18)
    for i, line in enumerate(("Do the following statements agree with the information given in Reading Passage 1?",
                              "Choose <b>TRUE</b> if the statement agrees with the information",
                              "Choose <b>FALSE</b> if the statement contradicts the information",
                              "Choose <b>NOT GIVEN</b> if there is no information on this")):
        p.text(726, y + 92 + i * 17, 680, 17, line, size=12)

    def question(qy, number, statement, pick, right):
        p.rect(726, qy, 24, 24, fill=PRIMARY_SOFT, stroke=PRIMARY_SOFT, r=24, value=str(number), color=PRIMARY, size=11, bold=True)
        p.text(758, qy, 650, 24, statement, size=13)
        for i, label in enumerate(("TRUE", "FALSE", "NOT GIVEN")):
            cy = qy + 40 + i * 24
            state = "wrong" if i == pick else ("right" if i == right else None)
            if state == "wrong":
                p.rect(740, cy - 9, 18, 18, fill=DARK, stroke=DARK, r=18)
            elif state == "right":
                p.rect(740, cy - 9, 18, 18, fill="#FFFFFF", stroke=PRIMARY, r=18, sw=3)
            else:
                p.rect(740, cy - 9, 18, 18, fill="#FFFFFF", stroke=DARK, r=18)
            p.text(770, cy - 12, 130, 24, f"<b>{label}</b>" if state else label, size=14, color=PRIMARY if state == "right" else INK)
            if state == "wrong":
                p.rect(900, cy - 11, 112, 22, fill=DARK, stroke=DARK, r=22, value="✗ Bạn chọn", color="#FFFFFF", size=11, bold=True)
            if state == "right":
                p.rect(900, cy - 11, 128, 22, fill=PRIMARY_SOFT, stroke=PRIMARY, r=22, value="✓ Đáp án đúng", color=PRIMARY, size=11, bold=True)
                p.rect(1316, cy - 12, 104, 24, fill="#FFFFFF", stroke=PRIMARY, r=8, value="📍 Xem vị trí", color=PRIMARY, size=11, bold=True)

    question(y + 166, 1, "Brazil's goalkeeper made his criticism of the Jabulani after the 2010 World Cup had ended.", 0, 1)
    question(y + 280, 2, "Like the Jabulani, the ball used at the previous World Cup had been criticised by players.", 0, 2)
    p.rect(1424, y + 64, 4, 130, fill=MEDIA, stroke=MEDIA, r=2)
    # D · explanation of the current question
    p.card(706, y + 392, 726, 234, r=14)
    p.zone(690, y + 398, "D")
    p.text(726, y + 400, 400, 24, "<b>Câu 1 - Giải thích đáp án</b>", size=14)
    p.rect(1150, y + 402, 262, 22, fill=PRIMARY_SOFT, stroke=PRIMARY, r=22, value="Bạn chọn <b>TRUE</b> · Đáp án đúng <b>FALSE</b>", color=PRIMARY, size=11)
    for i, line in enumerate(("<u>Bước 1:</u> Hiểu câu hỏi",
                              "Câu hỏi nghĩa là: Thủ môn đội tuyển Brazil đã chê Jabulani (bóng chính thức của giải) sau khi World Cup 2010 kết thúc.",
                              "→ Câu hỏi xoay quanh <b>thời điểm đưa ra lời chê</b>: trước hay sau giải đấu.",
                              "<u>Bước 2:</u> Tìm keywords được paraphrase",
                              "Brazil's goalkeeper ~ giữ nguyên · made his criticism ~ complained to journalists",
                              "after the 2010 World Cup had ended ~ Shortly before the 2010 World Cup began (ngược nhau về thời điểm)",
                              "<u>Bước 3:</u> So sánh và đối chiếu",
                              "Đoạn 1 nói thủ môn Júlio César chê bóng <b>trước</b> khi World Cup 2010 bắt đầu, trái với câu hỏi (sau khi kết thúc) → <b>FALSE</b>.")):
        p.text(726, y + 434 + i * 21, 690, 20, line, size=11)
    p.rect(1424, y + 400, 4, 100, fill=MEDIA, stroke=MEDIA, r=2)
    # E · question strip coloured by result + navigation
    p.rect(0, y + 634, DESKTOP_W, 54, fill=SOFT, stroke=LINE, r=0)
    p.zone(14, y + 648, "E")
    right_set = {4, 5, 17, 22, 24, 26}
    p.rect(94, y + 640, 372, 42, fill="#FFFFFF", stroke=LINE, r=8)
    p.rect(482, y + 640, 372, 42, fill="#FFFFFF", stroke=LINE, r=8)
    for n in range(1, 27):
        x = 98 + (n - 1) * 28 if n <= 13 else 486 + (n - 14) * 28
        if n == 1:
            p.rect(x - 3, y + 646, 30, 30, fill="#FFFFFF", stroke=INK, r=30, sw=2)
        ok = n in right_set
        p.rect(x, y + 649, 24, 24, fill=PRIMARY if ok else DARK, stroke=PRIMARY if ok else DARK, r=24, value=str(n), color="#FFFFFF", size=10, bold=True)
    p.rect(872, y + 646, 28, 28, fill="#FFFFFF", stroke=LINE, r=28, value="‹", size=16)
    p.rect(906, y + 646, 28, 28, fill="#FFFFFF", stroke=LINE, r=28, value="›", size=16)
    p.rect(980, y + 655, 10, 10, fill=PRIMARY, stroke=PRIMARY, r=10)
    p.text(996, y + 650, 60, 20, "Đúng", size=12)
    p.rect(1060, y + 655, 10, 10, fill=DARK, stroke=DARK, r=10)
    p.text(1076, y + 650, 60, 20, "Sai", size=12)
    p.btn(1265, y + 644, 125, 40, "Làm bài khác", "secondary", size=13)


def p43_listening_explanation(f):
    # Listening explanation, opened from the result ("Xem giải thích"): transcript with the answer sentence located + audio player |
    # the form with each answer corrected (wrong, struck through -> right) | question strip coloured by result. Sample figures.
    h = 804
    p = screen(f, "P-43", "Listening Explanation", "Practice", h=h)
    y = navbar(p, role="learner", active="Luyện tập 4 kỹ năng", child="Listening")  # site header (y = 116)

    def w(s):
        return int(len(s) * 7.3) + 10

    # A · top bar
    p.rect(0, y, DESKTOP_W, 48, fill=SOFT, stroke=LINE, r=0)
    p.zone(14, y + 11, "A")
    p.rect(66, y + 12, 24, 24, fill="#FFFFFF", stroke=DARK, r=24, value="✕", size=12, bold=True)
    p.text(104, y + 10, 560, 28, "<b>Listening · Section 1 — Volunteer work application</b>", size=14)
    p.rect(694, y + 8, 100, 32, fill=PRIMARY, stroke=PRIMARY, r=32, value="⏱ 00:01:05", color="#FFFFFF", size=14, bold=True)
    p.text(808, y + 10, 160, 28, "Band Score: <b>2.5</b>", size=13, color=PRIMARY)
    p.rect(1134, y + 7, 107, 34, fill="#FFFFFF", stroke=LINE, r=34, value="⚙ Cài đặt", size=13, bold=True)
    p.rect(1251, y + 7, 167, 34, fill="#FFFFFF", stroke=LINE, r=34, value="↗ Chia sẻ bài làm", size=13, bold=True)
    # B · transcript + audio player
    p.card(8, y + 56, 690, 570, r=14)
    p.zone(656, y + 62, "B")
    turns = (("William:", ("Okay.", "Let's get started.", "What's the best phone number to contact you on?")),
             ("Grace:", ("My mobile phone's probably best.", "The number's 0216367189.", "But I can't always answer it during the day.")),
             ("William:", ("Okay.", "I'll make a note that email's a good way to contact you.", "What's the address?")),
             ("Grace:", ("<span style='background-color:#E8EDFB'>It's graceb@travel.co.nz.</span>", "I chose it when I was younger, and I just haven't changed it since.")),
             ("William:", ("It's easy to remember.", "Now do you have any particular qualifications, Grace?")),
             ("Grace:", ("I'm a housewife now, but I used to be in teaching.", "I trained for that and got my diploma, although I haven't done it for years.")),
             ("William:", ("Alright.", "I need to find out when you'll be available during the week.")))
    ty = y + 70
    for i, (speaker, lines_) in enumerate(turns):
        p.text(24, ty, 76, 20, f"<b>{speaker}</b>", size=13)
        p.text(104, ty, 580, 20 * len(lines_), "<br>".join(lines_), size=13, valign="top")
        if i == 3:
            p.rect(330, ty + 1, 56, 18, fill=PRIMARY, stroke=PRIMARY, r=18, value="Câu 1", color="#FFFFFF", size=10, bold=True)
        ty += 20 * len(lines_) + 14
    p.rect(690, y + 64, 4, 90, fill=MEDIA, stroke=MEDIA, r=2)
    p.rect(9, y + 566, 688, 1, fill=LINE, stroke=LINE, r=0)
    p.text(20, y + 583, 110, 24, "00:00 / 06:13", size=11, color=MUTED)
    p.text(134, y + 583, 24, 24, "🔊", size=13, align="center")
    p.progress(162, y + 592, 130, 6, h=6)
    p.rect(330, y + 583, 28, 28, fill="#FFFFFF", stroke=DARK, r=28, value="↺5", size=10, bold=True)
    p.rect(368, y + 580, 34, 34, fill=PRIMARY, stroke=PRIMARY, r=34, value="▶", color="#FFFFFF", size=11, bold=True)
    p.rect(412, y + 583, 28, 28, fill="#FFFFFF", stroke=DARK, r=28, value="↻5", size=10, bold=True)
    p.rect(590, y + 580, 90, 34, fill="#FFFFFF", stroke=LINE, r=34, value="⏱ <b>1x</b>", size=12)
    # C · the form, every answer corrected (wrong -> right); the chip plays the matching part of the audio
    p.card(706, y + 56, 726, 570, r=14)
    p.zone(690, y + 62, "C")
    p.text(726, y + 62, 500, 26, "<b>Questions 1 - 10</b>", size=18)
    p.text(726, y + 92, 680, 20, "Complete the notes below. Write ONE WORD AND/OR A NUMBER for each answer.", size=12)
    p.rect(726, y + 120, 686, 500, fill="#FFFFFF", stroke=DARK, r=0)
    p.text(726, y + 128, 686, 22, "<b>Volunteer work application form</b>", size=11, align="center")
    rows = (("t", 152, "<b>Name:</b> Grace Brown"), ("t", 176, "<b>Mobile phone number:</b> 021 636 7189"), ("h", 200, "Email address"),
            ("a", 224, "graceb@", 1, "trevel", "travel", ".co.nz"), ("h", 250, "Qualification"), ("a", 274, "a diploma in", 2, "teacher", "teaching", ""),
            ("h", 300, "Agreed work hours"), ("a", 324, "from", 3, "9.50", "9.15", "am to 2pm Monday to Friday"),
            ("h", 350, "Volunteer work experience"), ("a", 374, "a volunteer city", 4, "tour", "guide", ""),
            ("a", 398, "a volunteer netball team", 5, "captain", "coach", ""), ("b", 422, "at Rugby World Cup"), ("h", 448, "Hobbies"),
            ("a", 472, "likes to work in her", 6, "gardening", "garden", ""), ("b", 496, "enjoys flower arranging"),
            ("a", 520, "plays the", 7, "piano", "guitar", ""), ("h", 546, "Type of work offered"),
            ("a", 570, "working on a", 8, None, "farm", "for a month"), ("b", 594, "working in a community centre with elderly people"))
    for row in rows:
        kind, yo = row[0], y + row[1]
        if kind == "t":
            p.text(744, yo, 660, 22, row[2], size=13)
        elif kind == "h":
            p.text(744, yo, 660, 22, f"<b>{row[2]}</b>", size=13)
        elif kind == "b":
            p.text(744, yo, 16, 22, "•", size=13)
            p.text(762, yo, 640, 22, row[2], size=13)
        else:
            _, _, prefix, number, wrong, right, suffix = row
            p.text(744, yo, 16, 22, "•", size=13)
            x = 762
            p.text(x, yo, w(prefix), 22, prefix, size=13)
            x += w(prefix)
            p.rect(x, yo, 56, 22, fill=PRIMARY_SOFT, stroke=PRIMARY_SOFT, r=22, value=f"▶ {number}", color=PRIMARY, size=10, bold=True)
            x += 64
            if wrong:
                p.text(x, yo, w(wrong), 22, f"<s>{wrong}</s>", size=13, color=DARK)
                x += w(wrong) + 4
            else:
                p.text(x, yo, 16, 22, "×", size=13, color=DARK, bold=True)
                x += 20
            p.text(x, yo, 24, 22, "→", size=13, align="center")
            x += 28
            p.text(x, yo, w(right), 22, f"<u><b>{right}</b></u>", size=13, color=PRIMARY)
            x += w(right) + 4
            p.text(x, yo, 22, 22, "📍", size=13)
            x += 28
            if suffix:
                p.text(x, yo, w(suffix), 22, suffix, size=13)
    p.rect(1424, y + 64, 4, 120, fill=MEDIA, stroke=MEDIA, r=2)
    # D · question strip coloured by result + navigation
    p.rect(0, y + 634, DESKTOP_W, 54, fill=SOFT, stroke=LINE, r=0)
    p.zone(14, y + 648, "D")
    p.rect(94, y + 640, 292, 42, fill="#FFFFFF", stroke=LINE, r=8)
    for n in range(1, 11):
        x = 98 + (n - 1) * 28
        if n == 1:
            p.rect(x - 3, y + 646, 30, 30, fill="#FFFFFF", stroke=INK, r=30, sw=2)
        if n == 8:
            p.rect(x, y + 649, 24, 24, fill="#FFFFFF", stroke=DARK, r=24, value=str(n), color=DARK, size=10, bold=True)
        else:
            ok = n >= 9
            p.rect(x, y + 649, 24, 24, fill=PRIMARY if ok else DARK, stroke=PRIMARY if ok else DARK, r=24, value=str(n), color="#FFFFFF", size=10, bold=True)
    p.rect(412, y + 646, 28, 28, fill="#FFFFFF", stroke=LINE, r=28, value="‹", size=16)
    p.rect(446, y + 646, 28, 28, fill="#FFFFFF", stroke=LINE, r=28, value="›", size=16)
    for lx, colour, label in ((520, PRIMARY, "Đúng"), (600, DARK, "Sai")):
        p.rect(lx, y + 655, 10, 10, fill=colour, stroke=colour, r=10)
        p.text(lx + 16, y + 650, 60, 20, label, size=12)
    p.rect(680, y + 654, 10, 10, fill="#FFFFFF", stroke=DARK, r=10)
    p.text(696, y + 650, 80, 20, "Bỏ trống", size=12)
    p.btn(1265, y + 644, 125, 40, "Làm bài khác", "secondary", size=13)


def p43_reading_exam(f):
    # Real-exam Reading runner (Thi thử): no practice tools; section band, passage | questions, part bar + submit.
    h = 804
    p = screen(f, "P-43", "Reading Exam", "Practice", h=h)
    y = navbar(p, role="learner", active="Luyện tập 4 kỹ năng", child="Reading")  # site header (y = 116)
    scroll = "#9CA3AF"
    # A · section band
    p.rect(0, y, DESKTOP_W, 80, fill=SOFT, stroke=LINE, r=0)
    p.zone(14, y + 27, "A")
    p.text(52, y + 14, 400, 26, "<b>Part 3</b>", size=16)
    p.text(52, y + 42, 700, 24, "Read the text and answer questions 27-40", size=14)
    p.rect(1390, y + 28, 24, 24, fill="#FFFFFF", stroke=DARK, r=24, value="✕", size=12, bold=True)
    # B · passage
    p.zone(8, y + 60, "B")
    p.text(12, y + 92, 670, 34, "<b>The rise and fall of the Gary Plan</b>", size=22, align="center")
    p.text(12, y + 130, 670, 40, "Within a decade of its birth in an Indiana steel town, William Wirt's platoon school had admirers across America and enemies on the streets of New York.", size=12, italic=True, align="center")
    for top, n in ((196, 6), (356, 4), (468, 5)):
        p.lines(24, y + top, 650, n, gap=24)
    p.rect(716, y + 90, 2, 536, fill=scroll, stroke=scroll, r=0)
    p.rect(699, y + 90, 18, 130, fill=scroll, stroke=scroll, r=0)
    p.rect(696, y + 330, 40, 34, fill="#FFFFFF", stroke=DARK, r=4, value="↔", size=16, bold=True)
    # C · questions
    p.zone(736, y + 60, "C")
    p.text(744, y + 94, 400, 24, "<b>Questions 27–30</b>", size=15)
    p.text(744, y + 124, 600, 24, "Choose the correct letter, <b>A</b>, <b>B</b>, <b>C</b> or <b>D</b>.", size=14)
    questions = ((27, 158, "What is the writer's main aim in the first paragraph?",
                  ("to question a promise that keeps being made", "to explain how the Gary Plan spread so widely",
                   "to take one side in a long political battle", "to warn that saving money can harm children's education"), 220),
                 (28, 383, "Why does the writer quote Randolph Bourne in the fourth paragraph?",
                  ("to confirm the schools' success using an outsider's view", "to show that the praise was mainly for the buildings",
                   "to suggest that the schools' fame went beyond the evidence"), 439))
    for number, top, statement, options, first in questions:
        p.text(744, y + top, 30, 24, f"<b>{number}</b>", size=15)
        p.text(780, y + top, 640, 24, statement, size=14)
        for i, label in enumerate(options):
            cy = y + first + i * 44
            p.rect(752, cy - 8, 16, 16, fill="#FFFFFF", stroke=DARK, r=16)
            p.text(784, cy - 12, 620, 24, label, size=14)
    p.rect(1412, y + 95, 15, 77, fill=scroll, stroke=scroll, r=0)
    # D · previous / next
    p.zone(1286, y + 518, "D")
    p.rect(1319, y + 504, 54, 54, fill=DARK, stroke=DARK, r=6, value="←", color="#FFFFFF", size=24)
    p.rect(1380, y + 504, 54, 54, fill=PRIMARY, stroke=PRIMARY, r=6, value="→", color="#FFFFFF", size=24)
    # E · part bar + submit
    p.rect(0, y + 634, DESKTOP_W, 54, fill=SOFT, stroke=LINE, r=0)
    p.zone(14, y + 648, "E")
    p.text(46, y + 648, 60, 26, "<b>Part 3</b>", size=13)
    for i in range(14):
        p.rect(108 + i * 28.5, y + 636, 24, 4, fill=MEDIA, stroke=MEDIA, r=2)
        p.text(106 + i * 28.5, y + 646, 28, 30, str(27 + i), size=13, align="center")
    p.rect(1389, y + 634, 51, 54, fill=MEDIA, stroke=LINE, r=0, value="✓", size=22, bold=True)


def writing_screen(f, frame):
    # Writing runner: task + chart + guide | essay sections | dictionary, under the site header (no footer).
    h = 804
    p = screen(f, "P-43", frame, "Practice", h=h)
    y = navbar(p, role="learner", active="Luyện tập 4 kỹ năng", child="Writing")  # site header (y = 116)
    # A · top bar
    p.rect(0, y, DESKTOP_W, 48, fill=SOFT, stroke=LINE, r=0)
    p.zone(14, y + 11, "A")
    p.rect(66, y + 12, 24, 24, fill="#FFFFFF", stroke=DARK, r=24, value="✕", size=12, bold=True)
    p.rect(1311, y + 7, 107, 34, fill="#FFFFFF", stroke=LINE, r=34, value="⚙ Cài đặt", size=13, bold=True)
    # B · task, chart and writing guide
    p.card(8, y + 60, 496, 616, r=14)
    p.zone(20, y + 47, "B")
    p.rect(20, y + 80, 472, 60, fill="#FFFFFF", stroke=DARK, r=4)
    p.text(28, y + 82, 456, 56, "The graph below shows the percentage of households owning four types of electronic devices between 1995 and 2015. Summarize the information by selecting and reporting the main features and make comparisons where relevant.", size=11, italic=True)
    p.img(20, y + 156, 472, 290, "Line graph · MP3 Player / Mobile / Computer / Tablet, 1995–2015")
    p.text(20, y + 462, 472, 24, "<b>HƯỚNG DẪN VIẾT BÀI</b>", size=15, align="center")
    p.text(20, y + 486, 472, 18, "IELTS Writing Task 1 - Percentage of households owning four types of electronic devices: 1995 - 2015", size=10, color=MUTED, italic=True, align="center")
    p.text(28, y + 516, 300, 20, "<b>1. Giải thích đề</b>", size=12, color=PRIMARY)
    p.text(38, y + 540, 300, 18, "<u>Giới thiệu dạng Line Graphs</u>", size=11, color=PRIMARY)
    p.text(38, y + 562, 440, 46, "Đề bài Percentage of households owning four types of electronic devices: 1995 - 2015 yêu cầu mô tả tỷ lệ phần trăm hộ gia đình sở hữu 4 loại thiết bị điện tử (MP3 Player, Mobile phone, Computer, Tablet) trong giai đoạn từ 1995 đến 2015.", size=10, valign="top")
    p.lines(38, y + 634, 440, 2, gap=16)
    p.rect(496, y + 72, 4, 110, fill=MEDIA, stroke=MEDIA, r=2)
    # C · essay sections
    p.card(513, y + 60, 604, 616, r=14)
    p.rect(514, y + 61, 602, 44, fill=SOFT, stroke=SOFT, r=0)
    p.zone(500, y + 47, "C")
    p.text(527, y + 72, 160, 22, "<b>Bài Sample từ YouPass</b>", size=12)
    p.rect(691, y + 75, 34, 16, fill=MEDIA, stroke=LINE, r=16)
    p.rect(693, y + 77, 12, 12, fill=DARK, stroke=DARK, r=12)
    p.text(960, y + 72, 143, 22, "Word count: 0", size=12, align="right")
    for label, ly, by, bh in (("Introduction", 103, 125, 39), ("Overview", 178, 201, 50), ("Body 1", 265, 288, 62), ("Body 2", 364, 386, 62)):
        p.text(527, y + ly, 300, 18, f"<b>{label}</b>", size=12)
        p.rect(527, y + by, 576, bh, fill="#FFFFFF", stroke=LINE, r=6, value="Nhập phần viết của bạn ở đây", color=MUTED, size=10, align="left", valign="top")
    p.text(527, y + 640, 200, 22, "Thời gian: --:--", size=11, color=MUTED)
    p.btn(905, y + 634, 100, 32, "Lưu nháp", "secondary", size=12)
    p.btn(1013, y + 634, 90, 32, "Nộp bài", "disabled", size=12)
    p.rect(506, y + 370, 6, 20, fill=MEDIA, stroke=MEDIA, r=3)
    p.rect(1119, y + 370, 6, 20, fill=MEDIA, stroke=MEDIA, r=3)
    # D · dictionary
    p.card(1126, y + 60, 306, 616, r=14)
    p.rect(1127, y + 61, 304, 44, fill=SOFT, stroke=SOFT, r=0)
    p.zone(1113, y + 47, "D")
    p.text(1142, y + 72, 220, 22, "🦉 <b>Tra từ vựng</b> <font color='#123AB5'>●</font>", size=12)
    p.rect(1134, y + 590, 290, 78, fill="#FFFFFF", stroke=LINE, r=8)
    p.rect(1134, y + 590, 145, 26, fill="#FFFFFF", stroke=LINE, r=8, value="Tra Việt-Anh", size=10, bold=True)
    p.rect(1279, y + 590, 145, 26, fill=SOFT, stroke=LINE, r=8, value="Tra Anh-Việt", size=10)
    p.text(1146, y + 626, 270, 18, "Nhập cụm Tiếng Việt cần tra", size=10, color=MUTED)
    p.text(1146, y + 648, 100, 18, "0/50 ký tự", size=10, color=MUTED)
    p.btn(1318, y + 644, 100, 22, "Tra từ vựng", "disabled", size=10)
    return p


def p43_writing(f):
    writing_screen(f, "Writing")


GUIDED_STEPS_DONE = (
    ("<b>1 · Introduction</b> — Paraphrase đề bài", "The line graph illustrates the fruit production, measured in millions of tonnes, in four different countries (Spain, Turkey, France, and Germany) over a 40-year period from 1970 to 2010."),
    ("<b>2 · Overview</b> — Nhận xét chung", "Overall, while Turkey and France showed a general increase in fruit production, Spain and Germany experienced a decline, particularly in the latter part of the period."),
    ("<b>3 · Body 1</b> — Câu chủ đề", "Throughout the entire period, Spain maintained its position as the leading fruit producer among the four nations."),
    ("<b>4 · Body 1</b> — Tả trend Spain (1970–2010)", "Spain's production fell gradually from about 14 million tonnes in 1970 to 9 million tonnes in 2010."),
    ("<b>5 · Body 2</b> — Câu chủ đề", "Turning to the other countries, Turkey and France showed a pattern that contrasted with Germany."),
    ("<b>6 · Body 2</b> — Tả trend Turkey & France", "Turkey's output rose steadily to about 12 million tonnes, while France's reached about 8 million tonnes by 2010."),
)


def writing_guided_screen(f, frame, complete=False):
    # Step-by-step Writing: task + chart | sentence-level stepper (done / current / locked) | hint panel + dictionary.
    h = 804
    p = screen(f, "P-43", frame, "Practice", h=h)
    y = navbar(p, role="learner", active="Luyện tập 4 kỹ năng", child="Writing")  # site header (y = 116)
    # A · top bar with step progress
    p.rect(0, y, DESKTOP_W, 48, fill=SOFT, stroke=LINE, r=0)
    p.zone(14, y + 11, "A")
    p.rect(66, y + 12, 24, 24, fill="#FFFFFF", stroke=DARK, r=24, value="✕", size=12, bold=True)
    p.text(520, y + 6, 400, 20, "<b>Bước 6 / 6</b> · Hoàn thành" if complete else "<b>Bước 3 / 6</b> · Body 1 — Câu chủ đề", size=12, align="center")
    p.progress(520, y + 32, 400, 100 if complete else 33, h=6)
    p.rect(1311, y + 7, 107, 34, fill="#FFFFFF", stroke=LINE, r=34, value="⚙ Cài đặt", size=13, bold=True)
    # B · task + chart
    p.card(8, y + 60, 380, 616, r=14)
    p.zone(20, y + 47, "B")
    p.rect(20, y + 80, 356, 78, fill="#FFFFFF", stroke=DARK, r=4)
    p.text(28, y + 82, 340, 74, "The line graph below shows the fruit production in four countries (Spain, Turkey, France and Germany) between 1970 and 2010. Summarize the information by selecting and reporting the main features and make comparisons where relevant.", size=11, italic=True)
    p.img(20, y + 172, 356, 420, "Line graph · fruit production (million tonnes), 1970–2010")
    p.btn(20, y + 604, 170, 30, "⤢ Phóng to biểu đồ", "secondary", size=12)
    # C · stepper
    p.card(396, y + 60, 640, 616, r=14)
    p.rect(397, y + 61, 638, 44, fill=SOFT, stroke=SOFT, r=0)
    p.zone(383, y + 47, "C")
    p.text(412, y + 72, 300, 22, "<b>✍ Hướng dẫn từng bước</b>", size=12)
    p.text(880, y + 72, 140, 22, "Word count: 187" if complete else "Word count: 74", size=12, align="right")
    if complete:
        p.rect(426, y + 130, 2, 400, fill=LINE, stroke=LINE, r=0)
        for i, (label, content) in enumerate(GUIDED_STEPS_DONE):
            top = 120 + i * 80
            p.rect(417, y + top, 20, 20, fill=PRIMARY, stroke=PRIMARY, r=20, value="✓", color="#FFFFFF", size=11, bold=True)
            p.text(448, y + top - 2, 420, 18, label, size=11, color=MUTED)
            p.text(950, y + top - 2, 70, 18, "✎ Sửa", size=10, color=PRIMARY, align="right")
            p.text(448, y + top + 18, 570, 40, content, size=12, valign="top")
        p.text(412, y + 642, 400, 20, "Đã xong cả 6 bước — sẵn sàng chấm điểm", size=10, color=MUTED, italic=True)
        p.btn(900, y + 636, 120, 30, "Chấm điểm", size=12)
    else:
        p.rect(426, y + 130, 2, 478, fill=LINE, stroke=LINE, r=0)
        done = ((120, "<b>1 · Introduction</b> — Paraphrase đề bài", "The line graph illustrates the fruit production, measured in millions of tonnes, in four different countries (Spain, Turkey, France, and Germany) over a 40-year period from 1970 to 2010."),
                (206, "<b>2 · Overview</b> — Nhận xét chung", "Overall, while Turkey and France showed a general increase in fruit production, Spain and Germany experienced a decline, particularly in the latter part of the period."))
        for top, label, content in done:
            p.rect(417, y + top, 20, 20, fill=PRIMARY, stroke=PRIMARY, r=20, value="✓", color="#FFFFFF", size=11, bold=True)
            p.text(448, y + top - 2, 420, 18, label, size=11, color=MUTED)
            p.text(950, y + top - 2, 70, 18, "✎ Sửa", size=10, color=PRIMARY, align="right")
            p.text(448, y + top + 18, 570, 54, content, size=12, valign="top")
        p.rect(417, y + 292, 20, 20, fill="#FFFFFF", stroke=PRIMARY, r=20, sw=3, value="3", color=PRIMARY, size=11, bold=True)
        p.text(448, y + 290, 500, 18, "<b>3 · Body 1 — Câu chủ đề</b>", size=12, color=PRIMARY)
        p.text(448, y + 312, 570, 20, "Nêu ý chính của đoạn: nước nào dẫn đầu và so sánh với các nước còn lại.", size=11, color=MUTED)
        p.rect(448, y + 338, 570, 104, fill=PRIMARY_SOFT, stroke=PRIMARY, r=8, sw=2, value="Throughout the entire period, Spain maintained its position as the leading fruit producer among the four nations", size=12, align="left", valign="top")
        p.text(448, y + 450, 200, 18, "18 từ", size=10, color=MUTED)
        p.btn(838, y + 448, 86, 30, "💡 Gợi ý", "secondary", size=12)
        p.btn(932, y + 448, 86, 30, "Tiếp tục", size=12)
        for top, label in ((506, "4 · Body 1 — Tả trend Spain (1970–2010)"), (552, "5 · Body 2 — Câu chủ đề"), (598, "6 · Body 2 — Tả trend Turkey & France")):
            p.rect(417, y + top, 20, 20, fill=MEDIA, stroke=LINE, r=20, value="🔒", size=9)
            p.text(448, y + top - 2, 520, 22, label, size=12, color=MUTED)
        p.text(412, y + 642, 400, 20, "Hoàn thành các bước để mở “Chấm điểm”", size=10, color=MUTED, italic=True)
        p.btn(900, y + 636, 120, 30, "Chấm điểm", "disabled", size=12)
    # D · hint panel + dictionary
    p.card(1044, y + 60, 388, 616, r=14)
    p.rect(1045, y + 61, 386, 44, fill=SOFT, stroke=SOFT, r=0)
    p.zone(1031, y + 47, "D")
    if complete:
        p.text(1060, y + 72, 300, 22, "<b>💡 Gợi ý</b>", size=12)
        p.text(1060, y + 118, 356, 60, "Bạn đã hoàn thành cả 6 bước. Chấm điểm bây giờ, hoặc quay lại sửa từng câu trước khi chấm.", size=12, valign="top")
    else:
        p.text(1060, y + 72, 300, 22, "<b>💡 Gợi ý · Bước 3</b>", size=12)
        p.text(1060, y + 118, 200, 16, "<b>LÝ THUYẾT</b>", size=10, color=PRIMARY)
        p.text(1060, y + 136, 356, 58, "Câu chủ đề của Body 1 nêu ý chính của đoạn: nhóm số liệu nào được so sánh và xu hướng chung của chúng.", size=12, valign="top")
        p.text(1060, y + 208, 200, 16, "<b>CẤU TRÚC GỢI Ý</b>", size=10, color=PRIMARY)
        p.rect(1060, y + 228, 356, 72, fill=SOFT, stroke=LINE, r=8, value="Throughout the period, [country] [verb] its position as the [highest / lowest] [category] among the [N] [group].", size=11, align="left")
        p.text(1060, y + 316, 200, 16, "<b>TỪ VỰNG GỢI Ý</b>", size=10, color=PRIMARY)
        for cx, cy, cw, label in ((1060, 338, 138, "maintain its position"), (1204, 338, 112, "leading producer"),
                                  (1060, 370, 112, "remain dominant"), (1178, 370, 66, "peak at"), (1250, 370, 110, "decline sharply"),
                                  (1060, 402, 80, "fluctuate")):
            p.rect(cx, y + cy, cw, 22, fill=PRIMARY_SOFT, stroke=PRIMARY, r=22, value=label, color=PRIMARY, size=10, bold=True)
        p.text(1060, y + 444, 260, 20, "<u>Xem câu mẫu ›</u>", size=12, color=PRIMARY)
    p.rect(1052, y + 590, 372, 78, fill="#FFFFFF", stroke=LINE, r=8)
    p.rect(1052, y + 590, 186, 26, fill="#FFFFFF", stroke=LINE, r=8, value="Tra Việt-Anh", size=10, bold=True)
    p.rect(1238, y + 590, 186, 26, fill=SOFT, stroke=LINE, r=8, value="Tra Anh-Việt", size=10)
    p.text(1064, y + 626, 300, 18, "Nhập cụm Tiếng Việt cần tra", size=10, color=MUTED)
    p.text(1064, y + 648, 100, 18, "0/50 ký tự", size=10, color=MUTED)
    p.btn(1326, y + 644, 90, 22, "Tra từ vựng", "disabled", size=10)
    return p


def p43_writing_guided(f):
    writing_guided_screen(f, "Writing Guided")


GRADE_CONFIRM_WRITING = dict(
    frame="Writing Grade Confirm", balance=30, cost=10, context="Writing Task 1 · Line graph · Viết tự do",
    benefits=("Band tổng và điểm 4 tiêu chí (TA, CC, LR, GRA)", "Bài viết được đánh dấu lỗi ngữ pháp, từ vựng, mạch lạc",
              "Gợi ý sửa và việc nên làm trước"),
    check="Số từ: 187 (tối thiểu 150 ✓)  ·  4/4 phần: Introduction, Overview, Body 1, Body 2 ✓",
)

GRADE_CONFIRM_GUIDED = dict(
    frame="Writing Guided Grade Confirm", balance=30, cost=10, context="Writing Task 1 · Line graph · Hướng dẫn từng bước",
    benefits=("Band tổng và điểm 4 tiêu chí (TA, CC, LR, GRA)", "Bài viết được đánh dấu lỗi và đối chiếu với từng bước",
              "Gợi ý sửa và việc nên làm trước"),
    check="6/6 bước hoàn thành ✓  ·  Số từ: 187 (tối thiểu 150 ✓)  ·  Đã dùng 2 lần Gợi ý",
)


def grade_confirm_dialog(p, cfg):
    # "Spend points to let the AI grade" dialog over the dimmed Writing screen. Sample figures: the balance matches the
    # "30 Points" of the site header; the cost is meant to be configurable.
    p.overlay(DESKTOP_W, 804)
    x, yy, w = 440, 170, 560
    inner = w - 56
    balance, cost = cfg["balance"], cfg["cost"]
    p.card(x, yy, w, 520, r=18)
    p.zone(x - 13, yy + 20, "A")
    p.text(x + 28, yy + 22, w - 100, 30, "<b>✨ Chấm bài bằng AI</b>", size=20)
    p.rect(x + w - 52, yy + 24, 26, 26, fill="#FFFFFF", stroke=DARK, r=26, value="×", size=16, bold=True)
    p.text(x + 28, yy + 62, inner, 40, "AI chấm theo 4 tiêu chí IELTS Writing và trả về Band, lỗi cần sửa và gợi ý cải thiện.", size=13, color=MUTED, valign="top")
    p.text(x + 28, yy + 106, inner, 20, f"<b>{cfg['context']}</b>", size=12, color=PRIMARY)
    p.zone(x - 13, yy + 146, "B")
    p.rect(x + 28, yy + 138, inner, 96, fill=PRIMARY_SOFT, stroke=PRIMARY, r=14)
    col = inner // 3
    for i, (label, value, strong) in enumerate((("Chi phí chấm", f"−{cost} point", True), ("Số dư hiện tại", f"{balance} point", False),
                                                ("Số dư sau khi chấm", f"{balance - cost} point", True))):
        cx = x + 28 + i * col
        p.text(cx + 16, yy + 154, col - 24, 16, label, size=11, color=MUTED)
        p.text(cx + 16, yy + 174, col - 24, 36, f"<b>{value}</b>", size=22 if strong else 20, color=PRIMARY if strong else INK)
        if i:
            p.rect(cx, yy + 154, 1, 62, fill=LINE, stroke=LINE, r=0)
    p.text(x + 28, yy + 252, inner, 20, "<b>Bạn sẽ nhận được</b>", size=13)
    for i, line in enumerate(cfg["benefits"]):
        p.text(x + 28, yy + 278 + i * 24, inner, 22, f"✓ {line}", size=12)
    p.rect(x + 28, yy + 362, inner, 54, fill=SOFT, stroke=LINE, r=10, value=cfg["check"], size=12, align="left")
    p.zone(x - 13, yy + 444, "C")
    p.btn(x + 28, yy + 436, 200, 44, "Quay lại chỉnh sửa", "secondary", size=13)
    p.btn(x + w - 28 - 262, yy + 436, 262, 44, f"Chấm bài · {cost} point", size=14)
    p.text(x + 28, yy + 490, inner, 18, "Bài sẽ được khóa sau khi chấm. Nếu AI gặp lỗi, point sẽ được hoàn lại.", size=11, color=MUTED, italic=True, align="center")


def p43_writing_grade_confirm(f):
    cfg = GRADE_CONFIRM_WRITING
    grade_confirm_dialog(writing_screen(f, cfg["frame"]), cfg)


def p43_writing_guided_grade_confirm(f):
    cfg = GRADE_CONFIRM_GUIDED
    grade_confirm_dialog(writing_guided_screen(f, cfg["frame"], complete=True), cfg)


NOT_ENOUGH_WRITING = dict(
    frame="Writing Not Enough Points", balance=0, cost=10,
    # point cards of the Key Activation dialog (P-10c): (card, points)
    cards=(("Thẻ Point 50", 50), ("Thẻ Point 100", 100)),
)


def not_enough_points_dialog(p, cfg):
    # The balance is under the cost of an AI grading: explain the gap and offer "Nạp Key" (points are added by activating a key,
    # as in P-10c); the essay is kept. Sample figures; Writing Guided uses the same popup.
    p.overlay(DESKTOP_W, 804)
    x, yy, w = 440, 170, 560
    inner = w - 56
    balance, cost = cfg["balance"], cfg["cost"]
    p.card(x, yy, w, 500, r=18)
    p.zone(x - 13, yy + 20, "A")
    p.text(x + 28, yy + 22, w - 100, 30, "<b>⚠ Bạn chưa đủ point để chấm bài</b>", size=20)
    p.rect(x + w - 52, yy + 24, 26, 26, fill="#FFFFFF", stroke=DARK, r=26, value="×", size=16, bold=True)
    p.text(x + 28, yy + 62, inner, 40, f"Chấm bài bằng AI cần {cost} point. Hãy nạp thêm point để tiếp tục — bài viết của bạn vẫn được giữ nguyên.", size=13, color=MUTED, valign="top")
    p.zone(x - 13, yy + 146, "B")
    p.rect(x + 28, yy + 118, inner, 96, fill=SOFT, stroke=DARK, r=14, sw=2)
    col = inner // 3
    for i, (label, value) in enumerate((("Chi phí chấm", f"{cost} point"), ("Số dư hiện tại", f"{balance} point"),
                                        ("Còn thiếu", f"{cost - balance} point"))):
        cx = x + 28 + i * col
        p.text(cx + 16, yy + 134, col - 24, 16, label, size=11, color=MUTED)
        if i == 2:
            p.rect(cx + 12, yy + 160, col - 28, 36, fill=DARK, stroke=DARK, r=8, value=f"<b>{value}</b>", color="#FFFFFF", size=20)
        else:
            p.text(cx + 16, yy + 156, col - 24, 44, f"<b>{value}</b>", size=22)
        if i:
            p.rect(cx, yy + 134, 1, 66, fill=LINE, stroke=LINE, r=0)
    p.zone(x - 13, yy + 244, "C")
    p.text(x + 28, yy + 238, inner, 22, "<b>🔑 Nạp point bằng Activation Key</b>", size=14)
    p.text(x + 28, yy + 262, inner, 18, "Nhập mã Activation Key được cấp để cộng point vào tài khoản.", size=12, color=MUTED)
    for i, (name, pts) in enumerate(cfg["cards"]):
        cy = yy + 292 + i * 52
        p.rect(x + 28, cy, inner, 44, fill="#FFFFFF", stroke=LINE, r=10)
        p.text(x + 44, cy, 230, 44, f"<b>{name}</b> · +{pts} Points", size=13)
        p.text(x + 280, cy, inner - 268, 44, f"đủ <b>{pts // cost}</b> lần chấm", size=13, color=PRIMARY, align="right")
    p.zone(x - 13, yy + 412, "D")
    p.btn(x + 28, yy + 404, 200, 44, "Quay lại chỉnh sửa", "secondary", size=13)
    p.btn(x + w - 28 - 262, yy + 404, 262, 44, "🔑 Nạp Key", size=14)
    p.text(x + 28, yy + 458, inner, 18, "Chưa có key? <u>Tư vấn miễn phí</u> để được hỗ trợ.", size=11, color=MUTED, align="center")


def p43_writing_not_enough_points(f):
    cfg = NOT_ENOUGH_WRITING
    p = writing_screen(f, cfg["frame"])
    for c in p.vertices():                      # the site header shows the real balance
        if c["value"] == "◯ Học viên · 30 Points ▾":
            c["value"] = f"◯ Học viên · {cfg['balance']} Points ▾"
    not_enough_points_dialog(p, cfg)


def p43_writing_mode_select(f):
    # Writing mode dialog (free writing / step-by-step guide) over the dimmed Writing catalog.
    h = 800
    p = screen(f, "P-43", "Writing Mode Select", "Practice", h=h)
    y = navbar(p, role="learner", active="Luyện tập 4 kỹ năng", child="Writing")  # site header (y = 116)
    # dimmed catalog: sidebar with Writing expanded + two-column list of tasks
    p.card(40, y + 24, 260, 640, r=16)
    p.text(64, y + 44, 220, 50, "<b>LUYỆN ĐỀ</b><br><font style='font-size:12px' color='#6B7280'>The IELTS Space</font>", size=18, valign="top")
    p.text(70, y + 110, 200, 30, "📖 Reading ˅", size=14)
    p.text(70, y + 154, 200, 30, "🎧 Listening ˅", size=14)
    p.rect(60, y + 198, 220, 42, fill=PRIMARY, stroke=PRIMARY, r=10, value="✎ Writing ˄", color="#FFFFFF", size=14, bold=True, align="left")
    for i, t in enumerate(("◉ Bài lẻ", "   ◉ Task 1", "   ○ Task 2", "○ Full đề")):
        p.text(84, y + 248 + i * 28, 190, 24, t, size=13, color=PRIMARY if i == 1 else INK)
    p.text(70, y + 386, 200, 30, "🎤 Speaking ˅", size=14)
    titles = ("Rain-shadow Desert Formation", "Going to the cinema", "Sports Watching vs. Participating",
              "Jobs in four sectors of the economy", "Layout Changes of a College Café", "Fruit production in four countries")
    for i, title in enumerate(titles):
        cx, cy = 330 + (i % 2) * 535, y + 24 + (i // 2) * 200
        p.card(cx, cy, 515, 180, r=14)
        p.img(cx + 12, cy + 12, 140, 156, ("Table", "Process", "Line graph")[i // 2])
        p.text(cx + 168, cy + 20, 330, 40, f"<b>{title}</b>", size=14, color=PRIMARY)
        p.lines(cx + 168, cy + 80, 320, 3, gap=20)
    p.overlay(DESKTOP_W, h)
    # dialog
    x, yy, w = 370, 150, 700
    p.card(x, yy, w, 536, r=18)
    p.zone(x - 13, yy + 20, "A")
    p.text(x + 24, yy + 12, w - 100, 32, "<b>[C21T3] - Rain-shadow Desert Formation</b>", size=18)
    p.rect(x + w - 48, yy + 16, 26, 26, fill="#FFFFFF", stroke=DARK, r=26, value="✕", size=12, bold=True)
    p.rect(x, yy + 56, w, 1, fill=LINE, stroke=LINE, r=0)
    p.text(x + 24, yy + 70, 400, 30, "<b>Chọn chế độ làm bài</b>", size=17)
    p.rect(x, yy + 111, w, 1, fill=LINE, stroke=LINE, r=0)
    p.rect(x + 1, yy + 112, w - 2, 331, fill=CANVAS, stroke=CANVAS, r=0)
    p.zone(x - 13, yy + 140, "B")
    # free writing
    cx, cy = x + 21, yy + 132
    p.rect(cx, cy, 316, 291, fill="#FFFFFF", stroke=LINE, r=12)
    p.img(cx + 20, cy + 21, 276, 159, "Preview: viết tự do")
    p.text(cx + 20, cy + 200, 276, 28, "<b>Viết tự do</b>", size=16, align="center")
    p.text(cx + 20, cy + 232, 276, 44, "Tự viết cả bài với hướng dẫn dạng văn bản, đếm từ, bấm giờ. Viết xong bấm Chấm điểm", size=12, color=MUTED, align="center", valign="top")
    # step-by-step guide (selected)
    cx = x + 358
    p.rect(cx, cy, 321, 291, fill=PRIMARY_SOFT, stroke=PRIMARY, r=12, sw=3)
    p.img(cx + 20, cy + 21, 281, 159, "Preview: hướng dẫn từng bước")
    p.text(cx + 20, cy + 200, 281, 28, "<b>Hướng dẫn từng bước</b>", size=16, align="center")
    p.text(cx + 20, cy + 232, 281, 44, "Chưa viết được cả bài? IELTS Space hướng dẫn bạn viết từng câu, từ lý thuyết đến gợi ý", size=12, align="center", valign="top")
    # start
    p.rect(x, yy + 443, w, 1, fill=LINE, stroke=LINE, r=0)
    p.zone(x - 13, yy + 466, "C")
    p.rect(x + w / 2 - 76, yy + 466, 152, 48, fill=PRIMARY, stroke=PRIMARY, r=48, value="Bắt đầu làm bài", color="#FFFFFF", bold=True, size=15)


def p44(f):
    h = 940
    p = screen(f, "P-44", "Populated", "Writing Practice", h=h)
    y = navbar(p, role="learner", active="Luyện tập 4 kỹ năng", child="Writing")
    p.zone(14, y + 18, "A")
    p.rect(0, y, DESKTOP_W, 72, fill="#FFFFFF", stroke=LINE, r=0)
    p.rect(40, y + 16, 110, 40, fill="#FFFFFF", stroke=DARK, r=20, value="← Thoát", size=14, bold=True)
    p.text(420, y + 20, 600, 32, "[Writing]  <b>Transport use in a European city</b>", size=16)
    p.text(1340, y + 20, 40, 32, "✎", size=20)
    y += 72
    p.zone(14, y + 24, "B")
    p.card(40, y + 24, 640, 640, r=14)
    p.text(60, y + 40, 300, 18, "WRITING PROMPT", size=11, color=PRIMARY, bold=True)
    p.text(60, y + 62, 600, 30, "<b>Transport use in a European city</b>", size=20)
    p.lines(60, y + 106, 600, 3, gap=22)
    p.text(60, y + 180, 300, 18, "TASK VISUAL", size=11, color=PRIMARY, bold=True)
    p.img(60, y + 206, 600, 300, "Bar chart (SVG) · legend Car / Bus / Bicycle …")
    p.btn(60, y + 524, 220, 44, "⤢ Phóng to biểu đồ", "secondary", size=13)
    p.zone(684, y + 24, "C")
    p.card(710, y + 24, 690, 640, r=14)
    p.text(730, y + 40, 300, 18, "YOUR RESPONSE", size=11, color=PRIMARY, bold=True)
    p.text(730, y + 62, 400, 30, "<b>Write your answer</b>", size=20)
    p.rect(1220, y + 50, 160, 40, fill=PRIMARY_SOFT, stroke=PRIMARY_SOFT, r=20, value="⏱ đếm ngược", color=PRIMARY, size=15, bold=True)
    p.rect(730, y + 110, 650, 440, fill="#FFFFFF", stroke=DARK, r=10, value="Start writing your response here…", color=MUTED, size=14, align="left", valign="top")
    p.text(730, y + 566, 460, 40, "Mục tiêu: ít nhất 150 từ. Bài viết chỉ được giữ trong phiên hiện tại.", size=13, color=MUTED)
    p.text(1200, y + 566, 180, 30, "<b>0</b> / 150 từ", size=14, align="right")
    footer(p, h - 64)


def p44a(f):
    h = 940
    p = screen(f, "P-44a", "Populated", "Writing Chart Zoom", h=h)
    navbar(p, role="learner", active="Luyện tập 4 kỹ năng", child="Writing")
    p.overlay(DESKTOP_W, h)
    p.card(220, 130, 1000, 660, r=18)
    p.zone(207, 150, "A")
    p.text(250, 150, 800, 30, "<b>Transport use in a European city</b>", size=20)
    p.text(1170, 150, 30, 30, "✕", size=18, color=MUTED, align="center")
    p.img(250, 200, 940, 540, "Enlarged bar chart (is-large)")
    p.zone(207, 200, "B")


def build(new):
    f = new("P-41_PracticeCatalog"); p41(f); f.save()
    f = new("P-41a_PracticeModeSelect"); p41a(f); f.save()
    f = new("P-42_ReadingPracticeTest"); p42(f); f.save()
    f = new("P-42a_CreateFlashcard"); p42a(f); f.save()
    f = new("P-42b_DictionaryLookup"); p42b(f); f.save()
    f = new("P-42c_SavedFlashcards"); p42c(f); f.save()
    f = new("P-42d_FloatingNotes"); p42d(f); f.save()
    f = new("P-43_ListeningPractice"); p43_catalog(f); p43_mode_select(f); p43_reading(f); p43_reading_exam(f); p43_reading_result(f); p43_reading_result_high(f); p43_reading_explanation(f); p43(f); p43_listening_exam(f); p43_listening_result(f); p43_listening_result_top(f); p43_listening_explanation(f); p43_writing_mode_select(f); p43_writing(f); p43_writing_grade_confirm(f); p43_writing_not_enough_points(f); p43_writing_guided(f); p43_writing_guided_grade_confirm(f); p43_writing_result(f); f.save()
    f = new("P-44_WritingPractice"); p44(f); screens_exam_account.writing_three_columns(f); f.save()
    f = new("P-44a_WritingChartZoom"); p44a(f); f.save()
