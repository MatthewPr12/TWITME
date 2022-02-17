from fastapi import FastAPI, Request, Form
from typing import Optional
from twitter_api import execute
from geocoder import get_coords
from fastapi.responses import HTMLResponse
from draw_map import create_map
from fastapi.templating import Jinja2Templates

app = FastAPI(title='User Friends Locations')
templates = Jinja2Templates(directory='maps')


@app.get("/", response_class=HTMLResponse)
def write_home(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})


@app.post("/submitform", response_class=HTMLResponse)
async def get_username(request: Request, user_name: str = Form(...)):
    friends_list = execute(user_name)
    friends = get_coords(friends_list)
    my_map = create_map(friends)
    my_map.save('maps/my_map.html')
    return templates.TemplateResponse('my_map.html', {'request': request})
    # return location(request, user_name)


# @app.get('/location', response_class=HTMLResponse)
# def location(request: Request, user_name: Optional[str]):
#     friends_list = execute(user_name)
#     friends = get_coords(friends_list)
#     my_map = create_map(friends)
#     my_map.save('maps/my_map.html')
#     return templates.TemplateResponse('my_map.html', {'request': request})
