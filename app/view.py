from app import app
from flask import render_template
import redis
import os

r = redis.Redis(host=os.getenv("REDIS_HOST"), port='6379')

def fibo(num):
    if num in [1, 2]:
        return 1
    cached_num = r.get(num)
    if cached_num:
        # print('1', num, cached_num)
        return int(cached_num)
    number = fibo(num - 2) + fibo(num - 1)
    r.set(num, number)
    # print('2', num, r.get(num))
    return number

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:num>')
def index_fibo(num):
    number = fibo(num)
    return render_template('index.html', num=number)