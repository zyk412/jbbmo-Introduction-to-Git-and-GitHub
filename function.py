# -------------------------------------------------------------
# 📘 数学基础函数宝典 · Function Properties & Graphs Summary
# Version: Final Complete Edition
# Author: 雅坤 × ChatGPT
# -------------------------------------------------------------

from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt
import numpy as np
import os

# -------------------------------------------------------------
# ✨ 页码功能
# -------------------------------------------------------------
def add_page_number(canvas, doc):
    page_num = canvas.getPageNumber()
    text = f"Page {page_num}"
    canvas.setFont("Helvetica", 9)
    canvas.setFillColorRGB(0.4, 0.4, 0.4)
    canvas.drawRightString(800, 15, text)

# -------------------------------------------------------------
# ✨ 样式设置
# -------------------------------------------------------------
title_style = ParagraphStyle(
    name='Title',
    fontName='Helvetica-Bold',
    fontSize=28,
    leading=34,
    alignment=1,
    textColor=colors.HexColor("#2E4053")
)

sub_style = ParagraphStyle(
    name='Subtitle',
    fontName='Helvetica',
    fontSize=18,
    leading=22,
    alignment=1,
    textColor=colors.HexColor("#5D6D7E")
)

text_style = ParagraphStyle(
    name='Text',
    fontName='Helvetica',
    fontSize=12,
    leading=18,
    textColor=colors.HexColor("#17202A")
)

# -------------------------------------------------------------
# ✨ 封面 / 目录 / 封底模块
# -------------------------------------------------------------
def add_cover_page(story):
    story.append(Spacer(1, 180))
    story.append(Paragraph("📘 数学基础函数宝典", title_style))
    story.append(Spacer(1, 20))
    story.append(Paragraph("Function Properties & Graphs Summary", sub_style))
    story.append(Spacer(1, 240))
    story.append(Paragraph("Designed for Math Learners", text_style))
    story.append(Paragraph("Created by ChatGPT × 雅坤", text_style))
    story.append(Spacer(1, 60))
    story.append(Paragraph("© 2025 Study Edition", text_style))
    story.append(PageBreak())

def add_table_of_contents(story, sections):
    story.append(Paragraph("📑 目录 (Table of Contents)", title_style))
    story.append(Spacer(1, 20))
    for idx, (section, funcs) in enumerate(sections.items(), start=1):
        toc_entry = f"{idx}. {section} — 包含 {len(funcs)} 个函数"
        story.append(Paragraph(toc_entry, text_style))
        for f in funcs:
            story.append(Paragraph(f"&nbsp;&nbsp;&nbsp;· {f}", text_style))
        story.append(Spacer(1, 8))
    story.append(PageBreak())

def add_back_cover(story):
    story.append(Spacer(1, 180))
    story.append(Paragraph("📘 数学基础函数宝典", title_style))
    story.append(Spacer(1, 20))
    story.append(Paragraph("Function Handbook — Final Edition", sub_style))
    story.append(Spacer(1, 200))
    story.append(Paragraph("“Mathematics is about understanding.”", text_style))
    story.append(Spacer(1, 40))
    story.append(Paragraph("— Designed by 雅坤 & ChatGPT", text_style))
    story.append(Spacer(1, 100))
    story.append(Paragraph("Thank you for learning with passion ❤️", text_style))

# -------------------------------------------------------------
# ✨ 函数定义区
# -------------------------------------------------------------
sections = {
    "Ⅰ. 代数函数 (Algebraic Functions)": ["Linear", "Quadratic", "Cubic", "Rational"],
    "Ⅱ. 指数与对数函数 (Exponential & Logarithmic)": ["Exponential", "Logarithmic"],
    "Ⅲ. 三角函数 (Trigonometric Functions)": ["Sine", "Cosine", "Tangent"],
    "Ⅳ. 反三角函数 (Inverse Trig Functions)": ["Arcsin", "Arccos", "Arctan"],
    "Ⅴ. 双曲函数 (Hyperbolic Functions)": ["Sinh", "Cosh", "Tanh"],
    "Ⅵ. 特殊函数 (Special Functions)": ["Absolute", "Sign", "Piecewise"]
}

