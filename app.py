
from flask import Flask
app = Flask(__name__)
@app.route('/')
def push():
    nc = NATS()

    future = asyncio.Future()

    async def sub(msg):
        nonlocal future
        future.set_result(msg)

        await nc.connect(servers=["nats://demo.nats.io:4222"])
        await nc.subscribe("time", cb=sub)

        unique_reply_to = nc.new_inbox()
        await nc.publish("time", b'', unique_reply_to)

    # Use the response
        msg = await asyncio.wait_for(future, 1)
        print("Reply:", msg)