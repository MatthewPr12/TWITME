from fastapi import FastAPI, Request
from typing import Optional
from twitter_api import execute
from geocoder import get_coords
from fastapi.responses import HTMLResponse
from draw_map import create_map
from fastapi.templating import Jinja2Templates

app = FastAPI(title='User Friends Locations')
templates = Jinja2Templates(directory='maps')

@app.get("/")
async def root():
    return {'message': 'Hello world!'}


@app.get("/about")
def about():
    return {'Data': 'Something'}


@app.get('/location', response_class=HTMLResponse)
def location(request: Request, user_name: Optional[str] = None):
    friends_list = execute(user_name)
    friends = get_coords(friends_list)
    my_map = create_map(friends)
    my_map.save('maps/my_map.html')
    return templates.TemplateResponse('my_map.html', {'request': request})
