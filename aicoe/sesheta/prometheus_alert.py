#!/usr/bin/env python3
# Sefkhet-Abwy Prometheus Alert
# Copyright(C) 2020
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


"""This will handle prometheus alert."""


import asyncio
import logging

import aiohttp
from aiohttp import web

from thoth.common import init_logging

from aicoe.sesheta.utils import notify_channel
from aicoe.sesheta.actions import __version__


init_logging(logging_env_var_start="SEFKHET__ABWY_LOG_")

_LOGGER = logging.getLogger("aicoe.sesheta")
_LOGGER.info(f"Thoth-Station Prometheus Alert Bot, Version v{__version__}")
logging.getLogger("googleapiclient.discovery_cache").setLevel(logging.ERROR)


routes = web.RouteTableDef()
app = web.Application()


@routes.post("/prometheus")
async def prometheus_alert_webhook_handler(request):
    """Entry point for prometheus alert webhook."""
    payload = await request.json()
    url = payload["externalURL"]
    if payload["status"] == "firing":
        alert_color = "#ff0000"
    else:
        alert_color = "#008000"
    notify_channel(
        "prometheus_alert",
        f"🔎 <font color='{alert_color}'>Prometheus Alert 🚨</font>: \n"
        f"<b>{payload['commonLabels']['alertname']}</b>"
        f" in instance <b>{payload['commonLabels']['instance']}</b>.\n"
        f"Job: <b>{payload['commonLabels']['job']}</b> \n"
        f"Severity: <font color='{alert_color}'>{payload['commonAnnotations']['severity']}</font>\n"
        f"<b>Status</b>: <font color='{alert_color}'>{payload['status']}</font>",
        f"{payload['commonLabels']['alertname']}",
        url,
    )
    return web.json_response({"text": "received"})


if __name__ == "__main__":
    _LOGGER.setLevel(logging.DEBUG)
    _LOGGER.debug("Debug mode turned on")

    app.add_routes(routes)
    web.run_app(app)
