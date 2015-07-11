from flask import *
from random import shuffle, choice

app = Flask(__name__)

flag = 'flag{N0t_to0_h4rd_r1t3?}'

chain = range(10000)
shuffle(chain)
goal_id = choice(chain)
links = {a:b for a,b in zip(chain[:-1], chain[1:])}
links[chain[-1]] = chain[0] # make the links circular

@app.route('/')
@app.route('/<int:chain_id>')
def root(chain_id=0):
    if not chain_id in links:
        return 'u wot m8'
    else:
        ret = str(links[chain_id])
        if chain_id == goal_id:
            ret += "\n" + flag
        return ret

if __name__ == '__main__':
    print goal_id
    app.run('0.0.0.0', 5000)
