from fastapi import FastAPI
import uvicorn
from routes.profile import profile

app = FastAPI(title="Приложение для знакомств",
              description="Познакомиться с хорошими людьми")

app.include_router(profile)

if __name__ == "__main__":
    uvicorn.run(app)
