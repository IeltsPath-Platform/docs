"""Wireframes (design target): personal flashcard sets — My Flashcards (P-51), Create Set (P-51a), Set Detail (P-51b) —
and the study modes of Set Study (P-59a): Flashcard, Dịch từ, Nối từ, Game.

A "học phần" is a flashcard deck of library-service (decks + flashcards, API-104…116). Layout follows the reference
screens of a flashcard app, restyled with the IELTS Space chrome (Sổ ghi nhớ › Flashcard của tôi). The flashcard is
the two-mode F045 card of screens_vocab_lesson.
"""
from wf import PRIMARY, PRIMARY_SOFT, INK, MUTED, LINE, SOFT, CANVAS, DARK, MEDIA
from chrome import navbar, footer, screen, DESKTOP_W

X0, CW = 100, 1240
WHITE = "#FFFFFF"
ORANGE = "#F97316"
GREEN, RED = "#16A34A", "#DC2626"
SETS = [("Environment – IELTS 6.0", 24, "Bạn", 62, "Hôm nay"), ("Bài 1: Nature &amp; Environment", 5, "Từ bài học · Buổi 1", 20, "Hôm qua"),
        ("Collocations Writing Task 2", 40, "Bạn", 35, "3 ngày trước"), ("Phrasal verbs thông dụng", 30, "Ms. Lan", 0, "Tuần trước"),
        ("Academic Word List – Sublist 1", 60, "IELTS Space", 12, "Tuần trước"), ("Speaking Part 1 – Hometown", 18, "Bạn", 100, "Tháng trước")]
TERMS = [("renewable energy", "năng lượng tái tạo"), ("reduce emissions", "giảm khí thải"), ("carbon footprint", "dấu chân carbon"),
         ("sustainable development", "phát triển bền vững"), ("protect wildlife", "bảo vệ động vật hoang dã")]


def sets_page(f, pid, frame, title, h):
    p = screen(f, pid, frame, title, h=h)
    y = navbar(p, role="learner", active="Sổ ghi nhớ", child="Flashcard của tôi") + 24
    return p, y


def crumb(p, y, *parts):
    trail = "  /  ".join(list(parts[:-1]) + [f"<b><font color='#123AB5'>{parts[-1]}</font></b>"])
    p.text(X0, y, 800, 24, f"‹   {trail}", size=13, color=MUTED)
    return y + 36


