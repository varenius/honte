# honte

#INSTALL/RUN instructions OS X catalina 10.15.3

# Get docker
Install docker https://hub.docker.com/editions/community/docker-ce-desktop-mac/
Start docker desktop

# Get honte-repo
git clone https://github.com/varenius/honte.git honte
cd honte

# Start backend
cd backend
python3 -m pipenv shell
python manage.py migrate
python manage.py runserver
Check: go to http://127.0.0.1:8000/
(Lägg till en random spelare: gå till http://127.0.0.1:8000/api/add)

# Start frontend
./build-frontend-docker.sh
./run-frontend-docker
cd frontend
yarn install
(Notera: yarn install laddar ner "hela internet" så det tar en stund.)
yarn start
