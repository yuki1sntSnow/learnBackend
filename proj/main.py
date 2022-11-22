from fastapi import Depends, FastAPI

from core.events import close_orm, init_orm
from core.exceptions import exception_handlers
from core.middleware import middlewares
from core.security import check_permissions
from core.utils import load_routers

app = FastAPI(
    on_startup=[init_orm],
    on_shutdown=[close_orm],
    middleware=middlewares,
    exception_handlers=exception_handlers,
)

load_routers(
    app,
    "router",
    no_depends="auth",
    # 这个环节注入认证依赖
    # depends=[Depends(check_permissions)],
)

if __name__ == "__main__":
    import uvicorn
    
    # uvicorn.run("main:app", reload=True)
    uvicorn.run("main:app", host="127.0.0.1", port=1902, reload=True)

