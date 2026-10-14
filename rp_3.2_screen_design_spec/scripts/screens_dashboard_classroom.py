"""Wireframes: Overview Dashboard (P-11), My Classroom (P-20, P-20a), Lesson Workspace (P-21), Vocabulary (P-50)
and the Writing Feedback frames of the Lesson Player (P-32).

Screens on mock data in the frontend; drawn for the FDS. Copy and sample data come from features/overview,
features/classroom, features/vocabulary, mocks/*.ts and learning-path/components/blocks/EssayBlock.tsx.
"""
from wf import PRIMARY, PRIMARY_SOFT, INK, MUTED, LINE, SOFT, CANVAS, DARK, MEDIA
from chrome import navbar, footer, screen, back_link, eyebrow, consult_fab, DESKTOP_W

X0, CW = 100, 1240
WHITE = "#FFFFFF"


# ------------------------------------------------------------------ Overview (/overview)
OV_X, OV_W = X0, CW
OV_TABS = ["Tổng quát", "Dữ liệu chi tiết", "Lịch sử ôn luyện", "Xếp hạng"]
OV_ICONS = ["▦", "▥", "◷", "♕"]


def overview_page(f, frame, h, active_tab):
    p = screen(f, "P-11", frame, "Overview Dashboard", h=h)
    y = navbar(p, role="learner", active="Trang chủ", child="Dashboard") + 32
    p.zone(268, 80, "A")
    consult_fab(p, DESKTOP_W - 210, h - 70)
    return p, y


def stat_cards(p, y):
    p.text(OV_X, y, 600, 30, "<b>Dữ Liệu Học Tổng Quan</b>", size=22)
    p.text(OV_X, y + 34, 600, 22, "Thống kê hoạt động học tập của bạn", size=14, color=MUTED)
    cards = [("◷", "Tổng thời gian học", "47h 20m", "+2h tuần này"), ("▣", "Số ngày học", "38 ngày", "có hoạt động học tập"),
             ("✓", "Số đề đã luyện", "124 đề", "đã hoàn thành"), ("◎", "Tỷ lệ chính xác", "76%", "trung bình các bài"),
             ("🔥", "Streak học", "28 ngày", "kỷ lục cá nhân")]
    cw = OV_W / 5
    p.card(OV_X, y + 70, OV_W, 150, r=14)
    for i, (icon, label, value, sub) in enumerate(cards):
        cx = OV_X + i * cw
        if i:
            p.rect(cx, y + 70, 1, 150, fill=LINE, stroke=LINE, r=0)
        p.icon(cx + 20, y + 88, icon, size=18, color=PRIMARY)
        p.text(cx + 20, y + 118, cw - 30, 20, label, size=13, color=MUTED)
        p.text(cx + 20, y + 142, cw - 30, 34, f"<b>{value}</b>", size=24)
        p.text(cx + 20, y + 182, cw - 30, 20, sub, size=12, color=PRIMARY if i == 0 else MUTED)
    return y + 240


def activity_calendar(p, y):
    """Month calendar of features/overview/components/OverviewActivityCalendar.tsx (current week from the fixture)."""
    h = 470
    p.zone(OV_X - 36, y, "D")
    p.card(OV_X, y, OV_W, h, r=14)
    p.text(OV_X + 24, y + 18, 600, 28, "<b>Biểu đồ “chăm chỉ” của bạn</b>", size=20)
    p.text(OV_X + 24, y + 48, 600, 20, "Bấm vào ngày/tuần để xem hoạt động học tập.", size=13, color=MUTED)
    p.rect(OV_X + OV_W - 110, y + 24, 14, 14, fill=PRIMARY, stroke=PRIMARY, r=3)
    p.text(OV_X + OV_W - 90, y + 20, 80, 22, "Đã học", size=13, color=MUTED)
    p.text(OV_X + 24, y + 82, 300, 30, "🔥 <b>28 ngày</b> giữ chuỗi", size=15)
    bx = OV_X + OV_W - 260
    p.rect(bx, y + 80, 36, 34, fill=WHITE, stroke=LINE, r=8, value="‹", size=16)
    p.rect(bx + 44, y + 80, 120, 34, fill=WHITE, stroke=LINE, r=8, value="Tháng này", size=13, bold=True)
    p.rect(bx + 172, y + 80, 36, 34, fill=WHITE, stroke=LINE, r=8, value="›", size=16)
    p.text(OV_X, y + 124, OV_W, 22, "<b>Tháng 10 / 2026</b>", size=14, align="center")
    gx, colw, rowh = OV_X + 24, (OV_W - 48) / 8, 46
    for i, day in enumerate(["", "T2", "T3", "T4", "T5", "T6", "T7", "CN"]):
        p.text(gx + i * colw, y + 150, colw, 22, f"<b>{day}</b>", size=13, color=MUTED, align="center")
    # October 2026 starts on Thursday; the fixture marks Mon–Fri of the current week (12–16 Oct) as studied
    day, first_col = 1, 3
    for week in range(5):
        ry = y + 178 + week * rowh
        selected = week == 2
        if selected:
            p.rect(gx, ry, OV_W - 48, rowh - 4, fill=PRIMARY_SOFT, stroke=PRIMARY, r=8)
        p.rect(gx + 6, ry + 6, colw - 12, rowh - 16, fill=WHITE, stroke=PRIMARY if selected else LINE, r=8,
               value=f"Tuần {week + 1}", size=12, color=PRIMARY if selected else INK, bold=selected)
        for col in range(7):
            if (week == 0 and col < first_col) or day > 31:
                continue
            cx = gx + (col + 1) * colw
            studied = 12 <= day <= 16
            today = day == 13
            p.rect(cx + 8, ry + 4, colw - 16, rowh - 12, fill=PRIMARY_SOFT if studied else WHITE,
                   stroke=PRIMARY if today else (PRIMARY_SOFT if studied else "none"), r=8, sw=2 if today else 1,
                   value=f"{day}{' 🔥' if studied else ''}", size=13, bold=today)
            day += 1
    p.rect(OV_X + 24, y + 410, OV_W - 48, 30, fill=SOFT, stroke=LINE, r=8,
           value="<b>Tuần 3 · 12/10/2026 – 18/10/2026</b>   5 ngày đã học / 7 ngày có dữ liệu trong tuần này.",
           size=13, align="left")
    p.text(OV_X + 24, y + h - 26, 600, 20, "Dữ liệu mẫu · Hoạt động minh họa trong tuần hiện tại.", size=12,
           color=MUTED, italic=True)
    return y + h + 24


