# Docker file for fastapi development environment
FROM python:3.9

WORKDIR /code

COPY ./requirements_fastapi.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# bash command to persistently run the container
# version 2: ["/bin/bash"]
# version 2: ["tail", "-f", "/dev/null"]
ENTRYPOINT ["/bin/bash", "-c"] 
CMD ["tail -f /dev/null"] 
