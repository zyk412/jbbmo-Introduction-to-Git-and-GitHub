# -*- coding: utf-8 -*-
"""
函数性质与图像总结 Function Summary
✅ 中英双语
✅ 自动生成函数图像
✅ 横版学习笔记风格
运行后会在当前文件夹生成 Function_Summary.pdf
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
import matplotlib.pyplot as plt
import numpy as np
import os

# 注册中英文通用字体
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))
font_name = 'HeiseiKakuGo-W5'

# 保存函数图像
def save_function_plot(filename, func, x_range, title):
    x = np.linspace(*x_range, 400)
    y = func(x)
    plt.figure(figsize=(5, 3))
    plt.plot(x, y)
    plt.title(title, fontsize=10)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# 函数列表
functions = [
    ("线性函数 Linear", lambda x: x, (-5, 5)),
    ("二次函数 Quadratic", lambda x: x**2, (-3, 3)),
    ("三次函数 Cubic", lambda x: x**3, (-3, 3)),
    ("有理函数 Rational", lambda x: 1/x, (-5, 5)),
    ("指数函数 Exponential", lambda x: np.exp(x), (-2, 2)),
    ("对数函数 Logarithmic", lambda x: np.log(x), (0.1, 5)),
    ("正弦函数 Sine", lambda x: np.sin(x), (-2*np.pi, 2*np.pi)),
    ("余弦函数 Cosine", lambda x: np.cos(x), (-2*np.pi, 2*np.pi)),
    ("正切函数 Tangent", lambda x: np.tan(x), (-np.pi/2 + 0.1, np.pi/2 - 0.1)),
    ("反正弦函数 Arcsin", lambda x: np.arcsin(x), (-1, 1)),
    ("反余弦函数 Arccos", lambda x: np.arccos(x), (-1, 1)),
    ("反正切函数 Arctan", lambda x: np.arctan(x), (-5, 5)),
    ("双曲正弦函数 Sinh", lambda x: np.sinh(x), (-3, 3)),
    ("双曲余弦函数 Cosh", lambda x: np.cosh(x), (-3, 3)),
]

# 分类结构
sections = {
    "代数函数 (Algebraic Functions)": [0, 1, 2, 3],
    "指数与对数函数 (Exponential & Logarithmic)": [4, 5],
    "三角函数 (Trigonometric Functions)": [6, 7, 8],
    "反三角函数 (Inverse Trig Functions)": [9, 10, 11],
    "双曲函数 (Hyperbolic Functions)": [12, 13],
}

# PDF 生成
def create_function_summary_pdf(filename="Function_Summary.pdf"):
    c = canvas.Canvas(filename, pagesize=landscape(A4))
    width, height = landscape(A4)

    # 封面
    c.setFont(font_name, 36)
    c.setFillColor(colors.HexColor("#002B5B"))
    c.drawCentredString(width / 2, height - 5 * cm, "函数性质与图像 Function Summary")
    c.setFont(font_name, 18)
    c.setFillColor(colors.HexColor("#1A5276"))
    c.drawCentredString(width / 2, height - 7 * cm, "中英双语 · 学习笔记风格 · Math Study Guide")
    c.showPage()

    # 内容页
    for section_title, indices in sections.items():
        c.setFont(font_name, 24)
        c.setFillColor(colors.HexColor("#002B5B"))
        c.drawString(2 * cm, height - 3 * cm, section_title)
        y = height - 5 * cm

        for i in indices:
            title, func, x_range = functions[i]
            img_file = f"{i}.png"
            save_function_plot(img_file, func, x_range, title)

            c.setFont(font_name, 18)
            c.setFillColor(colors.black)
            c.drawString(2 * cm, y, f"• {title}")
            c.drawImage(img_file, 10 * cm, y - 2 * cm, width=10 * cm, height=6 * cm)
            y -= 8 * cm

            os.remove(img_file)  # 删除临时图像文件

            if y < 5 * cm:
                c.showPage()
                y = height - 3 * cm
                c.setFont(font_name, 24)
                c.setFillColor(colors.HexColor("#002B5B"))
                c.drawString(2 * cm, y, section_title)
                y -= 2 * cm

        c.showPage()

    c.save()
    print(f"✅ 成功生成：{filename}")

if __name__ == "__main__":
    create_function_summary_pdf()

