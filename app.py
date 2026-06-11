from flask import Flask, request, render_template
from data.event_info import EVENT_NAME, EVENT_DESCRIPTION, EVENT_NOTICE
from data.options import GROUP_OPTIONS, ACTIVITY_OPTIONS
from data.page_text import WELCOME_TEXT, FORM_HINT, RESULT_TITLE
from data.registrations import registrations

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        event_name=EVENT_NAME,
        event_description=EVENT_DESCRIPTION,
        event_notice=EVENT_NOTICE,
        group_options=GROUP_OPTIONS,
        activity_options=ACTIVITY_OPTIONS,
        welcome_text=WELCOME_TEXT,
        form_hint=FORM_HINT,
    )


@app.route("/result", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        group = request.form.get("group", "")
        activity = request.form.get("activity", "")
        reason = request.form.get("reason", "").strip()
        if name:
            registrations.insert(0, {
                "name": name,
                "group": group,
                "activity": activity,
                "reason": reason,
            })

    # 统计各活动方向人数
    activity_count = {}
    for r in registrations:
        act = r.get("activity", "未指定")
        activity_count[act] = activity_count.get(act, 0) + 1

    return render_template(
        "result.html",
        event_name=EVENT_NAME,
        result_title=RESULT_TITLE,
        total=len(registrations),
        registrations=registrations,
        activity_count=activity_count,
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
