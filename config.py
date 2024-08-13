import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5746000602:AAEQ_h-XXBh5yThTXUJPuyrYB4X-4of08gg")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "5587539"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8670b598fef377e6782429b1f664dce6")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://mrformula23:mrformula23@cluster0.durmg1d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
