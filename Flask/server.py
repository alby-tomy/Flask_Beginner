from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    tasks.append(task)
    return redirect(url_for('index'))

@app.route('/update/<int:index>', methods=['POST'])
def update(index):
    new_task = request.form.get('new_task')
    if 0 <= index < len(tasks):
        tasks[index] = new_task
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)