def learning_orbit(p, y):
    h = 430
    p.zone(OV_X - 36, y, "E")
    p.card(OV_X, y, OV_W, h, r=14)
    p.text(OV_X + 24, y + 18, 500, 28, "<b>My Learning Orbit</b>", size=20)
    p.text(OV_X + 24, y + 48, 500, 20, "Cùng xem “hành tinh” của riêng bạn nhé!", size=13, color=MUTED)
    cx, cy = OV_X + OV_W / 2, y + 250
    st = "ellipse;whiteSpace=wrap;html=1;fillColor=#123AB5;strokeColor=#123AB5;fontColor=#FFFFFF;fontFamily=Arial;fontSize=13;"
    p.cell("BAND HIỆN TẠI<br><b><font style='font-size:30px'>6.5</font></b><br>Mục tiêu: 7.5 IELTS", st,
           cx - 80, cy - 80, 160, 160)
    skills = [("Listening", "5.0", "PRIORITY FOCUS", 70, ["Part 1 · 5/10", "Part 2 · 5/10", "Part 3 · 5/10", "Part 4 · 5/10"]),
              ("Reading", "5.5", "PRIORITY FOCUS", 65, ["Part 1", "Part 2", "Part 3"]),
              ("Writing", "5.5", "IMPROVE", 55, ["Task Achievement/Response", "Coherence & Cohesion", "Lexical Resource",
                                                 "Grammatical Range & Accuracy"]),
              ("Speaking", "5.5", "IMPROVE", 55, ["Fluency & Coherence", "Lexical Resource",
                                                  "Grammatical Range & Accuracy", "Pronunciation"])]
    bw, bh = 330, 160
    spots = [(OV_X + 24, y + 84), (OV_X + OV_W - 24 - bw, y + 84), (OV_X + 24, y + 256), (OV_X + OV_W - 24 - bw, y + 256)]
    for (name, band, tag, pct, parts), (bx, by) in zip(skills, spots):
        p.card(bx, by, bw, bh, r=12)
        p.text(bx + 14, by + 10, 200, 22, f"<b>● {name}</b>", size=15)
        p.text(bx + bw - 90, by + 10, 80, 22, f"<b>{band}</b> band", size=13, align="right")
        p.chip(bx + 14, by + 38, tag, kind="active" if tag == "PRIORITY FOCUS" else "neutral", size=11)
        p.progress(bx + 14, by + 72, bw - 80, pct)
        p.text(bx + bw - 56, by + 64, 44, 22, f"{pct}%", size=12, align="right")
        p.text(bx + 14, by + 88, bw - 28, bh - 92, "<br>".join(parts), size=11, color=MUTED, valign="top")
    return y + h + 24


def study_plan_and_space(p, y):
    h = 420
    lw = 560
    p.zone(OV_X - 36, y, "F")
    p.card(OV_X, y, lw, h, r=14)
    p.text(OV_X + 24, y + 18, 400, 28, "<b>Study Plan</b>", size=20)
    p.text(OV_X + 24, y + 48, 460, 20, "Kế hoạch AI cá nhân hoá – Hôm nay, 25/08", size=13, color=MUTED)
    p.text(OV_X + 24, y + 76, 300, 20, "Hôm nay: <b>Tổng 120 phút</b>", size=13)
    p.text(OV_X + lw - 160, y + 76, 40, 20, "<b>2/5</b>", size=13, color=PRIMARY)
    p.progress(OV_X + lw - 116, y + 82, 90, 40)
    tasks = [("Nghe", "Unit 4 – Listening Practice", 30, True), ("Đọc", "Reading Passage: Education", 20, True),
             ("Từ vựng", "Ôn 24 từ – Space Repetition", 10, False), ("Viết", "Writing Task 2 – Line Graph Essay", 45, False),
             ("Nói", "Speaking Part 2 – Hometown", 15, False)]
    for i, (cat, title, mins, done) in enumerate(tasks):
        ty = y + 110 + i * 50
        p.rect(OV_X + 24, ty, lw - 48, 42, fill=SOFT if done else WHITE, stroke=LINE, r=8)
        p.text(OV_X + 34, ty, 24, 42, "✔" if done else "○", size=16, color=PRIMARY if done else MUTED, align="center")
        p.chip(OV_X + 66, ty + 9, cat, kind="outline", size=11, w=72)
        p.text(OV_X + 148, ty, 300, 42, f"<s>{title}</s>" if done else title, size=13, color=MUTED if done else INK)
        p.text(OV_X + lw - 110, ty, 80, 42, f"{mins} phút", size=12, color=MUTED, align="right")
    p.btn(OV_X + 24, y + h - 62, 240, 42, "Xem tất cả các kế hoạch", kind="secondary", size=13)
    p.btn(OV_X + lw - 224, y + h - 62, 200, 42, "Bắt đầu học ngay", size=13)
    rx, rw = OV_X + lw + 20, OV_W - lw - 20
    p.card(rx, y, rw, h, r=14)
    p.text(rx + 20, y + 18, rw - 40, 28, "<b>SPACE Autonomy</b>", size=20)
    p.text(rx + 20, y + 48, rw - 40, 20, "Thang 0: Dependent ➔ 3: Transfer – Cập nhật cuối module", size=12, color=MUTED)
    st = "ellipse;whiteSpace=wrap;html=1;fillColor=#E8EDFB;strokeColor=#123AB5;strokeWidth=2;fontColor=#123AB5;fontFamily=Arial;fontSize=12;"
    p.cell("LEVEL<br><b><font style='font-size:26px'>2.6</font></b><br>/ 3 Transfer", st, rx + rw / 2 - 60, y + 130, 120, 120)
    nodes = [("S – Scope", "3/3 – Independent", rx + rw / 2 - 70, y + 76), ("P – Probe", "2/3 – Guided", rx + rw - 150, y + 150),
             ("A – Assemble", "3/3 – Independent", rx + rw - 160, y + 262), ("C – Communicate", "3/3 – Independent", rx + 20, y + 262),
             ("E – Evaluate", "2/3 – Guided", rx + 10, y + 150)]
    for title, score, nx, ny in nodes:
        p.rect(nx, ny, 140, 48, fill=WHITE, stroke=LINE, r=8, value=f"<b>{title}</b><br>{score}", size=11)
    p.rect(rx + 16, y + h - 74, rw - 32, 58, fill=PRIMARY_SOFT, stroke=PRIMARY_SOFT, r=8, size=12, align="left",
           value="<b>Đề xuất:</b> P và E đang thấp hơn các bước còn lại – hệ thống ưu tiên nhiệm vụ Probe và Eva-review trong 2 tuần tới.")
    return y + h + 24


def ai_recommendations(p, y):
    h = 260
    p.zone(OV_X - 36, y, "G")
    p.card(OV_X, y, OV_W, h, r=14)
    p.text(OV_X + 24, y + 18, 320, 28, "<b>Gợi Ý Ôn Luyện Từ AI</b>", size=20)
    p.chip(OV_X + 290, y + 22, "Cá nhân hoá theo lộ trình", kind="active", size=11)
    recs = [("🎧", "Ưu tiên cao", "Luyện nghe", "Đề luyện nghe môn trắc nghiệm, chủ đề Lifestyle – ưu tiên cao"),
            ("↻", "Cần ôn hôm nay", "Ôn Flashcard Hôm Nay", "24 từ theo lịch Spaced Repetition cá nhân hoá cần ôn hôm nay"),
            ("✎", "Điểm yếu", "Writing Task 2 Practice", "Essay chủ đề Education – điểm yếu cần cải thiện gấp, hãy tích cực ôn")]
    cw = (OV_W - 48 - 32) / 3
    for i, (icon, badge, title, desc) in enumerate(recs):
        cx = OV_X + 24 + i * (cw + 16)
        p.card(cx, y + 62, cw, 176, r=12, fill=SOFT)
        p.icon(cx + 14, y + 76, icon, size=20, color=PRIMARY, box=30)
        p.chip(cx + cw - 130, y + 80, badge, kind="outline", size=11, w=116)
        p.text(cx + 14, y + 116, cw - 28, 24, f"<b>{title}</b>", size=15)
        p.text(cx + 14, y + 142, cw - 28, 44, desc, size=12, color=MUTED, valign="top")
        p.btn(cx + 14, y + 194, 140, 34, "▶ Bắt đầu ngay", size=12)
    return y + h + 24


