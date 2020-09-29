from app import db
from app.models import User, Task

Task.query.delete()
User.query.delete()

jerry = User(username='jerry')
ben = User(username='ben10')

db.session.add(jerry)
db.session.add(ben)
db.session.commit()

all_users = User.query.all()

# print(all_users[0].id, all_users[0].username)

task1 = Task(title="Marble Rye", description="Bye my marble rye from bakery", done=False, user=jerry)
task2 = Task(title="Eat Dinner", description="Get table at the restaurant", user=jerry)
db.session.add(task1)
db.session.add(task2)
db.session.commit()

tasks = Task.query.all()

# print(tasks)
# print(tasks[1].done)