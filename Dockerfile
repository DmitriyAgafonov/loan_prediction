FROM python:3-onbuild
RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY  . .
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["main.py"]

