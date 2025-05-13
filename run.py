
from app import app
import os

# Автокомпиляция переводов, если не скомпилированы
if not os.path.exists("translations/es/LC_MESSAGES/messages.mo"):
    os.system("pybabel compile -d translations")

if __name__ == "__main__":
    app.run(debug=True)
