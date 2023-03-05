1) git clone https://github.com/iosokolov/didactic-tribble.git
2) cd didactic-tribble
3) poetry install
4) docker-compose up
5) python airflow/main.py server
6) python airflow/main.py consumer
7) python airflow/main.py scheduler (optional)
8) run search:
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

9) get result after 60 seconds:  
    ```
    curl --request GET \
      --url http://127.0.0.1:9000/results/fce63793-4234-4539-9f1c-b10de0fcb09c/EUR
    ```


### TODO:
- dql and retry queues
- makefile
- full containerization
- 