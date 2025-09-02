# -- 基础设置 ------------------------------------------------

project = 'MyDocs Demo'
author = 'YourName'
release = '0.1'

extensions = [
    "myst_parser",        # 支持 Markdown
    "sphinx_copybutton",  # 代码块复制按钮
    "sphinx_design",      # 卡片、按钮、栅格布局
]

templates_path = ['_templates']
exclude_patterns = []

# -- HTML 输出 ------------------------------------------------
html_theme = 'furo'
html_static_path = ['_static']
