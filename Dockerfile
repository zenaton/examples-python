FROM python:3.5

WORKDIR /app

# Install Zenaton
RUN curl https://install.zenaton.com | sh

# Install dependencies
ADD requirements.txt ./
RUN pip install -r requirements.txt

ENTRYPOINT ["./start_zenaton"]