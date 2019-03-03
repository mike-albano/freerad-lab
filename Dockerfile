FROM freeradius/freeradius-server:latest

RUN apt-get update
RUN apt-get install -y python python-pip
COPY raddb/ /etc/raddb/
COPY ./ /
RUN pip install -r /gnxi/gnmi_cli_py/requirements.txt

RUN ["chmod", "+x", "/gnxi/gnmi_cli_py/py_gnmicli.py"]
RUN ["chmod", "+x", "/runner.py"]
CMD [ "python", "/mnt/hostdir/runner.py" ]
