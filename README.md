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



## how to boot up docker container and point it to your local folder
docker run -p 8888:8888 -v "<local folder location>" <docker_image_name>
docker run -p 8888:8888 -v "C:\Users\fsani\OneDrive\Desktop\ML_projec_5232:/home/jovyan/work" jupyter_for_ml_proj
