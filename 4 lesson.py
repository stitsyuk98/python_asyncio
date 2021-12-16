"""

"""
from quart import Quart, render_template

app = Quart(__name__)

@app.route("/")
async def hello():
    name = 'Word!'
    return await render_template("hello.html", name=name)

app.run(port=8000)

#TODO: 11 video