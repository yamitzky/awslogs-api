# awslogs-api
API version of https://github.com/jorgebastida/awslogs

## Install

### Local

```
pip install -r requirements.txt
python api.py
```

### Docker

```
docker run -p 5000:5000 yamitzky/awslogs-api
```

## Usage

It provides Swagger UI. Browse http://localhost:5000/ui

![swagger ui screenshot](https://raw.githubusercontent.com/yamitzky/awslogs-api/master/swagger.png)

### /groups

`awslogs groups`

### /streams

`awslogs streams log_group_name`

### /logs

`awslogs get log_group_name`
