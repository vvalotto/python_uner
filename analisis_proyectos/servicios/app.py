from analisis_proyectos.servicios.api import *
from analisis_proyectos.servicios.configurador import *


if __name__ == "__main__":
    app_api.run(host='127.0.0.1', port=5050, debug=True)
