import sys
print("Python ejecutándose desde:")
print(sys.executable)

from app.index import app

if __name__ == "__main__":
    app.run(debug=True)