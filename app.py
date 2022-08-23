from support.imports import *



app = Flask('app')
Base.metadata.create_all(BaseService.engine)



if __name__ == '__main__':
    app.run(port=8000, debug=True)
