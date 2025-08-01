FROM nvidia/cuda:12.1.1-runtime-ubuntu20.04

# Install Python 3.12 and other dependencies
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

# Install wget and nginx to fetch Miniconda and serve frontend
RUN apt-get update && \
    apt-get install -y wget nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Miniconda on x86 or ARM platforms
RUN arch=$(uname -m) && \
    if [ "$arch" = "x86_64" ]; then \
    MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-py312_25.3.1-1-Linux-x86_64.sh"; \
    elif [ "$arch" = "aarch64" ]; then \
    MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-py312_25.3.1-1-Linux-aarch64.sh"; \
    else \
    echo "Unsupported architecture: $arch"; \
    exit 1; \
    fi && \
    wget $MINICONDA_URL -O miniconda.sh && \
    mkdir -p /root/.conda && \
    bash miniconda.sh -b -p /root/miniconda3 && \
    rm -f miniconda.sh


WORKDIR /src
COPY ./requirements.txt /src/requirements.txt
COPY ./api /src/api
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Setup frontend
COPY client/ /usr/share/nginx/html/
RUN rm /usr/share/nginx/html/index.html || true
RUN mv /usr/share/nginx/html/main.html /usr/share/nginx/html/index.html

# Configure Nginx to proxy API calls
COPY nginx.conf /etc/nginx/nginx.conf

# Create startup script
COPY start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 80
CMD ["/start.sh"]
