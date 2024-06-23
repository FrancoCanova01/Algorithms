# Algorithms

## Setup (Windows)
Build Docker Container
```bash
docker build -t algos:1 .
```

Run docker image
```bash
docker run -v ${PWD}:/usr/src/app -it algos:1
```

Now connect using VSCode Remote Connect functionality. Verify that the local folder is linked to the container folder by creating a new file and verifying that its created both inside container an in local filesystem.