def overview_general(f, frame="Tổng quát"):
    h = 2550
    p, y = overview_page(f, frame, h, "Tổng quát")
    p.zone(OV_X - 36, y, "B")
    hw = 610
    p.rect(OV_X, y, hw, 260, fill=PRIMARY, stroke=PRIMARY, r=18)
    p.rect(OV_X + 30, y + 40, 56, 56, fill="#2A4FC4", stroke="#2A4FC4", r=12, value="🎓", size=22, color=WHITE)
    p.text(OV_X + 100, y + 38, 400, 22, "Xin chào,", size=15, color=WHITE)
    p.text(OV_X + 100, y + 60, 460, 40, "<b>Username 👋</b>", size=30, color=WHITE)
    p.text(OV_X + 30, y + 124, 520, 24, "Band hiện tại: <b>5.0</b> → Mục tiêu: <b>7.0</b>", size=15, color=WHITE)
    p.rect(OV_X + 30, y + 176, 160, 46, fill=WHITE, stroke=WHITE, r=10, value="<b>Tiếp tục học ▶</b>", color=PRIMARY, size=15)
    p.text(OV_X + 210, y + 172, 360, 54, "Bài học tiếp theo:<br><b>Bài 13 · Thứ Sáu 18:00</b>", size=14, color=WHITE)
    cx, cwid = OV_X + hw + 20, OV_W - hw - 20
    p.card(cx, y, cwid, 260, r=18)
    p.text(cx + 24, y + 22, 300, 22, "▤ Khoá Đang Học", size=14, color=MUTED)
    p.text(cx + 24, y + 50, 300, 38, "<b>IELTS 7.0</b>", size=28, color=PRIMARY)
    p.text(cx + 24, y + 98, cwid - 48, 20, "Khai giảng: 14/07/2026   Kết thúc: 14/09/2026", size=12, color=MUTED)
    p.text(cx + 24, y + 140, 150, 20, "Tiến Độ Khoá", size=13, color=MUTED)
    p.text(cx + cwid - 200, y + 140, 176, 20, "<b>37.5%</b> hoàn thành", size=13, align="right")
    p.progress(cx + 24, y + 170, cwid - 48, 37)
    p.text(cx + 24, y + 196, 150, 20, "<b>12</b>/32 buổi", size=13)
    p.text(cx + cwid - 200, y + 196, 176, 20, "Còn 20 buổi kết thúc", size=13, color=MUTED, align="right")
    y += 280
    p.card(OV_X, y, OV_W, 106, r=14)
    p.text(OV_X + 24, y + 40, 160, 24, "<b>IELTS JOURNEY</b>", size=13, color=MUTED)
    p.rect(OV_X + 230, y + 66, OV_W - 290, 2, fill=LINE, stroke=LINE, r=0)
    for label, band, nx, kind in (("Bắt đầu", "4.5", OV_X + 214, "start"), ("Hiện tại", "5.5", OV_X + 600, "now"),
                                  ("Target", "7.0", OV_X + OV_W - 84, "target")):
        p.text(nx - 20, y + 14, 80, 20, label, size=12, color=MUTED, align="center")
        st = ("ellipse;whiteSpace=wrap;html=1;fontFamily=Arial;fontSize=14;fontStyle=1;"
              + {"start": "fillColor=#FFFFFF;strokeColor=#C9CED6;fontColor=#123AB5;",
                 "now": "fillColor=#123AB5;strokeColor=#123AB5;fontColor=#FFFFFF;",
                 "target": "fillColor=#FFFFFF;strokeColor=#123AB5;dashed=1;strokeWidth=2;fontColor=#123AB5;"}[kind])
        p.cell(band, st, nx, y + 46, 40, 40)
    y += 130
    p.zone(OV_X - 36, y, "C")
    y = stat_cards(p, y)
    y = activity_calendar(p, y)
    y = learning_orbit(p, y)
    y = study_plan_and_space(p, y)
    ai_recommendations(p, y)
    return p


