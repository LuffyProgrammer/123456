DE python: 3.9

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requisitos.txt

CMD ["python", "./main.py"]
