FROM python:2.7
RUN apt-get update && apt-get install -y \
    python-pip
RUN pip install six
RUN pip install numpy
ADD build /build
ADD server2.py /
ADD gen-py /gen-py
CMD ["cd", "gen-py"]
CMD ["ls","-a"]
CMD [ "python", "./server2.py" ]