# ------------------------------------------------------------------ P-51 My Flashcards
def p51(f):
    h = 1000
    p, y = sets_page(f, "P-51", "Danh sách học phần", "My Flashcards", h)
    p.zone(X0 - 36, y, "A")
    p.text(X0, y, 600, 40, "<b>Flashcard của tôi</b>", size=30)
    p.text(X0, y + 42, 700, 22, "Các học phần bạn tạo, lưu từ bài học hoặc từ điển. Bấm một học phần để xem thẻ và bắt đầu học.",
           size=14, color=MUTED)
    p.rect(X0 + CW - 230, y + 4, 230, 46, fill=PRIMARY, stroke=PRIMARY, r=23, value="<b>+ Tạo học phần mới</b>", size=14, color=WHITE)
    y += 84
    p.rect(X0, y, 420, 42, fill=WHITE, stroke=LINE, r=21, value="⌕  Tìm học phần…", size=13, color=MUTED, align="left")
    x = X0 + 440
    for i, t in enumerate(("Tất cả (6)", "Của tôi (3)", "Từ bài học (1)", "Đã lưu (2)")):
        x = p.chip(x, y + 9, t, kind="solid" if i == 0 else "neutral", size=12)
    p.text(X0 + CW - 200, y, 200, 42, "Sắp xếp: Gần đây ▾", size=13, color=MUTED, align="right")
    y += 66
    p.zone(X0 - 36, y, "B")
    cw = (CW - 32) / 3
    for i, (name, n, owner, pct, when) in enumerate(SETS):
        cx, cy = X0 + (i % 3) * (cw + 16), y + (i // 3) * 236
        p.card(cx, cy, cw, 220, r=16)
        p.rect(cx + 20, cy + 20, 64, 22, fill=PRIMARY_SOFT, stroke="none", r=11, value=f"<b>{n} thẻ</b>", size=11, color=PRIMARY)
        p.text(cx + cw - 140, cy + 20, 120, 22, when, size=11, color=MUTED, align="right")
        p.text(cx + 20, cy + 54, cw - 40, 48, f"<b>{name}</b>", size=17, valign="top")
        p.cell(owner[0], "ellipse;whiteSpace=wrap;html=1;fillColor=#E8EDFB;strokeColor=#123AB5;fontColor=#123AB5;fontSize=11;",
               cx + 20, cy + 108, 26, 26)
        p.text(cx + 54, cy + 108, cw - 80, 26, owner, size=12, color=MUTED)
        p.text(cx + 20, cy + 146, 160, 20, "Đã thuộc" if pct == 100 else f"Đã thuộc {pct}%", size=11, color=MUTED)
        p.progress(cx + 20, cy + 170, cw - 160, pct)
        p.btn(cx + cw - 120, cy + 160, 100, 36, "▶ Học", size=12)
    footer(p, h - 64)
    return p


# ------------------------------------------------------------------ P-51a Create Set
def p51a(f):
    h = 1160
    p, y = sets_page(f, "P-51a", "Tạo học phần", "Create Set", h)
    y = crumb(p, y, "Flashcard của tôi", "Tạo học phần mới")
    mw = 860
    p.zone(X0 - 36, y, "A")
    p.text(X0, y, 500, 40, "<b>Tạo một học phần mới</b>", size=26)
    p.rect(X0 + mw - 290, y + 2, 90, 40, fill=PRIMARY_SOFT, stroke="none", r=20, value="<b>Tạo</b>", size=13, color=PRIMARY)
    p.rect(X0 + mw - 190, y + 2, 190, 40, fill=PRIMARY, stroke=PRIMARY, r=20, value="<b>Tạo và ôn luyện</b>", size=13, color=WHITE)
    p.rect(X0, y + 52, 120, 30, fill=SOFT, stroke="none", r=15, value="🌐 Công khai ▾", size=12)
    y += 100
    p.rect(X0, y, mw, 50, fill=SOFT, stroke="none", r=10, value="<b>Tiêu đề</b>", size=14, color=MUTED, align="left")
    p.rect(X0, y + 58, mw, 56, fill=SOFT, stroke="none", r=10, value="Thêm mô tả…", size=13, color=MUTED, align="left", valign="top")
    y += 140
    p.zone(X0 - 36, y, "B")
    p.rect(X0, y, 90, 36, fill=SOFT, stroke="none", r=18, value="+ Nhập", size=12)
    p.rect(X0 + 100, y, 160, 36, fill=SOFT, stroke="none", r=18, value="+ Thêm sơ đồ  🔒", size=12)
    p.text(X0 + mw - 300, y, 60, 36, "Gợi ý", size=13, align="right")
    p.rect(X0 + mw - 230, y + 9, 36, 18, fill=PRIMARY, stroke=PRIMARY, r=9)
    p.cell("", "ellipse;fillColor=#FFFFFF;strokeColor=none;", X0 + mw - 214, y + 11, 14, 14)
    for i, icon in enumerate(("⌕", "⇄", "⌨")):
        p.cell(icon, "ellipse;whiteSpace=wrap;html=1;fillColor=#F3F4F6;strokeColor=none;fontSize=14;fontColor=#6B7280;",
               X0 + mw - 180 + i * 46, y, 36, 36)
    p.cell("🗑", "ellipse;whiteSpace=wrap;html=1;fillColor=#B91C1C;strokeColor=none;fontSize=14;", X0 + mw - 40, y, 36, 36)
    y += 56
    p.zone(X0 - 36, y, "C")
    for i in range(3):
        cy = y + i * 150
        p.card(X0, cy, mw, 136, r=14)
        p.text(X0 + 20, cy + 14, 40, 22, f"<b>{i + 1}</b>", size=14)
        p.text(X0 + mw - 70, cy + 12, 50, 22, "═   🗑", size=13, color=MUTED, align="right")
        for k, (label, x) in enumerate((("THUẬT NGỮ", X0 + 120), ("ĐỊNH NGHĨA", X0 + 120 + (mw - 260) / 2 + 10))):
            fill = TERMS[i][k] if i < 2 else ""
            p.rect(x, cy + 48, (mw - 260) / 2 - 10, 42, fill=SOFT, stroke="none", r=8, value=fill, size=13, align="left")
            p.text(x, cy + 96, 200, 18, label, size=10, color=MUTED, bold=True)
        for x in (X0 + 20, X0 + mw - 96):
            p.rect(x, cy + 44, 76, 54, fill=WHITE, stroke=LINE, r=6, dashed=True, value="▨<br>Hình ảnh", size=10, color=MUTED)
    p.rect(X0 + mw / 2 - 90, y + 460, 180, 40, fill=SOFT, stroke="none", r=20, value="<b>+ Thêm thẻ</b>", size=13)
    sx, sw = X0 + mw + 30, CW - mw - 30
    p.zone(sx - 30, y - 196, "D")
    p.card(sx, y - 196, sw, 640, r=18)
    p.text(sx + sw - 90, y - 180, 70, 30, "◷   ✕", size=15, color=MUTED, align="right")
    p.text(sx + 20, y - 140, 60, 40, "✦", size=30, color=PRIMARY)
    p.text(sx + 20, y - 96, 300, 24, "<b>AI tạo thẻ</b>", size=16)
    for i, (title, body) in enumerate((("Chuyển tệp thành thẻ", "Tải lên PDF, PPT, DOCX hoặc dán ghi chú, AI tạo thẻ trong vài giây."),
                                       ("Kiểm tra lại trước khi thêm", "Xem trước các thẻ đã tạo và chọn thẻ muốn thêm vào học phần."),
                                       ("Gợi ý nghĩa và ví dụ", "Điền sẵn định nghĩa, IPA, ví dụ từ từ điển (API-82) khi bạn gõ thuật ngữ."))):
        ty = y - 60 + i * 84
        p.text(sx + 20, ty, 24, 24, "▤", size=16, color=PRIMARY)
        p.text(sx + 52, ty, sw - 72, 76, f"<b>{title}</b><br><font color='#6B7280'>{body}</font>", size=12, valign="top")
    p.card(sx + 12, y + 260, sw - 24, 170, r=14, fill=SOFT)
    p.text(sx + 28, y + 274, sw - 56, 60, "Nhập câu lệnh, dán ghi chú hoặc tải lên tài liệu.", size=13, color=MUTED, valign="top")
    p.cell("+", "ellipse;whiteSpace=wrap;html=1;fillColor=#E8EDFB;strokeColor=none;fontSize=18;fontColor=#123AB5;", sx + 28, y + 350, 34, 34)
    p.cell("↑", "ellipse;whiteSpace=wrap;html=1;fillColor=#F3F4F6;strokeColor=none;fontSize=14;fontColor=#6B7280;", sx + sw - 62, y + 350, 34, 34)
    p.text(sx, y + 400, sw, 20, "Được AI hỗ trợ ⓘ · có hạn mức theo ngày", size=11, color=MUTED, align="center")
    footer(p, h - 64)
    return p


# ------------------------------------------------------------------ shared study controls (reference: flashcard app)
def study_controls(p, cx, cw, y, idx, total):
    p.rect(cx + cw / 2 - 360, y, 720, 40, fill=PRIMARY_SOFT, stroke="none", r=0, size=12,
           value="⌨ <b>Phím tắt</b>   Nhấn [ phím cách ] hoặc nhấp vào thẻ để lật · ← / → chuyển thẻ")
    y += 56
    p.rect(cx, y, 180, 44, fill=PRIMARY_SOFT, stroke="none", r=22, value="<b>Sắp xếp thẻ ghi nhớ</b>", size=12, color=PRIMARY)
    mid = cx + cw / 2
    p.rect(mid - 170, y, 90, 44, fill=SOFT, stroke="none", r=22, value=f"<font color='{RED}'><b>✕</b></font>", size=18)
    p.text(mid - 70, y, 140, 44, f"<b>{idx} / {total}</b>", size=14, align="center")
    p.rect(mid + 80, y, 90, 44, fill=SOFT, stroke="none", r=22, value=f"<font color='{GREEN}'><b>✓</b></font>", size=18)
    p.text(cx + cw - 220, y, 220, 44, "↶     ⤨     ⚙     ⛶", size=16, color=MUTED, align="right")
    p.rect(cx, y + 58, cw, 4, fill=MEDIA, stroke="none", r=2)
    p.rect(cx, y + 58, cw * idx / total, 4, fill=PRIMARY, stroke="none", r=2)
    return y + 70


def mode_tabs(p, x, y, w, active):
    tw = (w - 32) / 3
    for i, (icon, label, badge) in enumerate((("▭", "Thẻ ghi nhớ", "Mới"), ("◌", "Học", ""), ("▤", "Kiểm tra", ""))):
        on = label == active
        p.rect(x + i * (tw + 16), y, tw, 48, fill=PRIMARY_SOFT if on else SOFT, stroke=PRIMARY if on else "none", r=10,
               value=f"<font color='#123AB5'>{icon}</font>  <b>{label}</b>" + (
                   f"  <font color='#FFFFFF' style='background-color:#38BDF8'>&nbsp;{badge}&nbsp;</font>" if badge else ""),
               size=14)


# ------------------------------------------------------------------ P-51b Set Detail
def p51b(f):
    from screens_vocab_lesson import flashcard
    h = 1500
    p, y = sets_page(f, "P-51b", "Thẻ ghi nhớ", "Set Detail", h)
    y = crumb(p, y, "Flashcard của tôi", "Environment – IELTS 6.0")
    p.zone(X0 - 36, y, "A")
    p.text(X0, y, 700, 40, "<b>Environment – IELTS 6.0</b>", size=28)
    p.text(X0, y + 42, 700, 22, "24 thẻ · Tạo bởi bạn · 🌐 Công khai · Cập nhật hôm nay", size=13, color=MUTED)
    p.btn(X0 + CW - 470, y + 4, 110, 42, "✎ Sửa", kind="secondary", size=13)
    p.btn(X0 + CW - 350, y + 4, 120, 42, "⤴ Chia sẻ", kind="secondary", size=13)
    p.rect(X0 + CW - 220, y + 4, 220, 42, fill=ORANGE, stroke=ORANGE, r=21, value="<b>▶ Bắt đầu học</b>", size=14, color=WHITE)
    y += 84
    cx, cw = X0 + 120, CW - 240
    mode_tabs(p, cx, y, cw, "Thẻ ghi nhớ")
    y += 66
    p.zone(X0 - 36, y, "B")
    p.text(cx + 20, y + 10, 200, 24, "💡 Hiển thị gợi ý", size=12)
    flashcard(p, cx, y + 40, cw, 340, side="front", mode="full", phrase="Renewable energy", ipa="/rɪˈnjuː.ə.bəl ˈen.ə.dʒi/",
              image="Ảnh pin mặt trời, tua-bin gió")
    y = study_controls(p, cx, cw, y + 396, 1, 24)
    y += 30
    p.zone(X0 - 36, y, "C")
    p.text(X0, y, 600, 28, "<b>Thuật ngữ trong học phần này (24)</b>", size=18)
    p.text(X0 + CW - 300, y, 300, 28, "Thứ tự gốc ▾", size=13, color=MUTED, align="right")
    for g, (group, color, rows) in enumerate((("Đang học (3)", ORANGE, TERMS[:3]), ("Đã thuộc (2)", GREEN, TERMS[3:]))):
        y += 44
        p.text(X0, y, 400, 22, f"<b><font color='{color}'>● {group}</font></b>", size=13)
        y += 30
        for term, vi in rows:
            p.card(X0, y, CW, 56, r=10)
            p.text(X0 + 24, y, 380, 56, f"<b>{term}</b>", size=14)
            p.rect(X0 + 420, y + 12, 1, 32, fill=LINE, stroke=LINE, r=0)
            p.text(X0 + 440, y, 560, 56, vi, size=14, color=INK)
            p.text(X0 + CW - 140, y, 120, 56, "☆    🔊    ✎", size=14, color=MUTED, align="right")
            y += 64
    p.rect(X0 + CW / 2 - 110, y + 10, 220, 42, fill=PRIMARY_SOFT, stroke="none", r=21, value="<b>Xem thêm 19 thẻ</b>", size=13, color=PRIMARY)
    footer(p, h - 64)
    return p


# ------------------------------------------------------------------ P-59a study modes
def p59a_flashcard(f):
    from screens_dictionary import study_page
    from screens_vocab_lesson import flashcard
    h = 1000
    p, y = study_page(f, "Flashcard", "Flashcard", h)
    p.zone(X0 - 36, y, "B")
    cx, cw = X0 + 170, 900
    p.text(cx + 20, y + 4, 200, 24, "💡 Hiển thị gợi ý", size=12)
    p.text(cx + cw - 200, y + 4, 180, 24, "Giản lược | <b>Đầy đủ</b>", size=12, align="right")
    flashcard(p, cx, y + 34, cw, 330, side="front", mode="full", phrase="wellbeing", ipa="/ˌwelˈbiː.ɪŋ/",
              meaning="sức khoẻ, hạnh phúc", image="Ảnh gợi nhớ")
    study_controls(p, cx, cw, y + 384, 5, 12)
    p.text(cx, y + 530, cw, 40, "✕ = chưa thuộc (thẻ quay lại cuối lượt) · ✓ = đã thuộc. Mỗi lượt ghi thời gian xem và đáp án "
           "(F045) để cập nhật Mức độ hiểu từ và lịch ôn.", size=12, color=MUTED, italic=True, align="center")
    footer(p, h - 64)
    return p


def p59a_translate(f):
    from screens_dictionary import study_page
    h = 980
    p, y = study_page(f, "Dịch từ", "Dịch từ", h)
    p.zone(X0 - 36, y, "B")
    cx, cw = X0 + 170, 900
    p.card(cx, y, cw, 420, r=20)
    p.chip(cx + 24, y + 22, "Câu 7/12 · Dịch sang tiếng Anh", kind="active", size=12)
    p.text(cx + 24, y + 66, cw - 48, 40, "<b>sức khoẻ tinh thần</b>", size=28)
    p.text(cx + 24, y + 110, cw - 48, 22, "Gợi ý: 2 từ · bắt đầu bằng “m… w…”", size=13, color=MUTED)
    p.rect(cx + 24, y + 150, cw - 48, 56, fill=WHITE, stroke=PRIMARY, r=12, sw=2, value="mental wellbeing", size=18, align="left")
    p.rect(cx + 24, y + 222, cw - 48, 56, fill="#ECFDF5", stroke=GREEN, r=12, align="left", size=13,
           value="✓ <b>Chính xác!</b> mental wellbeing /ˈmen.təl ˌwelˈbiː.ɪŋ/ 🔊")
    p.text(cx + 24, y + 300, 200, 30, "<u>Tôi không biết</u>", size=13, color=PRIMARY)
    p.btn(cx + cw - 200, y + 344, 176, 46, "Câu tiếp ›", size=14)
    footer(p, h - 64)
    return p


def p59a_match(f):
    from screens_dictionary import study_page
    h = 980
    p, y = study_page(f, "Nối từ", "Nối từ", h)
    p.zone(X0 - 36, y, "B")
    cx, cw = X0 + 170, 900
    p.card(cx, y, cw, 470, r=20)
    p.chip(cx + 24, y + 22, "Nối từ với nghĩa · 3/5 cặp", kind="active", size=12)
    words = ("wellbeing", "obesity", "nutrition", "sedentary", "therapy")
    means = ("sự béo phì", "sức khoẻ, hạnh phúc", "liệu pháp", "ít vận động", "dinh dưỡng")
    pairs = {0: 1, 1: 0, 2: 4}
    left, right = [], []
    for i, w in enumerate(words):
        done = i in pairs
        left.append(p.rect(cx + 60, y + 70 + i * 74, 300, 56, fill="#ECFDF5" if done else WHITE, stroke=GREEN if done else LINE,
                           r=12, value=f"<b>{w}</b>", size=15))
    for i, m in enumerate(means):
        done = i in pairs.values()
        sel = i == 3
        right.append(p.rect(cx + cw - 360, y + 70 + i * 74, 300, 56, fill="#ECFDF5" if done else (PRIMARY_SOFT if sel else WHITE),
                            stroke=GREEN if done else (PRIMARY if sel else LINE), r=12, sw=2 if sel else 1, value=m, size=15))
    for a, b in pairs.items():
        p.edge(left[a], right[b], color=GREEN, exit=(1, 0.5), entry=(0, 0.5))
    p.cells = [c.replace("edgeStyle=orthogonalEdgeStyle", "edgeStyle=none") if isinstance(c, str) else c
               for c in p.cells]  # matched pairs read as straight lines
    p.text(cx, y + 448, cw, 20, "Chọn một từ bên trái rồi chọn nghĩa bên phải · nối sai thì ô rung đỏ", size=12, color=MUTED,
           italic=True, align="center")
    footer(p, h - 64)
    return p


def p59a_game(f):
    from screens_dictionary import study_page
    h = 980
    p, y = study_page(f, "Game", "Game", h)
    p.zone(X0 - 36, y, "B")
    cx, cw = X0 + 170, 900
    p.card(cx, y, cw, 500, r=20)
    p.text(cx + 24, y + 18, 400, 30, "<b>Ghép thẻ nhanh</b>", size=20)
    p.text(cx + cw - 300, y + 18, 276, 30, "⏱ <b>00:18.4</b>     ★ Kỷ lục 00:24.1", size=15, align="right")
    tiles = ("wellbeing", "dinh dưỡng", "therapy", "sự béo phì", "nutrition", "ít vận động",
             "obesity", "sức khoẻ, hạnh phúc", "sedentary", "liệu pháp", "", "")
    tw, th = (cw - 48 - 30) / 4, 90
    for i, t in enumerate(tiles):
        tx, ty = cx + 24 + (i % 4) * (tw + 10), y + 70 + (i // 4) * (th + 12)
        if not t:
            p.rect(tx, ty, tw, th, fill=SOFT, stroke=LINE, r=12, dashed=True)
            continue
        sel = i in (0, 7)
        p.rect(tx, ty, tw, th, fill=PRIMARY_SOFT if sel else WHITE, stroke=PRIMARY if sel else LINE, r=12, sw=2 if sel else 1,
               value=f"<b>{t}</b>" if sel else t, size=14, shadow=sel)
    p.text(cx + 24, y + 392, cw - 48, 40, "Chạm 2 ô cùng nghĩa để xoá chúng. Ô ghép đúng biến mất, sai thì cộng 1 giây.",
           size=12, color=MUTED, align="center")
    p.btn(cx + cw / 2 - 90, y + 440, 180, 42, "↻ Chơi lại", kind="secondary", size=13)
    footer(p, h - 64)
    return p


def build(new):
    f = new("P-51_MyFlashcards")
    p51(f)
    f.save()
    f = new("P-51a_CreateSet")
    p51a(f)
    f.save()
    f = new("P-51b_SetDetail")
    p51b(f)
    f.save()
