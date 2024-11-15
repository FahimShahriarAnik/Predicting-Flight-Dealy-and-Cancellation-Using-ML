# ML Project 5232

This project is focused on building and deploying machine learning models using Docker and Jupyter Notebook.

## Features
- Prebuilt Docker environment for Jupyter Notebook.
- Volume mapping to sync local files with the container.
- Includes essential Python libraries like NumPy, Pandas, and Matplotlib.

## Prerequisites
- Docker installed on your system.
- Python environment (optional for testing locally).

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name


## Link to Git cheat sheet
https://education.github.com/git-cheat-sheet-education.pdf


## To build the docker in local system:
Run the following command in terminal
docker-compose up build

After that,
run docker-compose up

## how to boot up docker container and point it to your local folder
docker run -p 8888:8888 -v "<local folder location>" <docker_image_name>
docker run -p 8888:8888 -v "C:\Users\fsani\OneDrive\Desktop\ML_projec_5232:/home/jovyan/work" jupyter_for_ml_proj

## how to run ipynb from local folder with the jupyter kernel
When you run the docker command, you get a link with token, paste that to upper right corner of jupyter notebook as your kernel.


## potential issues
run the following command to check if your files are in sync with docker folder.

docker exec -it <container_id> ls /home/jovyan/work

the list of files should be same as the local folder you want to sync with, according to docker-compose file.