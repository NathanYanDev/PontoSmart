FROM python:3.10.3-slim-bullseye

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-base-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Instalar dlib
WORKDIR /opt
RUN git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git && \
    cd dlib && \
    python3 setup.py install

# Instalar dependências Python
COPY requirements.txt /opt/requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r /opt/requirements.txt

# Copiar aplicação
COPY app/ /app
WORKDIR /app

CMD ["python", "main.py"]
