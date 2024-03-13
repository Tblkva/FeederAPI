# from FeederAPI.Characters import champs_db
#
# if __name__ == '__main__':
#     print(champs_db)

import uvicorn

if __name__ == '__main__':
    uvicorn.run('webapp.app:app', host="127.0.0.1", port=5000, reload=True)