# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
import json
import os
from datetime import datetime
import hashlib

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# 管理员账号密码（写死在代码中）
ADMIN_USERNAME = 'feedback'
ADMIN_PASSWORD = 'feedback123'  # 实际使用中应使用更安全的密码

FEEDBACK_FILE = 'feedbacks.json'

def load_feedbacks():
    """从JSON文件加载反馈"""
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_feedbacks(feedbacks):
    """将反馈保存到JSON文件"""
    with open(FEEDBACK_FILE, 'w', encoding='utf-8') as f:
        json.dump(feedbacks, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    """用户端反馈页面"""
    return render_template('index.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    """提交反馈"""
    feedback_text = request.form.get('feedback')
    class_name = request.form.get('class_name')
    student_name = request.form.get('student_name', '')
    is_anonymous = request.form.get('anonymous') == 'on'
    
    # 验证必填字段
    if not feedback_text:
        flash('反馈内容不能为空', 'error')
        return redirect(url_for('index'))
    
    # 如果不是匿名提交，班级和姓名为必填
    if not is_anonymous and not class_name:
        flash('班级不能为空', 'error')
        return redirect(url_for('index'))
    
    if is_anonymous:
        student_name = '匿名'
        class_name = '匿名班级'
    
    feedbacks = load_feedbacks()
    
    new_feedback = {
        'id': len(feedbacks) + 1,
        'feedback': feedback_text,
        'class_name': class_name,
        'student_name': student_name,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'is_anonymous': is_anonymous
    }
    
    feedbacks.append(new_feedback)
    save_feedbacks(feedbacks)
    
    flash('反馈提交成功！', 'success')
    return redirect(url_for('index'))

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    """管理员登录页面"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # 验证管理员账号密码
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            flash('登录成功！', 'success')
            return redirect(url_for('admin'))
        else:
            flash('用户名或密码错误', 'error')
    
    return render_template('admin_login.html')

@app.route('/admin')
def admin():
    """后台管理页面"""
    # 检查是否已登录
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    feedbacks = load_feedbacks()
    return render_template('admin.html', feedbacks=feedbacks)

@app.route('/admin/logout')
def admin_logout():
    """管理员登出"""
    session.pop('admin_logged_in', None)
    flash('您已成功登出', 'success')
    return redirect(url_for('admin_login'))

@app.route('/delete_feedback/<int:feedback_id>', methods=['POST'])
def delete_feedback(feedback_id):
    """删除反馈"""
    # 检查是否已登录
    if not session.get('admin_logged_in'):
        flash('请先登录', 'error')
        return redirect(url_for('admin_login'))
    
    feedbacks = load_feedbacks()
    feedbacks = [f for f in feedbacks if f['id'] != feedback_id]
    
    # 重新编号
    for i, feedback in enumerate(feedbacks):
        feedback['id'] = i + 1
    
    save_feedbacks(feedbacks)
    flash('反馈删除成功！', 'success')
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)