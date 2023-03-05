1) git clone https://github.com/iosokolov/didactic-tribble.git
2) cd didactic-tribble
3) poetry install
4) docker-compose up
5) cd airflow
6) alembic upgrade heads
7) python main.py server
8) python airflow/main.py consumer (new terminal)
9) python airflow/main.py scheduler (new terminal)
10) run search:
     ```
     curl --request POST \
       --url http://127.0.0.1:9000/search
     ```

     get a response:  
     ```
     {
         "search_id": "fce63793-4234-4539-9f1c-b10de0fcb09c"
     }
    ```

11) get result after 60 seconds:  
     ```
     curl --request GET \
       --url http://127.0.0.1:9000/results/fce63793-4234-4539-9f1c-b10de0fcb09c/EUR
     ```


### TODO:
- dql and retry queues
- makefile
- full containerization
- tests
- authorization
- pydantic