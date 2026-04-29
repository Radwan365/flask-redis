from flask import Flask
import redis

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def home():
    return 'Welcome to my Flask Redis app!'

@app.route('/count')
def count():
    r.incr('count')
    return f'Visit count: {r.get("count")}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)