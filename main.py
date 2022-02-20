"""
create web app and tie up all the needed scripts
"""
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from twitter_api import execute
from geocoder import get_coords
from draw_map import create_map

app = FastAPI(title='User Friends Locations')
templates = Jinja2Templates(directory='maps')


@app.get("/", response_class=HTMLResponse)
def write_home(request: Request):
    """
    home page
    :param request:
    :return:
    """
    return templates.TemplateResponse('home.html', {'request': request})


@app.post("/submitform", response_class=HTMLResponse)
async def get_username(request: Request, user_name: str = Form(...)):
    """
    return html map
    :param request:
    :param user_name:
    :return:
    """
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
