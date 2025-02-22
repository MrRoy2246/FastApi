from fastapi import FastAPI



app = FastAPI() #instance
@app.get('/') #decorate
def index():
    return {'data':{'name':'abin'}}

@app.get('/about')
def about():
    return{'data':'about page'}