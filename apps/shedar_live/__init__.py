# -*- coding: utf-8 -*-
import pathlib, jinja2, aiohttp_jinja2
from aiohttp import web
from aiohttp.web_request import Request
from python_chzzk import Chzzk


root_dir = pathlib.Path(__file__).resolve().parent
class ShedarLive(web.Application):
    def __init__(self, chzzk:Chzzk, channel_id:str, develop:bool):
        super().__init__()

        self.chzzk = chzzk
        self.channel_id = channel_id
        self.develop = develop

        self.add_routes([
            # assets
            web.static("/assets", str(root_dir.joinpath("assets"))),
            # routes
            web.get("/", self.profile), web.get("", self.profile),
            web.get("/contact/", self.contact),
            # api
            web.post("/checkIsLive", self.check_is_live)
        ])

        # setup template
        aiohttp_jinja2.setup(
            self, loader = jinja2.FileSystemLoader(str(root_dir.joinpath("templates")))
        )

    async def profile(self, req:Request):
        return aiohttp_jinja2.render_template(
            "profile.html", req, {
                "baseUrl": "/shedar/" if self.develop else "/",
                "channelId": self.channel_id
            }
        )
    
    async def contact(self, req:Request):
        return aiohttp_jinja2.render_template(
            "contact.html", req, {
                "baseUrl": "/shedar/" if self.develop else "/",
                "emailAddress": "이메일(추가 예정)",
                "emailTitle": "기본 제목"
            }
        )
    

    async def check_is_live(self, req:Request):
        channel = await self.chzzk.channel(self.channel_id)

        return web.json_response({
            "isLive": channel.open_live
        })
