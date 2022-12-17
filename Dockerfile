# start by pulling the python image
FROM python:3.8-alpine
FROM continuumio/miniconda3
RUN pip install --upgrade pip
# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR ./app

# install the dependencies and packages in the requirements file
RUN conda install -c anaconda psutil 
RUN conda install -c anaconda imagecodecs
RUN pip3 install -r requirements.txt
RUN conda install -c anaconda pillow 
RUN conda install -c anaconda numpy
RUN conda install -c anaconda tensorflow
# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]