# -------------------------------------------------------------
# ✨ 图像绘制函数
# -------------------------------------------------------------
def plot_function(func_name):
    x = np.linspace(-5, 5, 400)
    y = None

    plt.figure(figsize=(6, 3))
    plt.axhline(0, color='gray', linewidth=0.8)
    plt.axvline(0, color='gray', linewidth=0.8)

    if func_name == "Linear":
        y = x
        plt.title("Linear: y = x")
    elif func_name == "Quadratic":
        y = x**2
        plt.title("Quadratic: y = x²")
    elif func_name == "Cubic":
        y = x**3
        plt.title("Cubic: y = x³")
    elif func_name == "Rational":
        y = 1/x
        plt.title("Rational: y = 1/x")
        plt.ylim(-5, 5)
    elif func_name == "Exponential":
        y = np.exp(x)
        plt.title("Exponential: y = eˣ")
        plt.ylim(0, 50)
    elif func_name == "Logarithmic":
        x = np.linspace(0.1, 5, 400)
        y = np.log(x)
        plt.title("Logarithmic: y = ln(x)")
    elif func_name == "Sine":
        y = np.sin(x)
        plt.title("Sine: y = sin(x)")
    elif func_name == "Cosine":
        y = np.cos(x)
        plt.title("Cosine: y = cos(x)")
    elif func_name == "Tangent":
        y = np.tan(x)
        plt.title("Tangent: y = tan(x)")
        plt.ylim(-5, 5)
    elif func_name == "Arcsin":
        x = np.linspace(-1, 1, 400)
        y = np.arcsin(x)
        plt.title("Arcsin: y = arcsin(x)")
    elif func_name == "Arccos":
        x = np.linspace(-1, 1, 400)
        y = np.arccos(x)
        plt.title("Arccos: y = arccos(x)")
    elif func_name == "Arctan":
        y = np.arctan(x)
        plt.title("Arctan: y = arctan(x)")
    elif func_name == "Sinh":
        y = np.sinh(x)
        plt.title("Sinh: y = sinh(x)")
    elif func_name == "Cosh":
        y = np.cosh(x)
        plt.title("Cosh: y = cosh(x)")
        plt.ylim(0, 10)
    elif func_name == "Tanh":
        y = np.tanh(x)
        plt.title("Tanh: y = tanh(x)")
    elif func_name == "Absolute":
        y = np.abs(x)
        plt.title("Absolute: y = |x|")
    elif func_name == "Sign":
        y = np.sign(x)
        plt.title("Sign: y = sgn(x)")
    elif func_name == "Piecewise":
        y = np.piecewise(x, [x < 0, x >= 0], [-1, 1])
        plt.title("Piecewise: y = {-1 (x<0), 1 (x≥0)}")

    plt.plot(x, y, color="#2874A6", linewidth=2)
    plt.tight_layout()
    filename = f"{func_name}.png"
    plt.savefig(filename)
    plt.close()
    return filename

# -------------------------------------------------------------
# ✨ PDF 生成主逻辑
# -------------------------------------------------------------
doc = SimpleDocTemplate("数学基础函数宝典.pdf", pagesize=landscape(A4))
story = []

add_cover_page(story)
add_table_of_contents(story, sections)

for section, funcs in sections.items():
    story.append(Paragraph(section, sub_style))
    story.append(Spacer(1, 20))
    for f in funcs:
        img_file = plot_function(f)
        story.append(Paragraph(f"🔹 {f} Function", text_style))
        story.append(Image(img_file, width=400, height=200))
        story.append(Spacer(1, 12))
    story.append(PageBreak())

add_back_cover(story)

doc.build(story, onLaterPages=add_page_number, onFirstPage=add_page_number)

# 清理生成的临时图片文件
for section, funcs in sections.items():
    for f in funcs:
        try:
            os.remove(f"{f}.png")
        except:
            pass

print("✅ 《数学基础函数宝典》已生成！")