def overview_detailed(f):
    h = 1480
    p, y = overview_page(f, "Dữ liệu chi tiết", h, "Dữ liệu chi tiết")
    p.zone(OV_X - 36, y, "B")
    p.card(OV_X, y, OV_W, 270, r=14)
    p.text(OV_X + 24, y + 18, 400, 28, "<b>Biểu đồ thời gian học</b>", size=20)
    p.text(OV_X + 24, y + 48, 400, 20, "Từ 01/9/2026 đến 7/9/2026", size=13, color=MUTED)
    p.text(OV_X + OV_W - 470, y + 22, 200, 22, "━ Thực tế   ┅ Kế hoạch", size=13, color=MUTED)
    fx = OV_X + OV_W - 250
    for i, label in enumerate(("Tuần", "Tháng", "Khoá")):
        p.chip(fx + i * 76, y + 22, label, kind="solid" if i == 0 else "neutral", w=68)
    p.rect(OV_X + 40, y + 140, OV_W - 80, 2, fill="#F97316", stroke="#F97316", r=0, dashed=True)
    for i, (dx, dy) in enumerate(((0, 30), (1, 22), (2, 18), (3, 2), (4, 26), (5, 12), (6, 16))):
        px = OV_X + 60 + dx * (OV_W - 120) / 6
        p.cell("", "ellipse;fillColor=#123AB5;strokeColor=#FFFFFF;strokeWidth=2;", px - 6, y + 130 + dy - 6, 12, 12)
    p.text(OV_X + 40, y + 120, OV_W - 80, 60, "line chart (static drawing)", size=11, color=MUTED, italic=True, align="center", valign="bottom")
    for i, day in enumerate(("T2", "T3", "T4", "T5", "T6", "T7", "CN")):
        p.text(OV_X + 40 + i * (OV_W - 120) / 6, y + 228, 40, 20, day, size=12, color=MUTED, align="center")
    y += 294
    lw = 560
    p.zone(OV_X - 36, y, "C")
    p.card(OV_X, y, lw, 330, r=14)
    p.text(OV_X + 24, y + 18, 300, 28, "<b>Tiến Độ 4 Kỹ Năng</b>", size=18)
    p.link(OV_X + lw - 110, y + 22, 90, "Chi tiết >", size=12, align="right")
    p.text(OV_X + 24, y + 46, 400, 20, "AI đánh giá so với kế hoạch lộ trình", size=12, color=MUTED)
    p.cell("", "rhombus;whiteSpace=wrap;html=1;fillColor=#E8EDFB;strokeColor=#123AB5;strokeWidth=2;", OV_X + 30, y + 110, 160, 160)
    p.text(OV_X + 30, y + 86, 160, 20, "Listening", size=11, color=MUTED, align="center")
    p.text(OV_X + 30, y + 274, 160, 20, "Writing", size=11, color=MUTED, align="center")
    for i, (skill, pct, status) in enumerate((("Listening", 62, "Đúng tiến độ"), ("Reading", 80, "Nhanh hơn"),
                                              ("Writing", 48, "Chậm hơn"), ("Speaking", 20, "Chậm hơn"))):
        ry = y + 100 + i * 50
        p.text(OV_X + 220, ry, 80, 22, skill, size=13)
        p.progress(OV_X + 300, ry + 8, 120, pct)
        p.text(OV_X + 426, ry, 40, 22, f"<b>{pct}%</b>", size=12)
        p.chip(OV_X + 468, ry, status, kind="active" if status == "Nhanh hơn" else "neutral", size=10, w=84)
    rx, rw = OV_X + lw + 20, OV_W - lw - 20
    p.rect(rx, y, rw, 330, fill=PRIMARY, stroke=PRIMARY, r=14)
    p.text(rx + 20, y + 18, 260, 28, "<b>You're moving forward</b>", size=18, color=WHITE)
    p.rect(rx + rw - 170, y + 20, 150, 26, fill="#2A4FC4", stroke="#2A4FC4", r=13, value="<b>+1.0 BAND</b> in 8 weeks", color=WHITE, size=11)
    for i, tab in enumerate(("Overall", "Listening", "Reading", "Writing", "Speaking")):
        p.rect(rx + 20 + i * 82, y + 62, 76, 26, fill=WHITE if i == 0 else "#2A4FC4", stroke="#2A4FC4", r=13,
               value=tab, color=PRIMARY if i == 0 else WHITE, size=11, bold=i == 0)
    p.rect(rx + 20, y + 104, rw - 40, 120, fill="#2A4FC4", stroke="#2A4FC4", r=10,
           value="band line chart · 20 Jun → 12 Aug", color="#C7D2F0", size=12)
    p.text(rx + 20, y + 238, 300, 34, "<b><font style='font-size:28px'>5.5</font></b>  Latest (from 4.5 on 20 Jun)", size=12, color=WHITE)
    p.rect(rx + 20, y + 280, rw - 40, 34, fill="#2A4FC4", stroke="#2A4FC4", r=8,
           value="On track: At your current pace, you're moving toward IELTS 6.5.", color=WHITE, size=11)
    y += 354
    p.zone(OV_X - 36, y, "D")
    p.card(OV_X, y, lw, 300, r=14)
    p.text(OV_X + 24, y + 18, 300, 28, "<b>Từ Vựng Cần Ôn</b>", size=18)
    p.link(OV_X + lw - 110, y + 22, 90, "Chi tiết >", size=12, align="right")
    p.cell("<b><font style='font-size:22px'>34%</font></b>",
           "ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#123AB5;strokeWidth=12;fontFamily=Arial;fontColor=#1F2937;",
           OV_X + 40, y + 70, 130, 130)
    p.btn(OV_X + 44, y + 230, 120, 36, "Ôn ngay ➔", size=12)
    for i, (n, label) in enumerate((("12", "Từ mới"), ("25", "Ôn lần 1"), ("34", "Ôn lần 2"), ("20", "Ôn lần 3"), ("110", "Đã thuộc"))):
        bx = OV_X + 210 + (i % 3) * 112
        by = y + 80 + (i // 3) * 100
        p.rect(bx, by, 96, 84, fill=PRIMARY_SOFT if i < 4 else SOFT, stroke=LINE, r=42,
               value=f"<b><font style='font-size:20px'>{n}</font></b><br>{label}", size=11)
    p.card(rx, y, rw, 300, r=14)
    p.text(rx + 20, y + 18, 300, 28, "<b>Phản Hồi Từ Mentor</b>", size=18)
    p.text(rx + 20, y + 58, 120, 22, "<b>Ms. Lan</b>", size=14)
    p.chip(rx + 100, y + 58, "Speaking", kind="active", size=11)
    p.text(rx + 20, y + 92, rw - 40, 140, "Phát âm của em tuần này đã có sự cải thiện vô cùng rõ rệt! Điểm sáng lớn nhất nằm ở độ "
           "tròn và rõ của các âm cuối (ending sounds), cùng khả năng kiểm soát luồng hơi tốt hơn hẳn so với tuần trước…",
           size=13, color=INK, valign="top")
    p.text(rx + 20, y + 256, 200, 20, "Updated: 11 Aug 2026", size=12, color=MUTED)
    p.link(rx + rw - 150, y + 254, 130, "View Feedback >", size=12, align="right")
    y += 324
    p.zone(OV_X - 36, y, "E")
    p.rect(OV_X, y, OV_W, 290, fill=PRIMARY, stroke=PRIMARY, r=14)
    p.text(OV_X + 24, y + 18, 400, 28, "<b>Các Khoá Học Của Tôi</b>", size=18, color=WHITE)
    p.text(OV_X + 24, y + 46, 400, 20, "Tất cả khoá đang theo học", size=12, color="#C7D2F0")
    p.text(OV_X + OV_W - 140, y + 22, 120, 22, "Xem tất cả >", size=12, color="#C7D2F0", align="right")
    courses = [("IELTS 6.0 Intensive", "Intermediate", "Khoá chính · 32 buổi", "12 / 32 buổi", 37),
               ("Ngữ Pháp Nâng Cao", "Upper-Inter", "Writing & Speaking · 20 buổi", "13 / 20 buổi", 65),
               ("Từ Vựng Academic", "Advanced", "IELTS Word list · 20 buổi", "4 / 20 buổi", 20),
               ("Speaking Masterclass", "Intermediate", "Phát âm & Fluency · 16 buổi", "8 / 16 buổi", 50)]
    cw = (OV_W - 48 - 48) / 4
    for i, (title, badge, sub, prog, pct) in enumerate(courses):
        cx = OV_X + 24 + i * (cw + 16)
        p.card(cx, y + 84, cw, 180, r=12)
        p.chip(cx + 14, y + 98, badge, kind="active", size=10)
        p.text(cx + 14, y + 132, cw - 28, 40, f"<b>{title}</b>", size=14, valign="top")
        p.text(cx + 14, y + 176, cw - 28, 20, sub, size=11, color=MUTED)
        p.progress(cx + 14, y + 214, cw - 28, pct)
        p.text(cx + 14, y + 230, cw - 28, 20, prog, size=11, color=MUTED)
    return p


def overview_placeholder(f):
    h = 760
    p, y = overview_page(f, "Tab chưa xây dựng", h, "Lịch sử ôn luyện")
    p.zone(OV_X - 36, y, "B")
    p.card(OV_X, y, OV_W, 220, r=14)
    p.text(OV_X, y + 46, OV_W, 30, "<b>Tính năng đang được cập nhật</b>", size=20, align="center")
    p.text(OV_X + 160, y + 86, OV_W - 320, 44, "Khu vực này đang hoàn thiện đồng bộ dữ liệu. Bạn có thể quay lại màn hình "
           "Overview hoặc Dữ liệu chi tiết.", size=14, color=MUTED, align="center")
    p.btn(OV_X + OV_W / 2 - 100, y + 148, 200, 44, "Quay về Overview", size=14)
    p.text(OV_X, y + 240, OV_W, 22, "Same card for Lịch sử ôn luyện and Xếp hạng.", size=12,
           color=MUTED, italic=True, align="center")
    return p


def build_overview(new):
    f = new("P-11_OverviewDashboard")
    overview_general(f)
    overview_detailed(f)
    overview_placeholder(f)
    p = overview_general(f, frame="Menu Dashboard")
    p.card(300, 116, 270, 224, r=12, stroke=DARK, sw=2)
    for i, (label, icon) in enumerate(zip(OV_TABS, OV_ICONS)):
        p.rect(310, 128 + i * 50, 250, 44, fill=PRIMARY_SOFT if i == 0 else WHITE,
               stroke="none", r=8, value=f"{icon}  {label}", color=PRIMARY if i == 0 else INK,
               bold=i == 0, size=14, align="left")
    for cell in p.vertices():
        if cell["y"] == -54:
            cell["value"] = "Hover / focus Dashboard → menu. Draw.io: click Dashboard to preview."
    f.save()


# ------------------------------------------------------------------ Writing Feedback (EssayBlock in /learn/lessons/:lessonId)
def writing_feedback(f, frame, passed):
    h = 1500 if not passed else 1300
    p = screen(f, "P-32", frame, "Lesson Player", h=h)
    y = navbar(p, role="learner", active="Khóa học") + 28
    mw = 820
    back_link(p, X0, y, "Writing Task 1 — Line Graph")
    eyebrow(p, X0, y + 40, "Bài 3 · Writing")
    p.text(X0, y + 62, mw, 40, "<b>Mô tả biểu đồ đường</b>", size=30)
    y0 = y + 124
    p.zone(X0 - 36, y0, "A")
    card_h = 1110 if not passed else 900
    p.card(X0, y0, mw, card_h, r=14, stroke=PRIMARY if passed else LINE, sw=2 if passed else 1)
    eyebrow(p, X0 + 20, y0 + 16, "Bài tập · Writing")
    p.text(X0 + 20, y0 + 38, 500, 26, "<b>EssayBlock</b> — Task 1", size=16)
    if passed:
        p.chip(X0 + mw - 110, y0 + 20, "✔ Đã đạt", kind="solid")
    p.text(X0 + 20, y0 + 74, mw - 40, 44, "The graph below shows the number of visitors to three museums between 2000 and 2020. "
           "Summarise the information by selecting and reporting the main features.", size=14, valign="top")
    p.img(X0 + 20, y0 + 126, 380, 150, "Biểu đồ đề bài")
    p.text(X0 + 20, y0 + 286, mw - 40, 20, "Tối thiểu 150 từ · đạt từ band 5.5 · mỗi lần chấm tốn 3 điểm (còn 27)", size=12, color=MUTED)
    ry = y0 + 316
    if not passed:
        p.zone(X0 - 36, ry, "B")
        p.text(X0 + 20, ry, 300, 22, "<b>Bài làm của bạn</b>", size=14)
        p.rect(X0 + 20, ry + 26, mw - 40, 170, fill=WHITE, stroke=DARK, r=8, value="The line graph illustrates how many people "
               "visited three museums …", color=INK, size=13, align="left", valign="top")
        p.text(X0 + 20, ry + 202, 200, 20, "162 từ", size=12, color=MUTED)
        p.btn(X0 + mw - 200, ry + 206, 180, 42, "Nộp bài · 3 điểm", size=14)
        ry += 270
    p.zone(X0 - 36, ry, "C")
    p.rect(X0 + 20, ry, mw - 40, 50, fill=SOFT if not passed else PRIMARY_SOFT, stroke=DARK if not passed else PRIMARY, r=8,
           value=f"<b>Band ước lượng: {'5.0 · Chưa đạt' if not passed else '6.0 · Đạt'}</b>", size=15, align="left")
    p.text(X0 + 20, ry + 60, mw - 40, 44, "The essay covers the main trends but the overview is missing and some figures are "
           "not compared.", size=13, color=INK, valign="top")
    p.text(X0 + 20, ry + 108, 300, 22, "<b>Tiêu chí</b>", size=14)
    for i, (crit, band, tip) in enumerate((("TA", "5.0", "Add a clear overview of the main trends."),
                                           ("CC", "5.5", "Group the museums by trend, not by year."),
                                           ("LR", "5.5", "Vary the verbs for increase and decrease."),
                                           ("GRA", "5.0", "Check the past tense in comparisons."))):
        cy = ry + 136 + i * 40
        p.rect(X0 + 20, cy, mw - 40, 34, fill=WHITE, stroke=LINE, r=6,
               value=f"<b>{crit}</b> · band {band} — {tip}", size=12, align="left")
    cy = ry + 302
    p.text(X0 + 20, cy, 300, 22, "<b>Sửa lỗi</b> (5 lỗi đầu)", size=14)
    for i, (bad, good) in enumerate((("visitor of the museum", "visitors to the museum"),
                                     ("increase dramatic", "increased dramatically"),
                                     ("in the other hand", "on the other hand"))):
        p.text(X0 + 20, cy + 28 + i * 26, mw - 40, 22, f"<s>{bad}</s> → <b>{good}</b>", size=13)
    cy += 120
    p.rect(X0 + 20, cy, mw - 40, 40, fill=WHITE, stroke=LINE, r=8, value="▸ <b>Bài mẫu</b>", size=13, align="left")
    p.text(X0 + 20, cy + 52, mw - 40, 20, "Band là ước lượng AI, không phải điểm IELTS chính thức.", size=12, color=MUTED, italic=True)
    rx, rw = X0 + mw + 40, CW - mw - 40
    p.card(rx, y + 40, rw, 240, r=16)
    p.text(rx + 20, y + 56, rw - 40, 20, "BÀI 3 · WRITING", size=12, color=MUTED, bold=True)
    p.text(rx + 20, y + 84, rw - 40, 28, f"<b>{'✔ Đã hoàn thành' if passed else '◉ Đang học'}</b>", size=17)
    p.btn(rx + 20, y + 150, rw - 40, 48, "Bài tiếp theo →" if passed else "Hoàn thành bài",
          kind="primary" if passed else "disabled")
    p.text(rx, y + 296, rw, 80, "Inline panel of the Lesson Player; the editor is hidden once the essay passes.",
           size=12, color=MUTED, italic=True, valign="top")
    footer(p, h - 64)
    return p


def writing_feedback_frames(f):
    """EssayBlock states, added to the P-32 Lesson Player file."""
    writing_feedback(f, "Writing Feedback — Chưa đạt", passed=False)
    writing_feedback(f, "Writing Feedback — Đã đạt", passed=True)


# ------------------------------------------------------------------ Classroom (/classroom)
SESSIONS = [(1, "Thứ 3", "07/09", "Bài 1: Nhập môn Anh ngữ", "completed", 100),
            (2, "Thứ 5", "08/09", "Bài 1: Nature & Environment", "today", 60),
            (3, "Thứ 7", "10/09", "Bài 2: Everyday Conversations", "upcoming", 30),
            (4, "Thứ 3", "12/09", "Bài 2: Listening Foundations", "upcoming", 30),
            (5, "Thứ 5", "14/09", "Bài 3: Building Vocabulary", "upcoming", 30),
            (6, "Thứ 7", "16/09", "Bài 3: Grammar in Context", "locked", 60),
            (7, "Thứ 3", "19/09", "Bài 4: Reading Strategies", "locked", 0),
            (8, "Thứ 5", "21/09", "Bài 4: Speaking Practice", "locked", 0),
            (9, "Thứ 7", "23/09", "Bài 5: Writing Structure", "locked", 0)]
SESSION_ACTION = {"completed": "✔ Xem lại buổi học", "today": "▶ Vào lớp ngay!", "upcoming": "◷ Chưa đến giờ học",
                  "locked": "🔒 Chờ mở lớp"}


def classroom_base(f, frame, h, pid="P-20", title="My Classroom"):
    p = screen(f, pid, frame, title, h=h)
    y = navbar(p, role="learner")
    p.zone(X0 - 36, y + 30, "A")
    p.rect(0, y, DESKTOP_W, 250, fill=PRIMARY, stroke=PRIMARY, r=0)
    p.rect(X0, y + 36, 64, 64, fill="#2A4FC4", stroke="#2A4FC4", r=32, value="🐻", size=26)
    p.text(X0 + 84, y + 34, 500, 40, "<b>LỚP HỌC CỦA TÔI</b>", size=28, color=WHITE)
    p.text(X0 + 84, y + 76, 500, 24, "Xin chào Minh Anh", size=16, color=WHITE)
    p.text(X0, y + 130, 780, 24, "▣ Mã lớp: IE3-88     🎓 Giáo viên: Jessi Thuy Anh     ◷ Thời gian: Thứ 3-5-7 | 18:30 - 20:30",
           size=14, color=WHITE)
    p.rect(X0 + CW - 400, y + 30, 400, 190, fill="#2A4FC4", stroke="#2A4FC4", r=16,
           value="<b>IELTS Cất cánh</b><br>3.0 – IELTS 4.0+<br><br>ClassProgressPanel (dark)", color=WHITE, size=14)
    y += 280
    p.zone(X0 - 36, y, "B")
    p.text(X0, y, 200, 36, "<b>Tháng 9/2026</b>", size=22)
    p.rect(X0 + 190, y + 2, 230, 34, fill=PRIMARY_SOFT, stroke=PRIMARY, r=17, value="● Join class! Vào lớp ngay", color=PRIMARY, size=13, bold=True)
    p.rect(X0 + 432, y + 2, 34, 34, fill=WHITE, stroke=LINE, r=8, value="‹", size=16)
    p.rect(X0 + 472, y + 2, 34, 34, fill=WHITE, stroke=LINE, r=8, value="›", size=16)
    p.btn(X0 + CW - 470, y, 150, 38, "Xem theo tháng", size=13)
    p.btn(X0 + CW - 310, y, 170, 38, "Xem theo lộ trình", kind="secondary", size=13)
    p.rect(X0 + CW - 128, y, 38, 38, fill=WHITE, stroke=LINE, r=8, value="▣", size=14)
    p.rect(X0 + CW - 82, y, 38, 38, fill=WHITE, stroke=LINE, r=8, value="☰", size=14)
    y += 60
    p.zone(X0 - 36, y, "C")
    gw = 920
    cw, chh = (gw - 32) / 3, 178
    for i, (n, wd, date, title, status, pct) in enumerate(SESSIONS):
        cx, cy = X0 + (i % 3) * (cw + 16), y + (i // 3) * (chh + 16)
        today = status == "today"
        p.card(cx, cy, cw, chh, r=14, stroke=PRIMARY if today else LINE, sw=2 if today else 1,
               fill=WHITE if status != "locked" else SOFT)
        p.chip(cx + 14, cy + 14, f"Buổi {n}", kind="solid" if today else "neutral", size=11)
        p.text(cx + 14, cy + 44, 100, 18, "IELTS 3.0", size=11, color=MUTED)
        p.text(cx + cw - 90, cy + 14, 76, 18, wd, size=11, color=MUTED, align="right")
        p.text(cx + cw - 90, cy + 32, 76, 22, f"<b>{date}</b>", size=14, align="right")
        p.text(cx + 14, cy + 72, cw - 28, 40, f"<b>{title}</b>", size=14, valign="top")
        p.text(cx + 14, cy + 112, cw - 28, 18, "◷ 18:30 - 20:30", size=12, color=MUTED)
        p.text(cx + 14, cy + 140, cw - 80, 22, SESSION_ACTION[status], size=12, color=PRIMARY if today else INK, bold=today)
        p.rect(cx + cw - 54, cy + 132, 40, 40, fill=WHITE, stroke=PRIMARY if pct else LINE, r=20, sw=3, value=f"{pct}%", size=10)
    ax = X0 + gw + 30
    p.zone(ax - 30, y, "D")
    p.card(ax, y, CW - gw - 30, 170, r=14)
    p.text(ax + 20, y + 16, 200, 20, "Mentor của bạn", size=13, color=MUTED)
    p.rect(ax + 20, y + 46, 52, 52, fill=PRIMARY_SOFT, stroke=PRIMARY, r=26, value="<b>L</b>", color=PRIMARY, size=18)
    p.text(ax + 84, y + 48, 180, 22, "<b>Ms. Lan</b>", size=16)
    p.text(ax + 84, y + 72, 180, 20, "IELTS Instructor", size=13, color=MUTED)
    p.btn(ax + 20, y + 116, CW - gw - 70, 38, "Nhắn Mentor", kind="secondary", size=13)
    return p


def classroom_populated(f):
    return classroom_base(f, "Populated", 1240)


def classroom_dialog(f):
    h = 1240
    p = classroom_base(f, "Populated", h, pid="P-20a", title="Lesson Detail")
    p.overlay(DESKTOP_W, h)
    dx, dw, dy = 300, 840, 170
    p.card(dx, dy, dw, 560, r=18)
    p.rect(dx, dy, dw, 170, fill=PRIMARY, stroke=PRIMARY, r=18)
    p.text(dx + dw - 50, dy + 14, 30, 30, "✕", size=18, color=WHITE, align="center")
    p.rect(dx + 28, dy + 24, 70, 24, fill=WHITE, stroke=WHITE, r=12, value="<b>Buổi 2</b>", color=PRIMARY, size=11)
    p.text(dx + 108, dy + 24, 100, 24, "● Hôm nay", size=12, color=WHITE)
    p.text(dx + 28, dy + 60, dw - 56, 40, "<b>Bài 1: Nature &amp; Environment</b>", size=26, color=WHITE)
    p.text(dx + 28, dy + 116, dw - 56, 22, "🎓 Khóa IELTS 3.0   ▣ IE3-88   ◷ 18:30 - 20:30   ◯ Jessi Thuy Anh", size=13, color=WHITE)
    sy = dy + 194
    p.btn(dx + 28, sy, 220, 110, "▶ Vào lớp ngay!", size=16)
    p.card(dx + 264, sy, 260, 110, r=12, fill=SOFT)
    p.rect(dx + 280, sy + 20, 60, 60, fill=WHITE, stroke=PRIMARY, r=30, sw=4, value="65%", size=12)
    p.text(dx + 352, sy + 14, 160, 50, "Hoàn thành 3 mục để đạt mục tiêu buổi!", size=12, valign="top")
    p.btn(dx + 352, sy + 70, 100, 28, "↻ Tiếp tục", kind="secondary", size=11)
    p.card(dx + 540, sy, dw - 568, 110, r=12, fill=SOFT)
    p.text(dx + 556, sy + 14, dw - 600, 60, "🔒 Hoàn thành bài tập để nhận đánh giá từ Mentor.", size=12, valign="top")
    p.chip(dx + 556, sy + 74, "Chưa chấm bài", kind="outline", size=11)
    ty = sy + 136
    p.text(dx + 28, ty, 160, 30, "<b><u>Homework Hub</u></b>", size=15, color=PRIMARY)
    p.text(dx + 200, ty, 200, 30, "Tài liệu buổi học", size=15, color=MUTED)
    hw = (dw - 56 - 48) / 4
    for i, (title, pct, action) in enumerate((("Ngữ pháp", 100, "Đã xong"), ("Từ vựng", 65, "Tiếp tục"),
                                              ("Quick Test tổng hợp", 0, "Bắt đầu"), ("IELTS Skills", 65, "Tiếp tục"))):
        hx = dx + 28 + i * (hw + 16)
        p.card(hx, ty + 46, hw, 150, r=12)
        p.text(hx + 14, ty + 60, hw - 28, 40, f"<b>{title}</b>", size=13, valign="top")
        p.progress(hx + 14, ty + 110, hw - 28, pct)
        p.text(hx + 14, ty + 130, 50, 20, f"{pct}%", size=12, color=MUTED)
        p.btn(hx + hw - 94, ty + 150, 80, 30, action, kind="primary" if action == "Bắt đầu" else "secondary", size=11)
    return p


def build_classroom(new):
    f = new("P-20_MyClassroom")
    classroom_populated(f)
    f.save()
    f = new("P-20a_LessonDetail")
    classroom_dialog(f)
    f.save()


# ------------------------------------------------------------------ Classroom Lesson Workspace (/lessons/:lessonId)
def lesson_ws(f, frame, view, pid="P-21", title="Lesson Workspace", card=None):
    """Class session page (/lessons/:lessonId). `card` = (side, mode, effect) of the flashcard view."""
    card_h = {"materials": 860, "quiz": 680, "vocabulary": 680, "flashcard": 880}[view]
    h = 380 + card_h
    p = screen(f, pid, frame, title, h=h)
    y = navbar(p, role="learner")
    p.zone(X0 - 36, y + 24, "A")
    p.cell("", "rounded=0;fillColor=#0D2B8D;strokeColor=none;gradientColor=#123AB5;gradientDirection=east;", 0, y, DESKTOP_W, 140)
    p.text(X0, y + 22, 140, 40, "<b>Buổi 1</b>", size=28, color=WHITE)
    p.rect(X0 + 130, y + 28, 130, 30, fill="#2A4FC4", stroke="#5B7DF0", r=15, value="<b>Khoá IELTS 3.0</b>", size=12, color=WHITE)
    p.rect(X0 + 272, y + 28, 230, 30, fill="#2A4FC4", stroke="#5B7DF0", r=15, value="<b>Bài 1: Nature &amp; Environment</b>",
           size=12, color=WHITE)
    p.text(X0, y + 84, 300, 22, "← Quay lại Thời khoá biểu", size=12, color="#C7D2F0")
    px = X0 + CW - 380
    p.rect(px, y + 20, 380, 100, fill="#1E3FA8", stroke="#5B7DF0", r=14)
    p.text(px + 18, y + 30, 240, 22, "▣ <b>Tiến độ Homework Hub</b>", size=13, color=WHITE)
    p.text(px + 18, y + 58, 200, 20, "Bạn đang làm bài", size=11, color="#C7D2F0")
    p.rect(px + 140, y + 58, 40, 20, fill=WHITE, stroke="none", r=10, value="<b>2/3</b>", size=11, color=PRIMARY)
    p.text(px + 290, y + 54, 70, 26, "<b>68%</b>", size=17, color=WHITE, align="right")
    p.rect(px + 18, y + 92, 344, 8, fill="#2A4FC4", stroke="none", r=4)
    p.rect(px + 18, y + 92, 234, 8, fill="#F97316", stroke="none", r=4)
    y += 170
    mw = 860
    p.zone(X0 - 36, y, "B")
    p.card(X0, y, mw, card_h, r=16)
    if view == "materials":
        eyebrow(p, X0 + 28, y + 24, "Tài liệu buổi học / Lesson Summary")
        p.text(X0 + 28, y + 48, mw - 56, 36, "<b>Bài 1: Nature &amp; Environment</b>", size=24)
        sections = [("Mục tiêu buổi học", "Từ vựng và cấu trúc chính", True),
                    ("Từ vựng trọng tâm", "Nhóm từ theo chủ đề môi trường", False),
                    ("Cấu trúc câu", "Mẫu câu cho Writing và Speaking", False)]
        sy = y + 108
        for title, desc, open_ in sections:
            sh = 210 if open_ else 72
            p.card(X0 + 28, sy, mw - 56, sh, r=12, stroke=PRIMARY if open_ else LINE)
            p.text(X0 + 48, sy + 14, 500, 22, f"<b>{title}</b>", size=15)
            p.text(X0 + 48, sy + 38, 500, 20, desc, size=12, color=MUTED)
            p.text(X0 + mw - 80, sy + 22, 24, 24, "▴" if open_ else "▾", size=16, color=MUTED, align="center")
            if open_:
                for i in range(3):
                    p.text(X0 + 48, sy + 80 + i * 36, mw - 120, 24, "✔ " + ["Nắm 6 từ khoá chủ đề Nature",
                           "Dùng được cấu trúc so sánh", "Luyện phát âm từ khó"][i], size=13)
            sy += sh + 14
        p.rect(X0 + 28, y + 800, mw - 56, 40, fill=SOFT, stroke=LINE, r=8,
               value="✔ Tài liệu đang được lưu trong phiên học của bạn.", size=13, align="left")
    elif view == "quiz":
        eyebrow(p, X0 + 28, y + 24, "Homework Hub / Ngữ pháp")
        p.text(X0 + 28, y + 48, mw - 56, 36, "<b>Bài 1: Nature &amp; Environment</b>", size=24)
        p.chip(X0 + 28, y + 96, "Ngữ pháp")
        p.chip(X0 + 120, y + 96, "Chọn một đáp án")
        p.text(X0 + mw - 100, y + 96, 72, 24, "<b>1 / 5</b>", size=14, align="right")
        p.rect(X0 + 28, y + 140, mw - 56, 64, fill=SOFT, stroke=LINE, r=12,
               value="▶  <b>Audio câu 1</b>   ━━━━●━━━━━━   🔊", size=14, align="left")
        p.text(X0 + 28, y + 228, mw - 56, 28, "<b>Choose the correct form: Forests ___ many species.</b>", size=17)
        p.text(X0 + 28, y + 260, mw - 56, 20, "Để làm bài nghe lại 1 lần, sau đó chọn đáp án đúng nhất.", size=13, color=MUTED)
        for i, choice in enumerate(("protect", "protects", "protecting", "protected")):
            sel = i == 0
            p.rect(X0 + 28, y + 300 + i * 62, mw - 56, 50, fill=PRIMARY_SOFT if sel else WHITE,
                   stroke=PRIMARY if sel else LINE, r=10, value=f"<b>{chr(65 + i)}</b>   {choice}", size=14, align="left")
        fy = y + 580
        p.btn(X0 + 28, fy, 140, 42, "‹ Câu trước", kind="disabled", size=13)
        p.btn(X0 + 180, fy, 140, 42, "Câu sau ›", kind="secondary", size=13)
        for i in range(5):
            p.rect(X0 + 360 + i * 46, fy + 2, 38, 38, fill=PRIMARY if i == 0 else WHITE, stroke=PRIMARY if i == 0 else LINE,
                   r=8, value=str(i + 1), color=WHITE if i == 0 else INK, size=13, bold=True)
        p.text(X0 + 28, fy + 60, 300, 22, "Đã trả lời 1/5 câu", size=13, color=MUTED)
    elif view == "flashcard":
        import screens_vocab_lesson  # F045 flashcard, shared with the dictionary lessons
        screens_vocab_lesson.homework_flashcard(p, X0, y, mw, card or ("front", "full", None))
    else:
        eyebrow(p, X0 + 28, y + 24, "Homework Hub / Từ vựng")
        p.text(X0 + 28, y + 48, 520, 36, "<b>Bài 1: Nature &amp; Environment</b>", size=24)
        p.text(X0 + 28, y + 90, 520, 20, "Ôn từ vựng theo chủ đề Nature và lưu lại các từ cần nhớ.", size=13, color=MUTED)
        p.rect(X0 + mw - 330, y + 50, 300, 42, fill=WHITE, stroke=DARK, r=8, value="⌕  Tìm từ, nghĩa hoặc chủ đề", color=MUTED, size=13, align="left")
        word_card(p, X0 + 28, y + 140, mw - 56, "sustainable", "adjective", "B2", "/səˈsteɪ.nə.bəl/",
                  "able to continue over a period of time without causing damage", "bền vững · có thể duy trì lâu dài",
                  ["environment", "nature"], "Cities need sustainable ways to reduce pollution.")
        word_card(p, X0 + 28, y + 400, mw - 56, "biodiversity", "noun", "C1", "/ˌbaɪ.əʊ.daɪˈvɜː.sə.ti/",
                  "the variety of plant and animal life in a particular habitat", "đa dạng sinh học",
                  ["environment", "academic"], "The project protects biodiversity in coastal forests.")
    sx, sw = X0 + mw + 30, CW - mw - 30
    p.zone(sx - 30, y, "C")
    p.card(sx, y, sw, 640, r=16)
    p.text(sx + 20, y + 18, sw - 40, 20, "LESSON RESOURCE", size=12, color=MUTED, bold=True)
    active = {"materials": "Slide bài giảng", "quiz": "Ngữ pháp", "vocabulary": "Từ vựng", "flashcard": "Từ vựng"}[view]
    ry = y + 46
    for label in ("Slide bài giảng", "Lesson Summary", "Từ vựng buổi học"):
        on = label == active or (view == "vocabulary" and label == "Từ vựng buổi học")
        p.rect(sx + 14, ry, sw - 28, 40, fill=PRIMARY_SOFT if on else WHITE, stroke=PRIMARY if on else "none", r=8,
               value=label, size=13, align="left", color=PRIMARY if on else INK, bold=on)
        ry += 46
    p.text(sx + 20, ry + 14, 160, 20, "HOMEWORK HUB", size=12, color=MUTED, bold=True)
    p.text(sx + sw - 70, ry + 14, 50, 20, "2 / 4", size=12, color=MUTED, align="right")
    ry += 42
    for label, prog in (("Ngữ pháp", "0%"), ("Từ vựng", "35%"), ("Quick Test tổng hợp", "100%")):
        on = label == active
        p.rect(sx + 14, ry, sw - 28, 40, fill=PRIMARY_SOFT if on else WHITE, stroke=PRIMARY if on else "none", r=8,
               value=label, size=13, align="left", color=PRIMARY if on else INK, bold=on)
        p.text(sx + sw - 70, ry, 44, 40, prog, size=12, color=MUTED, align="right")
        ry += 46
    p.text(sx + 20, ry + 14, 160, 20, "IELTS SKILLS", size=12, color=MUTED, bold=True)
    p.text(sx + 20, ry + 40, sw - 40, 40, "🎓 Luyện kỹ năng được mở sau khi hoàn thành bài tập.", size=12, color=MUTED, valign="top")
    p.rect(sx, y + 660, sw, 130, fill=PRIMARY, stroke=PRIMARY, r=14)
    p.text(sx + 18, y + 670, 200, 20, "Mentor của bạn", size=11, color="#C7D2F0")
    p.cell("<b>L</b>", "ellipse;whiteSpace=wrap;html=1;fillColor=#F97316;strokeColor=#FFFFFF;fontColor=#FFFFFF;fontSize=17;",
           sx + 18, y + 696, 46, 46)
    p.text(sx + 76, y + 694, 200, 48, "<b>Ms. Lan</b><br><font color='#C7D2F0'>IELTS Instructor</font>", size=13, color=WHITE, valign="top")
    p.rect(sx + 18, y + 750, sw - 36, 30, fill="#2A4FC4", stroke="#5B7DF0", r=8, value="Nhắn Mentor", size=12, color=WHITE)
    return p


def build_lesson_workspace(new):
    f = new("P-21_LessonWorkspace")
    lesson_ws(f, "Tài liệu buổi học", "materials")
    lesson_ws(f, "Homework — Ngữ pháp", "quiz")
    lesson_ws(f, "Homework — Từ vựng", "vocabulary")
    lesson_ws(f, "Homework — Flashcard", "flashcard")
    f.save()


# ------------------------------------------------------------------ Vocabulary (/vocabulary)
def word_card(p, x, y, w, word, pos, level, ipa, meaning, vi, tags, example):
    p.card(x, y, w, 240, r=14)
    iw = 200
    p.text(x + 20, y + 16, 260, 32, f"<b>{word}</b>", size=24)
    p.chip(x + 290, y + 22, pos, kind="neutral", size=11)
    p.chip(x + 390, y + 22, level, kind="active", size=11, w=40)
    p.rect(x + 440, y + 18, 34, 34, fill=WHITE, stroke=LINE, r=17, value="🔊", size=13)
    p.text(x + 20, y + 56, 500, 20, f"UK {ipa}    US {ipa}", size=13, color=MUTED)
    p.text(x + 20, y + 82, w - iw - 60, 22, meaning, size=14)
    p.rect(x + 20, y + 112, w - iw - 60, 40, fill=SOFT, stroke=LINE, r=8,
           value=f"{pos} · <b>{level}</b> · <b>{vi}</b>", size=13, align="left")
    p.rect(x + w - iw - 80, y + 115, 34, 34, fill=WHITE, stroke=LINE, r=17, value="🔖", size=13)
    tx = x + 20
    for tag in tags:
        tx = p.chip(tx, y + 164, tag, kind="outline", size=11)
    p.text(x + 20, y + 198, w - iw - 60, 24, f"<i>“{example}”</i>", size=13, color=MUTED)
    p.rect(x + w - iw - 20, y + 20, iw, 200, fill=PRIMARY_SOFT, stroke=LINE, r=12,
           value="Hình ảnh gợi nhớ<br><br>🌿", size=13, color=PRIMARY)


VOCAB = [("sustainable", "adjective", "B2", "/səˈsteɪ.nə.bəl/", "able to continue over a period of time without causing damage",
          "bền vững · có thể duy trì lâu dài", ["environment", "nature"], "Cities need sustainable ways to reduce pollution."),
         ("biodiversity", "noun", "C1", "/ˌbaɪ.əʊ.daɪˈvɜː.sə.ti/", "the variety of plant and animal life in a particular habitat",
          "đa dạng sinh học", ["environment", "academic"], "The project protects biodiversity in coastal forests."),
         ("renewable", "adjective", "B2", "/rɪˈnjuː.ə.bəl/", "able to be replaced naturally and used again",
          "có thể tái tạo", ["energy", "environment"], "Solar power is a renewable source of energy.")]


def vocabulary(f, frame, empty=False):
    h = 1560 if not empty else 900
    p = screen(f, "P-50", frame, "Vocabulary / Dictionary", h=h)
    y = navbar(p, role="learner", active="Sổ ghi nhớ", child="Học") + 28
    p.zone(X0 - 36, y, "A")
    p.rect(X0, y, CW, 150, fill=PRIMARY, stroke=PRIMARY, r=18)
    p.text(X0 + 32, y + 26, 600, 20, "<b>IELTS SPACE DICTIONARY</b>", size=13, color="#C7D2F0")
    p.text(X0 + 32, y + 50, 700, 42, "<b>Từ điển học theo chủ đề</b>", size=30, color=WHITE)
    p.text(X0 + 32, y + 98, 700, 22, "Tra cứu, nghe phát âm và lưu lại từ cần ôn.", size=15, color=WHITE)
    p.rect(X0 + CW - 150, y + 54, 118, 42, fill=WHITE, stroke=WHITE, r=21, value="<b>📑 6 từ</b>", color=PRIMARY, size=15)
    y += 180
    p.zone(X0 - 36, y, "B")
    eyebrow(p, X0, y, "VOCABULARY LIST")
    p.text(X0, y + 22, 600, 36, "<b>Nature &amp; Environment</b>", size=26)
    p.text(X0, y + 62, 600, 22, "Từ vựng cốt lõi cho Reading, Writing và Speaking.", size=14, color=MUTED)
    query = "rainforest" if empty else ""
    p.rect(X0 + CW - 380, y + 22, 380, 44, fill=WHITE, stroke=DARK, r=8,
           value=f"⌕  {query or 'Tìm từ, nghĩa hoặc chủ đề'}", color=INK if query else MUTED, size=14, align="left")
    y += 100
    p.text(X0, y, 300, 22, f"<b>{0 if empty else 6} từ phù hợp</b>", size=14)
    p.chip(X0 + CW - 170, y, "Nature &amp; Environment", kind="active", size=11, w=170)
    y += 40
    p.zone(X0 - 36, y, "C")
    if empty:
        p.card(X0, y, CW, 160, r=14, dashed=True)
        p.text(X0, y + 46, CW, 30, "🌿", size=24, align="center", color=PRIMARY)
        p.text(X0, y + 86, CW, 24, "Không tìm thấy từ phù hợp. Hãy thử một từ khóa khác.", size=15, color=MUTED, align="center")
    else:
        for i, entry in enumerate(VOCAB):
            word_card(p, X0, y + i * 260, CW, *entry)
        p.text(X0, y + 790, CW, 22, "… ecosystem, conserve, carbon footprint (6 words in the sample list)", size=12,
               color=MUTED, italic=True, align="center")
    footer(p, h - FOOTER_OFFSET)
    return p


FOOTER_OFFSET = 64


def build_vocabulary(new):
    f = new("P-50_Vocabulary")
    vocabulary(f, "Populated")
    vocabulary(f, "Empty search", empty=True)
    f.save()


def build(new):
    build_overview(new)
    build_classroom(new)
    build_lesson_workspace(new)
    build_vocabulary(new)
