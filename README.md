# Python Django in Docker (with configured debugger)

## How to use

Then build

    docker-compose build

And run composition

    docker-compose up -d

Then run 

    ./script_main.sh

And run **[7] - Django make and apply migrations**

After this you may:
- Go to **Admin panel** http://localhost:8000/admin/ (username: **root** password: **root**)
- Go to **All products** http://localhost:8000/
- Go to **All basket** http://localhost:8000/basket/

## How to use basked
1) Add product to basked using button **Add to basket** (on page: **http://localhost:8000/**)
2) Go to page **http://localhost:8000/basket/** (where you can change the count of products)
3) Click on the button **Buy all**


## Deploy 
- **http://d4dd-5-128-71-145.ngrok.io**
- **https://d4dd-5-128-71-145.ngrok.io**
