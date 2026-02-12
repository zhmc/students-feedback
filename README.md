# 学生反馈系统 (Students Feedback System)

这是一个基于Flask开发的学生反馈收集管理系统，允许学生匿名或实名提交反馈，并提供管理员后台进行反馈管理。

## 项目地址

[https://github.com/zhmc/students-feedback](https://github.com/zhmc/students-feedback)

## 功能特性

### 用户端功能
- 学生可以提交反馈意见
- 支持匿名或实名提交
- 填写班级和姓名信息
- 反馈数据持久化存储

### 管理员功能
- 管理员登录验证
- 查看所有反馈信息
- 删除不当反馈内容
- 会话管理和登出功能

## 技术栈

- 后端：Python Flask框架
- 前端：HTML模板 + CSS样式
- 数据存储：JSON文件存储
- 安全性：会话管理

## 文件结构

students-feedback/
├── app.py                 # 主应用文件
├── static/
│   └── css/
│       ├── bs.css         # Bootstrap样式
│       └── style.css      # 自定义样式
├── templates/
│   ├── admin.html         # 管理员后台页面
│   ├── admin_login.html   # 管理员登录页面
│   ├── base.html          # 基础模板
│   ├── contact.html       # 联系页面
│   └── index.html         # 用户反馈主页面
└── README.md              # 项目说明文件
```

## 安装与运行

### 环境要求
- Python 3.6+
- pip包管理器

### 安装步骤

1. 克隆项目到本地：
```bash
git clone https://github.com/zhmc/students-feedback.git
cd students-feedback
```

2. 创建虚拟环境并激活：
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. 安装依赖：
```bash
pip install Flask
```

4. 运行应用：
```bash
python app.py
```

5. 访问应用：
- 用户端：http://localhost:5000
- 管理员登录：http://localhost:5000/admin/login

## 默认管理员账户

- 用户名：`feedback`
- 密码：`feedback123`

## 使用说明

### 提交反馈
1. 访问首页，填写反馈内容
2. 选择是否匿名提交
3. 如非匿名，需填写班级和姓名
4. 点击提交按钮完成反馈

### 管理员操作
1. 登录管理员账户
2. 查看所有反馈列表
3. 可对不当内容执行删除操作
4. 登出时点击退出按钮

## 代码特点

- 简单易懂的Flask应用结构
- 数据持久化存储到JSON文件
- 包含基础的安全措施（会话管理）
- 支持匿名与实名反馈提交

## 配置选项

在 [app.py](file://e:\zh_mc\back\app.py) 文件中可配置以下参数：
- [ADMIN_USERNAME](file://e:\zh_mc\back\app.py#L11-L11) - 管理员用户名
- [ADMIN_PASSWORD](file://e:\zh_mc\back\app.py#L12-L12) - 管理员密码
- [FEEDBACK_FILE](file://e:\zh_mc\back\app.py#L14-L14) - 反馈数据存储文件路径
- `SECRET_KEY` - Flask应用密钥

## 贡献指南

欢迎提交Issue和Pull Request来改进这个项目。

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 作者

zh_mc

## 致谢

感谢所有为本项目贡献代码和建议的人。
