# 班级活动报名与统计网页

一个基于 Flask 的动态网页项目，用于班级活动报名和统计。

## 功能

- 首页：填写姓名、小组、活动方向、一句话说明
- 结果页：显示当前报名人数、各活动方向人数、最近报名列表

## 本地运行

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

然后访问 http://127.0.0.1:5000

## 团队协作

本项目采用 Fork + PR 工作流：

| 角色 | 分支 | 修改文件 |
|------|------|----------|
| 组长 | main | 仓库管理、审核合并 |
| 组员 A | member-a-event-info | data/event_info.py |
| 组员 B | member-b-options | data/options.py |
| 组员 C | member-c-page-text | data/page_text.py |
| 组员 D | member-d-sample-data | data/registrations.py |
